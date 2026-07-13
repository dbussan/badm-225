# Chapter 8 Study Guide — Persuasive Messages
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(8, 'Persuasive Messages',
    'Moving readers who could say no toward yes — with structure, evidence, and influence that survives scrutiny.')

h1(doc, 'How to use this guide')
para(doc, 'Persuasion is the summit of Unit 3: requests where the reader holds real power to refuse. '
    'This chapter assembles everything before it — Chapter 2’s audience planning, Chapter 3’s '
    'strategy, Chapter 16’s influence ethics — into message architecture. Read it alongside the '
    '“Influencing Positively” work in this course; they are the same skill in two costumes.')

h1(doc, 'What persuasion is (and is not)')
para(doc, 'A persuasive message asks a reader to spend something — money, time, comfort, political '
    'capital — that they are free not to spend. That freedom is the defining condition: you are not '
    'instructing subordinates or informing colleagues; you are earning a decision. Two consequences '
    'follow. First, the reader’s interests are the only fuel available — Chapter 2’s you-view stops '
    'being good manners and becomes the entire engine. Second, ethics stay load-bearing: influence '
    'built on true claims and real overlap survives scrutiny and repeat encounters; anything else is '
    'manipulation on a timer (the visibility test below applies to every technique in this '
    'chapter, and Chapter 16 leans on it too).')

h1(doc, 'The appeals: ethos, pathos, logos — balanced')
figure(doc, os.path.join(FIG, 'ch8_appeals.png'),
    'Figure 1. Aristotle’s three appeals. The weakest leg is where persuasion fails.',
    'Triangle of Aristotle’s appeals: ethos (credibility) at the top, pathos (values and emotion) and logos (evidence and logic) at the base. A persuasive message balances all three; the weakest leg is where it fails.')
para(doc, 'Twenty-three centuries after Aristotle catalogued them, the appeals remain the diagnostic '
    'kit for any pitch (Aristotle, trans. 2007). Logos is the evidence architecture: numbers, pilots, '
    'comparisons. Pathos is the connection to what the audience already values — security, pride, '
    'fairness, time with their families; business writing rarely needs tears, but it always needs '
    'stakes. Ethos is the permission to be believed: your track record, your demonstrated grasp of '
    'the reader’s world, and — powerfully — your visible fairness in naming costs and objections. '
    'Diagnose failed pitches with the triangle: brilliant logic that died usually lacked ethos; a '
    'beloved presenter whose idea went nowhere usually skipped logos.')

h1(doc, 'The AIDA architecture')
figure(doc, os.path.join(FIG, 'ch8_aida.png'),
    'Figure 2. AIDA: attention, interest, desire, action — a pipeline, not a paint-by-numbers.',
    'AIDA sequence: attention (a hook belonging to the reader — problem, statistic, question), interest (the reader’s situation named accurately), desire (evidence — numbers, pilots, social proof, objections answered), action (one small, specific, dated ask).')
para(doc, 'The classic persuasive sequence — attention, interest, desire, action — has organized '
    'sales writing for over a century, and its modern cousin, Monroe’s Motivated Sequence, has '
    'organized persuasive speaking nearly as long (Monroe, 1935). The stages do real work when each '
    'earns its name. Attention belongs to the reader, not to you: their problem quantified (“we '
    're-enter every sample twice”), a question they feel, a stake they own — never “We are pleased '
    'to introduce our company.” Interest is your accuracy about their situation; readers lean in '
    'when they feel understood, and stop reading when paragraph two reveals you don’t know how '
    'their lab actually works. Desire is the evidence layer — where logos lives and objections get '
    'answered. Action is one small, specific, dated ask. The whole pipeline can run in four '
    'sentences or four pages; scale is style, sequence is structure.')

h1(doc, 'The evidence layer: how desire is actually built')
figure(doc, os.path.join(FIG, 'ch8_cialdini.png'),
    'Figure 3. Cialdini’s six levers — each ethical only when the underlying claim is true.',
    'Cialdini’s six influence principles: reciprocity (give first), consistency (small yeses grow), social proof (four of five regional labs already switched), liking (rapport as groundwork), authority (cite credentials, data, experts), scarcity (real deadlines and limits, never invented ones).')
