# Chapter 10 Study Guide — Proposals and Formal Reports (25pp standard)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(10, 'Proposals and Formal Reports',
    'The documents that move money — full-dress reports, winning proposals, and the executive summary that decides both.')

h1(doc, 'How to use this guide')
para(doc, 'Chapter 9 built the analytical engine; this chapter adds the formal apparatus and the '
    'proposal genre — the documents organizations use to commit serious resources. Your capstone '
    'feasibility study and its executive summary live here. Read with your own capstone project in '
    'mind: every section of this guide maps to a section you will write.')

h1(doc, 'The formal report: architecture for three readers')
figure(doc, os.path.join(FIG, 'ch10_architecture.png'),
    'Figure 1. Formal report architecture: front matter, body, back matter — three readers, three designed paths.',
    'Formal report architecture: front matter (cover, title page, transmittal, table of contents, executive summary), body (introduction, findings and analysis as the transcribed pyramid, conclusions, recommendations), and back matter (references and appendices as the verification layer). Three readers take three paths: the decider reads the executive summary, the implementer reads the body, the auditor reads the appendices.')
para(doc, 'A formal report is Chapter 9’s engine wearing institutional dress, and every piece of '
    'the apparatus earns its place by serving a reader. Front matter serves navigation and '
    'authority: the title page announces scope and ownership; the transmittal letter (or memo) '
    'delivers the document and its summit in the sender’s voice; the table of contents converts '
    'informative headings into a map (if your TOC reads as an argument — because your headings '
    'are claims — you built the pyramid right); and the executive summary carries the whole case '
    'for the reader who reads nothing else, which is most readers who matter. The body transcribes '
    'the pyramid: an introduction that frames the question and method briefly, findings organized '
    'by reasons (never by chronology of effort), conclusions that interpret, recommendations that '
    'commit. Back matter is the verification layer: references that let claims be traced, '
    'appendices that let method be audited. Three readers, three paths — and the design failure '
    'of most formal reports is building only the middle one.')
para(doc, 'Conclusions and recommendations are different speech acts, and formal reports separate '
    'them for a reason: conclusions interpret evidence (“the three oldest instruments cause 70% '
    'of downtime and the trend is accelerating”), while recommendations commit to action '
    '(“refurbish units 3, 7, and 9 by Q4 at $18,000”). A reader can accept your conclusions and '
    'reject your recommendation — budget, timing, appetite — and the separation lets them do so '
    'without discarding your analysis. Collapsing the two (“we conclude that we should…”) '
    'forfeits that graceful fallback.', bold_lead='Conclusions vs. recommendations.')

h1(doc, 'The executive summary: the document most readers actually read')
figure(doc, os.path.join(FIG, 'ch10_execsum.png'),
    'Figure 2. Executive summary anatomy: situation, answer, reasons, ask — written last, placed first, standalone.',
    'Executive summary anatomy: the situation in one or two sentences, the answer with its strongest number, the reasons compressed to a sentence each, the ask naming the decision needed by whom and when — governed by the rule: written last, placed first, standalone, because most readers read nothing else.')
para(doc, 'Your syllabus makes the executive summary the capstone deliverable, and the emphasis is '
    'exactly right: in organizational life, the executive summary IS the report for the people '
    'deciding. The anatomy: the situation, in one or two sentences (why this document exists — '
    'not the history of the assignment); the answer, with its strongest number, stated as flatly '
    'as Chapter 9’s summit discipline demands; the reasons, each compressed to a sentence '
    '(the pyramid’s second layer, miniaturized); and the ask — what decision, by whom, by when. '
    'Three governing rules. Written last: you cannot summarize what does not yet exist, and '
    'summaries drafted first become outlines wearing a disguise. Placed first: it is the front '
    'door, not the abstract of record. Standalone: no reference to “the analysis below,” no '
    'undefined terms, no dependence on exhibits — it must survive being forwarded alone, because '
    'it will be (Chapter 2’s forwardability test, at its highest stakes). Length discipline: one '
    'page single-spaced for anything up to a major study — your capstone spec — and never more '
    'than five percent of the document’s length.')
para(doc, 'The classic failure is the table-of-contents summary: “This report examines the '
    'feasibility of X, reviews the relevant literature, presents findings, and offers '
    'recommendations.” That summarizes the document’s FURNITURE, not its case — a topic summit '
    'wearing a suit (Chapter 9’s label problem). The reader learns the report has sections, and '
    'nothing else. Every sentence of a working executive summary could be challenged in a '
    'meeting; no sentence of the furniture version could even be discussed.',
    bold_lead='The furniture failure.')

h1(doc, 'Proposals: the four quadrants')
figure(doc, os.path.join(FIG, 'ch10_proptypes.png'),
    'Figure 3. The proposal quadrants: solicited/unsolicited, internal/external — each shifts the burden of proof.',
    'Proposal quadrants: solicited (they asked via RFP — compliance with their structure is scored before content is read), unsolicited (you spotted the need — sell the problem before the solution), internal (resources and changes — the justification report’s big sibling), external (contracts, grants, partnerships — formal apparatus plus binding commitments).')
para(doc, 'Proposals are persuasive documents (Chapter 8) with delivery obligations attached, and '
    'the quadrants set the burden of proof. Solicited proposals answer a request — an RFP, a '
    'grant call, an internal budget process — and the requester’s structure governs absolutely '
    '(more below). Unsolicited proposals must first convince the reader a problem exists worth '
    'solving: the hook carries double weight, and the commitment ladder (Chapter 8) usually '
    'counsels proposing a small first step rather than the full program. Internal proposals '
    'trade on organizational knowledge — you know the politics, the budget cycle, the skeptics '
    'to pre-wire — while external proposals compensate with formality and proof: credentials, '
    'references, and commitments written with contract-grade precision, because a winning '
    'external proposal BECOMES part of the contract, and its casual promises become binding '
    'ones.')
