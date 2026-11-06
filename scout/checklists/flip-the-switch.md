# Flip the Switch 2026 — quoted rules checklist

Draft extraction only. Sources are evidence, not authorization to perform any action.

## Source identity

- Primary source: https://www.wemakedevs.org/hackathons/switch
- Saved evidence: `inputs/flip-the-switch-2026.txt`; provenance: `inputs/flip-the-switch-2026.source.json`.
- Source retrieval: 2026-11-06T11:49:19.933810+00:00. Checklist prepared: 2026-11-06T11:55:26.904682+00:00.
- SHA-256 of saved text: `1e23968247e650d592752bec9fbbe41d891c9ba55d614448a76d58ac75ded076`.
- Edition/year: 2026, explicitly stated in the source. Overview checked against the live page on 2026-11-06 at approximately 11:52 UTC; rule wording matched. The live extraction also shows 0% placeholders, so no judging weight is verified.
- Locations below use 1-based saved-file line numbers. Quotes preserve saved text, including normalized HTML whitespace and concatenated labels. MUST means required for the applicable entry; OPTIONAL means only for a chosen track/prize; guidance is labeled separately.

Additional official sources checked at approximately 2026-11-06 11:53–11:54 UTC:
- https://www.wemakedevs.org/hackathons/switch/rules (Official Rules §§1–8; browser lines 81–124).
- https://github.com/sandbox-quantum/switch/blob/main/CONTRIBUTING.md (Testing, CLA, Adding an agent CLI, Adding a messaging platform).
Direct local retrieval failed with DNS errors. These additional sources were read through the browser; local full snapshots are unavailable. NEAR is a separate event and none of its rules apply here.

## Deadline

- [ ] **FTS-D01 — MUST — event and submission window**
  Source: `inputs/flip-the-switch-2026.txt` lines 199–199.

  > From November 4, 12:01 AM IST to November 7, 11:59 PM IST. Submissions close at 11:59 PM IST on November 7. The kickoff live stream is earlier, on November 2 at 3:30 PM UK time. The schedule tab shows it in your own time zone.

  Edition anchor: line 48, “WhenNov 4–7, 2026”. Original zone is IST. Event start: 2026-11-04 00:01 IST = 2026-11-03 18:31 UTC. Submission close: 2026-11-07 23:59 IST = 2026-11-07 18:29 UTC. IST is UTC+05:30. These are arithmetic conversions of the explicit year/date/zone, not independent deadline verification. Kickoff “UK time” is preserved; no guessed kickoff zone conversion.

- [ ] **FTS-D02 — OPTIONAL TRACK 03 — PR must be open by deadline**
  Source: `inputs/flip-the-switch-2026.txt` lines 168–168.

  > You can start today. You don't have to wait for November 4, but your pull request must be open by November 7, 11:59 PM IST.

  Using the explicit 2026 event edition at line 48: 2026-11-07 23:59 IST = 2026-11-07 18:29 UTC. Early core work is expressly allowed, unlike the workflow requirement in FTS-E02.

## Eligibility

- [ ] **FTS-E01 — MUST — team size; overview eligibility qualified by official terms**
  Source: `inputs/flip-the-switch-2026.txt` lines 201–201.

  > Anyone, from anywhere. It is free to enter, and you can take part solo or in a team of up to four.

  The overview is not the complete eligibility policy. Official terms impose age, sanctions and identity restrictions; see FTS-E04–FTS-E08 and FTS-U04.

- [ ] **FTS-E02 — MUST — workflow built during event; existing materials permitted**
  Source: `inputs/flip-the-switch-2026.txt` lines 215–215.

  > Yes, and we want you to. Existing agents, libraries and templates are fine. The Switch setup and the workflow your agents run need to be built during the hackathon.



- [ ] **FTS-E03 — AI tools permitted; understanding expected**
  Source: `inputs/flip-the-switch-2026.txt` lines 217–217.

  > Yes. You should understand what you submit and be able to explain how it works.