para(doc, 'Decades of experimental work identify recurring levers that move decisions — six in '
    'Cialdini’s original framework, with a seventh (unity) added in the 2021 expanded edition — '
    'and each maps onto message craft. Reciprocity: the favor precedes the ask — the '
    'analysis you attach free is why the meeting request lands (Chapter 6’s goodwill capital, '
    'cashing a check). Consistency: people honor their own prior commitments, which is why pilots '
    'precede rollouts and why the commitment ladder (below) works. Social proof: “four of the five '
    'regional labs have switched” moves risk-averse readers more than any adjective. Authority: '
    'cite the credential, the dataset, the named expert. Liking: rapport built before the pitch is '
    'groundwork; during the pitch it is garnish. Scarcity: real deadlines move decisions — and '
    'invented ones destroy ethos the day they are discovered, which is always. The ethical test for '
    'all six is truth: every lever is legitimate exactly when the claim underneath it is real.')

h1(doc, 'Two-sided arguments: concede to convince')
figure(doc, os.path.join(FIG, 'ch8_twosided.png'),
    'Figure 4. Two-sided beats one-sided with every audience that isn’t already convinced — and weak arguments dilute strong ones.',
    'Comparison of one-sided argument (only your case; works only on the already-convinced) versus two-sided argument with rebuttal (yes, it costs $2,400 — here is the six-week payback; wins with skeptics and survives scrutiny). Note: weak throwaway arguments dilute strong ones.')
para(doc, 'Chapter 2 introduced objection-naming as planning; persuasion research gives it teeth. '
    'With any audience that is skeptical, informed, or will hear the counterarguments later — '
    'i.e., every business audience worth persuading — two-sided messages with rebuttal outperform '
    'one-sided cheerleading: naming the strongest objection yourself earns the credibility that '
    'makes your rebuttal believable. Two disciplines refine it. Concede the real objection, not a '
    'straw man; readers know the difference. And resist the urge to pile on every argument you '
    'have: averaging psychology means a weak reason dilutes strong ones — three strong claims beat '
    'three strong claims plus four filler ones. Depth of processing matters too: audiences who care '
    'scrutinize arguments, while distracted audiences ride cues like authority and social proof '
    '(the central and peripheral routes of Petty & Cacioppo, 1986) — which is why the same message '
    'needs numbers for the analyst and the one-line social proof for the skimmer above her.')

h1(doc, 'The commitment ladder and the calibrated ask')
figure(doc, os.path.join(FIG, 'ch8_ladder.png'),
    'Figure 5. The commitment ladder: each small yes makes the next one natural.',
    'Commitment ladder: read the one-pager, join the twenty-minute demo, run a two-week pilot, adopt team-wide — each small yes making the next natural.')
figure(doc, os.path.join(FIG, 'ch8_spectrum.png'),
    'Figure 6. Calibrate the ask to the audience’s starting position, from hostile to supportive.',
    'Audience position spectrum from hostile (goal: reduce hostility, not win today) through skeptical (two-sided argument with evidence and a small first ask) and neutral (benefits plus clear action) to supportive (make acting easy now).')
para(doc, 'The single most common persuasive error is asking for marriage on the first date: '
    'team-wide adoption, in one email, from a cold start. The ladder converts one large '
    'improbability into a sequence of small probabilities — read the one-pager, take the demo, run '
    'the pilot — each step easy, each yes making the next one consistent (Cialdini’s commitment '
    'lever, structured). Calibration completes it: supportive audiences need the action made easy '
    'now; neutral ones need benefits and a clear ask; skeptics need the two-sided treatment and the '
    'smallest possible first rung; hostile audiences are a special case where today’s win is '
    'reduced hostility and a kept channel — Chapter 16’s face-saving rules matter more than any '
    'sequence.')

h1(doc, 'The proposal skeleton: persuasion at business scale')
figure(doc, os.path.join(FIG, 'ch8_proposal.png'),
    'Figure 7. The proposal skeleton: hook, solution and value, evidence, cost framed honestly, the small dated ask.',
    'Proposal skeleton: hook (the reader’s problem quantified), solution plus value (what it does to their numbers), evidence (pilot data, reference customers, the strongest objection answered), cost framed against the cost of doing nothing, and the ask (one small dated step such as a thirty-minute demo).')