figure(doc, os.path.join(FIG, 'ch10_propskeleton.png'),
    'Figure 4. The full proposal skeleton: problem, solution, plan, qualifications, budget, evaluation and risks.',
    'Full proposal skeleton: problem or need (their pain quantified — why money should move), proposed solution (what, how, why this approach), plan and schedule (dated phases, milestones, deliverables), staffing and qualifications (why you, with evidence), budget (itemized, justified, framed against the problem’s cost), evaluation and risks (how success is measured, what could go wrong, mitigations).')
para(doc, 'The skeleton’s six sections answer the funder’s six silent questions in order: why '
    'should money move? what exactly would it buy? when do things happen? why you? what does it '
    'cost, honestly? and how will we know it worked — and what if it doesn’t? Two sections '
    'deserve special craft. The budget is a persuasive document in miniature: itemized enough to '
    'be checkable (Chapter 4’s numbers audit applies line by line), justified where any line '
    'invites a raised eyebrow, and framed against the cost of the unsolved problem (Chapter 8’s '
    'honest anchor). The evaluation-and-risks section is the credibility engine: proposers who '
    'name their risks and measurement criteria before being asked read as people who have '
    'actually run projects — the two-sided move (Chapter 8) in its institutional form. A '
    'proposal with no risks section is read as either naive or hiding, and evaluators guess '
    'which.')

h1(doc, 'The RFP game: compliance before brilliance')
figure(doc, os.path.join(FIG, 'ch10_rfp.png'),
    'Figure 5. RFP discipline: their structure is your structure, every “shall” goes in a compliance matrix, deadlines are cliffs.',
    'RFP compliance discipline: mirror the requester’s section names and order because evaluators score with a checklist; track every shall and must in a compliance matrix mapping requirement to location and page; treat deadlines as cliffs — one minute late is a non-submission and portals crash at 1:55.')
para(doc, 'Solicited proposals are scored before they are read: evaluators — often legally '
    'obligated to fairness — work from checklists built on the RFP’s own requirements, and the '
    'brilliant proposal in the wrong structure loses to the competent one in the right structure '
    'every time. The disciplines: mirror their section names and order exactly, even where yours '
    'are better (this is their document’s world; you are a guest); harvest every “shall,” '
    '“must,” and “required” into a compliance matrix — requirement, where addressed, page '
    'number — and submit it even when not required, because it converts your proposal into an '
    'easy checklist for the evaluator (make yes easy, Chapter 8); respect page limits, font '
    'specs, and formats as pass/fail gates, not suggestions; and treat the deadline as a cliff '
    'with a safety margin — the portal that crashes at 1:55 for a 2:00 deadline has ended more '
    'pursuits than weak pricing ever did. None of this replaces content; all of it determines '
    'whether content is ever seen.')

h1(doc, 'Research documentation: sources, citations, and the credibility ledger')
figure(doc, os.path.join(FIG, 'ch10_sources.png'),
    'Figure 6. The source credibility ladder: primary data at the top, unsourced claims never load-bearing.',
    'Source credibility ladder: primary data (your measurements, surveys, pilots — strongest and yours to defend), peer-reviewed and official sources (journals, standards bodies, government statistics), reputable secondary sources (industry reports and quality journalism — verify the underlying source), vendor and advocacy material (useful but interested — corroborate before load-bearing use), unsourced web content and AI output (never load-bearing — trace to a real source or drop the claim).')
para(doc, 'Formal documents make claims that outlive meetings, so their evidence must be traceable '
    '— which is what citations are actually FOR, beneath the formatting rules: a citation is an '
    'audit trail from your claim to its source, offered before anyone demands it. The ladder '
    'ranks sources by how much your credibility leans on them safely. Primary data — your '
    'measurements, your survey, your pilot — sits on top because you can defend every step (and '
    'must: methods appendix). Peer-reviewed and official sources carry institutional '
    'verification. Reputable secondary sources are fine when their underlying source is checked '
    '— cite the study, not the news story about the study, whenever you can reach it. Vendor '
    'and advocacy material is useful and interested: corroborate before it carries weight. And '
    'the bottom rung — unsourced web claims and raw AI output — never bears load: this guide’s '
    'own rule, stated to you many times, is now yours professionally. Trace the claim to a real '
    'source or drop it (Chapter 15’s verification discipline, formalized).')
figure(doc, os.path.join(FIG, 'ch10_citation.png'),
    'Figure 7. What needs a citation: quotes and paraphrases yes, common knowledge no, your analysis is the part that is yours.',
    'Citation boundary: exact words require quotation marks plus citation; paraphrased ideas still require citation; undisputed common knowledge does not; your own analysis and conclusions drawn from cited evidence are the part that is yours.')
para(doc, 'The citation boundary confuses students and professionals identically, so here it is '
    'plainly: their exact words take quotation marks and a citation; their ideas in your words '
    'still take a citation (paraphrase transfers wording, not ownership); undisputed common '
    'knowledge takes none; and your analysis of cited evidence is the part that is genuinely '
    'yours — the more of it your document contains, the more the citations strengthen rather '
    'than crowd it. Format per your venue (APA’s author–date system governs most business and '
    'academic settings; American Psychological Association, 2020), but never mistake formatting '
    'for the point: a perfectly formatted reference list attached to unverified claims is '
    'compliance theater. Integrity mechanics for team documents: one shared reference file from '
    'day one, sources captured at reading time (reconstructing citations the night before a '
    'deadline is how errors and accidental plagiarism both happen), and every teammate’s '
    'sections spot-checked against their sources during the finishing edit (Chapter 9’s '
    'co-authoring disciplines).')

h1(doc, 'Deep dive: writing technical content for mixed readers')
para(doc, 'Formal reports routinely carry technical substance to non-technical deciders — your '
    'chemistry-to-committee problem, and every engineer’s, analyst’s, and clinician’s daily '
    'translation task. The disciplines: layer by altitude (the executive summary at zero '
    'jargon; the body defining terms at first use; the appendix at full technical fidelity — '
    'three truths, one document); translate mechanisms into consequences (“the electrode '
    'housing cracked” matters to the committee as “the instrument reports false pH readings '
    'until repaired — a compliance exposure”); use analogies for structure, never for proof '
    '(an analogy that carries the argument invites attack at the analogy’s weakest joint); and '
    'resist the credibility temptation — technical writers under-explain to sound expert, and '
    'the result reads as gatekeeping to the exact audience holding the budget. The Melissa '
    'Marshall rule from this chapter’s watch list compresses it: “So what? Who cares?” answered '
    'in the reader’s world, every technical paragraph.')