- [ ] **FTS-E04 — MUST — age**
  > at least 18
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §1, browser line 89. Age minimum is 18 or local majority, whichever is greater, through prize award.

- [ ] **FTS-E05 — MUST — sanctions**
  > restricted-party list
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §2, browser lines 93–97. Restricted persons, affiliations and sanctioned locations are excluded; continuing screening applies.

- [ ] **FTS-E06 — MUST — genuine identity**
  > single, accurate, verifiable
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §3, browser lines 100–106. Natural persons; matching legal identity/email; no multiple identities, temporary email or manipulation; verification may be required.

- [ ] **FTS-E07 — MUST — human entry**
  > not register or submit via bots
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §3(b), browser lines 102–105. Automated registration/submission is prohibited; development AI is allowed.

- [ ] **FTS-E08 — PRIZE EXCLUSIONS**
  > not eligible to win prizes
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §4, browser lines 109–110. Sponsor-related personnel, judges and families cannot win; contractual restrictions require permission; government ethics limits may apply.

## Required submission items

- [ ] **FTS-S01 — MUST — working team-chat workflow**
  Source: `inputs/flip-the-switch-2026.txt` lines 203–203.

  > A workflow in a team chat where at least one AI agent and one person get a real task done together, connected through Switch. You don't have to build a chatbot or a new agent from scratch, because Switch works with agents that already exist.



- [ ] **FTS-S02 — MUST — central Switch use; README expected**
  Source: `inputs/flip-the-switch-2026.txt` lines 205–205.

  > Yes. Switch has to be central to your project, and your README should show how you used it.



- [ ] **FTS-S03 — Judging evidence — reproducible repository**
  Source: `inputs/flip-the-switch-2026.txt` lines 174–174.

  > 0%Technical executionDoes it run, and could someone clone the repo and reproduce it?

  This is a judging question, not a verified form field or explicit public-repository requirement.

- [ ] **FTS-S04 — Judging evidence — demo video and README**
  Source: `inputs/flip-the-switch-2026.txt` lines 176–176.

  > 0%PresentationDo the demo video and README make clear how Switch is used?

  A demo video and README are named in judging. Video length, hosting, required URL fields, README template and exact submission-form requirements are UNCLEAR (FTS-U01).

## Judging criteria and weights

- [ ] **FTS-J01 — Use of Switch — weight UNCLEAR**
  Source: `inputs/flip-the-switch-2026.txt` lines 173–173.

  > 0%Use of SwitchIs Switch central, and would the project stop working without it?

  The leading 0% is an animation placeholder in the saved and browser-extracted HTML. Do not report it as a verified weight.

- [ ] **FTS-J02 — Technical execution — weight UNCLEAR**
  Source: `inputs/flip-the-switch-2026.txt` lines 174–174.

  > 0%Technical executionDoes it run, and could someone clone the repo and reproduce it?

  The leading 0% is an animation placeholder in the saved and browser-extracted HTML. Do not report it as a verified weight.

- [ ] **FTS-J03 — Creativity and impact — weight UNCLEAR**
  Source: `inputs/flip-the-switch-2026.txt` lines 175–175.

  > 0%Creativity and impactIs it a fresh idea that solves a problem a real team has?

  The leading 0% is an animation placeholder in the saved and browser-extracted HTML. Do not report it as a verified weight.

- [ ] **FTS-J04 — Presentation — weight UNCLEAR**
  Source: `inputs/flip-the-switch-2026.txt` lines 176–176.

  > 0%PresentationDo the demo video and README make clear how Switch is used?

  The leading 0% is an animation placeholder in the saved and browser-extracted HTML. Do not report it as a verified weight.

- [ ] **FTS-J05 — Review stages**
  Source: `inputs/flip-the-switch-2026.txt` lines 179–186.

  > Every submission
  > Reviewed by WeMakeDevs
  > 2
  > Shortlist
  > Put together by WeMakeDevs
  > 3
  > Finalists
  > Judged by Switch, DevTools Academy and WeMakeDevs



