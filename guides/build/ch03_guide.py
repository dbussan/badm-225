# Chapter 3 Study Guide — Organizing and Drafting Business Messages
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(3, 'Organizing and Drafting Business Messages',
    'Direct and indirect strategy, outlines that think, paragraphs that hold together, and sentences that carry weight.')

h1(doc, 'How to use this guide')
para(doc, 'Chapter 2 decided what your message is for; this chapter builds it. You will learn the two '
    'master patterns for organizing any business message, then work down through outlines, paragraphs, '
    'and sentences — the load-bearing structures of professional writing. Read once through, do the '
    'sentence-workshop exercises with a pen, then hit the Chapter 3 practice bank on the course site.')

h1(doc, 'The organizing decision: direct or indirect?')
para(doc, 'Every business message makes one structural choice before any other: does the main point '
    'come first, or do the reasons come first? That choice — direct versus indirect strategy — '
    'is decided by one input from your Chapter 2 planning: how will the reader feel about the message?')
figure(doc, os.path.join(FIG, 'ch3_strategy.png'),
    'Figure 1. The two master patterns. Reader reaction — not writer comfort — picks the pattern.',
    'Comparison of two message structures. Direct pattern for receptive or neutral readers: main point first, then details and reasons, then goodwill close. Indirect pattern for resistant readers or bad news: buffer and context first, then reasons, then the main point with a forward-looking pivot.')
para(doc, 'The direct pattern serves receptive and neutral audiences — which is most business '
    'communication, most days. Main point in the first sentence; explanation after; goodwill close. It '
    'respects the F-pattern scanning behavior from Chapter 2, survives forwarding, and reads as '
    'confidence. The indirect pattern serves resistance: bad news, refusals, and persuasion against '
    'the grain, where a blunt opening would slam the reader’s mind shut before your reasons get a '
    'hearing. There, honest context and reasons precede the point, so the conclusion arrives '
    'pre-justified. Chapters 7 and 8 develop the indirect arts in full; this chapter’s job is the '
    'decision itself.')
para(doc, 'Two abuses to avoid. Do not use indirect structure to hide from routine clarity — burying '
    'an ordinary request under three paragraphs of preamble is not diplomacy; it is fog. And do not '
    'use directness as a license for bluntness in sensitive moments — “your project is cancelled, '
    'details below” is a wound with a bibliography. Strategy follows the reader’s stakes.',
    bold_lead='The abuses.')

h1(doc, 'Outlining: thinking before formatting')
para(doc, 'An outline is not paperwork — it is the cheapest place to discover that your message does '
    'not hold together. The working method takes three steps: dump every point you might make (the '
    'scratch list); group the points into three-ish families and name each family (these names become '
    'your headings or topic sentences); then sequence the families direct or indirect, per Figure 1.')
figure(doc, os.path.join(FIG, 'ch3_outline.png'),
    'Figure 2. An outline is your purpose, decomposed. Every branch must serve the box above it.',
    'Outline tree diagram: the purpose at top branches into three main points — cost, quality, timeline — each supported by sub-points such as quotes and payback, pilot data and reviews, phases and risks.')
para(doc, 'The discipline that makes outlines work is the same unity test paragraphs use: every branch '
    'must serve the box above it. A fascinating fact that serves no family gets cut, however fond of '
    'it you are — Chapter 2 already warned that planning is also deciding what to leave out. And '
    'keep the families few: working memory comfortably juggles about seven items, plus or minus two '
    '(Miller, 1956), and tired readers on phones hold fewer. Three main points is a business classic '
    'for a reason.')

h1(doc, 'Paragraphs: one claim, held together')
figure(doc, os.path.join(FIG, 'ch3_paragraph.png'),
    'Figure 3. Paragraph anatomy: topic sentence first, support that serves it, coherence that ties it, and the unity test.',
    'Paragraph anatomy diagram: topic sentence stating the paragraph’s one claim first; support providing evidence for that claim only; coherence through transitions and echoed key words; and a unity test — any sentence not serving the topic sentence belongs in another paragraph.')
para(doc, 'Business paragraphs open with their point — the topic sentence is the paragraph’s thesis, '
    'and everything after it is employed by it. Three properties make a paragraph professional. Unity: '
    'one claim per paragraph; the sentence that wanders off supports some other claim and should live '
    'there instead. Coherence: sentences connect through transitions (however, therefore, for example) '
    'and through echoed key words — if sentence one is about “turnaround time,” sentence two should '
    'say “that time,” not “this issue.” Brevity: on screens, four to six lines is a paragraph; eight '
    'is a wall. White space is not wasted space — it is the reader’s handhold.')
para(doc, 'The coherence machinery has a scientific description worth knowing. Readers expect the '
    'opening of a sentence (the topic position) to carry familiar information — the thing we are '
    'already talking about — and the end of a sentence (the stress position) to carry the news '
    '(Gopen & Swan, 1990). Prose that honors old-before-new feels lucid without the reader knowing '
    'why; prose that violates it feels choppy even when every sentence is grammatical.')
figure(doc, os.path.join(FIG, 'ch3_stress.png'),
    'Figure 4. Topic and stress positions: readers expect old information first and the news at the end (Gopen & Swan, 1990).',
    'Sentence position diagram: the topic position at the sentence opening carries old, familiar information; the middle carries connective tissue; the stress position at the sentence end carries new information and emphasis.')
para(doc, 'The stress position is also your emphasis dial. “The committee rejected the proposal” '
    'stresses the proposal; “The proposal was rejected by the full committee” stresses who did it. '
    'Put what you want remembered where the reader’s emphasis naturally lands: last.', bold_lead='Use it.')

h1(doc, 'Sentences: the units that carry weight')
h2(doc, 'Voice: active by default, passive on purpose')
figure(doc, os.path.join(FIG, 'ch3_voice.png'),
    'Figure 5. Active is the default; passive is a tool; passive that hides accountability is the hazard.',
    'Comparison of active voice — “Maria approved the budget,” actor visible, shorter, faster to decode — versus passive voice — “The budget was approved,” useful when the actor is unknown, obvious, or better unnamed. Warning zone: passive that hides accountability, such as “mistakes were made,” when the reader needs to know the actor.')