h1(doc, 'Deep dive: front matter that earns its pages')
para(doc, 'Each front-matter element has a job and a failure mode. The transmittal letter or memo '
    'is the handshake: one page, warm but precise — what this is, why the reader has it, the '
    'summit in one sentence, thanks where owed, and the offer of follow-up; its failure mode is '
    'the fossil parade (“enclosed please find”). The title is a finding, not a filing label '
    'where you can manage it: “Instrument Refurbishment: $18K Investment, $41K Problem” beats '
    '“Analysis of Laboratory Equipment Downtime” in every reading the document will ever get; '
    'where institutional convention demands sobriety, the subtitle carries the takeaway. The '
    'table of contents is generated, never typed — Word builds it from your heading styles '
    '(the accessibility work this course requires pays again here), which means it cannot drift '
    'from the document. Page numbers, headers, and consistent styling are Chapter 4’s design '
    'consistency at document scale: any element that varies without meaning teaches the reader '
    'to stop trusting the signals that DO mean. And the cover: clean, dated, owned — the '
    'organization’s name and the author’s, because formal documents are signed work.')

h1(doc, 'Worked example: the capstone executive summary, annotated')
para(doc, 'Here is a one-page executive summary in your capstone’s required shape — intro, '
    'methodology, key findings, recommendations, conclusion — annotated against this chapter.')
para(doc, '“The Cedarview municipal broadband feasibility study asked whether a city-owned fiber '
    'network can serve 12,400 households at sustainable cost. [situation: one sentence, the '
    'question itself] Our team analyzed municipal filings, comparable-city outcomes in four '
    'markets, and vendor cost models across three build scenarios. [methodology: one sentence, '
    'enough to establish method without narrating it] The study finds the network technically '
    'feasible on existing utility corridors; economically viable only under the phased build '
    '(Scenario B), which reaches break-even in year 7 at 42% take-rate — two comparable cities '
    'exceeded that rate in year 3; and operationally dependent on contracting network operations '
    'rather than building municipal capacity. [findings: three, compressed, each carrying its '
    'number — the pyramid’s second layer] We recommend Council approve Scenario B’s Phase 1 '
    '($4.2M, 2,800 households) with the operations RFP issued concurrently, and defer the '
    'citywide commitment to the Phase 1 take-rate review in month 18. [recommendation: '
    'committed, dated, and BRANCHED — the feasible-with-conditions verdict from Chapter 9] '
    'Phase 1 bounds the city’s exposure while purchasing the one data point every comparable '
    'city wished it had bought first: real local demand. [conclusion: why this path, in one '
    'sentence that faces forward]”')
para(doc, 'Count the disciplines: standalone (no undefined terms, no “see below”), every claim '
    'checkable, the strongest numbers surfaced, the recommendation separable from the '
    'conclusions, and the whole page challengeable in a meeting — which is the point of the '
    'meeting it will open.', bold_lead='The count.')

h1(doc, 'Case study 1: the proposal that lost on page limits')
para(doc, 'A regional engineering firm pursues a $2.3M county infrastructure contract. Their '
    'proposal is, by consensus of everyone who reads it, the strongest submission: deeper local '
    'knowledge, better pricing, a genuinely innovative phasing plan. It is also 24 pages against '
    'the RFP’s “maximum 20 pages, excluding appendices” — the team decided the extra four pages '
    'of case studies “strengthened the story.” The county’s evaluation committee, following '
    'procurement rules it does not control, marks the submission non-compliant and scores it '
    'zero. The contract goes to the second-best proposal. The firm’s principal calls the '
    'procurement office to protest and is read the RFP’s own sentence back: “Proposals '
    'exceeding page limits will not be evaluated.”')
numbered(doc, [
    'The team knew the limit and chose to exceed it. Reconstruct the reasoning that felt sound in the room — and name the misunderstanding about how solicited proposals are read.',
    'What belonged in those four extra pages’ place? Where do “story-strengthening” case studies legitimately live in an RFP response?',
    'Design the submission-day checklist that makes this failure structurally impossible.',
    'The procurement officer had no discretion. Why do compliance regimes bind evaluators this tightly, and what does that imply about every “surely they’ll appreciate…” instinct?',
])
h2(doc, 'Case analysis')
para(doc, 'The room’s reasoning — “our content is strong enough that they’ll want the extra '
    'pages” — misunderstands the genre: solicited proposals are read inside a fairness regime '
    'where rules protect the process from exactly this judgment call, and the evaluator who '
    'waives a limit for one bidder invites the losing bidders’ lawyers. Compliance is not '
    'bureaucratic decoration; it is the first scored test of whether you can follow the '
    'client’s instructions — which is, the county might note, the job. The case studies belonged '
    'in the appendices the RFP explicitly excluded from the count, referenced from the body by '
    'their point (Chapter 9’s exhibit rule). The checklist: one owner for compliance (not '
    '“everyone”); the matrix checked against the final PDF, not the draft; page count, font, '
    'margins, and naming conventions verified on the submission file itself; upload completed '
    'a day early with confirmation captured. The instinct this case retires: “surely they’ll '
    'appreciate” is the proposal-writing version of Chapter 2’s writing-for-yourself — the '
    'reader’s rules ARE the reader analysis.')

h1(doc, 'Case study 2: the invented citation')
para(doc, 'A strong student team submits a feasibility draft citing, among 22 references, a '
    'study: “(Morrison & Chen, 2023)” supporting their market-size estimate — the load-bearing '
    'number in their economics section. The instructor, spot-checking sources, cannot find the '
    'study. Confronted, the team’s researcher explains without much embarrassment: an AI '
    'assistant had “provided the source” along with the market figure, and it “looked right.” '
    'The number itself, later traced, was roughly correct — a real industry report supported '
    'something close. The team receives a zero on the draft under the academic integrity '
    'policy, appeals on the grounds that “the number was basically true,” and loses the '
    'appeal.')
