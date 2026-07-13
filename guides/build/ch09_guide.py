# Chapter 9 Study Guide — Informal Reports (built to 25pp standard)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(9, 'Informal Reports',
    'Progress, incidents, minutes, and recommendations — the documents that carry facts to decisions.')

h1(doc, 'How to use this guide')
para(doc, 'Unit 4 begins the long-form genres: documents with sections, evidence, and readers who '
    'act on them. This chapter covers the informal report family — everything from the weekly '
    'status to the recommendation memo — and the structural engine underneath all of them, the '
    'pyramid. Read with a real report beside you (one you must write, or one you recently '
    'received), and apply each section to it as you go. The practice bank and your market-research '
    'assignment both draw directly on this material.')

h1(doc, 'The report family: informational and analytical')
figure(doc, os.path.join(FIG, 'ch9_family.png'),
    'Figure 1. The informal report family: informational reports say what is; analytical reports argue what should be.',
    'Report family map: informal reports divide into informational (reporting what is — progress, trip, meeting minutes, incident) where the reader asks what happened, and analytical (recommending what should be — justification, feasibility, comparison) where the reader asks what should we do. The test: a report ending in a recommendation follows analytical rules.')
para(doc, 'Every informal report answers one of two reader questions. Informational reports answer '
    '“what happened?” — the progress update, the trip report, the minutes, the incident record. '
    'Their virtues are accuracy, completeness proportionate to stakes, and findability: they are '
    'the organization’s sensory system, and they succeed when a reader far from the events can '
    'reconstruct what matters. Analytical reports answer “what should we do?” — the '
    'justification, the comparison, the feasibility study your capstone builds toward. They '
    'inherit every informational virtue and add the persuasive machinery of Chapter 8: a '
    'recommendation, reasons, evidence, and the objections answered. The boundary test is the '
    'ending: if your report concludes with a recommendation, it is analytical no matter how much '
    'reporting it contains — and the analytical rules (answer first, pyramid structure) govern.')
para(doc, '“Informal” describes the container, not the care: informal reports travel as email, '
    'memo, or a few headed pages rather than with covers and transmittal letters (Chapter 10’s '
    'formal apparatus). The thinking standards are identical — a three-paragraph recommendation '
    'memo that moves $50,000 deserves every discipline in this guide.', bold_lead='A word on “informal.”')

h1(doc, 'The engine: conclude first, then structure')
figure(doc, os.path.join(FIG, 'ch9_pipeline.png'),
    'Figure 2. The report pipeline: define the question, gather, conclude — then structure the case, then draft.',
    'Report pipeline in five steps: define the question the report answers, gather data and evidence, conclude — reach the answer before structuring — then pyramid the material (answer, reasons, evidence), then draft and revise using chapters three and four.')
para(doc, 'The deepest report-writing error happens before any writing: structuring the document '
    'as the story of the investigation (“first we looked at… then we considered…”) instead of '
    'as the case for its conclusion. Chapter 3 named this the archaeology problem; reports are '
    'where it does the most damage, because reports are long enough for the reader to get lost in '
    'the dig. The pipeline’s discipline is the third step: reach your conclusion BEFORE you '
    'structure — in one sentence, written down, tested against Chapter 2’s purpose template. '
    'Only then decide the architecture. Writers who structure before concluding produce documents '
    'that wander toward an ending; writers who conclude first produce documents where every '
    'section knows its job.')

h1(doc, 'The pyramid principle')
figure(doc, os.path.join(FIG, 'ch9_pyramid.png'),
    'Figure 3. The pyramid: the answer on top, grouped reasons beneath, evidence beneath those (Minto, 2009).',
    'Pyramid structure: the answer — renew with TechServe — at top; three grouped reasons beneath it (cost saves $22K a year, risk of switching exceeds savings, quality of support beats all bidders); evidence, data, exhibits, and sources beneath each reason.')
para(doc, 'The structural idea that organizes consulting reports, executive memos, and every '
    'well-built recommendation is Barbara Minto’s pyramid (Minto, 2009): the answer at the top; '
    'beneath it, the two-to-four grouped reasons that support it; beneath each reason, its '
    'evidence. Three properties make the pyramid work. Vertical logic: each layer answers the '
    'question the layer above provokes — the answer provokes “why?”, the reasons provoke “how do '
    'you know?”, the evidence answers. Horizontal logic: reasons at the same level must be the '
    'same KIND of thing (Chapter 3’s parallel altitude) and, ideally, mutually exclusive and '
    'collectively exhaustive — no overlaps, no gaps; “cost, risk, quality” covers a vendor '
    'decision; “cost, price, budget” is one reason wearing three names. And the summit '
    'discipline: the top of the pyramid is a genuine answer (“renew with TechServe”), never a '
    'topic (“vendor analysis”) — if your summit is a noun phrase, you have a filing label, not a '
    'conclusion.')
para(doc, 'The pyramid also generates your document mechanically: the summit becomes the opening '
    'and the subject line; the reasons become the headings, in decision-weight order; the '
    'evidence becomes the body under each heading; and anything supporting no reason gets cut or '
    'exiled to an appendix. Students who internalize this one figure stop asking “how should I '
    'organize my report?” forever — the answer is always: build the pyramid, then transcribe '
    'it.', bold_lead='From pyramid to pages.')

h1(doc, 'The progress report: cadence, candor, and the status line')
figure(doc, os.path.join(FIG, 'ch9_progress.png'),
    'Figure 4. The progress report skeleton: status line, done, in progress, blocked/risks, next + ask.',
    'Progress report skeleton: a one-sentence status line with no suspense; done items with dates; in-progress work with expected completion; blocked items and risks with what threatens the date and what is needed; next period’s plan plus any decision needed from the reader.')