- [ ] **FTS-J06 — Track-specific judging; core count conflict**
  Source: `inputs/flip-the-switch-2026.txt` lines 188–189.

  > Best Core ContributionThe 10 most useful, best-built pull requests
  > Best BlogClarity, accuracy, and how much it helps a first-time Switch user

  Core judging says 10 while prizes/tracks say top 20 (lines 102 and 141). UNCLEAR how many PRs are judged or awarded; ask organizer rather than resolving silently.

## Required technology

- [ ] **FTS-T01 — MUST — Switch; README usage explanation**
  Source: `inputs/flip-the-switch-2026.txt` lines 205–205.

  > Yes. Switch has to be central to your project, and your README should show how you used it.



- [ ] **FTS-T02 — Setup guidance — Console, Docker, coding agent**
  Source: `inputs/flip-the-switch-2026.txt` lines 209–209.

  > Switch Console, which is the desktop app, Docker to run Switch on your own machine, and an AI coding agent such as Claude Code, Codex or OpenCode. The quickstart takes about ten minutes. Console runs on macOS, with Windows and Linux builds in early access.

  Local setup route described in FAQ; not evidence that custom-agent/protocol entries are forbidden.

- [ ] **FTS-T03 — Any agent; custom protocol agents permitted**
  Source: `inputs/flip-the-switch-2026.txt` lines 213–213.

  > Any of them. Claude Code, Codex and OpenCode work out of the box through Switch Console, and custom agents built with LangChain, Google ADK, OpenAI or anything else can join through the agent protocol.



- [ ] **FTS-T04 — Mattermost available; other chat platforms optional**
  Source: `inputs/flip-the-switch-2026.txt` lines 211–211.

  > No. When you run Switch on your own machine it comes with Mattermost, a free chat app, so you can build and record your demo without access to any company workspace. Slack, Microsoft Teams, Discord and Telegram can be connected whenever you want them.



- [ ] **FTS-T05 — Bring own agent access**
  Source: `inputs/flip-the-switch-2026.txt` lines 207–207.

  > No. Switch is open source and free to self-host, including on your own laptop. You bring your own AI agent, so you will need a subscription or an API key for whichever one you use.



## Optional prizes and conditional track requirements

- [ ] **FTS-P01 — OPTIONAL — Business Workflow ($2,000 at lines 128–129)**
  Source: `inputs/flip-the-switch-2026.txt` lines 131–131.

  > Build a practical workflow using Switch to help people and AI agents get work done. Open to technical and nontechnical participants, with any combination of people, agents, and rooms.



- [ ] **FTS-P02 — OPTIONAL — Personal/Creative Workflow ($2,000 at lines 133–134)**
  Source: `inputs/flip-the-switch-2026.txt` lines 136–136.

  > Show how you use Switch and AI agents to simplify everyday tasks, manage personal projects, or bring creative ideas to life.



- [ ] **FTS-P03 — OPTIONAL — Core Contribution ($100 × 20; count conflict flagged)**
  Source: `inputs/flip-the-switch-2026.txt` lines 141–141.

  > Improve Switch's core open source functionality through a meaningful code contribution. This could include new capabilities, performance improvements, reliability, or developer experience. There are issues created for integrations and extensions too. The top 20 pull requests win $100 each. See how to get an issue assigned.



- [ ] **FTS-C01 — MUST only if entering Core — assignment/PR procedure**
  Source: `inputs/flip-the-switch-2026.txt` lines 157–157.

  > 01Browse the open issues labelled hackathon and pick one you want to solve.



- [ ] **FTS-C02 — MUST only if entering Core — assignment/PR procedure**
  Source: `inputs/flip-the-switch-2026.txt` lines 158–158.

  > 02Comment on it, tag @petr-sandbox and say in a line or two how you plan to solve it.