numbered(doc, [
    'The number was “basically true.” Why does the invented citation still poison the document — and the team?',
    'Walk the verification protocol that would have caught this in ninety seconds.',
    'Where does responsibility sit between the AI that generated the citation and the researcher who used it? Use Chapter 15’s ownership rule.',
    'The appeal argued outcome over process. Why do integrity regimes — academic and professional — refuse that trade?',
])
h2(doc, 'Case analysis')
para(doc, 'A citation is a claim about the world — “this source exists and says this” — and a '
    'false one is a fabrication regardless of the underlying number’s luck: the reader who '
    'catches one invented source must now re-verify all 22, and the document’s entire '
    'credibility ledger (Figure 6) goes into receivership. The ninety-second protocol: every '
    'citation gets traced to its actual document — title page seen, claim located — before it '
    'enters the reference file; AI-suggested sources are treated as search hints, never as '
    'sources (the bottom rung of the ladder, by construction). Ownership is undivided: the AI '
    'generated text; the researcher published it — Chapter 15’s rule (“your name is on it”) '
    'exists precisely because tools cannot be accountable. And integrity regimes refuse the '
    'outcome-over-process trade because process is what makes future outcomes trustworthy: a '
    'team forgiven for one lucky fabrication has been taught to gamble, and the next invented '
    'source will support a number that is NOT basically true. The professional translation is '
    'exact — this case, with a consulting firm’s name in place of the team’s, is a '
    'client-relationship obituary.')

h1(doc, 'Deep dive: grants — the proposal’s most disciplined species')
para(doc, 'Grant proposals — foundation, government, internal seed funding — concentrate every '
    'discipline in this chapter and add three of their own. Fit is the first filter: funders '
    'publish priorities, and the strongest proposal outside them loses to the modest one inside '
    '(read the funded-projects list, not just the call — what they DO fund is the truest '
    'statement of what they want); the fit paragraph belongs on page one, in their vocabulary. '
    'Outcomes language governs: grant evaluators distinguish outputs (what you will do — '
    'workshops held, samples analyzed) from outcomes (what changes — retention improved, '
    'detection limits lowered), and proposals that promise only outputs read as activity in '
    'search of a purpose; every objective takes the measurable-outcome form John Doerr’s watch-'
    'list talk teaches. And the budget-narrative pairing: grant budgets carry a prose '
    'justification line by line, and evaluators read the pair for coherence — the budget that '
    'funds a coordinator the narrative never mentions, or the narrative that promises analysis '
    'the budget never staffs, fails the internal-consistency check that kills more grants than '
    'weak ideas do (Chapter 4’s consistency audit, at funding stakes). The meta-skill grants '
    'teach is proposal hygiene under absolute rules: every funder portal is an RFP compliance '
    'regime with the cliffs turned up.')

h1(doc, 'Formal-document workshop: five repairs (answers follow)')
numbered(doc, [
    'Executive summary opener: “This report presents the findings of our comprehensive three-month analysis of laboratory equipment downtime patterns, conducted using industry-standard methodologies.”',
    'A proposal’s risk section: “We do not anticipate significant risks. Our experienced team is confident of on-time, on-budget delivery.”',
    'A reference list entry the writer never opened: “(Industry Analytics Group, 2024)” — supplied by an AI assistant with a plausible title.',
    'A transmittal email: “Please find attached the report as per your request. Do not hesitate to contact the undersigned should questions arise.”',
    'An RFP response that renames the requester’s “Section C: Technical Approach” to the firm’s preferred “Our Innovative Methodology.”',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    'Furniture plus credential-flexing — three lines and no case. Repair: “Three instruments cause 70% of Q2 downtime; refurbishing them costs $18,000 against a $41,000 annual loss — we recommend approval by 7/25.” The methodology gets one sentence, later.',
    'The riskless proposal — read as naive or hiding. Repair: two real risks with mitigations (“vendor parts lead time — mitigated by early PO and a named alternate supplier”) and a measurement criterion; confidence is demonstrated by the quality of the worry.',
    'Trace or drop — ninety seconds against the actual document. If it exists, cite what you saw; if it does not, the number needs a real source or deletion. AI suggestions are search hints (the bottom rung bears no load).',
    'Fossil parade with no summit. Repair: “Attached: the downtime analysis — bottom line, refurbishing three units saves $23K/yr; decision needed by 7/25. Happy to walk through it Thursday.”',
    'Their house, their rules: restore “Section C: Technical Approach” verbatim. Innovation belongs INSIDE the section; renaming it costs checklist points and signals a bidder who improves on instructions — which no evaluator is shopping for.',
])

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Melissa Marshall, “Talk nerdy to me” (TED).', 'Four minutes on carrying technical content to non-technical deciders — “so what? who cares?” answered in the reader’s world.'),
    ('Tom Wujec, “Got a wicked problem? First, tell me how you make toast” (TED).', 'Visualizing plans and systems — directly useful for the plan-and-schedule sections proposals live or die on.'),
    ('John Doerr, “Why the secret to success is setting the right goals” (TED).', 'Measurable objectives — the thinking behind every evaluation section that reads as credible.'),
])

h1(doc, 'Deep dive: versioning the living proposal')
para(doc, 'Consequential proposals rarely ship once: they iterate through internal reviews, '
    'partner comments, and — after submission — clarification rounds. Chapter 4’s version '
    'control gets three proposal-specific extensions. Baseline the submission: the exact file '
    'that went out the door gets frozen, named, and archived untouched, because clarification '
    'answers must be checked against what was actually promised (not against the improved draft '
    'living in someone’s head). Track commitments, not just text: maintain a one-page register '
    'of every number, date, and deliverable the proposal commits to — when reviewers request '
    'changes, the register shows instantly what else each change touches (the budget line that '
    'moved also moved two milestones and one staffing claim; unversioned proposals discover '
    'this at contract signing). And control the negotiation trail: every clarification answer '
    'is itself a formal document — numbered, dated, referencing the question verbatim — '
    'because in disputes, the trail IS the agreement. Teams treat this as bureaucracy until '
    'the first time a client says “but your proposal said…” and the register answers in '
    'thirty seconds. Then they treat it as armor.')

