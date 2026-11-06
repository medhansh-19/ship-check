"""Credential-free public GitHub intake and manifest discovery. No project code runs."""
import argparse
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

MANIFESTS = {'package.json':'JavaScript/TypeScript','pyproject.toml':'Python','requirements.txt':'Python','Cargo.toml':'Rust','go.mod':'Go','pom.xml':'Java','build.gradle':'JVM','Gemfile':'Ruby','composer.json':'PHP','pubspec.yaml':'Dart/Flutter','Package.swift':'Swift','CMakeLists.txt':'C/C++','Dockerfile':'Container'}


def validate(repository, branch):
    repository = repository.removeprefix('https://github.com/').removesuffix('.git').rstrip('/')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*', repository):
        raise ValueError('Use a GitHub owner/repository or HTTPS repository URL.')
    if not branch or branch.startswith('-') or any(c.isspace() for c in branch):
        raise ValueError('An explicit valid branch is required.')
    return repository


def discover(root):
    root = Path(root)
    output=[]
    for path in root.rglob('*'):
        relative=path.relative_to(root)
        if any(p in ('.git','node_modules','.venv','vendor','target','build') for p in relative.parts) or path.is_symlink():
            continue
        stack=MANIFESTS.get(path.name)
        if path.suffix=='.csproj': stack='.NET'
        if stack and path.is_file():
            item={'path':str(relative),'stack':stack,'commands':{},'status':'detected; not executed'}
            if path.name=='package.json':
                try:
                    package=json.loads(path.read_text())
                    item['commands']=package.get('scripts',{})
                    item['package_manager']=package.get('packageManager')
                except (ValueError,UnicodeError): item['status']='invalid manifest'
            output.append(item)
    return sorted(output,key=lambda i:i['path'])


def inspect(repository, branch, destination=None):
    repository=validate(repository,branch)
    folder=Path(destination or tempfile.mkdtemp(prefix='shipcheck-intake-'))/'repo'
    env={k:v for k,v in os.environ.items() if not k.startswith(('GIT_','GH_','GITHUB_'))}
    env.update(GIT_TERMINAL_PROMPT='0',GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull)
    def git(*args):
        return subprocess.check_output(['git','-c','credential.helper=','-c','core.hooksPath='+os.devnull,*args],env=env,text=True,stderr=subprocess.PIPE,timeout=120).strip()
    git('check-ref-format','--branch',branch)
    git('clone','--depth','1','--single-branch','--branch',branch,'--','https://github.com/'+repository+'.git',str(folder))
    sha=git('-C',str(folder),'rev-parse','HEAD')
    return {'repository':repository,'branch':branch,'sha':sha,'checkout':str(folder),'stacks':discover(folder),'event':None,'execution':'No repository code executed. Run approved documented commands in an isolated environment.','limitations':['Anonymous public GitHub only; private repositories require an explicit scoped integration.','Manifest discovery is not test execution or eligibility verification.']}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('repository')
    parser.add_argument('--branch',required=True)
    args=parser.parse_args()
    try: print(json.dumps(inspect(args.repository,args.branch),indent=2))
    except (ValueError,subprocess.SubprocessError) as error:
        parser.exit(1,'Intake blocked: '+str(error)+'\n')