para(doc, 'Internal proposals — the persuasive genre you will write most — compress into five '
    'moves. The hook quantifies the reader’s problem in their numbers. The solution is stated with '
    'its value logic (Chapter 17’s language: what it does to willingness-to-pay or cost). The '
    'evidence layer carries the pilot data, the reference, and the strongest objection answered in '
    'daylight. The cost appears framed against the cost of doing nothing — the honest comparison, '
    'since “no” is never free. And the ask is one rung of the ladder, dated. Note what is absent: '
    'company history, feature tours, and adjectives. Executives fund arithmetic attached to '
    'credible people.')

h1(doc, 'Deep dive: pricing the ask — anchors, frames, and the honest use of both')
para(doc, 'How a number is presented changes how it is judged, and persuasive writers work with '
    'that psychology honestly or lose to those who don’t. Anchoring: the first number in a '
    'negotiation or proposal becomes the reference point everything after is judged against '
    '(Kahneman, 2011) — which is why the cost-of-doing-nothing belongs BEFORE your price '
    '(“duplicate entry burns roughly $31,000 of tech time annually; the system costs $6,800”), '
    'and why leaving the anchor to the reader’s imagination surrenders the frame. Relative '
    'framing: $6,800 “per year” and “$130 a week” and “about the cost of one external audit '
    'finding” are the same number wearing three coats — choose the comparison native to the '
    'reader’s mental accounting, and choose truthfully (the “pennies a day” frame on a '
    'multi-year commitment is technically true and reads as a trick, which prices your ethos in '
    'for free). Loss and gain frames: prospect theory’s central finding — losses loom larger '
    'than equivalent gains — means “stop losing 30 tech-hours a month” and “save 30 tech-hours '
    'a month” are not the same sentence to a human reader; loss frames move risk-averse '
    'audiences harder, and overusing them reads as fearmongering. The ethical line for all three '
    'is the one this chapter keeps drawing: frames select among true presentations; they never '
    'manufacture false ones. The comparison must hold up when the analyst checks it — because '
    'the analyst checks it.')

h1(doc, 'Deep dive: persuading committees — the multi-reader pitch')
para(doc, 'Proposals increasingly face committees, and committees are not big individuals — they '
    'are small political systems with predictable dynamics. The pre-work matters more than the '
    'document: Chapter 16’s pre-wiring (individual conversations before the meeting) surfaces '
    'each member’s objection while it is still cheap to address, converts the persuadable into '
    'co-owners (“building on Dana’s suggestion…” in the proposal itself), and identifies the '
    'one member whose skepticism anchors the others. The document then writes to the room’s '
    'currencies at once (Chapter 2’s benefit taxonomy, deployed in parallel): the economic case '
    'for the budget holder, the operational case for the implementer, the risk case for the '
    'chair — each labeled, each findable by its owner in a skim. Committee-specific craft: '
    'give the group something to decide, not something to discuss (“approve the pilot” beats '
    '“thoughts on automation?” — committees discuss indefinitely and decide only what is '
    'framed decidably); anticipate the tabling move (“if more data is wanted, the pilot IS the '
    'data gathering” pre-empts the committee’s favorite non-decision); and build the summary '
    'page as if it were the only page, because for most members it is. Win the pre-wired '
    'members, arm the summary page, and the meeting ratifies what the process already built — '
    'which is what experienced proposers mean when they say the meeting is the last step of '
    'persuasion, not the first.')