para(doc, 'The progress report is the workhorse of organizational trust, and Chapter 5’s cadence '
    'rules govern its rhythm: fixed schedule, fixed skeleton, deltas over restatements. The '
    'skeleton’s crown is the status line — one sentence, first position, answering the only '
    'question every reader brings: are we on track? “On track for Aug 16 go-live” or “At risk: '
    'vendor certification slipped — recovery plan below” — either way, no suspense (the '
    'archaeology problem’s smallest habitat is the status report that makes its reader hunt for '
    'the verdict). The BLOCKED section carries the report’s integrity: Chapter 7’s MUM research '
    'predicts exactly what happens to progress reports — risks get softened, slips get deferred '
    '“one more week,” and green dashboards precede red surprises. The professional’s edge is the '
    'honest yellow: named early, paired with a plan, calibrated precisely. Readers audit '
    'retrospectively — when a project fails, its old status reports get reread, and the author '
    'who called the risk in week three owns the credibility that the week-eleven optimist spent.')

h1(doc, 'Minutes: the decision record, not the transcript')
figure(doc, os.path.join(FIG, 'ch9_minutes.png'),
    'Figure 5. Minutes that matter: decisions, owners, deadlines, open questions — one page, same day.',
    'Comparison of transcript minutes — who said what in order, long, late, unread, occasionally dangerous — versus decision minutes: decisions, owners, deadlines, and open questions on one page, sent the same day.')
para(doc, 'Meeting minutes fail in two directions. The transcript — who said what, in order — '
    'is long, late, unread, and occasionally dangerous (the recorded stray remark that becomes '
    'Exhibit A; Chapter 5’s permanence gradient applies to minutes doubly). The void — no '
    'minutes at all — produces five private versions of one meeting (Chapter 1’s frame-of-'
    'reference problem at group scale) and the eventual dispute about what was agreed. The craft '
    'is decision minutes: decisions made (verbatim where wording matters), owners and deadlines '
    'for each action, open questions explicitly parked, and attendance — one page, sent the same '
    'day while memories still match (Chapter 6’s confirmation logic, scaled to the room). Two '
    'operating rules: the minute-taker is a role, not a status (rotate it, and never make it the '
    'only woman in the room by default — a pattern research and common observation both flag), '
    'and contested wording gets resolved IN the meeting (“let me read back the decision as I’ll '
    'record it”) rather than litigated by email afterward.')

h1(doc, 'The incident report: grammar as a safety system')
figure(doc, os.path.join(FIG, 'ch9_incident.png'),
    'Figure 6. Incident anatomy: what happened, impact, root cause, corrective actions with owners, prevention.',
    'Incident report anatomy: what happened in time order with actors named; impact including injuries, downtime, product, and exposure; root cause traced honestly rather than stopped conveniently; corrective actions each with an owner and a date; and prevention — the system change that makes recurrence hard.')
para(doc, 'Chapter 3’s case introduced the incident report that named no one; here is the full '
    'genre. The sequence: what happened, in time order, with actors named — active voice is not '
    'stylistic here but functional, because organizations can only fix what the grammar admits '
    'happened. Impact, quantified: downtime, product lost, exposure created. Root cause, traced '
    'honestly: the discipline is refusing the convenient stop — “technician error” is where lazy '
    'investigations park, one “why?” short of the training gap, staffing pattern, or design flaw '
    'that produced the error and will produce the next one. Corrective actions, each with an '
    'owner and a date — “corrective measures have been identified” is the passive-camouflage '
    'tell that nothing will change. And prevention: the system change that makes recurrence hard, '
    'which is the sentence auditors, regulators, and Chapter 6’s customers all read first. Tone '
    'discipline: incident reports written to assign blame get gamed (the MUM effect '
    'institutionalized — future incidents go unreported); reports written to fix systems get '
    'fed. The organizations with the best safety records are not the ones with the fewest '
    'incidents to report; they are the ones whose reporting is safe enough to be complete.')

h1(doc, 'The justification report: your first analytical genre')
para(doc, 'The justification/recommendation report is Chapter 8’s proposal skeleton wearing report '
    'structure, and it is the analytical genre you will write most. The architecture, direct from '
    'the pyramid: the recommendation with its strongest number, first (“Replace the Lab 2 '
    'centrifuge with the Beckman Coulter X-30R — $28,570 installed, payback inside seven '
    'months”); the reasons as headings in decision-weight order (Cost · Risk · Capability); '
    'evidence under each, concrete to Chapter 4’s checkable standard; the alternatives considered '
    '— including doing nothing — each with the honest reason it lost (the two-sided credibility '
    'move: a recommendation that considered no alternatives reads as a preference wearing a '
    'report); and the ask, dated (approval, budget line, signature). Length follows stakes, not '
    'ego: a one-page justification that moves the decision is senior work; the twelve-page '
    'version that proves effort is the archaeology problem with a table of contents.')

h1(doc, 'Data displays: tables, charts, and the one-point rule')
figure(doc, os.path.join(FIG, 'ch9_tablechart.png'),
    'Figure 7. Table for exact values, chart for shape — and either way, the display makes one point.',
    'Table versus chart chooser: tables when readers need exact values (lookup, comparison of specifics, audit trails); charts when readers need shape (trend, proportion, outlier, at-a-glance comparison). Either way: the title states the takeaway, units are labeled, sources named, axes start at zero unless clearly marked.')
para(doc, 'Reports carry numbers, and numbers need vehicles. The chooser: tables serve readers who '
    'need exact values — lookup, line-item comparison, audit; charts serve readers who need '
    'shape — trend, proportion, outlier. The craft canon (Tufte, 2001; Few, 2012) compresses to '
    'principles you can apply this week. One display, one point: a chart trying to show four '
    'things shows none — split it. The title carries the takeaway: “Figure 2: Response times '
    'fell 41% after barcode intake” informs even readers who never parse the bars; “Figure 2: '
    'Response Time Data” informs no one (Chapter 3’s informative headings, wearing axes). '
    'Integrity mechanics: axes start at zero for bar charts or announce loudly that they don’t '
    '(the truncated axis is the most common honest-numbers-dishonest-picture trick in business); '
    'units and periods on every axis; sources named; and the data-ink discipline — gridlines, '
    '3-D effects, and decoration compete with the point (Tufte’s enduring insult for it: '
    '“chartjunk”). Finally, integration: every exhibit is referenced in the text by its point '
    '(“as Figure 2 shows, the drop followed the intake change”), because an unreferenced exhibit '
    'is cargo the reader must unload alone.')