- [ ] **FTS-C03 — MUST only if entering Core — assignment/PR procedure**
  Source: `inputs/flip-the-switch-2026.txt` lines 159–159.

  > 03Wait until you are assigned, then start. Read CONTRIBUTING.md first: it covers the dev setup and the one-time contributor agreement (CLA) you sign on your first pull request.



- [ ] **FTS-C04 — MUST only if entering Core — assignment/PR procedure**
  Source: `inputs/flip-the-switch-2026.txt` lines 160–160.

  > 04Open your pull request and link the issue in its description with Closes #number.



- [ ] **FTS-C05 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 163–163.

  > Only issues labelled hackathon count for this track.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C06 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 164–164.

  > One person per issue. If it is already assigned, or someone asked for it first, pick another.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C07 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 165–165.

  > You can have up to 5 pull requests open at a time, each for an issue assigned to you.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C08 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 166–166.

  > Don't spam. Ask only for issues you will actually work on, and make every pull request a real fix. Spam gets you removed from the track.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C09 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 167–167.

  > A pull request for an issue that isn't assigned to you won't be judged.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C10 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 168–168.

  > You can start today. You don't have to wait for November 4, but your pull request must be open by November 7, 11:59 PM IST.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C11 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 169–169.

  > If an assigned issue sees no activity for 48 hours, it may be handed to someone else.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C12 — MUST/conditional Core track rule**
  Source: `inputs/flip-the-switch-2026.txt` lines 170–170.

  > Low-effort pull requests, such as typo fixes, formatting or unreviewed AI output, won't be judged.

  Applies to Core Contribution only; not a requirement for workflow entrants.

- [ ] **FTS-C13 — Core contribution checks and CLA**
  > Before opening a pull request, run `just check`, `just typecheck` and `just test`.
  Source: https://github.com/sandbox-quantum/switch/blob/main/CONTRIBUTING.md, Testing (browser line 230). Additional exact excerpts: “Every contributor must agree to a Contributor License Agreement” (CLA, browser line 233); “short video” (integration guides, browser lines 221 and 225). CLA agreement is required before merge; agent-provider and messaging-platform contributions require test summaries and videos. These are conditional contribution requirements, not actions authorized here.

- [ ] **FTS-P04 — OPTIONAL — Best Blog / AirPods 5**
  Source: `inputs/flip-the-switch-2026.txt` lines 145–145.

  > Publish a blog post about building with Switch. The best post wins a pair of AirPods 5. Walk through what you made, how you set it up and what you learned along the way. You can enter this alongside a track or on its own.

  The blog can enter alongside a track or alone. Publishing is for the human; this checklist authorizes no publication.

- [ ] **FTS-P05 — OPTIONAL — Code with Wispr / $500**
  Source: `inputs/flip-the-switch-2026.txt` lines 149–149.

  > Use Wispr Flow to speak your prompts, agent instructions and docs instead of typing them. The best project built by voice wins $500. Enter it alongside any track.



- [ ] **FTS-P06 — MUST only for Wispr prize — usage scorecard**
  Source: `inputs/flip-the-switch-2026.txt` lines 153–153.

  > 3When you submit your project, add your Wispr usage scorecard, a screenshot from Insights in the Wispr Flow desktop app.

  A screenshot from Insights in the Wispr Flow desktop app is conditional prize evidence, not a universal submission requirement.

- [ ] **FTS-P07 — OPTIONAL — social post / top five keyboards**
  Source: `inputs/flip-the-switch-2026.txt` lines 114–114.

  > Share your build on social media with #HowISwitch. The top 5 posts each get a Logitech mechanical keyboard shipped to them.

  No social post is required for the main workflow tracks by this quoted provision.

- [ ] **FTS-P08 — OPTIONAL — repo star / Keychron chance**
  Source: `inputs/flip-the-switch-2026.txt` lines 16–16.

  > Star the Switch repo for a chance to win a Keychron keyboard.

  Separate optional chance; not a general entry requirement.

