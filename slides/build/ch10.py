# Chapter 10 — Proposals and Formal Reports (43 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 10"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Proposals and Formal Reports",
    "The documents that move money · executive summaries · RFP compliance · sources that survive scrutiny", D)
notes(s, "Chapter 10: the formal apparatus. Everything from Chapter 9's pyramid, plus front matter, back matter, and the compliance game.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Map", "any proposal onto the quadrants — solicited/unsolicited, internal/external — and know which burden of proof you carry."),
    ("Build", "the six-part proposal skeleton: problem, solution, plan, staffing, budget, risks."),
    ("Win", "the RFP compliance game: their structure, their checklist, their deadline — before your brilliance is even read."),
    ("Assemble", "a formal report's three layers — front matter, body, back matter — for three different readers."),
    ("Write", "the executive summary last, place it first, and make it stand alone."),
    ("Grade", "every source on the credibility ladder and cite it with integrity."),
], D, nxt())
notes(s, "Objectives map to the Chapter 10 practice bank and the capstone feasibility report.")

s = stat_slide(prs, "Proposals are how money moves", "$",
    "Almost every dollar that changes hands between organizations — grants, contracts, budgets, partnerships — was asked for in writing first.",
    [("The proposal is persuasion (Chapter 8)", "wearing formal dress: same pipeline, higher stakes, stricter rules."),
     ("The formal report is analysis (Chapter 9)", "built for readers who weren't in the room — including readers you'll never meet."),
     ("Together they are the genre where", "writing skill converts most directly into funded work."),
    ], D, nxt())
notes(s, "Framing: this chapter is the commercial summit of the course. Students who write fundable proposals have a permanently portable skill.")

s = section_slide(prs, "01", "The proposal quadrants",
    "Who asked, and who's paying — two questions that set your burden of proof.", D, nxt())
notes(s, "Section 1: classification. The quadrants matter because each shifts what you must prove first.")

s = two_col_slide(prs, "Solicited or unsolicited?",
    "SOLICITED — they asked", [
        "An RFP (request for proposals) defines the need, format, and deadline",
        "The problem is already sold — your job is the best answer",
        "Compliance with THEIR structure is scored before content",
        ("Burden of proof:", "why YOU, against known competitors"),
    ],
    "UNSOLICITED — you spotted it", [
        "You saw a need they haven't formally named",
        "You must sell the PROBLEM before any solution (Chapter 8's hook)",
        "No format rules — but no budget line waiting either",
        ("Burden of proof:", "why THIS problem deserves money at all"),
    ], D, nxt())
notes(s, "The unsolicited proposal spends its first third proving the problem exists and costs money — skipping that step is the genre's classic failure.")

s = two_col_slide(prs, "Internal or external?",
    "INTERNAL — inside your organization", [
        "Justification reports' big sibling (Chapter 9)",
        "Reader knows the context; skip the company history",
        "Currency: hours, budget lines, strategic fit",
        ("Tone:", "direct, memo-dressed, politically aware — pre-wire it (Chapter 8)"),
    ],
    "EXTERNAL — crossing the boundary", [
        "Contracts, grants, client work — binding commitments",
        "Reader may know nothing; context earns its pages",
        "Formal apparatus expected: letterhead, signatures, terms",
        ("Tone:", "write like a contract, because it may become one"),
    ], D, nxt())
notes(s, "External proposals become legal documents on acceptance — every promised deliverable and date should be written as if a lawyer will read it, because one might.")

s = flow_slide(prs, "The six-part proposal skeleton", [
    ("PROBLEM", "Their pain, quantified — why money should move"),
    ("SOLUTION", "What, how, and why THIS approach"),
    ("PLAN", "Phases, milestones, deliverables — dated"),
    ("STAFFING", "Why you — ethos with evidence"),
    ("BUDGET", "Itemized, justified, framed"),
    ("RISKS", "What could go wrong + mitigations"),
], D, nxt(), note_text="Every funder reads with three questions: is the problem real? will this fix it? can THESE people deliver it? The skeleton answers them in order.")
notes(s, "The spine of the chapter. Each part gets its own slide next — the skeleton is memorizable, the craft is in the parts.")