h1(doc, 'Persuasion workshop: five repairs (answers follow)')
numbered(doc, [
    '“Our firm has 47 years of combined experience and a passion for excellence. We offer end-to-end solutions across the full spectrum of your needs. We would welcome the opportunity to discuss how we can add value.”',
    '“The new software has 14 major features including customizable dashboards, real-time sync, advanced reporting, mobile access, API integration, and much more!”',
    '“You need to approve this by Friday or the whole project fails. There is really no alternative. Everyone agrees this is the only option.”',
    '“This proposal will save money, improve morale, increase efficiency, boost quality, enhance our reputation, and position us for the future.”',
    '“I know you’re busy and this probably isn’t a priority and I hate to even ask, but if you ever have a spare moment, maybe we could possibly chat about the budget idea sometime?”',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    'Vendor-view hook, zero reader content: no problem named, no evidence, an ask (“discuss how we can add value”) that costs an hour and promises nothing. Repair: open with THEIR quantified problem, offer one number of proof, ask for thirty minutes with an agenda.',
    'A feature tour where a mechanism-to-outcome chain belongs. Repair: pick the ONE feature that serves this reader’s known pain, ladder it to their outcome (“real-time sync means your Friday reconciliation disappears”), park the rest in an attachment.',
    'Manufactured scarcity plus false consensus plus reactance bait — three ethos detonations in three sentences (Brehm, 1966: pressure this naked gets tested on principle). Repair: the real deadline with its real reason, the honest alternative and its cost, and the freedom acknowledged (“your call — here’s what each path looks like”).',
    'Six unweighted claims — the dilution effect in its natural habitat; the reader averages them into mush. Repair: the best THREE, each with its evidence; cut “enhance our reputation and position us for the future” entirely (rung-one abstractions, Chapter 4).',
    'The ask apologized into nonexistence: five hedges, no benefit, no size, no date. Repair: “Fifteen minutes this week on the budget idea? The Q3 numbers make it timely, and I think it saves your team real hours — Thursday afternoon work?” Confidence is not presumption; it is information about whether YOU believe the pitch.',
])

h1(doc, 'Templates appendix: three pitches to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. The internal proposal email (full AIDA in one screen)')
para(doc, '“Subject: Cut duplicate sample entry — pilot proposal (decision by 7/18). Our techs '
    'enter every sample twice; at current volume that’s ~400 duplicate entries a week and our '
    'most likely audit finding. Barcode intake eliminates the second entry: the Fargo lab’s '
    '90-day pilot cut entry time 41% with zero transcription findings. Cost: $6,800/yr against '
    '~30 tech-hours/month currently burned — payback in about seven weeks. The honest downside: '
    'two clunky weeks while it learns our codes; Fargo called week three ‘never going back.’ '
    'Ask: approve a 60-day pilot on Line 2 (vendor holds the discount through 7/18). Comparison '
    'sheet attached.”')
h2(doc, '2. The commitment-ladder opener (cold, external)')
para(doc, '“Subject: Question about your March webinar on LIMS validation. Dr. Alvarez — your '
    'audit-trail segment solved a problem my lab fought all year, except one piece: amendment '
    'logs under 21 CFR 11. If you have fifteen minutes in the next two weeks, I’d value your '
    'answer — and I’ll send our validation checklist in return, which your team may find '
    'useful.” (Their expertise honored, one specific question, reciprocity offered, smallest '
    'possible rung.)')
h2(doc, '3. The budget defense (persuading to KEEP something)')
para(doc, '“Before the line item goes: the tutoring center cost $38K last year and retained 61 '
    'students who cited it in exit surveys — at $9,400 tuition each, that’s $573K of retained '
    'revenue against $38K of cost. Cutting it books the savings this quarter and the losses '
    'next fall, where they won’t carry the center’s name. If the budget must give, the '
    'evening-hours pilot ($6K) is the honest candidate — details attached.” (Loss frame, '
    'earned; the counter-offer that proves good faith.)')

h1(doc, 'Research corner: why fewer, stronger arguments win')
para(doc, 'Two findings deserve their own spotlight because they cut against instinct. First, the '
    'dilution effect: when strong arguments share a message with weak ones, audiences average '
    'rather than add — the throwaway “it will also look more modern!” measurably weakens the '
    '$40,000 savings claim beside it. Prune ruthlessly; your case is your best three arguments, not '
    'your longest list. Second, the elaboration insight (Petty & Cacioppo, 1986): persuasion that '
    'travels the central route — real scrutiny of real arguments — produces durable agreement, '
    'while peripheral-route persuasion (cues, likability, authority glow) produces agreement that '
    'evaporates under later counter-argument. The practical translation: win the analyst with '
    'evidence even when you could charm the room, because the room will talk to the analyst '
    'tomorrow.')

h1(doc, 'Worked example: the same pitch, before and after')
para(doc, 'Before (sent to a lab director): “Our company is a leading provider of innovative sample '
    'management solutions trusted by hundreds of laboratories. Our platform offers barcode '
    'integration, customizable workflows, cloud backup, audit trails, and much more. We would love '
    'to schedule a demonstration to show you everything our solution can do!”')