para(doc, 'Active voice — actor, verb, object — is shorter, faster to decode, and honest about who '
    'did what: the professional default. Passive voice is not an error; it is a tool with three '
    'legitimate jobs: the actor is unknown (“the shipment was damaged in transit”), the actor is '
    'irrelevant or obvious (“the samples were stored at −80 °C”), or diplomatic construction '
    'deliberately spotlights the action over the person (“the figures were transposed” in a message '
    'where blame is not the point). The hazard is the fourth use: passive as accountability camouflage. '
    '“Mistakes were made” is the most famous evasion in political history precisely because everyone '
    'hears the hidden actor. When the reader needs to know who, name who.')
h2(doc, 'Rhythm: vary the length')
figure(doc, os.path.join(FIG, 'ch3_rhythm.png'),
    'Figure 6. Sentence-length variety. After several long sentences, a short one lands like a verdict.',
    'Bar chart of sentence lengths in a well-paced paragraph: 18, 22, 7, 25, and 12 words — the seven-word sentence highlighted as the punch that variety makes possible.')
para(doc, 'Uniform sentences anesthetize — fifteen 20-word sentences in a row read like a metronome. '
    'Professionals vary length deliberately, and they know the trick hiding in Figure 6: after two or '
    'three long sentences, a short one lands like a verdict. It works. Reserve very short sentences '
    'for the points that deserve the spotlight, or the spotlight stops meaning anything.')
h2(doc, 'Parallelism: same job, same form')
para(doc, 'Items doing the same grammatical job must wear the same grammatical form. “The training '
    'covers safety procedures, report filing, and client communication” — three noun phrases, one '
    'clean series. “The training covers safety procedures, how to file reports, and communicating '
    'with clients” breaks the pattern three ways and the reader feels every seam. Parallelism matters '
    'double in the places business readers actually look: bulleted lists, headings, and resume lines. '
    'Start every bullet in a list with the same part of speech and your document looks edited before '
    'anyone reads a word.')
h2(doc, 'Chunking: design for working memory')
figure(doc, os.path.join(FIG, 'ch3_chunk.png'),
    'Figure 7. Chunk for the reader: grouped, labeled lists respect the limits of working memory (Miller, 1956).',
    'Comparison of a wall of text containing fourteen items in one paragraph, which overflows working memory, versus the same content grouped into three headed lists of four to five items each — readable, recallable, actionable. Working memory holds about seven plus or minus two chunks.')
para(doc, 'Fourteen requirements in a paragraph is a memory test; three headed lists of four to five '
    'is a document. Miller’s famous “magical number seven, plus or minus two” (Miller, 1956) is the '
    'reason phone numbers come pre-chunked and the reason your reader cannot follow your unbroken '
    'paragraph of conditions. Group, label, list — the outline logic of Figure 2, applied at the '
    'smallest scale.')

h1(doc, 'Drafting: permission to write badly, briefly')
para(doc, 'With plan and outline in hand, draft fast and forgive yourself. The draft’s only job is to '
    'exist — judging while generating stalls both (the phase separation from Figure 1 of the '
    'chapter’s process). Practical drafting habits: write the easy section first, not necessarily the '
    'opening — momentum transfers; keep the outline visible and let topic sentences come straight '
    'from it; when a wording fight breaks out, type the clumsy version, mark it [FIX], and keep '
    'moving; and never stop at the end of a section — park mid-thought so re-entry is easy tomorrow. '
    'Rudolf Flesch, whose readability research shaped plain-language practice for decades, preached '
    'the same underlying ethic: write for the reader’s ease, not the writer’s ceremony (Flesch, 1949).')

h1(doc, 'Research corner: what makes prose feel clear')
para(doc, 'Clarity has been studied, and three findings recur. First, readers process '
    'actor-action sentences fastest — prose whose grammatical subjects are characters and whose verbs '
    'are actions reads as “clear,” while prose built on abstractions performing abstract verbs reads '
    'as “academic” (the central lesson of Joseph Williams’ classic style curriculum; Williams & '
    'Bizup, 2017). Second, nominalizations — verbs frozen into nouns — are the main machine of '
    'murk: “make a decision about the implementation of” is “decide to implement” wearing three '
    'coats. Unfreeze the verb and sentences shrink and quicken. Third, familiar-before-new ordering '
    '(Gopen & Swan, 1990) does more for flow than any transition word. None of this requires talent; '
    'all of it is checkable in revision — which is Chapter 4’s whole business.')

h1(doc, 'Worked examples: three repairs')
h2(doc, '1. Unburying the lead (direct strategy)')
para(doc, 'Before: “Our team met twice this month to evaluate vendors. We considered many options and '
    'several had competitive prices. After careful discussion of the criteria, we recommend TechServe '
    'for the contract.” After: “We recommend TechServe for the contract. Our team compared five '
    'vendors across two meetings; TechServe offered the best combination of price and support '
    'coverage.” The recommendation moves from the stress position of paragraph three to the topic '
    'position of sentence one — where a neutral, busy reader will actually meet it.')
h2(doc, '2. Unfreezing the nominalizations')
para(doc, 'Before: “The implementation of the utilization of the new scheduling system will result in '
    'a reduction of conflicts.” After: “Using the new scheduling system will reduce conflicts.” Nine '
    'words gone, no meaning lost: implementation, utilization, and reduction were all verbs in '
    'witness protection.')
h2(doc, '3. Repairing the series')
para(doc, 'Before: “The new hires will learn safety procedures, how to file reports, and communicating '
    'with clients.” After: “The new hires will learn safety procedures, report filing, and client '
    'communication” — or, all verbs: “…will learn to follow safety procedures, file reports, and '
    'communicate with clients.” Either form works; mixing forms never does.')

h1(doc, 'Deep dive: four more organizational patterns (and when each serves)')
para(doc, 'Direct and indirect are the master strategies, but inside a message’s body, content '
    'organizes itself along one of several logics — and choosing deliberately beats inheriting '
    'whichever order your notes happened to arrive in.')