s = bullets_slide(prs, "The problem section: where proposals are won", [
    ("Quantify the pain in the reader's units.", "'Manual intake burns 30 tech-hours a month' — their hours, their dollars, their risk (Chapter 8's hook, formalized)."),
    ("Cite the source of every number.", "A problem statement built on 'it seems like a lot' funds nothing; the helpdesk export funds projects."),
    ("Show the cost of doing nothing.", "The status quo has a price tag — print it. 'No' is never free, and this paragraph proves it."),
    ("Stop before the solution leaks in.", "A problem section that mentions your product is a sales pitch wearing a lab coat — readers smell it instantly."),
], D, nxt())
notes(s, "Funders fund problems, then choose solutions. The discipline of keeping the solution out of the problem section is what makes the problem credible.")

s = bullets_slide(prs, "Solution and plan: specific enough to be checked", [
    ("The solution states the mechanism,", "not the magic: what happens, in what order, producing what — 'barcode intake replaces manual entry at both benches.'"),
    ("Why THIS approach beats the alternatives:", "name the two you rejected and the reason (two-sided argument, Chapter 8) — evaluators are comparing anyway."),
    ("The plan converts promise to milestones:", "phases with dates, deliverables per phase, and what the client sees at each gate."),
    ("Every vague verb is a negotiation you'll lose later.", "'Optimize workflows' commits you to nothing and to everything — 'reduce intake time below 60 seconds' can be verified and invoiced."),
], D, nxt())
notes(s, "The dated-milestone plan is also your future protection: scope creep attacks proposals with fuzzy deliverables first.")

s = bullets_slide(prs, "Staffing: ethos with a résumé", [
    ("Name the people who will actually do the work,", "with the two credentials each that matter for THIS project — not the firm's whole trophy case."),
    ("Relevant beats impressive.", "'Ran three lab migrations this size' outweighs 'twenty years of industry leadership' every time."),
    ("Show capacity, not just capability:", "evaluators fund teams that visibly have room — 'lead assigned at 60% for the duration' answers the unasked question."),
    ("Past performance is the strongest evidence:", "one named, referenceable, similar project — with its result — beats a page of adjectives (social proof, Chapter 8)."),
], D, nxt())
notes(s, "The staffing section is where unsupported confidence goes to die. Two credentials per person, chosen for fit, is the discipline.")

s = bullets_slide(prs, "The budget: arithmetic with an argument", [
    ("Itemize to the level the reader must defend.", "Your funder has a funder — give them the line items THEY need to justify the yes upstairs."),
    ("Justify the big lines in one sentence each.", "'Two calibration units at $3,200 — one per bench, eliminating the queue' — number, purpose, consequence."),
    ("Frame the total against the problem's cost.", "'$24K against the $67K the current process burns annually' — the budget's last line should recall the problem's first number."),
    ("No padding, no lowballing.", "Padding gets found in evaluation; lowballing gets found in month three — both are reputation events, one is also a loss."),
], D, nxt())
notes(s, "The framing rule ties budget to problem quantification — the two sections argue as a pair. Lowballing discussion: winning unprofitable work is losing slowly.")

s = bullets_slide(prs, "Risks and evaluation: the section that builds trust", [
    ("Name the real risks yourself.", "The evaluator has already thought of them — your naming them first converts a vulnerability into ethos (two-sided, again)."),
    ("Each risk gets a mitigation, not a shrug.", "'Vendor delay → pre-ordered long-lead items in week one' — the pair is the point."),
    ("Define success measurably, in advance.", "'Intake under 60 seconds, zero transcription findings at 90 days' — agreed metrics make your final report unarguable (Chapter 8's pilot case)."),
    ("Include how and when you'll report.", "The promised cadence — 'milestone reports at each gate' — is a small line that signals operational maturity."),
], D, nxt())
notes(s, "The risks section is counterintuitively where trust is built: proposals with no named risks read as either naive or evasive, and evaluators can't tell which is worse.")

s = section_slide(prs, "02", "The RFP game",
    "Compliance is scored before content is read.", D, nxt())
notes(s, "Section 2: solicited proposals and the compliance discipline that decides them.")

s = bullets_slide(prs, "Their structure is your structure", [
    ("Mirror the RFP's section names and order — exactly.", "Evaluators score with a checklist built from their own document; making them hunt costs you points before content is judged."),
    ("Answer every requirement where they expect it,", "even when your material fits better elsewhere — 'see section 4' is a point deduction wearing a courtesy."),
    ("Respect every format rule:", "page limits, font sizes, file formats — a 21-page response to a 20-page limit can be disqualified unread, and sometimes is."),
    ("Brilliance is tiebreaker, compliance is entry.", "The order matters: non-compliant proposals don't reach the round where brilliance counts."),
], D, nxt())
notes(s, "Government and institutional RFPs especially: compliance screening happens before scoring, and it is clerical, not judgmental. The rules are the rules.")