para(doc, 'After: “Your techs re-enter every sample ID twice — once at intake, once at analysis — '
    'which at your posted volume is roughly 400 duplicate entries a week and your most likely source '
    'of transcription errors at audit. Barcode intake eliminates the second entry: in a 90-day pilot '
    'at a lab your size, entry time fell 41% and transcription findings went to zero. It costs '
    '$6,800 a year — against the ~30 tech-hours a month the duplicate entry currently burns. The '
    'two labs in your network already using it are glad to take a call. Worth a 30-minute demo '
    'Thursday, before your Q4 audit prep starts?”')
para(doc, 'Autopsy the difference: the hook moved from the vendor’s pride to the reader’s problem, '
    'quantified in the reader’s own volume; features became one mechanism tied to one outcome; '
    'evidence arrived with a pilot number and social proof; cost showed up voluntarily, framed '
    'against the status quo’s cost; and the ask shrank from “everything our solution can do” to '
    'one dated half hour with a reason attached. Same product. Different discipline.',
    bold_lead='The autopsy.')

h1(doc, 'Case study 1: the fundraising email A/B test')
para(doc, 'A university alumni office tests two appeals for a scholarship fund. Version A: “Our '
    'university has a proud tradition of excellence spanning 140 years. The Alumni Scholarship Fund '
    'supports deserving students in continuing that tradition. Every gift matters. Please consider '
    'giving today.” Version B: “Last year, 61 students stayed enrolled because an alumni-funded '
    'scholarship covered the gap their aid package missed — students like Maria R., a first-gen '
    'junior in chemistry who works twenty hours a week at the campus lab. This year 74 students are '
    'on the waiting list. $180 covers one student’s lab fees for a semester; 500 alumni giving that '
    'amount clears the entire list. Will you cover one student’s fees — by Friday, when the '
    'enrollment hold lifts?” Version B outraises A by a factor the office describes as “not '
    'close.”')
numbered(doc, [
    'Map both versions onto AIDA. Where does Version A leave the pipeline?',
    'Inventory Version B’s levers: identify the pathos vehicle, the logos spine, the social proof, the scarcity — and check each for truthfulness.',
    'Version B asks for $180, not “support.” Connect the calibrated ask to the ladder and to Kahneman-style concreteness (Chapter 4).',
    'Draft Version C for a different audience: a corporation considering a $25,000 named sponsorship. What changes in every stage?',
])
h2(doc, 'Case analysis')
para(doc, 'Version A is institution-view throughout: its attention belongs to the university, its '
    'interest stage never names a reader, its desire layer is one adjective (“deserving”), and its '
    'action (“consider giving”) is unfalsifiable. Version B runs the full pipeline: attention '
    'through a concrete stake (61 students, one named story — pathos as a person, not a plea), '
    'desire through arithmetic ($180 = lab fees; 500 gifts = the list cleared) that makes one '
    'donor’s marginal effect visible, social proof and scarcity that are both checkably true, and '
    'an action that is small, specific, dated, and reasoned. The corporate Version C shifts every '
    'stage’s currency: attention becomes workforce pipeline, desire becomes named-fund visibility '
    'and recruiting access, the ask becomes a meeting — because at $25,000 the ladder, not the '
    'letter, closes the gift.')

h1(doc, 'Case study 2: persuading upward — the timesheet mutiny')
para(doc, 'A team lead must persuade her skeptical field crew — twelve technicians who already '
    'distrust “office software” — to adopt mobile timesheets, after a mandate from finance. Her '
    'first draft, written in ten minutes, opens: “Starting Monday, all time entry moves to the '
    'FieldTime app. This is mandatory per Finance. Training video attached. Non-compliance will '
    'delay payroll processing.” She sleeps on it (Chapter 4) and rewrites: “You told me the worst '
    'part of Fridays is reconstructing the week from memory — some of you keep paper logs just to '
    'survive it. The app kills that: you log a job in two taps when you close it, and Friday '
    'becomes zero paperwork. Real talk on the downside: the first week is clumsy while it learns '
    'your job codes — Rob’s crew at the Fargo yard said week one was annoying and week three was '
    '‘never going back.’ Finance requires this by month-end either way; what I can offer is the '
    'easy path: I’ll be on the 6:30 call Monday to walk the first entry with you, and I’ve loaded '
    'everyone’s codes already. Two taps Monday morning. That’s the whole ask.”')