bullets(doc, [
    ('Order of importance', '— the business default. Most decision-relevant first, descending. Serves deciders and skimmers; the inverted pyramid at section scale. Choose it unless a reason exists not to.'),
    ('Problem → solution', '— name the pain, then the remedy. The natural skeleton for proposals and recommendations; it front-loads the reader’s motivation to keep reading. Weakness: overused as drama when the reader already knows the problem — then it reads as padding before the point.'),
    ('Chronological', '— time order. Right for procedures (do this, then this), incident reports (what happened when), and project histories. Wrong — seductively wrong — for recommendations, where “the order I did the work” buries the conclusion (the analyst’s heartbreak from Case 1).'),
    ('Spatial / categorical', '— by location, division, or component: the facilities report walking building by building, the review covering product line by product line. Serves completeness and lookup; pair it with an importance-ordered summary so the reader gets a verdict, not just a tour.'),
    ('Comparison', '— alternative by alternative against shared criteria. The vendor evaluation’s natural shape. The craft decision: organize by option (easy to write, hard to compare) or by criterion (harder to write, and exactly how the reader thinks). Choose by criterion when a decision is being made.'),
])
para(doc, 'The meta-rule underneath all five: organize by the reader’s use of the document, not by '
    'the writer’s process of producing it. Every pattern above is legitimate somewhere; the '
    'chronology of your effort is legitimate almost nowhere.', bold_lead='The meta-rule.')

h1(doc, 'Deep dive: the coherence machinery, annotated')
para(doc, 'Old-to-new flow is easier to admire than to build, so here is a paragraph with its '
    'machinery exposed. The sample: “The committee approved the pilot program. THAT APPROVAL came '
    'with two conditions. THE FIRST CONDITION caps enrollment at forty students; THE SECOND requires '
    'a midterm report. THAT REPORT — due March 15 — will decide whether the pilot becomes '
    'permanent.”')
para(doc, 'Watch the handoffs: each sentence opens by grabbing the previous sentence’s news '
    '(approval → that approval; two conditions → the first… the second; a report → that report) '
    'and closes by delivering new cargo into the stress position (two conditions; forty students; '
    'March 15; permanent). The reader is never asked to hold an orphaned fact — every new item is '
    'delivered into a hand the previous sentence already opened. Now the broken version: “The pilot '
    'program was approved by the committee. Enrollment caps at forty students as one of two '
    'conditions. March 15 is when a report is due, which is the second condition, and permanence '
    'depends on it.” Same facts; every handoff dropped; the reader assembles the relationships '
    'themselves. Grammatical, complete — and exhausting. When your prose “feels choppy” and you '
    'cannot say why, audit the handoffs first.', bold_lead='The handoffs.')

h1(doc, 'Deep dive: verbs are the engines')
para(doc, 'The fastest single upgrade to drafting is promoting real verbs. Three audits, in rising '
    'order of ambition.')
para(doc, 'The be-verb audit: circle every is/are/was/were. Each is a junction where a stronger verb '
    'may be hiding: “The new policy is a source of confusion for staff” → “The new policy confuses '
    'staff.” Not every be-verb deserves eviction — “the deadline is Friday” is perfect — but a '
    'paragraph running four be-verbs deep has parked its engines.', bold_lead='Audit one.')
para(doc, 'The nominalization audit, refined: Chapter 3 taught unfreezing; here is the taxonomy. '
    'Guilty nominalizations bury the action of THIS sentence (“made a decision” → “decided”). '
    'Innocent ones name established things: “the decision” as a known object under discussion '
    '(“the decision reached Legal on Tuesday”) is a noun doing honest noun work. The test: is the '
    'action happening in this sentence, or being referred to? Unfreeze the first; keep the second.',
    bold_lead='Audit two.')
para(doc, 'The actor audit: for each sentence, ask “who does what?” — then check whether the '
    'grammatical subject is the who and the verb is the what. “There was agreement among the leads '
    'regarding the postponement of testing” has actors (the leads) and an action (agreeing to '
    'postpone) — both exiled from their grammatical posts. Reinstate them: “The leads agreed to '
    'postpone testing.” Prose whose subjects are characters and whose verbs are actions is what '
    'readers experience as “clear” — the Williams principle from the research corner, now as a '
    'drill (Williams & Bizup, 2017).', bold_lead='Audit three.')

h1(doc, 'Deep dive: paragraph rhythm at document scale')
para(doc, 'Sentence-length variety has a document-level twin: paragraph rhythm. A page of uniform '
    'five-line paragraphs reads as a gray wall even when each paragraph is internally sound; '
    'variety — a three-line opener, a longer development paragraph, a one-line pivot — gives the '
    'page a pulse and gives emphasis somewhere to live. The one-sentence paragraph is the strongest '
    'move in the kit.')
para(doc, 'Used once per document, it lands like a gavel.')
para(doc, 'Used constantly, it is confetti — and its power dies with inflation (the same economics '
    'as Chapter 3’s emphasis toolbox). Deploy it for the verdict, the turn, or the single fact '
    'everything else serves. One more document-scale habit: let white space do structural work — '
    'the gap between sections is a breath the reader needs, not wasted paper. Dense pages read as '
    'hard even when the sentences are easy; layout is part of drafting, not decoration after it.')

h1(doc, 'Headings: the skeleton that skims')
para(doc, 'Anything longer than a screen needs headings — they are the document’s outline, left '
    'visible for the reader. Two crafts matter. First, make headings informative, not categorical: '
    '“Cost: TechServe saves $22,000/year” outworks “Cost Analysis,” because a skimmer reading only '
    'headings should still receive your argument. (Test your next document exactly that way: read '
    'the headings alone. Do they tell the story?) Second, keep heading levels parallel and shallow — '
    'two levels serve almost every business document; four levels is a filing system, not a message. '
    'Headings also discipline the writer: a section that cannot be honestly summarized in its heading '
    'is usually two sections, or none.')