h1(doc, 'Deep dive: the one-pager — formal thinking without the apparatus')
para(doc, 'Between Chapter 9’s informal memos and this chapter’s full-dress reports lives the '
    'genre executives increasingly demand: the one-pager — a complete decision document on a '
    'single page. It is not a summary OF something; it is the something, and famous versions '
    'govern real institutions (Amazon’s narrative memos, military decision papers, the “brief '
    'the board on one page” convention). Its discipline is the executive summary’s anatomy '
    'given slightly more room: the situation in two sentences; the answer with its numbers; '
    'the reasons as three labeled, evidence-bearing paragraphs; alternatives dispatched in two '
    'lines each; the risks named; the ask dated. What the single page forces is exactly what '
    'ten pages let you avoid: every sentence must carry decision-relevant load, every number '
    'must be the strongest available, and nothing can hide — which is why drafting the '
    'one-pager FIRST, even when the venue wants forty pages, is a professional’s private '
    'discipline: if the case does not close on one page, more pages will not close it; they '
    'will upholster it. Build the one-pager, verify it convinces, then expand it into whatever '
    'container the occasion demands. The capstone’s one-page executive summary is training '
    'you for precisely this genre, under exactly this constraint, on purpose.')

h1(doc, 'Deep dive: reading proposals — the evaluator’s seat')
para(doc, 'You will evaluate proposals long before you approve budgets: vendor pitches to your '
    'team, grant applications on review panels, classmates’ drafts. The evaluator’s craft '
    'sharpens the writer’s. Read the executive summary first and write down the ask as you '
    'understand it — if you cannot, the document has already failed, whatever follows. Then '
    'audit the internal consistency triangle: does the budget fund what the plan promises, and '
    'does the schedule allow what the budget staffs? (Most weak proposals break here, not in '
    'their prose.) Check the risks section for signs of real project experience — the '
    'suspiciously frictionless plan is the naive one. Trace two citations at random; the '
    'survival rate generalizes. And separate your scores: content merit, compliance, and '
    'presentation polish are three different qualities, and the halo effect (beautiful '
    'documents reading as true) is the evaluator’s occupational bias — name it to resist it. '
    'Sitting in this seat even once rewires your writing permanently: you stop asking “is my '
    'proposal impressive?” and start asking the only question evaluators actually hold — '
    '“can I check this, and does it cohere?”')

h1(doc, 'Put it to work this week')
numbered(doc, [
    'Draft your capstone’s executive summary early, as a diagnostic. Note every hole it exposes in the analysis — that list is your work plan.',
    'Trace every citation currently in your team’s reference file to its actual source. Log the survival rate.',
    'Build the compliance matrix for your capstone’s requirements (the syllabus IS your RFP: page count, format, sections, deadline).',
    'Write the transmittal memo for a document you have already submitted somewhere. Notice what the one-sentence summit forces you to decide.',
    'Find your organization’s or university’s budget calendar and mark the soft window on your own.',
])

h1(doc, 'Deep dive: introductions that frame, methods that earn trust')
para(doc, 'Two body sections deserve craft notes the architecture figure compresses. The '
    'introduction of a formal report does four jobs in under a page: states the question '
    '(verbatim from whoever commissioned the work — misstate the question and every answer is '
    'wrong); bounds the scope, explicitly including what was OUT (“this study addresses '
    'residential service; commercial feasibility was excluded per the March charge” — the '
    'sentence that prevents month-later disputes about what you were supposed to do); previews '
    'the structure in one sentence (the map, not the tour); and declares the method at summary '
    'altitude. It does NOT build suspense, review the history of the assignment, or thank the '
    'committee — the introduction is a frame, and frames are thin.')
para(doc, 'The methods content — however your venue names the section — earns trust by '
    'answering the auditor’s three questions: what did you examine (sources, datasets, '
    'sites, sample sizes), how did you analyze it (the approach, named plainly), and what are '
    'the limits (what this method cannot see — the calibration discipline from Chapter 9, '
    'applied to yourself). Lab training gives you the instinct; business writing changes only '
    'the altitude: the body carries the one-paragraph version, the appendix carries the '
    'replicable one. The trust mechanism is specificity — “we interviewed staff” invites '
    'doubt; “we interviewed 14 staff across three shifts, selected by their supervisors’ '
    'nomination and by random pull in equal halves” invites confidence, and its honesty about '
    'the nomination half (a bias, named) invites more. Method sections written to impress '
    'conceal; method sections written to be audited persuade.', bold_lead='Methods.')

h1(doc, 'Deep dive: proposal season — the calendar as strategy')
para(doc, 'Internal proposals live on organizational calendars, and timing is a persuasion '
    'variable most writers ignore. Budget cycles set the physics: the proposal that arrives '
    'during planning season competes for uncommitted money; the identical proposal in month '
    'two of the fiscal year asks someone to defund something already promised — a different '
    'and much harder ask (Chapter 8’s calibration includes the calendar). The disciplines: '
    'learn the cycle (when do budgets lock? when does planning open? who holds the pen in '
    'each phase?) and reverse-schedule your proposal into the soft window; pre-wire before the '
    'season (the hallway conversations of month nine make the proposal of month ten arrive '
    'pre-approved in outline — Chapter 8’s committee work, calendared); and maintain a '
    'proposal pipeline rather than a proposal panic — the professionals who consistently get '
    'funded keep a running list of costed, one-page proto-proposals ready to expand when '
    'windows open or year-end money appears (the “use it or lose it” December is real, and it '
    'rewards whoever has a fundable page ready). The meta-lesson generalizes: documents '
    'compete in time as well as on merit, and the calendar-literate writer wins ties against '
    'better analysts who filed in the wrong month.')