numbered(doc, [
    'The mandate exists either way. What does persuasion add when compliance could be commanded — and what would the first draft have cost beyond compliance?',
    'Find the two-sided move, the social proof, and the calibrated first ask in the rewrite.',
    'The rewrite opens with the crew’s own words about Fridays. Which appeal is that, and why does it outperform any statistic here?',
    'Rewrite the finance-mandate sentence for maximum honesty AND minimum resentment. What does Chapter 16 say about invoking authority you didn’t choose?',
])
h2(doc, 'Case analysis')
para(doc, 'Commanded compliance and earned adoption produce identical week-one numbers and opposite '
    'trajectories: the first draft purchases sullen minimum usage plus a grapevine narrative '
    '(“office doesn’t trust us”), while the rewrite spends persuasion on what mandates cannot buy '
    '— good-faith usage and the crew’s own advocates. Its machinery: attention via the crew’s '
    'articulated pain (pathos with perfect ethos, because it proves she listened — Chapter 1’s '
    'listening as influence); a genuine two-sided concession (“week one is clumsy”) that buys the '
    'credibility spent on “never going back”; peer-level social proof (Rob’s crew, not a vendor '
    'quote); and a first ask shrunk to two taps with the leader physically present at 6:30 — '
    'skin in the game as ethos. The mandate sentence models honest authority-invoking: state the '
    'constraint plainly, take no shelter behind it, and locate your own agency in what you can '
    'offer (“the easy path”). Blaming finance would be true and corrosive; owning the transition is '
    'true and useful.')

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Niro Sivanathan, “The counterintuitive way to be more persuasive” (TED).', 'The dilution effect, from the researcher himself: why your weakest argument is subtracting from your strongest.'),
    ('Daniel Pink, “The puzzle of motivation” (TED).', 'What actually moves people when tasks require thought — essential calibration for anyone persuading professionals.'),
    ('Ernesto Sirolli, “Want to help someone? Shut up and listen” (TED).', 'Persuasion’s prerequisite in one story: proposals built on the audience’s actual situation, not your model of it.'),
])

h1(doc, 'Persuasion self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'My hooks belong to the reader — their problem, their stake — not to me or my product.',
    'I can name the strongest real objection to my last pitch, and I named it in the message.',
    'My evidence layer contains numbers or verifiable claims, not adjectives.',
    'I prune weak arguments rather than piling them on.',
    'My asks are calibrated: one rung, small, specific, dated.',
    'I use social proof and scarcity only when they are literally true.',
    'I balance the triangle: I know which appeal is my habitual weakest.',
    'I persuade rather than merely announce, even when I hold the authority to command.',
    'I build ethos before I need it — the favor precedes the ask.',
    'Every technique I use would survive the reader seeing it named.',
])
para(doc, 'Scoring: 16–20, you are already the colleague whose proposals get funded — refine the '
    'evidence layer. 10–15, drill the reader-owned hook and the calibrated ask. Below 10, one rule '
    'this week: name the objection yourself. Retake at midterm.')