h1(doc, 'Deep dive: lists — the most abused structure in business writing')
para(doc, 'Lists earn their power from three properties prose lacks: they promise parallel items, '
    'they expose count (“three risks” is verifiable at a glance), and they give scanners handholds. '
    'Every abuse of lists breaks one of those promises. The semantics come first: numbered lists '
    'promise sequence or rank — steps that happen in order, priorities that descend; bulleted lists '
    'promise siblings — items of equal standing in no meaningful order. Numbering non-sequential '
    'items falsely implies priority; bulleting a procedure hides that order matters. Choose the '
    'marker by the logic, not the aesthetic.')
para(doc, 'Depth discipline: every item in one list should live at the same altitude — a list '
    'mixing “restructure the supply chain” with “fix the typo on page 4” has broken its sibling '
    'promise, and the reader can no longer trust the count. Length discipline: list items are '
    'compressed prose, not paragraphs wearing bullets; when an item sprawls past two lines, either '
    'compress it or promote it to a headed paragraph. And the density ceiling: a document that is '
    'ALL lists has abdicated — lists excerpt and structure; prose argues, connects, and persuades. '
    'The strongest business pages alternate: a short paragraph that thinks, a list that lands, a '
    'paragraph that draws the consequence. When you cannot decide which to use, ask what the reader '
    'does with the content: scan, count, or execute → list; follow reasoning → prose.',
    bold_lead='Three disciplines.')

h1(doc, 'Deep dive: engineering the drafting session')
para(doc, 'Drafting fast is partly psychology and partly logistics, and both can be engineered. The '
    'psychology first: the blank-page dread that stalls drafts is almost always premature judging '
    '— the internal editor auditioning sentences before they exist. The professional’s trick is '
    'giving the draft explicit permission to be bad: label the file DRAFT-UGLY, tell yourself '
    'nobody sees version one, and remember that revision (Chapter 4) is scheduled — the safety net '
    'is real, so the tightrope can be fast. Perfectionism at the drafting stage is not high '
    'standards; it is judging done at the wrong time, and it produces both worse drafts and fewer '
    'of them.')
para(doc, 'The logistics: draft in sessions sized to the work — 25 to 45 minutes of genuinely '
    'unpinged time (Chapter 5’s attention rules are drafting rules too), with the outline visible '
    'and sources already gathered, because mid-draft research trips are where momentum goes to die. '
    'If a fact is missing, type [GET Q2 NUMBER] and keep moving; collection is a different errand '
    'than composition. End every session mid-thought with a note about what comes next — “next: '
    'the risk section, lead with the vendor dependency” — and tomorrow’s restart costs thirty '
    'seconds instead of twenty minutes. Writers who manage momentum outproduce writers who manage '
    'sentences, at identical talent.', bold_lead='Session design.')

h1(doc, 'The transitions toolbox')
para(doc, 'Coherence between paragraphs is built with the same two tools as coherence within them: '
    'signposts and echoes. Signpost transitions declare the logical relationship — addition '
    '(moreover, also), contrast (however, on the other hand), cause (therefore, as a result), '
    'sequence (first, next, finally), example (for instance). Echo transitions repeat a key word '
    'from the previous paragraph’s stress position in the new paragraph’s topic position: a '
    'paragraph ending on “…which raises the question of cost” hands off perfectly to “That cost has '
    'three components.” Echoes are the stronger tool — invisible, unfakeable, and impossible to '
    'sprinkle on afterward, because they only exist where the thinking actually connects. If you '
    'cannot write the echo, the paragraphs may not belong next to each other.')

h1(doc, 'From outline to draft: a 20-minute walkthrough')
para(doc, 'Here is the full pipeline on a real task: recommending a vendor to a neutral VP '
    '(the Riverside-style memo every analyst eventually writes).')
numbered(doc, [
    'Minutes 0–2 — the plan (Chapter 2): “So that the VP approves renewing with TechServe by Friday, because renegotiated terms save $22,000 a year.” Reader: executive skimmer, neutral, will forward to finance (secondary ring).',
    'Minutes 2–6 — the scratch list: fifteen points, dumped without order: pricing history, the two meetings, competitor quotes, support-response data, migration risk, contract deadline, the pilot glitch, renewal discount…',
    'Minutes 6–9 — grouping: three families emerge and get names that will become headings: “Cost: renewal saves $22K” · “Risk: switching costs exceed savings” · “Quality: support metrics beat all bidders.” The pilot glitch joins Quality; the meeting history joins nothing and dies.',
    'Minutes 9–10 — strategy call: neutral reader → direct. Sentence one is the recommendation plus the strongest number; the families follow in decreasing order of decision weight; the contract deadline becomes the dated call to action.',
    'Minutes 10–20 — the sprint draft: topic sentences copied straight from the family names, support filled beneath each, [FIX] marks left where wording fought back. Draft exists. Judging is scheduled for tomorrow — that is Chapter 4’s appointment.',
])
para(doc, 'Twenty minutes, and the hard intellectual work — deciding, grouping, sequencing — is '
    'finished before the prose pressure starts. Writers who skip to minute ten spend an hour lost in '
    'their own scratch list, formatting sentences that the outline would have deleted.',
    bold_lead='The math.')

h1(doc, 'Teardown: the finished memo opening, annotated')
para(doc, '“I recommend renewing the TechServe contract on the renegotiated terms attached, which '
    'save $22,000 annually. [main point + strongest number, topic position of the entire document] '
    'The decision is due Friday the 20th; details below support a same-week approval. [deadline '
    'surfaced early; permission to skim granted explicitly] Cost: renewal beats all three competing '
    'bids… [informative heading carries the argument; topic sentence = family name] Risk: switching '
    'would cost more than it saves for at least 26 months… [second family, decision-weight order] '
    'Quality: TechServe’s support response averaged 2.1 hours in our pilot versus an industry '
    'median of 9… [concrete over adjectival — the scrutinizer is served] Could you approve by '
    'Friday so we lock the renewal discount? [call to action: act, date, reason]”')
para(doc, 'Every structural rule in this chapter appears in eleven lines: direct strategy, '
    'frontloaded stress-worthy number, informative headings, topic sentences from the outline, '
    'evidence in the body, and a dated ask. The VP can decide from the first two sentences — and '
    'audit everything beneath them.', bold_lead='Count the rules.')