h1(doc, 'Research corner: why answer-first feels wrong and works')
para(doc, 'Writers resist the pyramid for a predictable reason: having worked through the '
    'analysis, they want the reader to experience the journey — the careful method, the '
    'considered alternatives, the earned conclusion. The resistance is narratively sound and '
    'cognitively backward. Working memory is small (Miller, 1956): a reader holding your '
    'unresolved question while wading through method retains fragments; a reader given the '
    'answer first converts everything after into confirmation or challenge — active processing '
    'against a known claim, which is both faster and more rigorous. This is also why answer-first '
    'documents generate better meetings: attendees argue with the recommendation instead of '
    'asking what it is. The journey has a home — the appendix, where the scrutinizer (Chapter 2) '
    'can audit your method after the summit convinced or provoked them. Trust the structure: '
    'the pyramid does not skip your work; it files it where each reader can find their layer.')

h1(doc, 'Worked example: one dataset, three documents')
para(doc, 'To see the family’s boundaries, watch one situation produce three different reports. '
    'The facts: your lab’s instrument downtime spiked in Q2; you investigated; the three oldest '
    'instruments caused 70% of it; a refurbishment contract costs $18,000 against $41,000 of '
    'annualized downtime cost.')
para(doc, 'As an informational report (the investigation summary): status line — “Q2 downtime '
    'traced: three instruments account for 70%.” Then the findings in importance order, the '
    'method in two sentences, the data table with the takeaway title. No recommendation; the '
    'reader asked what happened.', bold_lead='Version one.')
para(doc, 'As an analytical report (the justification): “Recommendation: refurbish instruments '
    '3, 7, and 9 under the vendor’s $18,000 contract — eliminating an estimated $29,000 of the '
    '$41,000 annual downtime cost.” Reasons as headings: Cost (payback in 7.4 months), Risk '
    '(failure trend is accelerating — Figure 1), Alternatives (replacement at $84,000 loses on '
    'payback; doing nothing books the $41,000). The same data, now employed by a conclusion.',
    bold_lead='Version two.')
para(doc, 'As a progress report entry (three weeks later): “At risk: instrument refurbishment — '
    'vendor’s parts delay pushes completion from Aug 2 to Aug 16; interim coverage arranged with '
    'Lab 4; no impact on client deliverables expected. Need from you: nothing yet; escalation '
    'call Thursday if the parts slip again.” The project the analysis launched, now reporting '
    'itself with Chapter 7’s honesty.', bold_lead='Version three.')
para(doc, 'One dataset, three genres, three architectures — selected by the reader’s question, '
    'never by the writer’s momentum. That selection is the chapter in one sentence.',
    bold_lead='The lesson.')

h1(doc, 'Deep dive: writing about uncertainty')
para(doc, 'Reports traffic in findings, and findings come with confidence levels the prose must '
    'carry honestly — a skill science writing formalized and business writing chronically fakes. '
    'The calibration vocabulary: “the data shows” (reserved for what the data actually shows), '
    '“the data suggests” (directional but underpowered), “we estimate” (a model with '
    'assumptions — name the load-bearing ones), “we believe” (judgment beyond the data — '
    'legitimate and labeled). Ranges beat points wherever knowledge is a range: “payback in 6–9 '
    'months depending on Q4 volume” is checkable and honest; “payback in 7.4 months” projected '
    'on three assumptions is Chapter 4’s false precision wearing a decimal. Caveats belong WITH '
    'their claims, not herded into a limitations paragraph nobody reads — “downtime cost '
    'assumes Q2’s client mix holds” travels next to the $41,000 it conditions. And the summit '
    'rule from the FAQ deserves its full statement: when the honest conclusion is conditional, '
    'structure the condition — “Refurbish IF the August audit passes instrument 7; replace if '
    'it fails; the decision point is August 12” is a pyramid with a branch, and executives '
    'trust branched answers from calibrated writers far more than clean answers from optimists. '
    'Your lab training already knows all this as significant figures and error bars; business '
    'writing is the same integrity, wearing sentences.')

h1(doc, 'Deep dive: the recurring institutional report')
para(doc, 'Beyond projects live the reports that recur by calendar: the monthly departmental, the '
    'quarterly compliance filing, the annual review input. Their special physics: nobody reads '
    'them closely until something goes wrong, and then they are read forensically — which sets '
    'the design brief. Optimize for the two reading modes simultaneously: a skimmable delta '
    'summary up top (“three changes from last quarter: …”) for the routine reader, and rigorous '
    'consistent detail beneath for the forensic one. Consistency is the compounding asset: '
    'identical structure, metrics, and definitions each period make trends visible and '
    'anomalies loud (a metric that quietly changes definition mid-year is a small lie with '
    'large forensic consequences). Automate the assembly where possible — the data pulls, the '
    'tables — and spend the recovered time on the one section automation cannot write: the '
    '“what this means” paragraph, where the period’s numbers become the department’s judgment. '
    'The recurring report you inherit is also a renovation opportunity: the sections nobody '
    'has read in years (test: ask) are candidates for the appendix or the axe, and the '
    'questions leadership actually asks each quarter are the sections it is missing.')

h1(doc, 'Report workshop: five repairs (answers follow)')
numbered(doc, [
    'Summit check: “Subject: Q2 Instrument Analysis. This report presents an analysis of instrument downtime patterns observed during the second quarter…”',
    '“The project is progressing well overall. The team has been working hard on multiple fronts. Some challenges have emerged but are being addressed. We remain optimistic about the timeline.”',
    'Reasons audit: a justification’s headings read — “1. Cost Savings. 2. Financial Benefits. 3. Budget Impact. 4. The Vendor’s Reputation.”',
    'Minutes excerpt: “Dana felt strongly that the deadline was unrealistic. Marcus disagreed, citing the client contract. After extended discussion of various perspectives, the group moved toward consensus.”',
    'Chart title: “Figure 3: Downtime Data by Instrument (2024–2026).” The chart shows three old instruments causing most downtime.',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    'Topic summit — a label where an answer belongs. Repair: “Subject: Three instruments cause 70% of Q2 downtime — refurbishment recommended ($18K, 7-month payback).” The report is now readable from its subject line.',
    'A status report with no status: four sentences of texture, zero verdicts, “challenges” unnamed. Repair: the skeleton — status line, done-with-dates, the named yellow with its plan, the ask.',
    'MECE failure: headings 1–3 are one reason (money) in three costumes, and #4 is a different KIND of thing (evidence, not a reason). Repair: “Cost · Risk · Capability,” with the vendor’s track record as evidence under Risk.',
    'Transcript minutes drifting toward hazard — feelings recorded, decision missing. Repair: “DECIDED: deadline holds at Aug 16 (client contract governs). Dana’s staffing concern logged as risk; mitigation (temp coverage) owner: Marcus, plan due Friday.”',
    'Topic title on a chart with a point. Repair: “Figure 3: Three pre-2019 instruments caused 70% of downtime — and their share is growing.” The reader who reads nothing else now knows the finding.',
])