s = icon_rows_slide(prs, "The compliance matrix: your submission insurance", [
    ("📋", "Harvest every 'shall' and 'must'", "Read the RFP with a highlighter; each one is a scored requirement, including the ones buried in appendices."),
    ("🗺", "Map requirement → your section → page", "Three columns; every row filled before submission — the empty row IS the finding."),
    ("👤", "Assign an owner per requirement", "On team proposals, unowned requirements are how 'I thought you had it' reaches the evaluator."),
    ("📎", "Submit the matrix with the proposal", "Many RFPs require it; the rest reward it — you just did the evaluator's first pass for them."),
], D, nxt())
notes(s, "The matrix is tedious and decisive. Teams that build it on day one write toward it; teams that build it the night before discover the gaps at the worst moment.")

s = bullets_slide(prs, "Deadlines are cliffs, not targets", [
    ("2:00 PM means 1:59 was the last safe minute.", "A 2:01 submission is a non-submission — no evaluator will ever see how good it was."),
    ("Portals crash at 1:55.", "Everyone submits in the final window; plan to be complete 24 hours early and uploaded by breakfast."),
    ("Time zones have eaten fortunes.", "'2:00 PM ET' read casually in Denver is a career story — convert every deadline to your clock, in writing, on day one."),
    ("The questions deadline matters too:", "most RFPs close clarification questions weeks before submission — the ambiguity you sit on becomes the guess you submit."),
], D, nxt())
notes(s, "Every proposal shop has a near-miss story; the 24-hour buffer rule is written in someone's scar tissue. The questions-deadline point is the one students don't know exists.")

s = bullets_slide(prs, "Case: the B+ that beat the A−", [
    ("Firm A wrote the smarter solution:", "genuinely better architecture, sharper pricing — organized their own way, two requirements answered 'throughout the document.'"),
    ("Firm B wrote the compliant one:", "every section mirrored the RFP, compliance matrix attached, every 'shall' traceable in thirty seconds."),
    ("Scoring: B won on points before quality was weighed.", "Two of A's requirements were marked 'not found' — the evaluators had 40 proposals and 40 minutes each."),
    ("The lesson:", "the evaluator's constraint is time, not intelligence. Compliance is how you respect it — and how you win with the second-best mousetrap."),
], D, nxt())
notes(s, "Composite of the standard procurement pattern. 'Not found' doesn't mean absent — it means not findable in the time an evaluator actually has.")

s = section_slide(prs, "03", "Formal report architecture",
    "Three layers, three readers, three paths through the document.", D, nxt())
notes(s, "Section 3: the formal report's anatomy — the upgrade kit bolted onto Chapter 9's pyramid.")

s = flow_slide(prs, "The three layers", [
    ("FRONT MATTER", "Cover · title page · transmittal · contents · executive summary"),
    ("BODY", "Introduction → findings → conclusions → recommendations"),
    ("BACK MATTER", "References · appendices — the verification layer"),
], D, nxt(), note_text="Three readers, three paths: the decider reads the executive summary, the implementer reads the body, the auditor reads the appendices. Design all three paths deliberately.")
notes(s, "The three-reader model organizes the whole section. Nobody reads a formal report cover to cover — it's a building with three entrances.")

s = icon_rows_slide(prs, "Front matter, piece by piece", [
    ("🏷", "Title page", "Title that states the subject AND scope · prepared for/by · date. 'Feasibility of Barcode Intake at the Fargo Lab' — not 'Lab Report.'"),
    ("✉", "Transmittal letter or memo", "The handshake: what this is, why they're receiving it, the one-line bottom line, and your contact for questions."),
    ("📑", "Table of contents", "Generated, never typed — informative headings (Chapter 3) make it read as a summary by itself."),
    ("⭐", "Executive summary", "The most-read page in the document — next two slides."),
], D, nxt())
notes(s, "The generated-TOC rule is practical: typed TOCs drift from reality by the third revision, and a wrong page number in the TOC indicts everything after it.")