h1(doc, 'Case study 1: the buried recommendation')
para(doc, 'A financial analyst spends two weeks evaluating whether her firm should renew a $180,000 '
    'software contract. Her email to the decision-making VP opens with the project’s history, walks '
    'through the evaluation criteria, discusses each of four alternatives in paragraph-long detail, '
    'notes some pricing nuances, and concludes — in the final paragraph, sentence three — that '
    'renewal on renegotiated terms is clearly best. The VP, triaging email between flights, reads the '
    'first paragraph, skims the second, files it “to finish later,” and asks a colleague that '
    'afternoon: “Did the software evaluation ever reach a conclusion?” The analyst hears about the '
    'comment and is stung — the conclusion was right there.')
numbered(doc, [
    'Where was the main point relative to the reader’s actual reading behavior (Chapter 2’s F-pattern)?',
    'This reader was neutral-to-receptive. Which strategy did the message need, and which did it get?',
    'Sketch the direct-strategy outline (Figure 2 style) for the same content: what becomes sentence one? What becomes skippable?',
    'The analyst chose indirect structure because she wanted to “show the work.” What legitimate need was she serving, and where does that content belong in a direct message?',
])
h2(doc, 'Case analysis')
para(doc, 'The message was organized as an archaeology of the analysis — the order in which the '
    'work was done — rather than for the decision the reader needed to make. Neutral reader, direct '
    'pattern: “I recommend renewing with TechServe on renegotiated terms, saving $22,000 annually; '
    'the comparison below supports it.” The two weeks of diligence is not wasted by frontloading — '
    'it moves into a labeled, skimmable body (Criteria · Alternatives · Pricing) that the VP can '
    'audit if she wishes and skip if she trusts. Showing the work is a legitimate ethos need; the '
    'stress position of the final paragraph is simply the wrong warehouse for it. The professional '
    'heartbreak in this case is common and avoidable: excellent analysis, invisible conclusion.')

h1(doc, 'Case study 2: the incident report that named no one')
para(doc, 'After a minor chemical spill, a lab supervisor files the incident report: “The secondary '
    'containment was found to have been compromised. The transfer was performed without the checklist '
    'having been completed. Corrective measures have been identified and will be implemented.” Legal '
    'is satisfied. The safety committee is not: reading it, they cannot tell who transferred, who '
    'skipped the checklist, whether “corrective measures” have an owner, or whether anything will be '
    'different by Friday. At the review meeting, the supervisor explains each item easily — the '
    'facts were never in doubt. The report simply hid them.')
numbered(doc, [
    'Identify every passive construction and classify it against Figure 5: legitimate tool or accountability camouflage?',
    'Rewrite the three sentences in active voice with named roles (not necessarily named individuals) and dated actions.',
    'When WOULD passive voice be appropriate in an incident report? Give one example.',
    'What does this case add to Chapter 1’s lesson about upward communication and bad news?',
])
h2(doc, 'Case analysis')
para(doc, 'Every sentence passes the grammar check and fails the reader. “Was found to have been '
    'compromised” hides who found it and when; “was performed without the checklist having been '
    'completed” hides the transfer technician’s training gap (the actual root cause); “measures have '
    'been identified” hides that no one yet owns them. Active rewrite: “During Tuesday’s transfer, '
    'the on-duty technician skipped the pre-transfer checklist; the secondary containment tray had a '
    'crack that inspection would have caught. The lab manager will retrain all transfer-qualified '
    'staff by March 14 and has replaced the tray.” Passive remains right where actors are genuinely '
    'irrelevant (“the tray was manufactured in 2019”). The deeper point joins this chapter to Chapter '
    '1: organizations learn from incidents only when reports carry actors, causes, and owners — '
    'grammar is a safety system.')

h1(doc, 'Watch list: three short pieces worth your time')
bullets(doc, [
    ('Helen Sword, “Beware of Nominalizations” (TED-Ed).', 'Five animated minutes on the “zombie nouns” that deaden prose — the unfreezing drill from this chapter, made memorable.'),
    ('Larry McEnerney, “The Craft of Writing Effectively” (University of Chicago Leadership Lab).', 'An hour that reframes writing around value to the reader rather than display by the writer — the most recommended writing lecture on the internet, for good reason.'),
    ('TED-Ed, “Grammar’s great divide: the Oxford comma.”', 'A short, fair fight over one comma — and a painless introduction to the idea that punctuation choices are clarity choices.'),
])

h1(doc, 'Drafting self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'I choose direct or indirect structure deliberately, based on the reader’s likely reaction.',
    'My main point appears in the first two sentences of routine messages.',
    'I outline (even three scratch lines) before drafting anything substantial.',
    'My paragraphs open with topic sentences.',
    'I can name the one claim each of my paragraphs makes.',
    'My default voice is active; my passives are chosen, not accidental.',
    'I vary sentence length — and save short sentences for points that deserve them.',
    'My lists are parallel: same job, same grammatical form.',
    'I chunk dense content into labeled groups instead of walls.',
    'I draft without editing, and edit without drafting.',
])
para(doc, 'Scoring: 16–20, your structural instincts are strong — Chapter 4 will sharpen the polish. '
    '10–15, drill the two lowest items; topic sentences and active voice pay fastest. Below 10, adopt '
    'one rule this week: main point first, in every routine message. Retake at midterm.')

h1(doc, 'The drafting playbook')
bullets(doc, [
    ('Blocked at the opening?', 'Draft the easiest section first; openings are easier to write once the middle exists.'),
    ('Sentence fighting back?', 'Type the clumsy version, mark [FIX], keep moving — revision is a separate appointment.'),
    ('Paragraph sprawling?', 'Find its topic sentence. If it has two, it is two paragraphs.'),
    ('Sentence feels muddy?', 'Find the actor and the action; make them subject and verb; unfreeze nominalizations.'),
    ('Series feels bumpy?', 'Check parallelism: same job, same form.'),
    ('List longer than seven?', 'Group and label — Miller’s limit is the reader’s limit.'),
    ('Want emphasis?', 'Short sentence, stress position, or a heading — not bold everything.'),
    ('Ending a work session?', 'Park mid-thought; tomorrow’s re-entry will thank you.'),
])

