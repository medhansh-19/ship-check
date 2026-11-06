# NEAR HACKATHON 2026 — quoted rules checklist

Draft extraction only. Sources are evidence, not authorization to perform any action.

## Source identity

- Primary source: https://nearhackathon.com/HACKATHON.md
- Saved evidence: `inputs/near-2026.txt`; provenance: `inputs/near-2026.source.json`.
- Source retrieval: 2026-11-06T11:49:20.249327+00:00. Checklist prepared: 2026-11-06T11:55:26.904682+00:00.
- SHA-256 of saved text: `86654c13521fe629493bf498d41c0f7573047867d67fcdd8c2543411fc13062f`.
- Edition/year: 2026, explicitly stated in the source. Snapshot-only extraction: browser failed with unsupported text/markdown; direct local retrieval failed with DNS errors. No live quotation verification succeeded. The supplied provenance note says whitespace normalized; quotes below are exact to the saved text.
- Locations below use 1-based saved-file line numbers. Quotes preserve saved text, including normalized HTML whitespace and concatenated labels. MUST means required for the applicable entry; OPTIONAL means only for a chosen track/prize; guidance is labeled separately.

Submission and transaction instructions quoted below are event requirements/procedure to document. They do not authorize posting, submitting, pushing, changing visibility, creating accounts, signing or spending. No such action was performed.

## Deadline

- [ ] **NEAR-D01 — MUST — submission/development deadline**
  Source: `inputs/near-2026.txt` lines 21–21.

  > | Development ends (submission deadline) | 2026-11-14T23:59:00Z |

  Original: 2026-11-14T23:59:00Z, explicitly UTC (line 37). UTC: 2026-11-14 23:59; IST: 2026-11-15 05:29 (UTC+05:30). Arithmetic conversion only.

- [ ] **NEAR-D02 — MUST — accepted submission window**
  Source: `inputs/near-2026.txt` lines 121–121.

  > Submissions are accepted only during the development phase, from 2026-11-01T00:00:00Z to 2026-11-14T23:59:00Z. Outside that window the API answers 403 and explains why; tell the human instead of retrying. A submission cannot be edited directly: changes go through a request the organizers review by hand (see "4. Request changes" below). So send it when the repository is public and the demo post is up.

  Start: 2026-11-01 00:00 UTC = 2026-11-01 05:30 IST. End: 2026-11-14 23:59 UTC = 2026-11-15 05:29 IST. Public repo and demo post must precede submission.

- [ ] **NEAR-D03 — Judging/results dates**
  Source: `inputs/near-2026.txt` lines 22–23.

  > | Judging starts | 2026-11-16T00:00:00Z |
  > | Results announced by | 2026-11-18T23:59:00Z |

  Judging: 2026-11-16 00:00 UTC = 2026-11-16 05:30 IST. Results by: 2026-11-18 23:59 UTC = 2026-11-19 05:29 IST. All zones anchored by line 37.

## Eligibility

- [ ] **NEAR-E01 — No prior sign-up**
  Source: `inputs/near-2026.txt` lines 8–8.

  > 1. Build the project with the human. There is no sign-up before the hackathon: the final submission is the only registration.