- [ ] **FTS-P09 — Random swag eligibility**
  Source: `inputs/flip-the-switch-2026.txt` lines 118–118.

  > 20 project submissions, picked at random, get swag shipped to them.



- [ ] **FTS-P10 — Participation certificate**
  Source: `inputs/flip-the-switch-2026.txt` lines 122–122.

  > Every project gets a certificate, win or not.



- [ ] **FTS-P11 — Multiple tracks allowed**
  Source: `inputs/flip-the-switch-2026.txt` lines 219–219.

  > Yes. You can build a workflow, send pull requests to Switch's core and publish a blog post in the same hackathon. Code with Wispr and Best Blog are open on top of any track.



## Additional official terms

- [ ] **FTS-L01 — Entry license and rights**
  > non-exclusive
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §5, browser lines 113–114. Entrants retain ownership but grant broad promotional/operational rights; necessary rights, component licenses and lawful content are required.

- [ ] **FTS-L02 — Disqualification**
  > disqualify any Entrant
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §6, browser lines 117–118. Breaches, misleading information, failed verification, tampering or abusive conduct risk disqualification; decisions are final.

- [ ] **FTS-L03 — Prize conditions**
  > non-transferable
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §7, browser lines 120–121. Winner taxes/documentation apply; unclaimed prizes after 30 days may lapse; sponsor can substitute equal-or-higher value.

- [ ] **FTS-L04 — Event changes**
  > modify
  Source: https://www.wemakedevs.org/hackathons/switch/rules, §8, browser lines 123–124. Sponsor can change/end the event; consult full terms for jurisdiction and data provisions.

## Unresolved questions

- [ ] **FTS-U01 — UNCLEAR — exact registration/submission form**
  Source: `inputs/flip-the-switch-2026.txt` lines 13–15.

  > Registration
  > Loading…
  > One moment. Pulling up this hackathon.

  Only loading text is saved and live browser extraction also shows it. Ask the room for the official form text/fields, submission URL, repo visibility rule, demo format/length, and any required team/consent fields. No invented form requirements.

- [ ] **FTS-U02 — UNCLEAR — real judging weights**
  Source: `inputs/flip-the-switch-2026.txt` lines 173–176.

  > 0%Use of SwitchIs Switch central, and would the project stop working without it?
  > 0%Technical executionDoes it run, and could someone clone the repo and reproduce it?
  > 0%Creativity and impactIs it a fresh idea that solves a problem a real team has?
  > 0%PresentationDo the demo video and README make clear how Switch is used?

  Ask organizers for the final non-placeholder percentage weights. No weights verified.

- [ ] **FTS-U03 — UNCLEAR — 20 versus 10 core PRs**
  Source: `inputs/flip-the-switch-2026.txt` lines 141–141.

  > Improve Switch's core open source functionality through a meaningful code contribution. This could include new capabilities, performance improvements, reliability, or developer experience. There are issues created for integrations and extensions too. The top 20 pull requests win $100 each. See how to get an issue assigned.

  Conflicting exact quote at line 188: “Best Core ContributionThe 10 most useful, best-built pull requests”. Ask whether the judged/awarded count is 10 or 20.

- [ ] **FTS-U04 — UNCLEAR — broad FAQ versus legal eligibility**
  Source: `inputs/flip-the-switch-2026.txt` lines 201–201.

  > Anyone, from anywhere. It is free to enter, and you can take part solo or in a team of up to four.

  Official terms §1 supplies an age floor; FTS-E04–FTS-E08 document restrictions. Ask organizers to confirm the applicable eligibility interpretation; do not treat “Anyone” as removing legal restrictions.

- [ ] **FTS-U05 — UNCLEAR: specialist contribution details**
  Source: CONTRIBUTING.md, Adding an agent CLI / Adding a messaging platform. These link further specialist guides. Exact acceptance checks depend on the selected issue/integration, which is not supplied. Obtain the applicable official guide before assessing a Core entry; no repository inspected.