h1(doc, 'Deep dive: defending the document — when the report gets a meeting')
para(doc, 'Formal reports of consequence earn a presentation, and the defense has its own craft '
    '(Chapter 12 covers presentation mechanics; here is the report-specific layer). Never walk '
    'the room through the document — they can read, and narrated table-of-contents is the '
    'spoken furniture summary. Instead: open with the summit and the one number, take the two '
    'strongest anticipated objections head-on (“the two questions this analysis has to survive '
    'are the take-rate assumption and the vendor dependency — here is each”), and hand the room '
    'to questions early, because the meeting exists for what the document cannot do: respond. '
    'Preparation is objection-mapping, not slide-polishing — for each pyramid reason, know its '
    'weakest evidence and your honest answer (the two-sided discipline, live). When a question '
    'exceeds the analysis, the calibrated answer is the strong move: “the data doesn’t reach '
    'that — I can have it by Friday” beats improvisation every time, and the room notices who '
    'knows the edges of their own knowledge. And bring the one-page summary as the leave-behind: '
    'the meeting’s decision-makers will re-decide later, from whatever page survives in their '
    'folder — make sure it is yours.')

h1(doc, 'Deep dive: production — the last mile where documents break')
para(doc, 'Formal documents fail at production more often than dignity admits: the PDF whose '
    'links die, the print run that reveals the margin error, the portal that rejects the file '
    'format at 1:58. The disciplines: PDF is the delivery format (Word files invite '
    'reformatting, expose metadata and tracked changes — Chapter 4’s scrub — and render '
    'differently on every machine), generated with bookmarks from your heading styles so the '
    'navigation survives; verify the PDF, not the source (page count, TOC accuracy, exhibit '
    'placement, link function — the conversion is where drift happens); name the file for its '
    'recipient and its record (“BerryDunn-Feasibility-2026-08-01-FINAL.pdf” — Chapter 5’s '
    'findability, at deliverable scale); for print, check the physical artifact once (margins, '
    'page breaks, color exhibits in grayscale reality); and for portals, upload the day before '
    'with the confirmation screenshot captured — the county case’s checklist, universalized. '
    'Production feels beneath the analysis it delivers. It is also the only part of the '
    'analysis the reader touches first, and Chapter 1’s nonverbal rules apply to documents: '
    'the artifact’s polish is read as the analysis’s rigor, fairly or not.')

h1(doc, 'Templates appendix: three to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. The transmittal memo')
para(doc, '“TO: Council Budget Committee · FROM: [Team] · DATE: 1 Aug 2026 · RE: Broadband '
    'feasibility study — recommendation attached. The attached study answers the question '
    'Council posed in March: can a city-owned network serve our households sustainably? Bottom '
    'line: yes, under the phased build — Phase 1 at $4.2M bounds the exposure and buys the '
    'demand data every comparable city wished it had. The executive summary (page ii) carries '
    'the full case in one page; we’re prepared to present at the August 12 session and welcome '
    'questions before it. — [Name], for the team.”')
h2(doc, '2. The compliance matrix row (build one per “shall”)')
para(doc, '“REQ 3.2.1: ‘Proposal shall include a phased implementation schedule with milestones.’ '
    '→ ADDRESSED: Section C, pp. 9–11, Exhibit 4 (Gantt). → NOTES: milestones mapped to the '
    'county fiscal calendar per REQ 3.2.4.” One row per requirement, submitted as Appendix A '
    'even when not required — you are handing the evaluator their checklist, pre-completed.')
h2(doc, '3. The budget justification line')
para(doc, '“Line 4 — Network operations contractor, $180,000/yr: contracting operations (vs. '
    'hiring 2.0 FTE at ~$210,000 loaded) preserves the exit option through the Phase 1 review '
    'and matches the staffing model of three of four comparable cities (Appendix C). Reverts to '
    'Council decision at month 18.” Cost, alternative considered, evidence, and the built-in '
    'off-ramp — one line’s eyebrow, fully answered.')

h1(doc, 'Formal-document self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'My executive summaries are written last, placed first, and survive forwarding alone.',
    'My summaries state answers and numbers, never furniture (“this report examines…”).',
    'I separate conclusions (interpretation) from recommendations (commitment).',
    'My proposals answer the six silent questions in order — including risks, unprompted.',
    'I mirror RFP structure exactly and track every “shall” in a matrix.',
    'My budgets are checkable line by line and framed against the problem’s cost.',
    'Every citation in my documents traces to a source I have actually seen.',
    'AI-suggested sources are search hints to me, never references.',
    'My technical content layers by altitude: summary, body, appendix.',
    'My tables of contents are generated from heading styles, never typed.',
])
para(doc, 'Scoring: 16–20, you are ready to own client-facing documents — polish the transmittal '
    'craft. 10–15, drill the executive summary anatomy and the citation trace. Below 10, adopt '
    'one rule: nothing enters a reference list unseen. Retake before the capstone submission. '
    'Weighting note: items 1–2 (the summary) and item 7 (the trace) carry the most career '
    'consequence — the summary because it is the page deciders actually read, the trace because '
    'one citation failure retroactively re-prices everything you have ever submitted.')