h1(doc, 'Templates appendix: three reports to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. The weekly status (email-scale)')
para(doc, '“Subject: Beckman rollout — on track for 8/16 (1 yellow). STATUS: on track. DONE: '
    'validation protocol approved (Tue); Line 2 staff trained (Thu). IN PROGRESS: parallel '
    'testing, completes 8/9. YELLOW: vendor’s parts shipment now 8/4 — no date impact if it '
    'holds; escalation call scheduled if it slips past 8/6. NEED FROM YOU: nothing this week.”')
h2(doc, '2. The one-page justification')
para(doc, '“RECOMMENDATION: refurbish instruments 3, 7, 9 under vendor contract — $18,000 '
    'against $41,000/yr downtime cost; payback ~7 months. COST: [two lines + table ref]. RISK: '
    'failure trend accelerating (Fig. 1); doing nothing books the $41K and the audit exposure. '
    'ALTERNATIVES: replacement ($84K, 2.4-yr payback — loses); do nothing (costed above). ASK: '
    'approve by 7/25 — vendor’s Q3 slot closes.”')
h2(doc, '3. Decision minutes')
para(doc, '“MEETING: Beckman steering, 7/18, 30 min. Attending: [names]. DECIDED: (1) go-live '
    'holds at 8/16; (2) refurbishment approved at $18K (motion: Reyes). ACTIONS: parts PO — '
    'Dana, by 7/21; interim coverage plan — Marcus, by 7/25. PARKED: Lab 4 consolidation '
    'question → September agenda. Next meeting: 8/1.”')

h1(doc, 'Put it to work this week')
numbered(doc, [
    'Take any report you must write and complete the pipeline’s step three first: the conclusion, one sentence, on paper, before any structure.',
    'Convert your next meeting’s notes into decision minutes within two hours. Send them.',
    'Add one honest yellow to your next status update — the risk you were saving for later.',
    'Retitle every exhibit in your current document as a takeaway. Notice which charts turn out to have no point.',
    'Cost the “do nothing” alternative for any pending recommendation. It is usually your strongest paragraph.',
])

h1(doc, 'Case study 1: the dashboard that lied politely')
para(doc, 'A software implementation team reports monthly to a steering committee via a one-page '
    'dashboard: green/yellow/red per workstream. For five months, everything is green — the '
    'project manager reasons each yellow-ish item is “about to resolve” and “not worth alarming '
    'the committee.” In month six, the integration workstream goes directly from green to red: '
    'the vendor interface, quietly behind since month two, cannot be ready for the contracted '
    'go-live. The committee is blindsided; an executive asks the obvious question — “how does a '
    'project go from all-green to failing in thirty days?” — and the honest answer is: it '
    'didn’t. The PM’s private tracker, subpoenaed by the post-mortem, shows the interface flagged '
    'internally for four months.')
numbered(doc, [
    'The PM never wrote a false sentence — each month’s green was a judgment call. Where exactly did the reporting become dishonest, and which discipline from this chapter marks the line?',
    'Rewrite month three’s dashboard entry for the integration workstream using the honest-yellow pattern: status, threat, plan, ask.',
    'The committee also owns part of this failure. What behaviors from Chapter 7 (receiving bad news) and Chapter 16 (rewarding messengers) would have changed what the PM sent?',
    'Design the dashboard rule that makes this failure structurally hard — a definition of green a “judgment call” cannot stretch.',
])
h2(doc, 'Case analysis')
para(doc, 'The dishonesty lives not in any sentence but in the calibration: “green” drifted from '
    '“on track” to “I believe I can still fix this quietly” — the MUM effect wearing a status '
    'color (Rosen & Tesser, 1970). The line this chapter draws is the status line’s contract: '
    'status reports exist to transfer the writer’s knowledge of risk to the reader while the '
    'risk is still cheap, and any reporting convention that lets private worry stay private has '
    'broken the genre’s one promise. The honest month-three entry: “YELLOW — vendor interface: '
    'two-sprint slip on the mapping layer; vendor added staff, recovery plan targets month five; '
    'the go-live date is safe if the May milestone holds — flagging now so a June decision, if '
    'needed, isn’t a surprise.” Note it protects the PM too: the yellow that precedes a red is '
    'diligence; the green that precedes it is the career event. The committee’s share: bodies '
    'that greet yellows with interrogations manufacture greens (the incentive design from '
    'Chapter 16), and the structural fix is a definition of green with teeth — “green = all '
    'milestones met AND no known risk to the next one” — plus the standing question that makes '
    'candor routine: “what’s the yellowest thing in your green?”')

h1(doc, 'Case study 2: the trip report nobody could use')
para(doc, 'Two sales engineers attend the industry’s largest trade show on the company’s dollar. '
    'Engineer A’s trip report, filed a week later: four pages, chronological — the flights, the '
    'booth setup, sessions attended day by day, “productive conversations” with named companies, '
    'a closing paragraph calling the show “valuable overall.” Engineer B’s, filed the morning '
    'after returning: one page. “Three findings that matter: (1) Competitor X is shipping '
    'barcode intake in Q4 — two customers confirmed pilots; our eighteen-month roadmap '
    'assumption is dead. (2) Meridian Labs (booth conversation, contact attached) wants a joint '
    'validation study — decision needed on pursuing by the 15th, their planning deadline. '
    '(3) The compliance session previewed the FDA draft guidance — the amendment-log requirement '
    'lands harder on us than expected; summary attached. Everything else was a trade show.” Six '
    'months later, guess which document shaped the product roadmap — and which engineer briefs '
    'the executive team before the next show.')
