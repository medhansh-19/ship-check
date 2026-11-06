"""Deliberately faulty rehearsal target for Ship Check; standard library only."""
import argparse
import json

TASKS = [
    {"title": "Connect Scout to Discord", "status": "done"},
    {"title": "Record the working workflow", "status": "open"},
    {"title": "Add the submission video URL", "status": "open"},
]


def summarize(tasks):
    completed = sum(task["status"] == "done" for task in tasks)
    return {"total": len(tasks), "completed": completed, "open": len(tasks) - completed}


def main():
    parser = argparse.ArgumentParser(description="Launch Ledger: a tiny team task summary")
    parser.add_argument("command", choices=("list", "summary"))
    args = parser.parse_args()
    print(json.dumps(TASKS if args.command == "list" else summarize(TASKS), indent=2))


if __name__ == "__main__":
    main()