h1(doc, 'Sentence workshop: ten repairs (answers follow)')
para(doc, 'Fix each with this chapter’s tools before checking the answers below. Name the tool as you '
    'use it — diagnosis is the skill.')
numbered(doc, [
    '“A decision was made to implement a postponement of the launch.”',
    '“Our team met twice. Many vendors were considered. Prices were compared carefully. We recommend Apex.”',
    '“The new policy affects vacation requests, how overtime is approved, and employees wanting to swap shifts.”',
    '“The report, which include last months figures, are due to the manger by Friday.”',
    '“It should be noted that there is a requirement for all visitors to sign in.”',
    '“The failure of the experiment was due to the contamination of the sample by the technician.” (The reader is the safety board.)',
    '“We provide innovative solutions leveraging synergistic capabilities to optimize outcomes.”',
    '“Employees must complete the form. The form is available on the portal. The portal requires your ID badge number. Badge numbers are printed on the badge back.”',
    '“Although the budget, which had been under review for several weeks by the committee that oversees departmental spending, was approved.”',
    '“The meeting is at 3. Bring the numbers. Don’t be late. It’s important. See you there.”',
    '“There was agreement among the leads regarding the postponement of testing.”',
    '“Although costs rose 8%, the project finished on schedule.” (You are the CFO’s analyst, flagging the budget.)',
    '“The system, which was installed in 2019 by the previous vendor whose contract was terminated for performance issues that were documented extensively, needs replacement.”',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    'Unfreeze the nominalizations: “We decided to postpone the launch.”',
    'Bury nothing: lead with “We recommend Apex,” then one supporting sentence — direct strategy plus active voice.',
    'Parallelism: “…affects vacation requests, overtime approvals, and shift swaps.”',
    'Proofreading layer (preview of Chapter 4): include→includes, months→month’s, are→is, manger→manager.',
    'Cut the throat-clearing and unfreeze: “All visitors must sign in.”',
    'Voice as accountability: for a safety board, name roles and causes — “The technician’s sampling procedure contaminated the sample, which invalidated the experiment.” (Diplomatic contexts might justify the original; safety review does not.)',
    'Buzzword fog: say the actual service — “We build scheduling software that cuts clinic wait times.” If you cannot replace the fog, the sentence had no cargo.',
    'Chunk and sequence: one numbered list, four steps, in doing-order — the reader should never assemble your process from prose shards.',
    'The sentence never lands: “Although” promises a contrast that never arrives. “After several weeks of committee review, the budget was approved.”',
    'Rhythm inverted: five staccato sentences bury the one that matters. “The 3:00 meeting decides next year’s budget — bring the numbers.” One verdict sentence beats five fragments.',
    'The actor audit: reinstate the who and the what. “The leads agreed to postpone testing.” Eleven words become six, and the sentence acquires a pulse.',
    'Subordination serves the reader’s job: for a budget flag, the cost fact takes the main clause — “Although the project finished on schedule, costs rose 8%.” Same facts, correct emphasis for THIS reader.',
    'The freight-train relative clause: split and sequence. “The system needs replacement. Installed in 2019 by a vendor later terminated for documented performance issues, it has outlived its support.” Main point first; history subordinated — or cut entirely if the reader doesn’t need it.',
])

h1(doc, 'Deep dive: subordination — deciding what rides in back')
para(doc, 'Complex sentences make a structural claim: the main clause carries the point; subordinate '
    'clauses carry context. Which is why the same two facts produce opposite sentences. “Although '
    'costs rose 8%, the project finished on schedule” is a success story with a footnote; “Although '
    'the project finished on schedule, costs rose 8%” is a budget problem wearing a consolation. '
    'Neither is dishonest — both facts appear in both — but each tells the reader what to weigh, '
    'and choosing is not optional: one clause WILL be main. Writers who subordinate at random are '
    'assigning emphasis at random, and their readers walk away weighing the wrong facts.')
para(doc, 'The drill: for any two-fact sentence, ask which fact the reader should act on — that '
    'fact gets the main clause and, ideally, the stress position at the end. Context, concession, '
    'and background ride in the subordinate clause, usually up front where the topic position '
    'expects the familiar. This is also the honest version of “spin”: emphasis assignment is a '
    'legitimate editorial power exactly as long as both facts remain visible and true. Burying the '
    'material fact in a subordinate clause of sentence nine is where emphasis management crosses '
    'into concealment — the Oakhurst lesson (Chapter 4) has a syntax edition.', bold_lead='The drill.')
para(doc, 'Punctuation completes the structural toolkit, because the marks between clauses are '
    'signals, not decoration. The colon promises delivery: what follows explains or itemizes what '
    'preceded. The semicolon claims siblinghood; it joins two complete thoughts of equal weight and '
    'implies the reader should feel the connection. The em-dash interrupts — for emphasis, for an '
    'aside that deserves attention — and loses its force with repetition, like every emphasis '
    'device in this chapter. Parentheses whisper (context the reader may skip). Choosing among them '
    'is choosing how loudly the connection speaks; the writer who knows the difference controls '
    'volume at a resolution most colleagues never notice — but every reader feels.',
    bold_lead='The marks as signals.')

h1(doc, 'Deep dive: closings — the document’s stress position')
para(doc, 'Everything Gopen and Swan teach about sentence ends scales to the whole document: the '
    'final position is where emphasis naturally lands, which makes closings too valuable to waste on '
    'ceremony. Yet most business documents end with their weakest material — “please don’t '
    'hesitate to reach out,” “thank you for your time and consideration” — boilerplate occupying '
    'the message’s most memorable real estate. The professional closing does one of three jobs. The '
    'action close restates the ask with its date, one final time, standing alone: after everything, '
    'the reader’s eyes leave the document holding exactly what to do (this is why the site’s email '
    'anatomy puts the call to action last). The consequence close names what the recommendation '
    'buys: “Approved this week, the renewal locks $22,000 in annual savings before the discount '
    'expires” — the stakes, freshly framed, as the parting image. The forward close, for messages '
    'without asks, points at the path ahead: “Next update Tuesday; escalation call Thursday if the '
    'fix slips.” All three share a property: they contain information. If your final sentence could '
    'be deleted with no loss, it is not a closing — it is upholstery sitting in the emphasis seat. '
    'Write closings the way you now write topic sentences: deliberately, and last, once the document '
    'has told you what deserves the final word.')