numbered(doc, [
    'Diagnose Engineer A’s report against the pipeline (Figure 2): which step was skipped, and what did the chronology cost?',
    'Engineer B’s report is organized by a principle. Name it, and connect it to the pyramid’s summit discipline.',
    'B’s report was also FASTER to write. Explain why answer-first documents are usually cheaper to produce, not just to read.',
    'Draft the one-line trip-report policy you would set for a team, and the skeleton you would attach to it.',
])
h2(doc, 'Case analysis')
para(doc, 'Engineer A skipped the conclude step: the report structures the trip (time order) '
    'because no conclusion was ever reached about what the trip MEANT — chronology is what '
    'writers reach for when they have not decided what matters (Chapter 3’s meta-rule, '
    'confirmed). The cost is total: four pages containing the same three findings, distributed '
    'where no skimming reader will assemble them. Engineer B organized by decision-relevance — '
    'the pyramid’s summit test applied ruthlessly (“three findings that matter” is an answer; '
    '“trip report” is a label) — and wrote faster because selection did the work compression '
    'never can: deciding what mattered took one hard thought; narrating everything took A a '
    'week of easy ones. The policy: “Trip reports are due within 48 hours, one page, organized '
    'as findings-that-matter with actions and deadlines attached; the itinerary is not a '
    'finding.” The deeper lesson travels beyond trip reports: every document you file is a '
    'sample of your judgment, and judgment is precisely the skill of knowing what matters. '
    'Reports display it — or its absence — more nakedly than any genre in this course.')

h1(doc, 'Deep dive: the same report, three altitudes')
para(doc, 'Reports travel vertically, and each altitude reads for different cargo. Reporting up, '
    'the executive layer wants the decision-relevant compression: the summit, the strongest '
    'number, the risk that could reach them, and the ask — one page or less, because their '
    'unit of attention is the meeting between meetings (Chapter 2’s skimmer, holding budget '
    'authority). Reporting across, peers and partner teams want the operational interface: what '
    'changes for them, when, and what you need from them — the coordination cargo that '
    'executive summaries omit. Reporting down — sharing your report with the team whose work '
    'it describes — is the altitude writers forget: the team reads for fairness (is our work '
    'represented accurately? who gets credit?) and for foreshadowing (what does this '
    'recommendation mean for our jobs?). One report can serve all three with layered design '
    '(summary → sections → appendix), but know which altitude is PRIMARY before writing, '
    'because the summit changes: “approve $18K” (up), “instrument downtime will drop 70% after '
    'August” (across), “your Q2 data made this case — here’s what happens next” (down). The '
    'report that serves no particular altitude serves none at all, which is the fate of most '
    'reports written “for the file.”')

h1(doc, 'Deep dive: getting your report actually read')
para(doc, 'A report competes for attention like every message (Chapter 5’s economics), and good '
    'internal marketing is legitimate craft, not vanity. The delivery package: a transmittal '
    'note that IS the executive summary (“attached: the instrument analysis — bottom line, '
    'refurbishing three units saves $23K/yr; decision needed by 7/25”), never “please find '
    'attached the report” (a naked attachment with a fossil escort). Timing: land it when the '
    'decision is live — the perfect report delivered after the budget meeting is archival; two '
    'days before, it is agenda-setting. The pre-brief: for consequential recommendations, walk '
    'the key decision-maker through the summit BEFORE wide distribution (Chapter 8’s '
    'pre-wiring) — surprises in meetings generate defensiveness, not approval. The follow-up: '
    'a report without a scheduled next touch (“I’ll bring this to Thursday’s ops meeting for '
    'the decision”) is a message in a bottle. And the meta-signal of length: a thick report '
    'signals thoroughness to exactly no one anymore; the one-pager with a rigorous appendix '
    'signals judgment plus depth — the combination that gets both read AND trusted.')

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Hans Rosling, “The best stats you’ve ever seen” (TED).', 'The most famous data presentation ever given — watch how every display makes exactly one point, loudly.'),
    ('David McCandless, “The beauty of data visualization” (TED).', 'Context and comparison as the source of meaning in numbers — the framing half of this chapter’s data section.'),
    ('Ben Wellington, “Making data mean more through storytelling” (TEDx).', 'A data scientist on why analyses fail without an answer-first story — the pyramid, discovered independently.'),
])

h1(doc, 'Deep dive: the feasibility question — this unit’s destination')
para(doc, 'Your capstone is a feasibility study, and its intellectual engine is a specialized '
    'analytical report worth previewing now. A feasibility study answers one question — can '
    'this work, and should we do it? — across four standard dimensions: technical feasibility '
    '(can it be built/done with available capability?), economic feasibility (do the numbers '
    'clear the bar — cost, benefit, payback?), operational feasibility (will it work HERE, '
    'with these people, processes, and politics?), and schedule feasibility (can it land when '
    'it must?). The pyramid’s summit for a feasibility study is always one of three verdicts: '
    'feasible (proceed, with the path), feasible-with-conditions (the branch structure from the '
    'uncertainty section — “viable if X; the decision point is [date]”), or not feasible (with '
    'the honest identification of which dimension kills it — usually more valuable than a '
    'forced yes). The classic student error is treating feasibility as advocacy: the study that '
    'was always going to say yes, gathering only confirming evidence (the advocacy line, '
    'crossed at term-paper scale). Graders and executives read for the same tell: does the '
    'operational section contain real friction? Does the economics section stress-test its own '
    'assumptions? A feasibility study that found no serious obstacles didn’t look — and its '
    'author’s judgment, not the project’s merits, becomes the finding.')