s = flow_slide(prs, "Executive summary anatomy", [
    ("SITUATION", "Why this document exists — one or two sentences"),
    ("ANSWER", "The recommendation + its strongest number"),
    ("REASONS", "The pyramid's second layer, one sentence each"),
    ("THE ASK", "Decision needed, by whom, by when"),
], D, nxt(), note_text="Written LAST · placed FIRST · standalone. Most readers read nothing else — the summary must survive being the only page anyone sees.")
notes(s, "The four-beat anatomy from the study guide's figure. 'Written last' because you can't summarize what doesn't exist yet; drafting it first produces a summary of intentions.")

s = bullets_slide(prs, "Executive summary discipline", [
    ("It is not a preview — it is the verdict.", "'This report examines three options…' summarizes the table of contents; 'Refurbish the three units — saving $23K a year' summarizes the REPORT."),
    ("Standalone means standalone:", "no 'as shown in section 3,' no undefined acronyms, no dependence on exhibits the reader won't open."),
    ("One page, hard limit.", "A two-page executive summary is a short report with an identity crisis — compress or cut."),
    ("Test it on someone who won't read the report.", "If they can state your recommendation and its reason afterward, it works. That test is the whole spec."),
], D, nxt())
notes(s, "The preview-vs-verdict distinction is the most common failure. The outsider test operationalizes 'standalone' into something students can actually run.")

s = two_col_slide(prs, "Conclusions vs. recommendations — keep them separate",
    "CONCLUSIONS — what the evidence means", [
        "'The current process cannot scale past 600 samples/week'",
        "Interpretations, drawn strictly from the findings",
        "Each conclusion traceable to specific evidence",
        "No new facts allowed here",
    ],
    "RECOMMENDATIONS — what to do about it", [
        "'Adopt barcode intake at both benches by Q4'",
        "Actions: verb-first, owner-ready, dated where possible",
        "Each recommendation traceable to a conclusion",
        "Numbered, so meetings can argue about #3 by name",
    ], D, nxt())
notes(s, "The chain must be auditable: finding → conclusion → recommendation. A recommendation with no parent conclusion is advocacy that snuck in — evaluators hunt for exactly those.")

s = bullets_slide(prs, "Back matter: the verification layer", [
    ("Appendices hold the journey", "the summit displaced: raw data, method detail, instrument specs, interview notes — everything the auditor needs and the decider skips."),
    ("Every appendix is referenced from the body,", "by its point: 'full survey results in Appendix B' — an unreferenced appendix is cargo (Chapter 9's exhibit rule)."),
    ("References let every claim be traced.", "The list is where 'trust me' becomes 'check me' — the report's whole credibility, itemized."),
    ("The appendix is not a landfill.", "Material that supports nothing in the body doesn't get to hide in the back — cut means cut."),
], D, nxt())
notes(s, "The verification layer completes the three-reader design: the auditor's path must be as deliberate as the decider's. Landfill appendices signal a writer who couldn't decide.")

s = section_slide(prs, "04", "Sources and citation",
    "The credibility ladder — and the boundary that protects your name.", D, nxt())
notes(s, "Section 4: research integrity. Formal reports live or die on whether their evidence survives hostile checking.")

s = icon_rows_slide(prs, "The source credibility ladder", [
    ("1", "Primary data — strongest", "Your measurements, surveys, pilots: yours to defend, and defensible."),
    ("2", "Peer-reviewed and official", "Journals, standards bodies, government statistics — vetted before you arrived."),
    ("3", "Reputable secondary", "Industry reports, quality journalism — verify the underlying source before leaning."),
    ("4", "Vendor and advocacy", "Useful, interested — corroborate before any load-bearing use."),
    ("5", "Unsourced web / AI output — never load-bearing", "Trace it to a real source or drop the claim. No exceptions for convenient claims."),
], D, nxt(), kicker="A recommendation is only as strong as the weakest source under its load-bearing claim.")
notes(s, "The ladder from the study guide. Rung 5 includes AI: fluent, confident, and uncited is exactly the failure mode the ladder exists to catch.")