h1(doc, 'Research corner II: measuring readability')
para(doc, 'Readability can be estimated, and Word will do it for you (File → Options → Proofing → '
    '“Show readability statistics”). The classic measures descend from Rudolf Flesch’s work: Flesch '
    'Reading Ease scores 0–100 (higher is easier; most successful business prose lands roughly '
    '50–70), and the Flesch-Kincaid Grade Level translates the same arithmetic into U.S. school '
    'grades (Flesch, 1949). Both formulas run on just two inputs — sentence length and syllables '
    'per word — which is both their utility and their limit. They cannot detect a buried lead, a '
    'broken parallel, or a lie; they only notice long sentences and long words. Use them as a smoke '
    'detector, not a judge: a grade level of 16 on a customer email is a real alarm; a grade level '
    'of 9 does not certify clarity. The deeper measures of this chapter — strategy, unity, '
    'old-to-new flow — still require a human reading like a reader.')

h1(doc, 'The emphasis toolbox')
para(doc, 'Everything in a message cannot be important, or nothing is. Professionals create emphasis '
    'with position and structure, in roughly this order of power:')
bullets(doc, [
    ('Position.', 'First sentence of the message; last position of the sentence (the stress position); first line after a heading. Real estate is emphasis.'),
    ('Isolation.', 'A one-sentence paragraph. Used once, it is a spotlight; used often, it is confetti.'),
    ('Sentence length.', 'The short sentence after long ones — the verdict effect from Figure 6.'),
    ('Labeled structure.', 'A heading or a bolded lead-in (“Deadline:”) — signage the F-pattern cannot miss.'),
    ('Typography, sparingly.', 'Bold for the one deadline or decision. Italics for gentle stress. ALL CAPS for nothing — it reads as shouting and scans worse.'),
    ('What does NOT work:', 'exclamation points, “very/really/extremely,” and bolding whole paragraphs — inflation that devalues the currency.'),
])

h1(doc, 'Structure by container: email, memo, report')
para(doc, 'The same architecture scales across containers; only the furniture changes. Email: subject '
    'line = the message’s job; sentence one = main point; one screen; lists over paragraphs; the call '
    'to action stands alone at the end where the F-pattern terminates. Memo: the To/From/Date/Subject '
    'block does your bibliographic work; a one-line summary tops anything over a page; informative '
    'headings carry the argument; the file-ability is the point — write for next year’s reader. '
    'Report (previewing Chapters 9–10): the executive summary IS the direct strategy — the whole '
    'argument in miniature, written last, placed first; sections follow the outline tree with '
    'headings as its visible branches; every exhibit earns its place by serving a named section. One '
    'skeleton, three bodies — master the skeleton and the containers stop being separate skills.')

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find a message you wrote that buried its lead. Reorganize it direct. What resisted — the content, or the feeling that showing your work first was safer?',
    'Collect three passive sentences from real documents around you and classify each: legitimate tool or camouflage? What does each hide?',
    'Take one paragraph you are proud of and map its topic/stress positions. Does information flow old → new? Where does it break?',
    'Time yourself drafting 200 words with editing forbidden, then 200 words editing as you go. Compare the clocks — and the drafts.',
    'Take two facts from your current work — one favorable, one not — and write the sentence both ways, subordinating each in turn. Which version would you send, and what does that choice reveal about the line between emphasis and concealment for you?',
    'Rewrite the closing sentence of the last three documents you produced. What was sitting in the stress position, and what deserved to be?',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'At this chapter’s level, the supervisor test gets structural teeth. Sendable-as-is now '
    'means: strategy matched to the reader’s reaction; the main point findable by a skimmer; '
    'paragraphs that each make one claim, opened by it; active voice except where passive is doing a '
    'chosen job; parallel series; no walls. A message can pass Chapter 2’s planning test and still '
    'fail here — right purpose, right audience, wrong architecture. Both layers get graded, in this '
    'course and in every inbox after it.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('Organizing by chronology of your work.', 'Fix: organize by the reader’s decision. History goes in a skippable labeled section, if anywhere.'),
    ('Indirect structure as procrastination.', 'Fix: indirect is for resistance and bad news, not for nerves about routine asks.'),
    ('Paragraphs without topic sentences.', 'Fix: state the claim first; audition every other sentence against it.'),
    ('Accidental passives.', 'Fix: circle every “was/were + verb-ed”; keep only the ones you can defend.'),
    ('Fourteen-item paragraphs.', 'Fix: group, label, list (Figure 7).'),
    ('Uniform sentence lengths.', 'Fix: read aloud; where you drone, split or combine. Save a short sentence for the verdict.'),
    ('Broken parallelism in lists.', 'Fix: first word of every bullet, same part of speech.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Isn’t indirect structure just manipulation?”', 'It is sequencing, not deception: every fact still arrives. Ordering reasons before a hard conclusion is how humans stay listening — the manipulation line is crossed by hiding facts, not by ordering them.'),
    ('“My professor said never use passive voice.”', 'A useful exaggeration for beginners. The mature rule: active by default, passive on purpose, never as camouflage.'),
    ('“How long should a paragraph be?”', 'One claim long. On screens that usually means 3–6 lines. If unity is intact, length is style; if unity is broken, even three sentences are too many.'),
    ('“Do these micro-rules matter once AI drafts for me?”', 'More. AI produces grammatical prose with generic structure; the value you add is exactly this chapter — strategy, emphasis, and rhythm chosen for a real reader (Chapter 15).'),
    ('“Three main points always?”', 'No — but if you have nine, the reader will remember three of them chosen at random. Better you choose which three, and group the rest beneath them.'),
    ('“Does organization matter in a two-line email?”', 'Yes, in miniature: which of the two lines comes first is still a strategy call, and the last words still sit in the stress position. The units shrink; the physics don’t.'),
    ('“I organize fine in outlines but my drafts drift.”', 'Keep the outline physically visible while drafting and copy each family name in as the topic sentence BEFORE writing the paragraph — drift usually means the outline left the room. If a paragraph still insists on becoming something else, the outline may be wrong; stop and re-group rather than fighting the prose.'),
    ('“Are semicolons too formal for email?”', 'They read formal, not wrong. In quick email the period is the workhorse; save semicolons for documents where their siblinghood signal earns its keep. No reader ever complained that two short sentences were too clear.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 3).', 'Direct/indirect calls, topic sentences, parallelism repairs, and voice choices — the bank mirrors this guide.'),
    ('Writing prompts (course site).', 'The reorganization and market-research outline prompts apply Figures 1 and 2 directly.'),
    ('Your market research assignment.', 'Its required sections are an outline handed to you — this chapter is how you fill them so each section holds together.'),
    ('Next chapter.', 'Chapter 4 is the judging phase: revising for conciseness and clarity, and proofreading like a professional.'),
    ('The lecture deck.', 'The Chapter 3 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Direct strategy', 'main point first, details after — for receptive and neutral readers.'),
    ('Indirect strategy', 'buffer and reasons before the main point — for resistant readers and bad news.'),
    ('Frontloading', 'placing the main point where scanning readers will actually meet it: first.'),
    ('Topic sentence', 'the paragraph’s one claim, stated first; everything after works for it.'),
    ('Unity / coherence', 'one claim per paragraph; sentences tied by transitions and echoed key words.'),
    ('Topic position / stress position', 'sentence opening (old information) and sentence end (the news and the emphasis) (Gopen & Swan, 1990).'),
    ('Active / passive voice', 'actor-verb-object versus acted-upon constructions; default versus tool.'),
    ('Nominalization', 'a verb frozen into a noun (“utilization”) — the main machine of murky prose.'),
    ('Parallelism', 'items with the same job wearing the same grammatical form.'),
    ('Chunking', 'grouping content into labeled sets sized for working memory (Miller, 1956).'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'One structural decision precedes all others: direct (main point first) for receptive readers, indirect (reasons first) for resistance and bad news.',
    'Outlines are thinking tools: dump, group into ~3 named families, sequence — and cut what serves no family.',
    'Paragraphs make one claim, open with it, and hold together through transitions and echoed key words.',
    'Sentences flow old-information-first to news-last; the stress position at the end is your emphasis dial (Gopen & Swan, 1990).',
    'Active voice is the default; passive is a tool for unknown, irrelevant, or diplomatically unnamed actors — never camouflage.',
    'Vary sentence length; save short sentences for verdicts. Keep series parallel. Chunk for working memory (Miller, 1956).',
    'Draft fast and judge later — generating and judging are different jobs, and doing both at once stalls both.',
])