h1(doc, 'Deep dive: from informal to formal — knowing when to escalate the container')
para(doc, 'This chapter’s genres travel light; Chapter 10 adds covers, transmittals, tables of '
    'contents, and front matter. The escalation triggers are worth knowing now, because choosing '
    'the container is part of the craft: escalate to formal when the audience crosses '
    'organizational boundaries (clients, regulators, boards — external readers expect the '
    'apparatus, and its absence reads as casualness about them); when the document’s lifespan '
    'is long (the study that will be cited for years earns the navigation aids a three-week '
    'memo doesn’t need); when the length demands it (past roughly ten pages, a table of '
    'contents stops being ceremony and starts being usability); and when the stakes ritualize '
    'it (funding decisions and compliance filings have expected forms, and violating form '
    'distracts from content). The mistake in both directions costs: the formal apparatus '
    'wrapped around a two-page recommendation is bureaucratic theater that delays its own '
    'reading, while the forty-page client feasibility study delivered as a naked email '
    'attachment squanders authority the work earned. The engine never changes — pyramid, '
    'evidence, honest display — which is why Chapter 10 will feel like an upgrade kit rather '
    'than a new machine.')

h1(doc, 'Deep dive: co-authored reports — one voice from many hands')
para(doc, 'Your market-research and feasibility work is team-written, and multi-author reports '
    'have a signature failure: the seams. Section two contradicts section four’s numbers; the '
    'tone lurches from academic to breezy at each handoff; three writers define the same term '
    'three ways. The disciplines that produce one voice: pyramid together, draft apart — the '
    'team builds the summit, reasons, and section assignments in one sitting (disagreements '
    'about the conclusion are cheap at the whiteboard and catastrophic at page nine); one data '
    'dictionary — shared definitions and a single source-of-truth spreadsheet before anyone '
    'types (Chapter 4’s consistency check, made structural); one finishing editor — after '
    'sections merge, a single hand runs the full three-pass revision on the whole document, '
    'with the mandate to normalize voice (rotating this role across assignments teaches '
    'everyone the skill); and the read-through meeting — the team reads the assembled draft '
    'together, aloud where contested, before submission, because seam errors are invisible to '
    'their authors and obvious to the room. Allocate the finishing time in the plan: teams '
    'that budget zero hours between “sections done” and “due” submit stapled drafts and call '
    'them reports — and every grader and every executive can tell.')

h1(doc, 'Deep dive: analysis or advocacy — the report writer’s line')
para(doc, 'Analytical reports live on a tension this course has met before (Chapter 2’s tailoring '
    'ethics, Chapter 8’s truth tests): you reached a conclusion, you want it adopted, and you '
    'control what the reader sees. Where does building the case end and cooking it begin? The '
    'analytical standard: the report presents the evidence that would let a competent skeptic '
    'reach YOUR conclusion — which requires including the evidence that gave you pause. The '
    'advocacy failure modes, each survivable by discipline: selection bias (the unfavorable '
    'data point that “didn’t fit” — include it, with your reasoning for why it doesn’t govern); '
    'the strawman alternative (comparing your recommendation against the worst version of the '
    'competitor — cost the strongest alternative, or the scrutinizer will, in the meeting); '
    'precision theater (decimals implying certainty the assumptions can’t back — Chapter 4); '
    'and the buried assumption (the payback math that quietly requires Q4 volume to hold — '
    'load-bearing assumptions get named at the summit, not discovered in the appendix). The '
    'operational test: imagine the person most skeptical of your recommendation reading with '
    'full access to your data. Every gap between what they would find and what you presented is '
    'a withdrawal against your name — and analytical credibility, once spent, prices every '
    'future report you file. You are allowed to be persuasive. You are required to be '
    'complete.')

h1(doc, 'Report-writing self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'I write the conclusion in one sentence before structuring any report.',
    'My report openings answer the reader’s question, not narrate my process.',
    'My headings are informative claims a skimmer could assemble into the argument.',
    'My reasons are parallel in kind, without overlaps or gaps.',
    'My status lines carry the verdict in sentence one — including the uncomfortable ones.',
    'My risks and yellows are reported while they are cheap.',
    'My minutes record decisions, owners, and deadlines — same day.',
    'My incident writing names actors, causes, and owners in active voice.',
    'My exhibits make one point each, stated in their titles.',
    'My alternatives sections include “do nothing,” honestly costed.',
])
para(doc, 'Scoring: 16–20, you already write like the person whose reports get forwarded upward — '
    'sharpen the exhibits. 10–15, drill the conclude-first pipeline and the status line. Below '
    '10, adopt one rule: no report leaves without its answer in the first sentence. Retake after '
    'your market-research assignment. A note on weighting: the conclude-first habit (item 1) and '
    'the honest yellow (item 6) drive more career outcomes than the other eight combined, because '
    'they are the two behaviors a reader can detect from a single document. If you must triage '
    'your practice, triage there.')