s = bullets_slide(prs, "Evaluating any source in ninety seconds", [
    ("Currency:", "when was this true? The 2019 benchmark in a 2026 report needs a reason to still be there."),
    ("Authority:", "who says so, and what would they know? An author, an institution, a method — findable or the rung drops."),
    ("Purpose:", "who benefits if you believe it? The vendor whitepaper isn't false — it's interested, and interest shapes selection."),
    ("Corroboration:", "does anyone independent agree? One source is a claim; two independent sources are the start of a fact."),
], D, nxt())
notes(s, "CAP+C — a fast, memorable screen. The purpose question does the most work in business contexts, where most convenient sources are interested ones.")

s = icon_rows_slide(prs, "Citation integrity: what needs a citation", [
    ("“”", "Quote", "Their exact words → quotation marks + citation. Both, always."),
    ("↺", "Paraphrase", "Their idea, your words → citation still required. Rewording transfers nothing."),
    ("🌐", "Common knowledge", "Undisputed and widely available → no citation needed."),
    ("💡", "Your analysis", "Your conclusions from cited evidence → the part that's actually yours — and the part your name should sit on."),
], D, nxt(), kicker="The boundary protects you twice: from plagiarism, and from owning claims you can't defend.")
notes(s, "The quadrant from the guide. The your-analysis rung reframes citation positively: citing generously makes clear which insights are original — it takes nothing away.")

s = bullets_slide(prs, "AI in the research pipeline", [
    ("AI is a research assistant, not a source.", "'ChatGPT says' is rung five — use it to find real sources, summarize them, and draft, never as the authority itself."),
    ("Verify every fact it hands you.", "AI produces plausible citations to papers that don't exist — check that the source is real AND says what's claimed (both failures are common)."),
    ("Disclose per your institution's and client's rules.", "Norms are still forming; the safe default is transparency about tools in the method section."),
    ("The judgment stays yours:", "source selection, evidence weighing, and the recommendation are the parts that can't be delegated — they're also the parts being graded, in school and after."),
], D, nxt())
notes(s, "The practical AI-research policy in four lines. The fabricated-citation problem is the vivid one: a confident reference to a nonexistent paper survives every check except the real one.")

s = bullets_slide(prs, "Documentation without the seminar", [
    ("Pick one style and be consistent.", "APA is the business-school default; consistency matters more than which style — mixed formats read as carelessness."),
    ("In-text: author and year carry the weight.", "(Okafor, 2025) — enough for the reader to find the full entry; page numbers for quotes."),
    ("The references list is a promise:", "every in-text citation appears there; everything there is cited in text. Orphans in either direction are findings."),
    ("Cite the version you actually used:", "the 2024 revision, the June dataset, the archived page — sources move, and your citation is a timestamp."),
], D, nxt())
notes(s, "Deliberately minimal: enough mechanics to be correct, pointed at consistency as the real standard. The two-way promise rule catches most student citation errors.")

s = section_slide(prs, "05", "Managing the living document",
    "Versions, teams, and the one-pager that travels ahead of the tome.", D, nxt())
notes(s, "Section 5: document operations — the unglamorous discipline that separates proposal shops from proposal accidents.")

s = bullets_slide(prs, "Versioning the living proposal", [
    ("One living copy, one owner", "(Chapter 5's rules, at contract stakes) — merge authority lives with a named person, or Saturday belongs to someone."),
    ("Freeze what leaves the building:", "'Proposal—as-submitted-2026-07-15' is a dated, read-only snapshot — because 'which version did they sign?' is a legal question."),
    ("Negotiations amend the frozen copy visibly:", "tracked changes against as-submitted, so every delta from the original promise is findable."),
    ("The version log is one line per freeze:", "date, what changed, who approved — thirty seconds of writing per event, hours of dispute insurance."),
], D, nxt())
notes(s, "From the guide's versioning deep dive. The as-submitted snapshot is the load-bearing habit: post-award disputes are almost always about which words were operative when.")

s = bullets_slide(prs, "Writing big documents as a team", [
    ("Divide by section, unify by skeleton:", "everyone writes into the agreed pyramid and compliance matrix — division of labor without division of structure."),
    ("One voice pass at the end, one editor.", "Six authors are audible in an unedited proposal; the final pass makes it one document instead of a stapled anthology."),
    ("Shared style decisions up front:", "terminology, tense, how the client is named — the two-minute glossary prevents two hundred inconsistencies."),
    ("The red team reads it cold:", "one colleague who wrote nothing, scoring it as the evaluator will — their confusion is your cheapest revision (Chapter 4, scaled up)."),
], D, nxt())
notes(s, "The red-team review is standard in serious proposal shops and unknown to students — one cold reader with the RFP's checklist finds what six authors can't.")