h1(doc, 'Journal prompts')
numbered(doc, [
    'Recall the last time you were genuinely persuaded of something consequential. Reverse-engineer it: which appeals, which levers, what sequence? What does your own case teach you?',
    'Find a pitch in your inbox that failed on you. Autopsy it against AIDA and the triangle: where exactly did it lose you?',
    'Write the two-sided version of something you currently advocate one-sidedly. Did conceding the objection weaken your position — or your attachment to it?',
    'Where in your life are you asking for marriage on the first date? Design the ladder.',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'Persuasive assignments in this course are graded on the pipeline: a hook the reader owns, '
    'accuracy about their situation, an evidence layer with at least one number and the strongest '
    'objection answered, honest levers, and a calibrated dated ask — plus everything Chapters 2–4 '
    'already require. The supervisor test sharpens here into the funding test: would a busy '
    'decision-maker, reading only your message, have what they need to say yes — and a reason to '
    'say it now?')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('The vendor-view hook.', 'Fix: open with their problem, quantified in their numbers. “We are pleased to introduce…” is a delete key’s favorite sentence.'),
    ('Feature tours.', 'Fix: one mechanism, tied to one outcome the reader already wants.'),
    ('Argument hoarding.', 'Fix: your best three. The dilution effect means the fourth is subtracting.'),
    ('The hidden price.', 'Fix: name the cost yourself, framed against the cost of doing nothing — the objection you name is the credibility you keep.'),
    ('The oversized ask.', 'Fix: one rung of the ladder, dated. Marriage proposals come after demos.'),
    ('Manufactured scarcity.', 'Fix: real deadlines only. Invented urgency detonates ethos on discovery — and discovery is certain.'),
    ('Winning the room, losing the analyst.', 'Fix: central-route evidence even when charm would carry the meeting; the room consults the analyst tomorrow.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Isn’t all this just manipulation with better manners?”', 'The visibility test settles it case by case: would the reader, seeing your technique named, still feel respected? True claims, real overlap, honest levers pass. Invented scarcity, straw-man concessions, and fake social proof fail — and also stop working the moment they’re detected, which makes ethics and effectiveness the same policy here.'),
    ('“Direct or indirect for persuasive messages?”', 'Persuasion is the third pattern: neither the blunt open of good news nor the buffer of bad news, but a reader-owned hook followed by the case. The ask can front-load once interest exists — hence the ladder.'),
    ('“How long should a persuasive message be?”', 'As long as the evidence requires and no longer — the dilution effect punishes padding. Four sentences can run full AIDA; a $250K proposal may need ten pages. Sequence is structure; length is stakes.'),
    ('“What if I win the argument and still get a no?”', 'Then the real objection was never spoken — budget cycles, politics, a competing loyalty. Ask for it: “What would need to be true for this to work?” (Chapter 16’s question tool). Sometimes the honest answer is Chapter 7’s: the no stands, and the path back is the prize.'),
    ('“Can AI write persuasion?”', 'It drafts pipelines competently and generates objection lists brilliantly (Chapter 2’s planning use). But the evidence must be yours and true, the audience knowledge is yours, and the ethos on the line is yours. Never let it invent the numbers — verify every claim it drafts (Chapter 15).'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 8).', 'Pipeline staging, appeal diagnosis, lever ethics, and ask calibration.'),
    ('“Influencing Positively” assignments.', 'This chapter is the written theory of that work; Chapter 16 is its spoken twin.'),
    ('Your market research and feasibility documents.', 'Their recommendation sections are proposals — Figure 7 is their skeleton.'),
    ('Next unit.', 'Chapters 9–10: reports and proposals at full scale, where today’s skeleton grows sections and evidence appendices.'),
    ('The lecture deck.', 'The Chapter 8 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Persuasive message', 'a request the reader is free to refuse — earning a decision rather than announcing one.'),
    ('Ethos / pathos / logos', 'credibility, values-and-emotion, and evidence-and-logic: the triangle whose weakest leg fails first (Aristotle).'),
    ('AIDA', 'attention → interest → desire → action; Monroe’s Motivated Sequence is its spoken sibling (Monroe, 1935).'),
    ('Reader-owned hook', 'an opening whose subject is the reader’s problem or stake, never the writer’s pride.'),
    ('Two-sided argument', 'conceding and rebutting the strongest real objection — credibility earned at the point of concession.'),
    ('Dilution effect', 'weak arguments average down strong ones; prune to your best three.'),
    ('Central / peripheral routes', 'durable persuasion through scrutinized arguments versus fragile persuasion through cues (Petty & Cacioppo, 1986).'),
    ('Commitment ladder', 'sequenced small yeses — one-pager, demo, pilot — replacing one large improbability.'),
    ('Calibrated ask', 'the request sized to the audience’s position on the hostile–supportive spectrum.'),
    ('Cialdini’s levers', 'reciprocity, consistency, social proof, liking, authority, scarcity — ethical exactly when true (Cialdini, 2021).'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Persuasion earns decisions from readers free to refuse — the you-view becomes the engine, and ethics stay load-bearing.',
    'Balance the triangle: ethos, pathos, logos — the weakest leg is where pitches die (Aristotle).',
    'Run the pipeline: reader-owned attention, accurate interest, evidence-built desire, one calibrated action (AIDA; Monroe, 1935).',
    'Argue two-sided: name and rebut the strongest real objection; prune weak arguments — dilution averages them in (Cialdini, 2021; Petty & Cacioppo, 1986).',
    'Climb the ladder: small dated asks, sequenced — pilots before rollouts, demos before contracts.',
    'Frame cost against the cost of doing nothing, and let every lever pass the truth test.',
    'Win the analyst, not just the room: central-route agreement is the kind that survives tomorrow’s counterargument.',
])