h1(doc, 'The report playbook')
bullets(doc, [
    ('Weekly status →', 'fixed skeleton, status line first, honest yellows, deltas only.'),
    ('Meeting happened →', 'decision minutes, one page, same day.'),
    ('Something broke →', 'incident anatomy: facts, impact, root cause, owners, prevention.'),
    ('Money or change to justify →', 'pyramid: recommendation + number first, reasons as headings, alternatives costed, dated ask.'),
    ('Trip or conference →', 'findings-that-matter within 48 hours; the itinerary is not a finding.'),
    ('Data to show →', 'table for exact values, chart for shape, takeaway in the title, axis honest.'),
    ('Long analysis →', 'summit and reasons up front; the journey lives in the appendix for the scrutinizer.'),
])

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find the last report you wrote and locate its answer. What page is it on — and what would the pyramid version’s first sentence be?',
    'Recall a green-to-red surprise you witnessed. Reconstruct the honest yellow that was never sent, and what made sending it feel unsafe.',
    'Take any chart from your work or news feed and rewrite its title as a takeaway. What did the original title hide?',
    'Write decision minutes for the last meeting you attended — from memory, one page. What could you not reconstruct, and what does that gap teach about same-day filing?',
    'Audit a recommendation you have made (in any format) against the advocacy line: what did you leave out, and would the skeptic-with-full-access test have passed?',
    'Identify the recurring report in your world nobody reads. Interview one recipient: what question do they actually bring to it, and what would the redesigned version lead with?',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'Report assignments in this course are graded on the pipeline and the pyramid: a '
    'findable answer, reasons that parallel and exhaust, evidence at the checkable standard, '
    'honest treatment of alternatives and risks, and exhibits that make their point in their '
    'titles — plus everything Chapters 2 through 4 already require. Your market-research '
    'assignment is precisely this chapter: its required sections are a pyramid scaffold, and the '
    'grading rubric’s “clarity, research quality, analysis” maps to summit, evidence, and '
    'horizontal logic. The supervisor test at report scale: could your reader act on page one '
    'alone — and audit everything behind it?')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('Structuring the investigation instead of the case.', 'Fix: conclude first — one written sentence — then pyramid.'),
    ('The topic summit.', 'Fix: “Vendor Analysis” is a label. “Renew with TechServe” is an answer. Answers only at the top.'),
    ('Overlapping reasons.', 'Fix: the MECE check — same kind, no overlaps, no gaps. “Cost, price, budget” is one reason in three costumes.'),
    ('The suspense status report.', 'Fix: verdict in sentence one. Your reader’s first question is the report’s first answer.'),
    ('Greens that mean “probably.”', 'Fix: define green with teeth; report the yellow while it is cheap — the audit is retrospective.'),
    ('Transcript minutes.', 'Fix: decisions, owners, deadlines, open questions. One page. Same day.'),
    ('Chartjunk and topic titles.', 'Fix: one point per display, takeaway in the title, honest axes, units everywhere.'),
    ('The missing “do nothing.”', 'Fix: cost the status quo — it is always an alternative, and pricing it is usually your strongest argument.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“My manager asked for ‘a quick update,’ not all this structure.”', 'The skeleton scales down gracefully: a quick update is a status line plus one honest yellow plus an ask — three sentences, full discipline. Structure is not length; it is knowing which three sentences.'),
    ('“Doesn’t answer-first spoil the reader’s independent judgment?”', 'The opposite, in practice: a reader given your answer and reasons can locate their disagreement precisely (“I buy cost, not risk”), which is judgment operating. The reader made to assemble your case themselves mostly assembles a different one.'),
    ('“What if my data doesn’t support a clean conclusion?”', 'Then THAT is the conclusion, reported with calibration: “the data supports refurbishment weakly; the deciding factor is risk tolerance, which is a management call — here is the decision framed.” Honest uncertainty at the summit beats false confidence and beats fog; it is also rarer and more trusted than either.'),
    ('“How many exhibits is too many?”', 'Every exhibit must be referenced by its point in the text; every unreferenced exhibit is cut or appendixed. Apply that rule and the count self-regulates — most reports lose a third of their exhibits and none of their force.'),
    ('“Can AI write my reports?”', 'It can pyramid your material impressively once YOU supply the conclusion — “structure these findings under this recommendation” is a strong prompt. It cannot reach the conclusion, verify the numbers, or own the recommendation (Chapters 4 and 15). The summit is yours; the masonry can be assisted.'),
    ('“My organization’s template forces the answer to page six. Do I fight it?”', 'Work both layers: fill the template (compliance is cheap) AND add the one-paragraph transmittal note that carries your summit — the note is where the executive actually reads you. Templates constrain documents; they rarely constrain cover messages.'),
    ('“How long should a progress report take to write?”', 'Fifteen minutes, if the project is instrumented: risks logged as they emerge, decisions confirmed as they happen (Chapter 6), the skeleton fixed. Status reports that take two hours are usually reconstructing the week — the report is late-stage evidence of missing daily habits, and fixing the habits fixes the report.'),
    ('“What belongs in the appendix versus the body?”', 'The body carries what the DECISION needs; the appendix carries what VERIFICATION needs. Test each element: if the recommendation stands without it but an auditor would want it — appendix. If the recommendation leans on it — body, at checkable summary strength, with the full detail behind.'),
    ('“My conclusion changed halfway through drafting. Start over?”', 'Celebrate first — the analysis worked. Then yes, rebuild the pyramid rather than steering the old draft: a document structured for conclusion A and patched toward conclusion B keeps A’s skeleton showing, and scrutinizing readers feel the ghost. Twenty minutes of restructuring beats two hours of patching, every time.'),
    ('“How do I report on work that mostly failed?”', 'As findings — because failed approaches ARE findings: “three of four methods proved unworkable, which narrows the viable path to X” is an analytical summit with real value. The report that buries a failed quarter in passive fog (Chapter 3’s incident case) teaches nothing and fools no one; the one that prices what was learned converts sunk cost into institutional knowledge — and marks its author as safe to give hard problems.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 9).', 'Genre selection, pyramid logic, status-line craft, and display integrity.'),
    ('Market research assignment.', 'Its section requirements are a pyramid scaffold — this chapter is the assignment’s instruction manual.'),
    ('The feasibility study (capstone).', 'Chapter 10 adds the formal apparatus; the analytical engine is already in your hands.'),
    ('Group project meetings.', 'Decision minutes, adopted this week, will make your team the organized one — visibly.'),
    ('The lecture deck.', 'The Chapter 9 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Informational / analytical reports', 'reporting what is versus recommending what should be — the ending determines the rules.'),
    ('The pipeline', 'define → gather → conclude → structure → draft: conclusions before architecture.'),
    ('Pyramid principle', 'answer at top, grouped reasons beneath, evidence beneath those (Minto, 2009).'),
    ('MECE', 'mutually exclusive, collectively exhaustive — the horizontal-logic test for reasons.'),
    ('Summit discipline', 'the top of the pyramid is an answer, never a topic.'),
    ('Status line', 'the one-sentence verdict that opens every progress report — no suspense.'),
    ('Honest yellow', 'the risk reported while cheap, paired with a plan — the antidote to green-to-red surprises.'),
    ('Decision minutes', 'decisions, owners, deadlines, open questions — one page, same day.'),
    ('Root cause', 'the honest end of the why-chain, past the convenient stop of “operator error.”'),
    ('Takeaway title', 'the exhibit caption that states the point: “response times fell 41%.”'),
    ('Chartjunk', 'decoration competing with data (Tufte, 2001) — gridlines, 3-D, and noise.'),
    ('Calibration vocabulary', '“shows / suggests / we estimate / we believe” — confidence carried honestly in the verbs.'),
    ('Transmittal note', 'the cover message that IS the executive summary — where the executive actually reads you.'),
    ('The skeptic test', 'would the person most opposed, with full data access, find gaps between what exists and what you presented?'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Reports divide by the reader’s question: informational (“what happened?”) and analytical (“what should we do?”) — a recommendation ending invokes analytical rules.',
    'Conclude before structuring: the pipeline’s third step is where good reports are actually made.',
    'The pyramid organizes everything: answer at top, MECE reasons as headings, evidence beneath, journey in the appendix (Minto, 2009).',
    'Progress reports live on the status line and die on dishonest greens — report the yellow while it is cheap.',
    'Minutes record decisions, owners, and deadlines — one page, same day; transcripts serve no one.',
    'Incident reports name actors, causes, and owners in active voice — grammar is a safety system, and blame-free reporting keeps the system fed.',
    'Displays make one point each, announce it in the title, and keep their axes honest (Tufte, 2001; Few, 2012).',
    'Every report samples your judgment: what you selected as mattering is the document’s real content.',
])