s = bullets_slide(prs, "The one-pager: the document that travels ahead", [
    ("Every big proposal needs a light envoy:", "one page — problem, solution, number, ask — for the meeting, the forward, the hallway."),
    ("It's the executive summary with a life of its own:", "same four beats, standing fully alone, formatted to be read on a phone in a corridor."),
    ("The one-pager gets you the meeting;", "the proposal survives the scrutiny the meeting triggers. Different jobs — build both, and build them to agree."),
    ("Keep them synchronized:", "a one-pager promising what the proposal doesn't say is a credibility event at the worst possible moment."),
], D, nxt())
notes(s, "From the guide's one-pager section. The synchronization warning is real: decks and one-pagers drift from the master document unless someone owns the pairing.")

s = bullets_slide(prs, "Case: the proposal that won on the appendix", [
    ("Two finalists, near-identical solutions and prices.", "The evaluation committee deadlocked and did what deadlocked committees do: sent both to their technical staff."),
    ("Firm A's appendix held the method:", "instrument validation data, the pilot's raw numbers, the survey with its denominator — every body-claim traceable in one hop."),
    ("Firm B's appendix held brochures.", "The technical reviewer's one-line memo: 'A shows their work; B shows their marketing.'"),
    ("The lesson:", "the auditor's path decided a seven-figure award. The verification layer isn't overhead — it's the tiebreaker you build in advance."),
], D, nxt())
notes(s, "The three-reader model closing its loop: proposals are won in the summary, defended in the body, and decided — more often than anyone admits — in the back matter.")

s = two_col_slide(prs, "The executive summary: before and after",
    "Before (a preview)", [
        "'This report examines the feasibility of automated sample intake at the Fargo facility.'",
        "'Multiple options were evaluated across several criteria.'",
        "'Findings and recommendations are presented in the sections that follow.'",
        "Three sentences; zero information",
    ],
    "After (a verdict)", [
        "'Barcode intake is feasible and pays back in 14 months. We recommend a two-bench rollout by Q4 ($24K).'",
        "'Three reasons: intake time drops 38% (pilot, App. C); transcription findings go to zero; the current process fails past 600 samples/week.'",
        "'Decision needed from the ops committee by July 25 to hold vendor pricing.'",
        "Situation → answer → reasons → ask",
    ], D, nxt(), left_fill=RGBColor(0xF7, 0xEA, 0xE8), left_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "The before column is recognizable from real reports — grammatically flawless, informationally empty. The after column is the four-beat anatomy, executed.")

s = takeaways_slide(prs, [
    "Know your quadrant: solicited proposals prove 'why us'; unsolicited ones prove the problem first.",
    "Six parts, in order: problem, solution, plan, staffing, budget, risks — each checkable, each dated.",
    "Compliance is entry, brilliance is tiebreaker: their structure, a compliance matrix, and a 24-hour deadline buffer.",
    "Three layers for three readers: summary for the decider, body for the implementer, appendix for the auditor.",
    "The executive summary is a verdict, written last, placed first, standing alone.",
    "Grade sources on the ladder; cite across the integrity quadrants; AI is an assistant, never a source.",
], D, nxt(), site_note="Practice now: course site → Chapter 10 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The proposal is the only genre where the reader's yes comes with money attached. Every rule in it exists because someone, somewhere, lost the money by breaking it.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Find a real RFP (grants.gov posts thousands). Build its compliance matrix — how many 'shall's did the casual read miss?",
    "Take a report you've written and draft its executive summary as a VERDICT. What did you have to decide that the report avoided deciding?",
    "Argue it: should the budget ever appear in the executive summary? When does the number help, and when does it ambush?",
    "Grade five sources from your last research project on the credibility ladder. What was load-bearing on rung four or five?",
    "Your team's proposal is due at 2:00 PM and the portal is down at 1:40. Walk through what you do — then design the process so it never happens.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 10 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 10 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Read:", "The Chapter 10 Study Guide — the full skeleton walkthrough, the RFP game, and the versioning deep dive."),
    ("Apply:", "Your capstone feasibility report uses this chapter's architecture end to end — start its compliance matrix now."),
    ("Coming next:", "Chapter 11 — professionalism, teamwork, and meetings: the workplace behaviors that give your documents their reputation."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch10-proposals-and-formal-reports.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