quiz(doc, [
    ('The defining condition of a persuasive message is:',
     ['A hostile reader', 'A large budget',
      'A reader free to refuse', 'An external audience']),
    ('Aristotle’s three appeals are:',
     ['Ethos, pathos, logos', 'Attention, interest, desire',
      'Hook, evidence, ask', 'Buffer, reasons, news']),
    ('A pitch with brilliant logic that still died most likely lacked:',
     ['Length', 'More features',
      'Formatting', 'Ethos — permission to be believed']),
    ('The attention stage of AIDA belongs to:',
     ['The writer’s company', 'The reader — their problem, stake, or question',
      'The product', 'The call to action']),
    ('“We are pleased to introduce our innovative solutions…” fails as a hook because:',
     ['Too short', 'Too informal',
      'It is vendor-view — the reader owns no part of it', 'It lacks scarcity']),
    ('Two-sided arguments outperform one-sided ones with:',
     ['Every audience not already convinced', 'No audiences',
      'Only hostile audiences', 'Only executives']),
    ('The dilution effect means:',
     ['Long messages persuade more', 'Evidence dilutes emotion',
      'Repetition persuades', 'Weak arguments average down strong ones — prune to your best']),
    ('Durable agreement comes from the central route because:',
     ['It is faster', 'Scrutinized arguments survive later counterargument; cue-based agreement evaporates (Petty & Cacioppo, 1986)',
      'It requires no evidence', 'Charm fades']),
    ('The commitment ladder works through which lever?',
     ['Scarcity', 'Authority',
      'Consistency — each small yes makes the next natural', 'Liking']),
    ('“Four of the five regional labs have already switched” is:',
     ['Social proof — legitimate exactly because it is checkable', 'Scarcity',
      'Reciprocity', 'A buffer']),
    ('Manufactured scarcity is a mistake because:',
     ['Deadlines never persuade', 'It shortens messages',
      'It is illegal everywhere', 'Its discovery is certain and detonates ethos']),
    ('Cost in a proposal should be framed:',
     ['In a footnote', 'Against the cost of doing nothing — the honest comparison',
      'After signature', 'Never']),
    ('In the timesheet case, “week one is clumsy” bought:',
     ['Sympathy', 'Time',
      'The credibility spent on “never going back” — the two-sided move', 'Nothing']),
    ('The calibrated ask for a skeptical audience is:',
     ['The smallest real rung — with the two-sided case beside it', 'Team-wide adoption now',
      'No ask at all', 'A mandate citation']),
], ['c', 'a', 'd', 'b', 'c', 'a', 'd', 'b', 'c', 'a', 'd', 'b', 'c', 'a'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Bring the best persuasive message you have ever received. Map its pipeline and levers — and identify the one choice that made it work.',
    'Which Cialdini lever does your industry overuse to the point of self-parody? What has that done to its effectiveness?',
    'Defend or attack: “Naming your price early is always the stronger move.” Use the two-sided research and one real example.',
    'Construct the commitment ladder for something you actually want this term — from first rung to final ask, with dates.',
    'Where is the line between calibrating to an audience and pandering to one? Build the test.',
])

references(doc, [
    'Aristotle. (2007). On rhetoric: A theory of civic discourse (G. A. Kennedy, Trans., 2nd ed.). Oxford University Press. (Original work ca. 350 BCE)',
    'Brehm, J. W. (1966). A theory of psychological reactance. Academic Press.',
    'Cialdini, R. B. (2021). Influence, new and expanded: The psychology of persuasion. Harper Business.',
    'Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.',
    'Monroe, A. H. (1935). Principles and types of speech. Scott, Foresman.',
    'Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch08-study-guide.docx')
finish(doc, os.path.abspath(out))