quiz(doc, [
    ('A report that ends in a recommendation is:',
     ['Informational', 'Informal and therefore unstructured',
      'A transcript', 'Analytical — and the analytical rules govern']),
    ('The pipeline’s critical third step is:',
     ['Formatting', 'Concluding — before structuring',
      'Choosing fonts', 'Scheduling the meeting']),
    ('The top of the pyramid must be:',
     ['A topic, like “Vendor Analysis”', 'A greeting',
      'An answer, like “Renew with TechServe”', 'The method']),
    ('MECE reasons are:',
     ['Mutually exclusive and collectively exhaustive — no overlaps, no gaps', 'As many as possible',
      'Chronological', 'All financial']),
    ('A progress report opens with:',
     ['Background', 'Last month’s recap',
      'The team roster', 'The status line — the verdict, no suspense']),
    ('The “honest yellow” exists because:',
     ['Dashboards need color', 'Risks reported while cheap prevent green-to-red surprises — and the audit is retrospective',
      'Yellow is calming', 'Committees require it']),
    ('Decision minutes record:',
     ['Who said what, in order', 'Only action items',
      'Decisions, owners, deadlines, open questions — same day', 'The debate verbatim']),
    ('In incident reports, active voice matters because:',
     ['Organizations can only fix what the grammar admits happened', 'It is shorter',
      'Passive is ungrammatical', 'Auditors prefer style']),
    ('“Technician error” as a root cause is usually:',
     ['The end of the investigation', 'The prevention sentence',
      'Legally required', 'The convenient stop, one “why?” short of the system cause']),
    ('Choose a table over a chart when readers need:',
     ['The trend', 'Exact values — lookup, specifics, audit',
      'Decoration', 'Proportions']),
    ('An exhibit’s title should:',
     ['Name the topic: “Response Time Data”', 'Be omitted',
      'State the takeaway: “Response times fell 41%”', 'List the sources']),
    ('A truncated bar-chart axis is:',
     ['The most common honest-numbers-dishonest-picture trick — start at zero or announce loudly', 'Standard practice',
      'Required for small differences', 'Tufte-approved']),
    ('The trip report that shaped the roadmap was organized by:',
     ['Chronology', 'Expense category',
      'Session titles', 'Decision-relevance — findings that matter, with actions attached']),
    ('Answer-first documents are cheaper to WRITE because:',
     ['They are shorter', 'Selection does the work — deciding what matters replaces narrating everything',
      'Templates exist', 'AI writes them']),
], ['d', 'b', 'c', 'a', 'd', 'b', 'c', 'a', 'd', 'b', 'c', 'a', 'd', 'b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Bring a real report (yours or received). Build its pyramid on one page: what is the summit, what are the reasons, and what content supported nothing?',
    'Why do organizations reward the reporting behaviors they claim to hate — the green dashboards, the transcript minutes, the twelve-page justifications? Locate the incentive.',
    'Defend or attack: “The one-page report is harder to write and more senior than the twelve-page report.” Use the two case studies.',
    'Your team’s dashboard: design the definition of green that a “judgment call” cannot stretch, and the ritual question that keeps yellows safe.',
    'Find a chart in the wild whose design misleads despite true numbers. Name the mechanism and rebuild it honestly.',
    'Your team report is due Friday and section drafts arrive Thursday night, contradictory. Walk the recovery: what gets triaged in what order, and which of this chapter’s disciplines would have prevented the crunch?',
    'An executive says: “Nobody reads reports anymore — put everything in a dashboard.” Defend the written analytical report, conceding what dashboards genuinely do better.',
])

h1(doc, 'A closing word: the report as career instrument')
para(doc, 'Reports are the only genre in this course that routinely travels above your manager’s '
    'head with your name attached. The email stays in the thread; the presentation ends with '
    'the meeting; the report gets forwarded — to the director deciding budgets, the VP asking '
    '“who wrote this?”, the committee two levels up that will never meet you but will read '
    'four pages of your thinking. That is the quiet career mathematics of this chapter: every '
    'report is an audition you didn’t know was scheduled, judged by people you may never see, '
    'on the one dimension organizations can least fake caring about — judgment, displayed as '
    'the selection of what matters. Write the status line honestly, build the pyramid '
    'ruthlessly, cost the alternatives fairly, and title the charts with their takeaways: the '
    'skills are teachable, this chapter just taught them, and somewhere above you is a reader '
    'who has been waiting for a report like that to cross their desk.')

references(doc, [
    'Few, S. (2012). Show me the numbers: Designing tables and graphs to enlighten (2nd ed.). Analytics Press.',
    'Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97.',
    'Minto, B. (2009). The pyramid principle: Logic in writing and thinking (3rd ed.). Financial Times/Prentice Hall.',
    'Rosen, S., & Tesser, A. (1970). On reluctance to communicate undesirable information: The MUM effect. Sociometry, 33(3), 253–263.',
    'Tufte, E. R. (2001). The visual display of quantitative information (2nd ed.). Graphics Press.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch09-study-guide.docx')
finish(doc, os.path.abspath(out))