quiz(doc, [
    ('The choice between direct and indirect strategy is decided by:', ['Message length','The reader’s likely reaction to the message','The writer’s seniority','The time of day']),
    ('The direct pattern opens with:', ['A buffer','The reasons','The main point','An apology']),
    ('Indirect strategy is appropriate for:', ['All internal email','Bad news and resistant readers','Any message to executives','Routine requests you feel nervous about']),
    ('A topic sentence is:', ['The last sentence of a paragraph','The paragraph’s one claim, stated first','Any sentence containing the topic word','A transition']),
    ('“The training covers safety procedures, how to file reports, and communicating with clients” fails on:', ['Unity','Parallelism','Voice','Chunking']),
    ('Readers expect the END of a sentence to carry:', ['Old information','The new information and emphasis (the stress position)','The subject','Transitions']),
    ('Which is a legitimate use of passive voice?', ['Hiding who made an error','“The samples were stored at −80 °C” — actor obvious/irrelevant','Making prose sound formal','Avoiding topic sentences']),
    ('“Mistakes were made” is famous as:', ['Good diplomacy','Passive voice used as accountability camouflage','A topic sentence','Parallel structure']),
    ('Miller’s (1956) “magical number” tells writers to:', ['Use seven paragraphs','Chunk content into labeled groups sized for working memory','Write seven-word sentences','Limit documents to seven pages']),
    ('A nominalization is:', ['A named actor','A verb frozen into a noun, like “utilization”','A proper noun','A parallel series']),
    ('“Using the new system will reduce conflicts” improves on “the implementation of the utilization of…” chiefly by:', ['Adding detail','Unfreezing nominalizations into verbs','Passive voice','A buffer']),
    ('After several long sentences, a very short sentence:', ['Is an error','Lands with emphasis — variety creates the spotlight','Must be deleted','Needs a semicolon']),
    ('The analyst’s buried recommendation failed because the message was organized by:', ['The reader’s decision','The chronology of her work','Direct strategy','Parallel structure']),
    ('In the incident-report case, the safety committee needed:', ['More formal language','Actors, causes, and owners — grammar as a safety system','Longer paragraphs','Indirect strategy']),
], ['b','c','b','b','b','b','b','b','b','b','b','b','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Find a real message organized by the writer’s process instead of the reader’s decision. Rebuild its outline direct. What earns sentence one?',
    'Collect three passives from documents around you and classify each: tool or camouflage? Rewrite the camouflage.',
    'Take your most recent substantial paragraph and audition every sentence against its topic sentence. What gets cut or moved?',
    'When has bluntness-as-directness hurt a message you sent or received? Where was the line between direct and merely abrupt?',
    'Chunk this: rewrite a dense policy paragraph from your workplace or university as labeled lists. What did the grouping decisions force you to understand?',
])

references(doc, [
    'Flesch, R. (1949). The art of readable writing. Harper & Brothers.',
    'Gopen, G. D., & Swan, J. A. (1990). The science of scientific writing. American Scientist, 78(6), 550–558.',
    'Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97.',
    'Nielsen, J. (2006). F-shaped pattern for reading web content. Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/',
    'Williams, J. M., & Bizup, J. (2017). Style: Lessons in clarity and grace (12th ed.). Pearson.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch03-study-guide.docx')
finish(doc, os.path.abspath(out))