- [ ] **NEAR-E02 — Permitted development/baseline window**
  Source: `inputs/near-2026.txt` lines 66–66.

  > **Q-001. Code before 2026-11-01?** Yes, from the announcement on 2026-10-19 (https://x.com/nearprotocol/status/2112257967818997891). The window runs from then to 2026-11-14. Earlier commits are baseline.



- [ ] **NEAR-E03 — Existing products conditional**
  Source: `inputs/near-2026.txt` lines 68–68.

  > **Q-002. Existing product on another chain?** Allowed. Only the NEAR integration built in the window is judged. Disclose in README.



- [ ] **NEAR-E04 — Existing repository separation**
  Source: `inputs/near-2026.txt` lines 70–70.

  > **Q-003. New repo required?** No. Dedicated branch, or tags pre-hackathon and hackathon-submission, plus a README section linking the diff.



- [ ] **NEAR-E05 — Old projects versus new features**
  Source: `inputs/near-2026.txt` lines 72–72.

  > **Q-004. Old project or new feature on it?** Old project as-is: no. New feature in the window: yes, if separated per Q-003. No minimum code size.



- [ ] **NEAR-E06 — Libraries/AI code permitted; disclose baseline**
  Source: `inputs/near-2026.txt` lines 74–74.

  > **Q-005. Libraries, templates, boilerplate?** All allowed, including own pre-hackathon libs and AI code. List in README; own old libs count as baseline.



- [ ] **NEAR-E07 — Testnet projects eligible**
  Source: `inputs/near-2026.txt` lines 84–84.

  > **Q-010. Testnet-only projects eligible?** Yes, all tracks. Mainnet only where the integration is mainnet-only.



- [ ] **NEAR-E08 — At most two independent disclosed projects per person**
  Source: `inputs/near-2026.txt` lines 94–94.

  > **Q-015. One person, several projects?** Allowed if projects are independent and disclosed: each README names the other project. Not the same project twice. One person, at most 2 different projects.



- [ ] **NEAR-E09 — One submission per project; all times UTC**
  Source: `inputs/near-2026.txt` lines 37–37.

  > All times are UTC. One submission per project.



## Required submission items

- [ ] **NEAR-S01 — MUST — public repo and reproducible machine-readable README**
  Source: `inputs/near-2026.txt` lines 104–104.

  > The repository may stay private while the team builds, but it must be public by 2026-11-14T23:59:00Z. Judges cannot open a private one. Claude Code and Codex screen every project before the human jury decides (Q-017), so write the README for a machine reader as well as a human one: what the product is, the problem it solves, and how to try it as "do X - see Y" steps a judge can follow. No marketing.

  Public deadline 2026-11-14 23:59 UTC = 2026-11-15 05:29 IST. This is a documented human obligation, not authorization to change visibility.

- [ ] **NEAR-S02 — MUST — LICENSE; public through judging**
  Source: `inputs/near-2026.txt` lines 92–92.

  > **Q-014. License?** Any. MIT is fine. Repo stays public through judging; add a LICENSE file.



- [ ] **NEAR-S03 — MUST — human publishes public X demo post**
  Source: `inputs/near-2026.txt` lines 108–108.

  > The human records a demo and publishes a public post on X: it says the project was built at NEAR HACKATHON, tags @NEARProtocol and #NEARHackathon, and has the demo video or screenshots attached. You can draft the text; the human posts it and gives you the link.



- [ ] **NEAR-S04 — OPTIONAL amplification tags; required tags identified**
  Source: `inputs/near-2026.txt` lines 117–117.

  > Every draft includes @NEARProtocol and #NEARHackathon, so the post shows up on the timeline. @NearLegion and @NearBuilders are optional: tagging them brings more community amplification and support.

  NEARProtocol and NEARHackathon tags are required; NearLegion and NearBuilders are optional.

- [ ] **NEAR-S05 — MUST for local-only demos — video, not screenshots alone**
  Source: `inputs/near-2026.txt` lines 88–88.

  > **Q-012. Local-only demo OK?** Yes: public repo, reproducible README, X post with a video; screenshots are not enough when judges cannot open the demo. Hosted demo is a plus; keep it up to 2026-11-18, ideally 2026-11-25.

  Hosted demo is a plus, not universally required. Source asks hosted availability to 2026-11-18, ideally 2026-11-25. Dates lack times: exact availability cutoff UNCLEAR; no guessed conversion.

- [ ] **NEAR-S06 — Demo presentation guidance**
  Source: `inputs/near-2026.txt` lines 110–115.

  > A good demo post:
  > - Lead with the user problem. Make the first line understandable to someone who doesn't know your project.
  > - Show one complete moment. In the demo, go from a real user action to a visible result. Skip long intros, architecture slides, and setup.
  > - Explain NEAR’s role concretely. Say what NEAR enables in this product — such as cross-chain settlement, private inference, or agent-controlled spending — and why that matters. Avoid a vague "powered by NEAR".
  > - Give people a next step. Link the demo and public repo, and ask a genuine question or invite specific feedback.

  Guidance for a good demo; distinguish from validation fields.

- [ ] **NEAR-S07 — MUST — human supplies identity, links, payout account and consent**
  Source: `inputs/near-2026.txt` lines 41–52.

  > Collect these before submitting. Do not guess, generate or fill in placeholders for any of them:
  > - Project name (2-80 characters)
  > - Team lead's name (2-80 characters)
  > - Contact email (max 160 characters). One person can send up to 2 submissions, for different projects that are independent and disclosed (see Q-015).
  > - Team size, one of: `1`, `2 - 4`, `4 - 6`, `6 - 8`, `8+`
  > - Tracks: one or more ids from the Tracks table below, every track the project fits. It is still one submission per project.
  > - NEAR account for the prize payout, mainnet: a named account such as `team.near` or a 64-character implicit account. The team creates it in any NEAR wallet; see https://docs.near.org/. Never create or invent one on their behalf.
  > - Link to the public repository judges will review. Each repository can be submitted only once.
  > - Link to the public demo post. The human writes and publishes it themselves.
  > - What they built (20-2000 characters): the problem, the product, and how NEAR fits in.
  > - Consent to the contact notice, read to them verbatim: "I agree that the organizers may use these details to review our submission and contact us about this hackathon."

  No values are collected/generated here. The exact contact notice is quoted in this item; consent must come from the human.

- [ ] **NEAR-S08 — MUST — validate payload; human confirms exact payload**
  Source: `inputs/near-2026.txt` lines 123–123.

  > Validate every field against the contract below, print the payload for the human, and send it only after they confirm:



- [ ] **NEAR-S09 — MUST — submission contract transport/body**
  Source: `inputs/near-2026.txt` lines 145–145.

  > `POST https://nearhackathon.com/api/applications` with `Content-Type: application/json`. Body up to 12000 bytes. Send exactly these fields:



- [ ] **NEAR-F01 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 149–149.

  > | requestId | string | UUID, generated once per submission and reused on retries |



- [ ] **NEAR-F02 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 150–150.

  > | projectName | string | 2-80 characters |



- [ ] **NEAR-F03 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 151–151.

  > | leadName | string | 2-80 characters |



- [ ] **NEAR-F04 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 152–152.

  > | email | string | valid email, max 160 characters, at most 2 submissions per email |



- [ ] **NEAR-F05 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 153–153.

  > | size | string | one of `1`, `2 - 4`, `4 - 6`, `6 - 8`, `8+`, exactly as written |



- [ ] **NEAR-F06 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 154–154.

  > | tracks | array of strings | one or more of `defi`, `thesis`, `privacy`, `business`, `swarms`, `security`, `agents`, `realworld`, `games`, `nfts`, `memecoins`, `social`, `open`, each listed once |



- [ ] **NEAR-F07 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 155–155.

  > | nearAddress | string | 2-64 characters, lowercase, matching `^(([a-z\d]+[-_])*[a-z\d]+\.)*([a-z\d]+[-_])*[a-z\d]+$` |



- [ ] **NEAR-F08 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 156–156.

  > | projectUrl | string | http(s) URL of the public repository, max 300 characters, unique: each repository is submitted once |



- [ ] **NEAR-F09 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 157–157.

  > | demoUrl | string | http(s) URL of the public demo post, max 300 characters |



- [ ] **NEAR-F10 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 158–158.

  > | idea | string | 20-2000 characters |



- [ ] **NEAR-F11 — MUST — exact API field validation**
  Source: `inputs/near-2026.txt` lines 159–159.

  > | consent | boolean | `true`, only after the human agreed to the contact notice |



- [ ] **NEAR-S10 — MUST — no extra fields/spam trap**
  Source: `inputs/near-2026.txt` lines 161–161.

  > Do not add other fields. In particular `website` is a spam trap: any non-empty value rejects the submission.



- [ ] **NEAR-S11 — MUST — one requestId; safe retry identity and private payload**
  Source: `inputs/near-2026.txt` lines 133–133.

  > Generate `requestId` once, with `uuidgen | tr A-Z a-z` or `node -e 'console.log(crypto.randomUUID())'`. Keep it: a retry after a network error or a 503 must reuse the same value, and the server then treats it as the same submission. Do not commit the payload; it contains personal data.



- [ ] **NEAR-S12 — MUST — example data is not real submission data**
  Source: `inputs/near-2026.txt` lines 131–131.

  > The values above are only an example of the shape. Never send them: ask the human for every value listed under "What the human decides" and build the payload from their answers.



- [ ] **NEAR-S13 — MUST — no duplicate; human request-changes route**
  Source: `inputs/near-2026.txt` lines 139–141.

  > If a saved submission has a mistake (a wrong repository or demo link, wallet, email, track or anything else), do not submit again: the same repository is rejected with 409, and a different link would count as another project. The human requests changes at https://nearhackathon.com/request-changes instead. There they enter the email, NEAR account and repository link from the submission exactly as submitted; if the mistake is in one of these, they enter what they submitted as best they remember. Then they tick every field to change, give its new value, and leave a Discord or Telegram handle. One request can change several fields.
  > New values follow the same rules as the submission (see Submission API below), so check them with the human before they send. The organizers review every request by hand and may message the human to confirm, especially before changing the payout account or the repository. Until a change is applied, the submission stays as it was. Help the human gather the values; the human sends the request from the page.



- [ ] **NEAR-S14 — API response handling (documented procedure only)**
  Source: `inputs/near-2026.txt` lines 163–170.

  > | Status | Meaning | What to do |
  > | --- | --- | --- |
  > | 201 | Submission saved | Done. Tell the human. |
  > | 400 | A field failed validation | Fix the fields listed in `fields` of the response and resend with the same requestId. |
  > | 403 | Submissions are not open, or the request looked cross-site | Tell the human. Do not retry. |
  > | 409 | Repository already submitted, or this email already has 2 submissions | The project was already submitted, or the human reached the limit. Ask the human; do not change the link or the email to get around it. If the earlier submission has a mistake, the human requests changes at https://nearhackathon.com/request-changes. |
  > | 413 | Body too large | Shorten the description. |
  > | 503 | Storage temporarily unavailable | Wait a minute and resend with the same requestId. |



- [ ] **NEAR-S15 — Form alternative / success criterion**
  Source: `inputs/near-2026.txt` lines 135–135.

  > A 201 response means the submission is saved: tell the human. If they prefer the form, the same fields are at https://nearhackathon.com/#apply.



- [ ] **NEAR-S16 — MUST — confirmation boundaries and secrets**
  Source: `inputs/near-2026.txt` lines 54–60.

  > ## Never without the human's explicit confirmation
  > - Send the submission. Print the full JSON payload first and wait for a yes. A second submission of the same repository is rejected, so there is one attempt per project. Mistakes are fixed by requesting changes, not by submitting again.
  > - Post anything on X or another network on their behalf.
  > - Make the repository public, push, or force-push.
  > - Sign transactions, spend tokens or deploy to mainnet.
  > - Commit secrets. Keys belong in environment variables, never in the repository.

  These are extracted source constraints. This rehearsal remains draft-only even if any source describes a possible transaction or submission.

## Judging criteria and weights

- [ ] **NEAR-J01 — AI screens; human jury decides**
  Source: `inputs/near-2026.txt` lines 98–98.

  > **Q-017. Claude Code and Codex role?** Screening, not deciding: reproducibility check, feature verification, structured report, preliminary score. Humans decide; low AI score alone cannot reject.



- [ ] **NEAR-J02 — Only in-window NEAR integration judged on existing cross-chain product**
  Source: `inputs/near-2026.txt` lines 68–68.

  > **Q-002. Existing product on another chain?** Allowed. Only the NEAR integration built in the window is judged. Disclose in README.



- [ ] **NEAR-J03 — Track-specific qualitative judging**
  Source: `inputs/near-2026.txt` lines 183–183.

  > | `thesis` | Investment Thesis | Build a long-term investment thesis for NEAR and back it with data: onchain analytics, live dashboards and models anyone can re-run. Judged on the evidence, not the conviction. | ONCHAIN DATA, DASHBOARDS, RESEARCH | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/02-thesis.md |



- [ ] **NEAR-J04 — Track-specific qualitative judging**
  Source: `inputs/near-2026.txt` lines 190–190.

  > | `games` | Games With Real Economies | Build NPCs with wallets, player-owned markets and economies that evolve without a dev patch. Judged on the game loop, not the token — bonus if players never notice the chain. | AGENT NPCS, SOCIAL LOGIN, NEAR INTENTS, NEP-245 | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/09-games.md |



- [ ] **NEAR-J05 — Track-specific qualitative judging**
  Source: `inputs/near-2026.txt` lines 192–192.

  > | `memecoins` | Memecoins With Mechanics | Build memecoins where the meme does something — supply that reacts to the community, treasuries with rules, onchain rituals and challenges. Judged on the mechanic, not the chart. | MEMECOINS, TOKEN MECHANICS, NEP-141 | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/11-memecoins.md |



- [ ] **NEAR-J06 — UNCLEAR: complete rubric and weights**
  No complete scoring rubric or numerical weights are present in the supplied snapshot (Rules lines 62–98; Tracks lines 172–194; Prizes lines 196–205). The qualitative quotes NEAR-J01–NEAR-J05 are the available evidence. Ask the room for official judging criteria/weights; do not invent equal weights.

## Required technology

- [ ] **NEAR-T01 — No named mandatory integrations; NEAR fit**
  Source: `inputs/near-2026.txt` lines 86–86.

  > **Q-011. Mandatory integrations?** None. Hints are hints. Own contract on NEAR that fits the track is enough.

  Own NEAR contract fitting the track is sufficient; do not infer any named partner integration is mandatory.

- [ ] **NEAR-T02 — Hints and Build-column protocols are optional**
  Source: `inputs/near-2026.txt` lines 174–178.

  > Put the `id` of every track the project fits in the `tracks` array of the submission. It is still one submission per project.
  > The Hints column is what the organizers hope to see in each track: NEAR features and themes worth building around. They are hints and wishes, not requirements, and so are the protocols named in the Build column (Q-011). Lean on the ones that fit the idea and name them in the README.
  > The Prompt column links an example prompt for the track, with links to relevant resources, from https://github.com/nearai/near-hackathon-prompt-examples. It is a starting point, not a requirement.



- [ ] **NEAR-T03 — 1Click JWT optional**
  Source: `inputs/near-2026.txt` lines 76–76.

  > **Q-006. 1Click JWT?** Not required. Without it, 0.2% fee. Register at https://partners.near-intents.org.



- [ ] **NEAR-T04 — Intents environment constraint; not permission to transact**
  Source: `inputs/near-2026.txt` lines 78–78.

  > **Q-007. Testnet for Intents?** None exists or is planned. Mainnet, separate dev accounts, tiny amounts, dry: true quotes.



- [ ] **NEAR-T05 — Test funds/cost guidance**
  Source: `inputs/near-2026.txt` lines 80–80.

  > **Q-008. Test funds?** Testnet NEAR is free (near-cli faucet, near-faucet.io). Mainnet costs not reimbursed by default. (see Q-007)

  Do not interpret this as permission to spend or request reimbursement.

- [ ] **NEAR-T06 — NEAR AI credit options — optional tool access**
  Source: `inputs/near-2026.txt` lines 64–64.

  > **Q-000. NEAR AI credits?** Buy with crypto or card in the NEAR AI Cloud dashboard (https://cloud.near.ai), or claim $10 by joining NEAR Builders (https://nearbuilders.org/join). Generate the API key in the dashboard.

  No purchase or account action authorized; this is not a universal eligibility requirement.

## Optional prizes and track selection

- [ ] **NEAR-P01 — Prize pool, currency and payout**
  Source: `inputs/near-2026.txt` lines 198–198.

  > Prize pool $250,000. One grand prize overall. 1st, 2nd and 3rd place in each of the 13 build tracks. Amounts are fixed in USD and paid in NEAR to the account given in the submission (see Q-016).



- [ ] **NEAR-P02 — Prize amounts**
  Source: `inputs/near-2026.txt` lines 200–205.

  > | Prize | Amount | Count | Total |
  > | --- | --- | --- | --- |
  > | Grand prize | $55,000 | 1 | $55,000 |
  > | 1st place | $10,000 | 13 | $130,000 |
  > | 2nd place | $3,000 | 13 | $39,000 |
  > | 3rd place | $2,000 | 13 | $26,000 |



- [ ] **NEAR-P03 — Payout schedule**
  Source: `inputs/near-2026.txt` lines 96–96.

  > **Q-016. Payout schedule?** Single payment, no vesting, within 30 days of results.



- [ ] **NEAR-P04 — Track choices — include all applicable ids, still one project entry**
  Source: `inputs/near-2026.txt` lines 174–174.

  > Put the `id` of every track the project fits in the `tracks` array of the submission. It is still one submission per project.



- [ ] **NEAR-TR01 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 182–182.

  > | `defi` | Unstoppable DeFi | Build exchanges, perps, lending, vaults and trading agents that settle across chains through NEAR Intents. Deep liquidity, no custodian, nobody to switch it off. | TRADING, NEAR INTENTS, CHAIN SIGNATURES | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/01-defi.md |



- [ ] **NEAR-TR02 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 183–183.

  > | `thesis` | Investment Thesis | Build a long-term investment thesis for NEAR and back it with data: onchain analytics, live dashboards and models anyone can re-run. Judged on the evidence, not the conviction. | ONCHAIN DATA, DASHBOARDS, RESEARCH | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/02-thesis.md |



- [ ] **NEAR-TR03 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 184–184.

  > | `privacy` | Privacy & Private AI | Explore confidential computation, private finance and AI that protects sensitive data. Build intelligence without exposure. | PRIVATE AI, TEE, NEAR AI CLOUD | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/03-privacy.md |



- [ ] **NEAR-TR04 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 185–185.

  > | `business` | Autonomous Business | Build AI-native businesses with treasury, sales, procurement, cross-chain payments via NEAR Intents and revenue sharing. Humans only set the constraints. | AI AGENTS, NEAR INTENTS, CHAIN SIGNATURES | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/04-business.md |



- [ ] **NEAR-TR05 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 186–186.

  > | `swarms` | AI Swarms | Build coordination markets, bidding, collective purchasing, intent-based settlement and emergent economies between agents. | MULTI-AGENT SYSTEMS, NEAR INTENTS, SUB-ACCOUNTS | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/05-swarms.md |



- [ ] **NEAR-TR06 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 187–187.

  > | `security` | AI Security & Defense | Build spending limits, policy engines, sandboxed wallets, reputation and scam detection. Give AI money without giving it the keys to everything. | AGENT SECURITY, FUNCTION CALL KEYS, TEE ATTESTATION | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/06-security.md |



- [ ] **NEAR-TR07 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 188–188.

  > | `agents` | Agent Economy | Build agents that earn, spend, negotiate, hire other agents and pay for APIs, compute or data — with crypto directly or through NEAR Intents. | AGENT COMMERCE, NEAR INTENTS, CHAIN SIGNATURES | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/07-agents.md |



- [ ] **NEAR-TR08 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 189–189.

  > | `realworld` | Real-World Money | Build payroll, invoicing, remittances, merchant payments and stablecoin rails for real businesses. Something a normal company could use tomorrow. | STABLECOINS, NEAR INTENTS, META TRANSACTIONS | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/08-realworld.md |



- [ ] **NEAR-TR09 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 190–190.

  > | `games` | Games With Real Economies | Build NPCs with wallets, player-owned markets and economies that evolve without a dev patch. Judged on the game loop, not the token — bonus if players never notice the chain. | AGENT NPCS, SOCIAL LOGIN, NEAR INTENTS, NEP-245 | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/09-games.md |



- [ ] **NEAR-TR10 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 191–191.

  > | `nfts` | NFTs That Do Something | Build NFTs as accounts — assets that own money, earn royalties, hold inventory, carry credentials, memberships or access rights. Ownership with behavior. | DYNAMIC NFTS, NEP-171, SUB-ACCOUNTS | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/10-nfts.md |



- [ ] **NEAR-TR11 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 192–192.

  > | `memecoins` | Memecoins With Mechanics | Build memecoins where the meme does something — supply that reacts to the community, treasuries with rules, onchain rituals and challenges. Judged on the mechanic, not the chart. | MEMECOINS, TOKEN MECHANICS, NEP-141 | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/11-memecoins.md |



- [ ] **NEAR-TR12 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 193–193.

  > | `social` | Social Money | Build shared budgets, programmable rewards, collective ownership and reputation-based access on top of Sputnik DAO and Trezu. Don't rebuild the multisig — build what communities do with it. | SPUTNIK DAO, TREZU, NAMED ACCOUNTS | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/12-social.md |



- [ ] **NEAR-TR13 — OPTIONAL track/theme; hints not requirements**
  Source: `inputs/near-2026.txt` lines 194–194.

  > | `open` | Open Innovation | Have an idea that refuses to fit a category? Explore new ways for money, intelligence and ownership to work together. | EXPERIMENTAL, CHAIN ABSTRACTION, BUILD YOUR OWN | https://github.com/nearai/near-hackathon-prompt-examples/blob/main/tracks/13-open.md |



- [ ] **NEAR-P05 — Ownership and promotional rights**
  Source: `inputs/near-2026.txt` lines 90–90.

  > **Q-013. Organizer rights to code?** No. Team keeps all rights; organizers get non-exclusive promo rights to name, screenshots, video, repo link.



- [ ] **NEAR-P06 — UNCLEAR: separate optional sponsor/side prizes**
  No separate sponsor side-prize eligibility is specified in the saved Prizes section (lines 196–205). Partner tool listings (lines 207–233) are ecosystem resources, not evidence of mandatory integration or extra awards. Ask if additional official prize rules exist.

## Unresolved questions

- [ ] **NEAR-U01 — UNCLEAR — exact hosted-demo cutoff time**
  Source: `inputs/near-2026.txt` lines 88–88.

  > **Q-012. Local-only demo OK?** Yes: public repo, reproducible README, X post with a video; screenshots are not enough when judges cannot open the demo. Hosted demo is a plus; keep it up to 2026-11-18, ideally 2026-11-25.

  Dates are supplied, hours are not. “All times are UTC” at line 37 does not supply a missing time. Ask for cutoff times if uptime compliance matters.

- [ ] **NEAR-U02 — UNCLEAR — coding window versus official event/submission start**
  Source: `inputs/near-2026.txt` lines 66–66.

  > **Q-001. Code before 2026-11-01?** Yes, from the announcement on 2026-10-19 (https://x.com/nearprotocol/status/2112257967818997891). The window runs from then to 2026-11-14. Earlier commits are baseline.

  Earlier coding allowed from 2026-10-19 announcement; Facts line 20 says event starts 2026-11-01T00:00:00Z. These concern different windows, not permission for early submission (NEAR-D02). The allowed coding-start hour is unspecified. Ask if a precise baseline cutoff is needed; do not guess.

- [ ] **NEAR-U03 — UNCLEAR: missing age/geographic/exclusion policy**
  The supplied Rules section (lines 62–98) does not state age, geographic, sanctions or organizer-affiliation exclusions. Do not import Switch rules or assert unrestricted eligibility. Ask for official eligibility terms.

- [ ] **NEAR-U04 — UNCLEAR: live changes and complete judging policy**
  Live retrieval did not succeed. Source line 4 warns:

  > Instructions for the AI coding agent helping a team take part in NEAR HACKATHON. The live version is https://nearhackathon.com/HACKATHON.md; read it again before submitting, because dates and rules may change.

  Ask the room for a fresh official saved file/pasted update and any full rubric before final submission. The saved API contract is available and extracted; no missing Switch form fields are imported into NEAR.