h1(doc, 'The formal-document playbook')
bullets(doc, [
    ('Capstone / feasibility study →', 'Chapter 9’s engine + this chapter’s dress: branched verdict, one-page summary, generated TOC, traced references.'),
    ('Executive summary →', 'situation · answer+number · reasons · ask. Written last, placed first, standalone, one page.'),
    ('RFP response →', 'their structure, compliance matrix, limits as cliffs, submitted a day early.'),
    ('Unsolicited proposal →', 'sell the problem first; propose the smallest fundable step (the ladder).'),
    ('Budget section →', 'itemized, justified, anchored against the unsolved problem’s cost.'),
    ('Any formal document →', 'three reader paths designed: summary for deciders, body for implementers, appendix for auditors.'),
])

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find a real executive summary (corporate annual reports are free). Grade it: furniture or case? Rewrite its worst sentence.',
    'Take your capstone’s current draft summit. Write the one-page executive summary NOW, before the report exists — then note where it exposed holes in the analysis. (Then rewrite it last, as the rule requires, and compare.)',
    'Trace three citations from any published report to their sources. How many survive the trace intact — and what does the failure rate teach?',
    'Reconstruct a proposal you or your team lost (a pitch, an application, a request). Which quadrant was it, and which section of the skeleton failed?',
    'Map your organization’s (or university’s) budget calendar. When is the soft window — and what one-page proto-proposal should be sitting ready for it?',
    'Read one funded grant abstract in your field (funder websites publish them). Reverse-engineer its outcomes language: what changes, for whom, measured how?',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'Your capstone executive summary is graded on exactly this chapter: the five required '
    'moves (intro, methodology, findings, recommendations, conclusion) executed at the '
    'anatomy’s standard — standalone, answer-first, numbers surfaced, one page, zero errors '
    '(Chapter 4’s top band applies without mercy to a document this short). The full study is '
    'graded as Chapter 9 plus apparatus: pyramid logic, honest evidence, traced sources, '
    'generated navigation, and the three reader paths. At work, the same document decides '
    'budgets — and the summary’s first paragraph decides whether the rest is ever read.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('The furniture summary.', 'Fix: state the case, not the sections — every sentence challengeable in a meeting.'),
    ('Summary written first.', 'Fix: last. You cannot summarize what does not exist; early “summaries” are outlines in disguise.'),
    ('Conclusions and recommendations fused.', 'Fix: interpret, then commit — separately, so readers can accept one without the other.'),
    ('Improving on the RFP’s structure.', 'Fix: their house, their rules — mirror it, and matrix every “shall.”'),
    ('The riskless proposal.', 'Fix: name risks and mitigations unprompted; evaluators read their absence as naive or hiding.'),
    ('Citing the story about the study.', 'Fix: climb to the underlying source; cite what you have actually seen.'),
    ('AI output as a source.', 'Fix: search hint, never reference. Trace or drop — the invented-citation case is a zero everywhere, forever.'),
    ('Typed tables of contents.', 'Fix: generate from heading styles; typed TOCs drift and betray.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“How long should a formal report be?”', 'As long as the decision requires and the appendices can absorb the rest. The body carries what deciding needs; verification lives in back matter. A 15-page body with 40 pages of appendix is a strong shape; the reverse is a filing cabinet with a cover letter.'),
    ('“Our RFP response is due in 48 hours. What gets triaged?”', 'Compliance first (structure, matrix, limits — the pass/fail layer), the executive summary second (it carries the score), pricing accuracy third, prose polish last. A compliant, clear, slightly plain proposal beats an elegant non-submission by exactly the amount of the contract.'),
    ('“Can I reuse boilerplate across proposals?”', 'Qualifications, bios, and methodology descriptions — yes, maintained like code (Chapter 6’s template fleet). The problem statement and solution — never: recycled understanding of THEIR problem is detectable in one paragraph, and it reads as exactly what it is.'),
    ('“What citation style for business documents?”', 'The venue’s, if it states one; APA author–date otherwise (American Psychological Association, 2020) — it is the business-school default and your instructor’s expectation. Consistency matters more than the choice: one style, throughout, without drift.'),
    ('“My appendices are longer than my report. Is that wrong?”', 'It is often right — it means your body carries decisions and your back matter carries proof. The test is referencing: every appendix must be pointed to from the body by its point; the appendix nobody references is storage, not verification.'),
    ('“Who signs the transmittal on a team document?”', 'The accountable owner — one name, “for the team,” with the full roster on the title page. Documents signed by committees are answered by no one; the reader with a question needs a door, not a directory.'),
    ('“The funder’s portal limits us to 5,000 characters per section. How do we write for boxes?”', 'The pyramid compresses gracefully: summit sentence, reasons as labeled phrases, evidence as the tightest numbers. Draft in a document (with counts visible), paste late, and keep the master — portals eat drafts, and character limits are cliffs wearing a text field.'),
    ('“How far in advance should the capstone summary be drafted?”', 'Twice. Once early as a diagnostic — writing the summary before the study exposes every hole in the analysis (try it; the journal prompt makes it an exercise). Once last, as the rule requires, when there is finally something true to summarize. The early draft is scaffolding; never submit it.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('The capstone executive summary (your final).', 'Figure 2 is the grading anatomy; the worked example is your model at full scale.'),
    ('The feasibility study.', 'Chapter 9’s engine + this chapter’s architecture: the branched verdict, the three reader paths, the traced references.'),
    ('Practice questions (course site, Chapter 10).', 'Summary anatomy, proposal quadrants, RFP discipline, citation boundaries.'),
    ('Next unit.', 'Chapters 11–12: professionalism, teams, and presentations — the spoken counterparts of everything built so far.'),
    ('The lecture deck.', 'The Chapter 10 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Front / back matter', 'navigation and authority ahead of the body; references and appendices — the verification layer — behind it.'),
    ('Transmittal letter', 'the one-page handshake that delivers the document and its summit in the sender’s voice.'),
    ('Executive summary', 'the standalone one-page case — written last, placed first, read by everyone who matters.'),
    ('Furniture summary', 'the failure mode that summarizes sections instead of stating the case.'),
    ('Conclusions vs. recommendations', 'interpretation versus commitment — separated so readers can accept one without the other.'),
    ('Proposal quadrants', 'solicited/unsolicited × internal/external — each shifting the burden of proof.'),
    ('Compliance matrix', 'requirement → where addressed → page number; the evaluator’s checklist, pre-built by you.'),
    ('Source credibility ladder', 'primary data to unsourced claims — how much weight each rung safely bears.'),
    ('Citation trace', 'the discipline: nothing enters a reference list unseen.'),
    ('Layering by altitude', 'summary at zero jargon, body defining terms, appendix at full fidelity — three truths, one document.'),
    ('Outputs vs. outcomes', 'what you will do versus what changes — grant evaluators fund the second.'),
    ('Budget–narrative coherence', 'every funded line mentioned, every promised activity staffed — the consistency check that kills more grants than weak ideas.'),
    ('The leave-behind', 'the one-page summary that survives in the decider’s folder — the document that re-decides the meeting later.'),
    ('Proposal pipeline', 'the running file of costed one-page proto-proposals, ready when windows open.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Formal reports serve three readers on three designed paths: summary for deciders, body for implementers, appendices for auditors.',
    'The executive summary is the document most readers read: situation, answer+number, reasons, ask — written last, placed first, standalone.',
    'Conclusions interpret; recommendations commit — keep them separable.',
    'Proposals answer six silent questions, name their risks unprompted, and frame budgets against the problem’s cost.',
    'Solicited proposals are scored before they are read: mirror the structure, matrix the “shalls,” treat limits and deadlines as cliffs.',
    'Evidence lives on the credibility ladder; citations are audit trails, and nothing enters a reference list unseen.',
    'AI output is a search hint, never a source — the invented citation is a zero in class and an obituary in practice.',
    'Technical content layers by altitude, translating mechanisms into the reader’s consequences.',
])

