# Ready-to-record faulty Switch rehearsal

Our entry is **Ship Check**. **Launch Ledger** is the deliberately faulty sample
that Ship Check audits. It is not a second hackathon entry or an eligibility claim.
Use only the real event: https://www.wemakedevs.org/hackathons/switch.

## Project and reset point

- Remote branch: `codex/demo-switch-faulty` in `medhansh-19/ship-check`.
- Local checkout: `/Users/medhanshadhlakha/Documents/ChatGPT/Ship Check Demo`.
- Original faulty commit: `fcea38b84b6a7c79a7938e1e8713250c29bbf56b`.
- Main Ship Check checkout and branch are separate.
- The target includes only the saved real Flip the Switch checklist, source
  snapshot, provenance and event deadline. No Wispr-only or invented event rules.

## Verified faults

1. The README command `python3 -m pip install -r requirements.txt` fails: the
   requirements file does not exist. The application only imports standard modules.
2. `python3 app.py list` shows one done task and two open tasks; `summary` wrongly
   reports three done and zero open.
3. The focused unit test fails with the expected incorrect summary; the empty-list
   test passes. These are actual execution results, not mocked failures.
4. Submission brief and video URL are absent.
5. Root LICENSE is absent. Label this general project hygiene, not a mandatory
   event requirement. Ask the owner before selecting a license.

Generic file checks and official event requirements must remain clearly separate.
Do not mark the sample as compliant with Switch integration, eligibility or legal
requirements. Those need actual evidence; the submitted workflow is Ship Check.

## Open before recording

1. Start Switch and Docker; open Discord's `Ship Check Demo` → `#ship-check-demo`.
2. From the main Ship Check directory, start the demo dashboard:

   ```sh
   python3 -m control.switch_local --bridge f2fcebe1-afc2-40a0-8ade-070436f2a519 --channel 1568294022110388326 --owner 1417535988829392978 --repo '/Users/medhanshadhlakha/Documents/ChatGPT/Ship Check Demo'
   ```

   Run only one dashboard Discord bridge process at a time. Open
   http://127.0.0.1:8787 and select `flip-the-switch` under Event rules.
3. Open the demo branch on GitHub and a terminal in the demo checkout.
4. Run `python3 app.py list`, then `python3 app.py summary`, then
   `python3 -m unittest discover -s tests -v`. Show the actual discrepancy.

## Discord prompts — send in order

First Scout:

> @shipcheck-scout Check https://www.wemakedevs.org/hackathons/switch for this recording. Use real source quotes and dates. We are demonstrating Ship Check by auditing a deliberately faulty sample project, Launch Ledger. Do not claim that the sample is our actual entry or that eligibility is verified. Share the complete Flip the Switch checklist with Auditor.

Then Auditor:

> @shipcheck-auditor Fresh-clone https://github.com/medhansh-19/ship-check branch codex/demo-switch-faulty. Audit Launch Ledger using Scout's real Flip the Switch checklist. Execute the README setup and unit tests, capture actual exit codes, and propose numbered fixes. Separate general project hygiene from actual event requirements. Do not invent a video, eligibility, legal acceptance or Switch integration. Wait for my explicit numbered approval before editing.

Read the proposed IDs. Approve the setup correction and counting bug only if the
diff is correct; defer missing evidence. Ask for the PR to target
`codex/demo-switch-faulty`, never `master`. The dashboard's own proposals cover
documentation; the Auditor handles the application logic fix and test evidence.

After reviewing and merging that demo PR, update only the demo checkout:

```sh
git -C '/Users/medhanshadhlakha/Documents/ChatGPT/Ship Check Demo' pull --ff-only origin codex/demo-switch-faulty
```

Show the automatic recheck. Rerun the unit tests to demonstrate the code repair;
the dashboard itself performs static checks. Leave missing video and personal
evidence visibly unresolved. A higher score is not event eligibility certification.

## Another take without erasing history

For a fresh attempt, create a new branch and worktree at the faulty commit above,
choose a new local directory and target that new branch in the Auditor prompt.
Do not force-reset a branch containing your reviewed repairs.

To restore the dashboard to Ship Check itself, stop the demo server and restart
the same command with `--repo .` from the main Ship Check directory.