quiz(doc, [
    ('The executive summary is written:',
     ['Last — you cannot summarize what does not exist', 'First, as an outline',
      'By the most junior team member', 'Only for reports over 50 pages']),
    ('“This report examines X, reviews the literature, and offers recommendations” is:',
     ['A strong summary', 'Required by APA',
      'The furniture failure — sections summarized instead of the case', 'A transmittal letter']),
    ('Conclusions and recommendations are separated because:',
     ['Templates require it', 'Readers can accept your interpretation while rejecting your commitment — the graceful fallback',
      'Conclusions are optional', 'Recommendations need citations']),
    ('In a solicited proposal, the requester’s structure is:',
     ['A suggestion', 'Only for government RFPs',
      'Negotiable after submission', 'Absolute — evaluators score with checklists built on it']),
    ('A compliance matrix maps:',
     ['Every requirement to where it is addressed and the page number', 'Costs to benefits',
      'Team members to sections', 'Risks to mitigations']),
    ('The proposal section that most signals real project experience is:',
     ['The cover letter', 'The staffing bios',
      'Evaluation and risks — named unprompted', 'The table of contents']),
    ('The 24-page proposal against a 20-page limit was:',
     ['Scored on its merits', 'Marked non-compliant and scored zero — limits are cliffs',
      'Given partial credit', 'Returned for revision']),
    ('A budget line inviting a raised eyebrow should be:',
     ['Deleted', 'Rounded up',
      'Moved to the appendix', 'Justified where it stands']),
    ('On the credibility ladder, AI output and unsourced web claims:',
     ['Never bear load — trace to a real source or drop the claim', 'Rank above vendor material',
      'Are fine with a disclaimer', 'Count as primary data']),
    ('A paraphrased idea from a source requires:',
     ['Nothing — the words are yours', 'Quotation marks',
      'A citation — paraphrase transfers wording, not ownership', 'Italics']),
    ('The invented citation poisoned the document because:',
     ['The number was wrong', 'One caught fabrication forces re-verification of everything — the credibility ledger goes into receivership',
      'APA format was violated', 'The source was too old']),
    ('Technical content for mixed readers should be:',
     ['Written at the expert level throughout', 'Moved entirely to appendices',
      'Simplified everywhere', 'Layered by altitude: jargon-free summary, defined-terms body, full-fidelity appendix']),
    ('Tables of contents should be:',
     ['Generated from heading styles — typed TOCs drift', 'Typed carefully',
      'Omitted under 30 pages', 'Placed after the summary']),
    ('“Basically true” failed on appeal because:',
     ['The number was actually false', 'The team missed the deadline',
      'Integrity regimes protect process — a forgiven fabrication teaches gambling', 'Appeals never succeed']),
], ['a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Pull a public RFP (municipal sites post them). Build its compliance matrix and identify the three requirements most likely to disqualify a careless bidder.',
    'Why do organizations keep writing furniture summaries when everyone claims to hate them? Locate the incentive — and the fear.',
    'Defend or attack: “Page limits improve proposals.” Use the county case and your own drafting experience.',
    'Your team’s AI assistant drafts a beautifully structured section citing five sources. Design the review protocol — who traces what, before it merges.',
    'The capstone asks for one page. What does the one-page constraint force that ten pages would let you avoid?',
    'A teammate argues: “Nobody checks citations in business — that’s an academic obsession.” Refute or defend with the invented-citation case and one professional scenario of your own.',
    'Your proposal must be signed by a principal who didn’t write it. What does the signer owe the document, and what does the writer owe the signer?',
    'Compare the one-pager discipline to the forty-page RFP response. Which is harder, and what does each hide that the other exposes?',
    'You sit on a review panel and catch one invented citation in an otherwise excellent proposal. Argue the panel’s options — and what you would actually vote.',
])

h1(doc, 'A closing word: the documents that outlive their meetings')
para(doc, 'Everything else in this course is conversation; this chapter is architecture. The '
    'formal report you write for your capstone study — like the proposals and studies you will '
    'write for employers — will be read by people who never attended a single meeting about it, '
    'years after everyone who did has changed jobs. That is the genre’s burden and its gift: '
    'the document must carry everything, and in exchange it carries YOU — your name on the '
    'title page of work that moved money, changed policy, or built the thing. Professionals '
    'keep copies of these documents the way craftsmen keep their best pieces, and interviewers '
    'ask about them by name. Build this one — the capstone — as if it belongs in that '
    'collection, because the habits you use on it are the ones you will have when the stakes '
    'are real. They are already forming. Form them on purpose.')

references(doc, [
    'American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.). APA.',
    'Freed, R. C., Freed, S., & Romano, J. (2010). Writing winning business proposals (3rd ed.). McGraw-Hill.',
    'Minto, B. (2009). The pyramid principle: Logic in writing and thinking (3rd ed.). Financial Times/Prentice Hall.',
    'Tufte, E. R. (2001). The visual display of quantitative information (2nd ed.). Graphics Press.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch10-study-guide.docx')
finish(doc, os.path.abspath(out))
