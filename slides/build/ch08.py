# Chapter 8 — Persuasive Messages (47 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 8"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Persuasive Messages",
    "Moving readers who could say no toward yes — structure, evidence, and influence that survives scrutiny", D)
notes(s, "Chapter 8: the summit of Unit 3. Twin of the Influencing Positively assignments.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Run", "the AIDA pipeline: reader-owned attention, accurate interest, evidence-built desire, one calibrated action."),
    ("Balance", "the triangle — ethos, pathos, logos — and diagnose which leg your pitches lack."),
    ("Argue", "two-sided: concede and rebut the strongest real objection."),
    ("Climb", "the commitment ladder: pilots before rollouts, demos before contracts."),
    ("Keep", "every lever ethical: true claims, real overlap, the visibility test."),
], D, nxt())
notes(s, "Objectives map to the Chapter 8 bank.")

s = bullets_slide(prs, "What persuasion is (and is not)", [
    ("The defining condition:", "the reader is FREE to refuse. You are earning a decision, not announcing one."),
    ("Consequence one:", "the reader's interests are the only fuel — the you-view becomes the engine."),
    ("Consequence two:", "ethics stay load-bearing. True claims and real overlap survive scrutiny; everything else is manipulation on a timer."),
    ("The test for every technique here:", "would the reader, seeing it named, still feel respected?"),
], D, nxt())
notes(s, "Chapter 16's visibility test governs the whole chapter.")

s = section_slide(prs, "01", "The appeals",
    "Ethos, pathos, logos — the weakest leg fails first.", D, nxt())
notes(s, "Section 1.")

s = icon_rows_slide(prs, "Diagnosing with the triangle", [
    ("🏛", "Logos — the evidence architecture", "Numbers, pilots, comparisons. Executives fund arithmetic."),
    ("♥", "Pathos — stakes, not tears", "Connection to what they already value: security, pride, fairness, time."),
    ("✓", "Ethos — permission to be believed", "Track record, demonstrated grasp of their world — and visible fairness in naming costs."),
    ("⚖", "The diagnosis", "Brilliant logic that died lacked ethos. The beloved presenter who went nowhere skipped logos."),
], D, nxt())
notes(s, "Aristotle's kit, 23 centuries on.")

s = section_slide(prs, "02", "The pipeline",
    "AIDA: a sequence, not a paint-by-numbers.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "Attention → Interest → Desire → Action", [
    ("ATTENTION", "The READER'S problem, quantified. Never “we are pleased to introduce…”"),
    ("INTEREST", "Their situation, named accurately — readers lean in when understood."),
    ("DESIRE", "The evidence layer: numbers, social proof, the objection answered."),
    ("ACTION", "One small, specific, dated ask. Yes, made easy."),
], D, nxt(), note_text="Four sentences or four pages — scale is stakes; sequence is structure. (Monroe's Motivated Sequence is the spoken sibling.)")
notes(s, "Each stage must earn its name.")

s = two_col_slide(prs, "The same pitch, before and after",
    "Before (vendor-view)", [
        "“Our company is a leading provider of innovative sample management solutions…”",
        "“…barcode integration, customizable workflows, cloud backup, and much more!”",
        "“We would love to schedule a demonstration!”",
    ],
    "After (reader-owned)", [
        "“Your techs re-enter every sample twice — ~400 duplicate entries a week, your top audit risk.”",
        "“In a 90-day pilot at a lab your size: entry time −41%, transcription findings zero. $6,800/yr against ~30 tech-hours/month burned now.”",
        "“The two labs in your network using it will take your call. 30-minute demo Thursday, before Q4 audit prep?”",
    ], D, nxt())
notes(s, "Same product, different discipline. Full autopsy in the study guide.")

s = section_slide(prs, "03", "The evidence layer",
    "Where desire is actually built — and where ethics live.", D, nxt())
notes(s, "Section 3.")

s = icon_rows_slide(prs, "Cialdini's six levers — ethical exactly when true", [
    ("⇄", "Reciprocity", "The favor precedes the ask — attach the free analysis, then request the meeting."),
    ("🪜", "Consistency", "Small yeses grow: pilots before rollouts. (The ladder, next slide.)"),
    ("👥", "Social proof", "“4 of 5 regional labs switched” moves risk-averse readers more than adjectives."),
    ("📜", "Authority", "Cite the credential, the dataset, the named expert."),
    ("⏳", "Scarcity", "REAL deadlines move decisions. Invented ones detonate ethos on discovery — and discovery is certain."),
], D, nxt())
notes(s, "Liking is the sixth: rapport built before the pitch is groundwork; during, garnish.")

s = flow_slide(prs, "The commitment ladder", [
    ("“Read the one-pager?”", "30 seconds of yes"),
    ("“Join the 20-min demo?”", "Low-stakes second yes"),
    ("“Run a 2-week pilot?”", "Evidence generated together"),
    ("“Adopt team-wide”", "Now consistent with three prior yeses"),
], D, nxt(), note_text="The most common persuasive error: asking for marriage on the first date. Calibrate the first rung to the audience — smallest for skeptics.")
notes(s, "One large improbability becomes a sequence of small probabilities.")

s = two_col_slide(prs, "Two-sided beats one-sided",
    "One-sided", [
        "Only your case, adjectives forward",
        "Works only on the already-convinced",
        "Collapses when they hear the counterargument later — and they will",
    ],
    "Two-sided + rebuttal", [
        "“Yes, it costs $2,400 — here's the six-week payback.”",
        "Credibility earned at the point of concession",
        ("Two disciplines:", "concede the REAL objection, not a straw man — and prune: weak arguments DILUTE strong ones"),
    ], D, nxt())
notes(s, "The dilution effect: audiences average arguments rather than add them. Best three, always.")

s = bullets_slide(prs, "Win the analyst, not just the room", [
    ("Two routes to yes (Petty & Cacioppo, 1986):", "central (scrutinized arguments) and peripheral (cues: charm, authority glow)."),
    ("Central-route agreement is durable;", "peripheral agreement evaporates under tomorrow's counterargument."),
    ("The practical rule:", "bring the numbers even when charm would carry the meeting — the room consults the analyst tomorrow."),
    ("Layer the message:", "the one-line social proof for the skimmer, the pilot data for the scrutinizer (Chapter 2's readers)."),
], D, nxt())
notes(s, "Why substance beats sizzle at business timescales.")

s = flow_slide(prs, "The proposal skeleton", [
    ("HOOK", "Their problem, quantified in their numbers"),
    ("SOLUTION + VALUE", "What it does to WTP or cost (Chapter 17's language)"),
    ("EVIDENCE", "Pilot data · references · the objection, answered in daylight"),
    ("COST, FRAMED", "Against the cost of doing nothing — “no” is never free"),
    ("THE ASK", "One rung, dated: “30-minute demo Thursday?”"),
], D, nxt(), note_text="Absent by design: company history, feature tours, adjectives.")
notes(s, "The internal proposal — the persuasive genre you'll write most.")

s = bullets_slide(prs, "Case: the fundraising A/B test", [
    ("Version A:", "“Our university has a proud tradition of excellence… every gift matters… please consider giving.” Institution-view at every stage."),
    ("Version B:", "“61 students stayed enrolled because alumni covered the gap… 74 are waitlisted. $180 covers one student's lab fees; 500 alumni clear the list. By Friday, when the enrollment hold lifts?”"),
    ("Every lever, checkably true:", "a named story (pathos as a person), donor-scale arithmetic, real scarcity, an ask that is small, specific, dated."),
    ("Result:", "“not close.”"),
], D, nxt())
notes(s, "Concreteness makes one donor's marginal effect visible.")

s = bullets_slide(prs, "Case: persuading when you could command", [
    ("The mandate exists — finance requires mobile timesheets.", "Draft one: “Mandatory per Finance. Training video attached. Non-compliance delays payroll.”"),
    ("The rewrite opens with the crew's own words", "about reconstructing Fridays from memory — listening as ethos."),
    ("The two-sided move:", "“week one is clumsy” buys the credibility spent on Rob's crew's “never going back.”"),
    ("The ask:", "two taps Monday, with the leader on the 6:30 call — skin in the game. Commands buy compliance; persuasion buys advocates."),
], D, nxt())
notes(s, "Honest authority-invoking: state the constraint, take no shelter behind it, own the easy path.")

s = section_slide(prs, "04", "Persuasive requests",
    "The everyday genre: favors, resources, and changes you can't command.", D, nxt())
notes(s, "Section 4: applied persuasion inside the organization — where most persuasive writing actually happens.")

s = bullets_slide(prs, "Asking for a favor that gets granted", [
    ("Make the ask immediately findable —", "buried favor-asks read as ambushes when finally discovered in paragraph four."),
    ("Show you did the homework their yes requires.", "'The dates that work are attached, the room is held, and I need only your slot preference' — effort transferred is friction removed."),
    ("Name why THEM, honestly.", "'You ran this format twice' is flattering because it's specific and true. Generic flattery is a tell."),
    ("Size the ask accurately and say the size.", "'This is roughly two hours across March' respects them; 'it won't take long' is what every large ask says."),
], D, nxt())
notes(s, "The complete-ask standard from Chapter 6 plus the persuasive layer: reduced friction, honest scoping, specific ethos.")

s = bullets_slide(prs, "The raise (or promotion) case, in writing first", [
    ("Build the memo before the meeting.", "One page: scope changes, delivered results with numbers, market context — the conversation then has an exhibit."),
    ("Argue the role, not the need.", "Rent going up is real and irrelevant; responsibility grown past the title is the fundable argument."),
    ("Pick the reader's moment.", "Budget season, post-win, review cycle — timing is a persuasion lever you fully control (scarcity's quiet cousin)."),
    ("Calibrate the rung:", "sometimes the winning ask is 'what would the case for senior analyst need to show by Q4?' — a first yes that writes the criteria with them."),
], D, nxt())
notes(s, "The commitment ladder applied to careers. The criteria-setting ask is the underused move: it converts a possible no into a co-authored plan.")

s = bullets_slide(prs, "Persuading peers: the process change nobody ordered", [
    ("You have no authority — which is the tell", "that this is pure persuasion: their interests are the only fuel available."),
    ("Lead with THEIR pain, not your vision.", "'You lose every Friday afternoon to the merge' beats 'I think we should modernize our workflow.'"),
    ("Pilot small, report honestly.", "'Two weeks, just our team, and we keep the old system running' — the reversible trial disarms the risk objection before it forms."),
    ("Let the early adopter sell it.", "Rob saying 'never going back' at standup outpersuades your best paragraph (social proof from inside the room)."),
], D, nxt())
notes(s, "Lateral persuasion is the purest test of the chapter. The timesheet case later runs this exact play.")

s = two_col_slide(prs, "The favor request: before and after",
    "Before", [
        "'Hey! Hope you're doing well! So this is kind of a big ask, and totally understand if you're busy…'",
        "Three paragraphs of apology-hedging before the ask surfaces",
        "The ask, once found: vague scope, no dates, no materials",
    ],
    "After", [
        "'Could you give the 20-minute welcome talk at analyst onboarding on March 12 (10:00, recorded)?'",
        "'Your session was rated #1 last cohort — the slot is genuinely yours to lose.'",
        "'Deck template and last year's recording attached; A/V handled. Confirm by the 3rd and I'll take everything else.'",
    ], D, nxt())
notes(s, "The hedging opener reads as considerate to the writer and as dread to the reader. The rewrite: findable ask, true ethos, transferred effort, dated close.")

s = section_slide(prs, "05", "Sales messages",
    "Persuasion to strangers — where every weakness gets deleted, not debated.", D, nxt())
notes(s, "Section 5: outbound sales writing. Colder audience, higher volume, zero patience — the pipeline under maximum compression.")

s = bullets_slide(prs, "Cold outreach that survives the delete reflex", [
    ("You have one line and two seconds.", "The subject and first sentence do 90% of the work — spend your best material there, not in paragraph three."),
    ("Prove you know THIS reader in sentence one.", "'Congrats on the Fargo expansion' beats 'Dear Decision Maker' by exactly the amount of research it took."),
    ("One idea per message.", "The cold email offering four products sells none — the confused reader deletes rather than chooses."),
    ("Make the first rung tiny.", "'Worth a 15-minute look?' converts; 'schedule a comprehensive consultation' is marriage-on-the-first-date at inbox scale."),
], D, nxt())
notes(s, "Everything from the pipeline, compressed to inbox physics. The research-shown-in-sentence-one move is what separates outreach from spam.")

s = icon_rows_slide(prs, "Anatomy of a sales message that works", [
    ("🎯", "Hook: their problem, quantified", "The reader's number, not your adjective — 'your team re-keys 400 entries a week.'"),
    ("💡", "Bridge: the mechanism in one line", "How it works, minus the feature tour — just enough to be credible."),
    ("📊", "Proof: one number, one name", "The pilot result and the referenceable customer — pick your single best of each."),
    ("🪜", "Ask: one small dated rung", "The 15-minute call, the sample, the one-pager — never the contract."),
    ("✍", "P.S.: the second-most-read line", "Skimmers read greeting, bolded text, and the P.S. — put real content there, not an afterthought."),
], D, nxt())
notes(s, "The P.S. research is old direct-mail wisdom that survives in email: it's prime real estate on the F-pattern's final fixation. One proof point beats five — the dilution effect again.")

s = bullets_slide(prs, "Calls to action that actually convert", [
    ("One CTA per message.", "'Reply, or call, or book here, or visit our site' is four ways to defer — a single button beats a menu of exits."),
    ("Specific beats available.", "'Does Thursday 2:00 or Friday 10:00 work?' converts better than 'let me know if you're interested' — the reader edits instead of composing."),
    ("Lower the perceived cost in the verb.", "'Take a look' outperforms 'review'; 'grab 15 minutes' outperforms 'schedule a meeting' — same act, lighter lift."),
    ("Date it or lose it.", "An undated CTA is filed under 'someday.' A real deadline with a real reason ('pilot slots close June 1 — we onboard four labs per quarter') moves it to this week."),
], D, nxt())
notes(s, "CTA craft is Chapter 6's dated-ask rule under conversion pressure. The either/or scheduling question is the classic friction-remover.")

s = two_col_slide(prs, "Features tell, outcomes sell",
    "Feature language (yours)", [
        "'256-bit encryption with SOC 2 Type II compliance'",
        "'Automated barcode-driven intake workflows'",
        "'Configurable dashboard with 40+ report templates'",
        "The reader must translate every line into 'so what?'",
    ],
    "Outcome language (theirs)", [
        "'Your auditor's security questionnaire: pre-answered.'",
        "'Sample check-in drops from 4 minutes to 40 seconds.'",
        "'The Monday report builds itself before you log in.'",
        "The translation is done — in the reader's units",
    ], D, nxt())
notes(s, "The discipline: finish every feature sentence with 'which means you…' and then delete everything before 'you.' Features are evidence FOR outcomes, not substitutes for them.")

s = bullets_slide(prs, "Case: the cold email that got the meeting", [
    ("Subject: 'Your Fargo lab's audit prep — 30 tech-hours back per month.'", "The reader's site, the reader's pain, the reader's units — before the message even opens."),
    ("Body: five sentences.", "The duplicate-entry problem (researched from a job posting), the one-line mechanism, one pilot number, one referenceable lab, the Thursday-or-Friday ask."),
    ("What was deleted from draft one:", "the company history paragraph, two more proof points, three features, and every adjective. The delete pass WAS the persuasion."),
    ("Reply, 22 minutes later:", "'Thursday. How did you know about the duplicate entry issue?' — research is the new charm."),
], D, nxt())
notes(s, "Composite of the chapter's whole toolkit at minimum length. The 'what was deleted' framing teaches the dilution effect as a drafting behavior.")

s = section_slide(prs, "06", "Objections",
    "The reader's side of the argument — handle it before it's spoken.", D, nxt())
notes(s, "Section 6: objection handling. Two-sided argument, systematized.")

s = bullets_slide(prs, "Inventory the objections before writing", [
    ("List every reason they could say no —", "price, risk, timing, effort, politics, past failures — before drafting a word of the pitch."),
    ("Sort into three piles:", "answer in the message (the strongest one or two), hold for the meeting (the technical ones), and fix in the offer (the ones that are just true)."),
    ("If an objection is correct, change the offer, not the wording.", "No paragraph survives contact with a valid 'no' — that's product feedback wearing a rejection costume."),
    ("The unanswered strongest objection", "is where your pitch dies after you leave the room — someone will raise it, and your absence will answer it."),
], D, nxt())
notes(s, "The pre-mortem for persuasion. The three-pile sort keeps the message lean (dilution!) while ensuring the lethal objection gets daylight.")

s = icon_rows_slide(prs, "The big four, and their honest answers", [
    ("💰", "Price: 'too expensive'", "Reframe against the cost of the problem: '$2,400 against 30 tech-hours a month' — no-cost is never zero-cost."),
    ("⚠", "Risk: 'what if it fails?'", "Shrink the bet, don't argue the odds: pilot, guarantee, exit clause — make failure cheap and reversible."),
    ("⏰", "Timing: 'not now'", "Find the real deadline in THEIR calendar: 'before Q4 audit prep' converts someday to a date."),
    ("🪨", "Status quo: 'what we have works'", "The strongest one — next slide. Never mock the current system; they chose it."),
], D, nxt())
notes(s, "Each objection has a characteristic honest answer and a characteristic manipulative one. Price: reframe, don't hide fees. Risk: reduce, don't dismiss. Timing: real deadlines only. Status quo: respect, then arithmetic.")

s = bullets_slide(prs, "Your real competitor is the status quo", [
    ("Most pitches lose to 'do nothing' —", "not to a rival. Doing nothing requires no meeting, no budget line, and no one's neck."),
    ("Status quo bias is rational-ish:", "switching has certain costs and uncertain benefits; your job is making the costs of STAYING visible and checkable."),
    ("Quantify the drift:", "'the current process costs 30 hours a month — that's $18K a year already being spent, invisibly' — no-decision is a decision with a price tag."),
    ("Honor what the old system got right.", "'It served well at 200 samples a week; you're at 900' — respect converts defenders into evaluators."),
], D, nxt())
notes(s, "The invisible-spend framing is the single most useful move in internal proposals: it converts 'new cost' into 'existing cost, finally on the books.'")

s = bullets_slide(prs, "Risk reversal: make yes cheap to un-choose", [
    ("Pilots and trials:", "the two-week reversible test converts 'commit' into 'look' — the ladder's whole logic in one offer."),
    ("Guarantees with teeth:", "'full refund, 90 days, no form' works precisely because it's expensive to offer — cheap guarantees signal cheap confidence."),
    ("Exit ramps in the contract:", "'cancel quarterly' closes deals that 'three-year term' kills; the option's existence matters more than its use."),
    ("Keep the old system running", "during the trial — 'we don't unplug anything until you say so' answers the fear nobody voices: being stranded."),
], D, nxt())
notes(s, "Risk reversal is where the seller eats the uncertainty instead of arguing it away — the structural version of two-sided honesty.")

s = section_slide(prs, "07", "Framing",
    "The same facts, arranged for a human brain — and the line that arrangement must not cross.", D, nxt())
notes(s, "Section 7: framing effects. Powerful, well-replicated, and ethically double-edged — taught with the guardrails attached.")

s = two_col_slide(prs, "Gain frame or loss frame?",
    "Gain frame", [
        "'Adopting this saves $18K a year'",
        "Best for: encouraging action under low threat, building toward opportunity",
        "Reads as optimistic — and is easier to ignore",
    ],
    "Loss frame", [
        "'Every quarter without it spends $4,500 on rework'",
        "Losses loom roughly twice as large as equivalent gains in decision research (Kahneman & Tversky)",
        "Stronger motivator — and quicker to read as manipulation if overdone",
        ("The rule:", "frame honestly toward the reader's real situation, and never invent the loss"),
    ], D, nxt())
notes(s, "Loss aversion is among the most replicated effects in behavioral science. Both frames describe identical facts — which is exactly why framing carries an ethics load: choose the frame that helps the reader see accurately, not the one that scares best.")

s = bullets_slide(prs, "Anchoring and contrast — use with the safety on", [
    ("The first number in the conversation", "gravitationally pulls every later number — which is why naming your price early (with justification) usually beats waiting."),
    ("Contrast is honest when both options are real:", "'the full package is $9,600; the core module you actually need is $2,400' — orientation, not theater."),
    ("The decoy trick — a fake option planted to steer —", "fails the visibility test: seeing it named, the reader feels played. Because they were."),
    ("Anchor with the problem, not just the price:", "'you're spending $18K on rework' is the anchor that makes $2,400 read as small AND true."),
], D, nxt())
notes(s, "Anchoring works whether or not it's fair — which is the point of teaching the guardrail alongside. The problem-cost anchor is both the most effective and the most defensible version.")

s = bullets_slide(prs, "Defaults, friction, and the architecture of yes", [
    ("Whatever happens by default, mostly happens.", "Opt-out enrollment beats opt-in by decades of evidence — set defaults you'd defend in public."),
    ("Every step you remove doubles completion.", "The pre-filled form, the held room, the calendar link — friction removal is persuasion that requires no rhetoric at all."),
    ("Make the desired path the easy path,", "and the message barely has to persuade: 'reply YES and I'll handle the rest' outperforms three paragraphs of reasons."),
    ("The ethics mirror:", "adding friction to the exit — cancellation mazes, buried unsubscribes — is the same science, running as a dark pattern. Don't."),
], D, nxt())
notes(s, "Choice architecture in one slide. The exit-friction call-out matters: students will recognize dark patterns from their own subscriptions, which makes the ethical line vivid.")

s = section_slide(prs, "08", "Persuading upward",
    "The pitch to power: one page, one decision, no adjectives.", D, nxt())
notes(s, "Section 8: executive persuasion — the highest-stakes, lowest-word-count version of everything so far.")

s = bullets_slide(prs, "The executive ask", [
    ("One page. One decision.", "Executives fund decisions, not documents — 'approve the $2,400 pilot' is a decision; 'thoughts?' is homework you assigned your boss."),
    ("Answer first (Chapter 3, always):", "the recommendation and its strongest number in the first two lines; the reasoning below for the readers who want it."),
    ("Translate everything into money or risk.", "Hours, errors, and delays all have exchange rates — do the conversion yourself; unconverted currency doesn't spend."),
    ("Pre-answer the one question they always ask:", "'what happens if we don't?' — the status quo cost, one line, near the top."),
], D, nxt())
notes(s, "The proposal skeleton at executive compression. 'What happens if we don't' is the question that kills more proposals than any objection — because nobody wrote the answer down.")

s = bullets_slide(prs, "The elevator answer (not pitch — answer)", [
    ("The question is always some form of 'what's this about?'", "You get roughly 30 seconds — prepared beats improvised by embarrassing margins."),
    ("The three-beat skeleton:", "the problem in their units → the fix in one sentence → the ask sized to the moment: 'can I get 20 minutes Thursday?'"),
    ("Match the altitude.", "The CFO version leads with dollars; the ops version leads with hours; the same truth, denominated differently (Chapter 2's audiences)."),
    ("End with the rung, not the vision.", "Hallway yeses are small: the meeting, the intro, the read — the rollout was never going to happen next to the coffee machine."),
], D, nxt())
notes(s, "Reframing from 'pitch' to 'answer' lowers the performance anxiety and raises the quality: it's a prepared response to a predictable question.")

s = bullets_slide(prs, "Pre-wiring: the meeting before the meeting", [
    ("Big asks should never debut in the big room.", "By decision day, every key attendee has seen the proposal and had their objection heard — privately, cheaply, first."),
    ("One-on-ones surface the real objections", "that the meeting's audience dynamics would bury — people say 'this threatens my team' in private and 'interesting questions remain' in public."),
    ("Incorporate visibly:", "'per Dana's point, the timeline now includes her team's freeze' — objectors who see their fingerprints become co-owners."),
    ("The meeting then ratifies", "what the hallway already decided. That's not politics corrupting persuasion — that's persuasion respecting how groups actually decide."),
], D, nxt())
notes(s, "Pre-wiring is standard senior practice that nobody teaches juniors. The reframe in the last bullet matters: students often read it as manipulation until they see it's just... listening, scheduled early.")

s = bullets_slide(prs, "Case: the pilot that sold itself", [
    ("The analyst wanted the full $40K platform.", "The CFO's calendar said no before she could. So the ask shrank: one team, one module, $2,400, sixty days, kill-switch included."),
    ("The pilot was designed to be reported:", "baseline measured first, three metrics agreed in advance with the skeptic — so the results would be THEIR numbers, not hers."),
    ("Day 60: entry time −38%, zero audit findings,", "and the skeptic presenting the results — social proof and consistency, wearing a lanyard."),
    ("The full platform was approved in the same meeting.", "Nobody was persuaded by the deck. They were persuaded by the yes they'd already said."),
], D, nxt())
notes(s, "The commitment ladder as a case: shrink the ask, co-design the evidence, let the skeptic own the win. 'Agreed metrics in advance' is the move that makes pilot results unarguable.")

s = bullets_slide(prs, "When the answer is no anyway", [
    ("Lose gracefully and visibly.", "'Understood — thanks for the real look' preserves every relationship the pitch built; arguing past the no burns them."),
    ("Ask the diagnostic question:", "'what would need to be true for this to work next cycle?' — a no with criteria is a yes with a date."),
    ("Log what the no taught:", "which objection landed, which evidence was missing, who influenced whom — the second pitch starts from data, not scratch."),
    ("Some nos are the system working.", "The proposal that dies under honest scrutiny was going to die more expensively later — scrutiny did you a favor."),
], D, nxt())
notes(s, "Persuasion includes losing well: it's a repeated game, and the person who takes a no professionally is the person whose next pitch gets a fair hearing.")

s = two_col_slide(prs, "Influence or manipulation? The four-question audit",
    "It's influence if…", [
        "Every factual claim survives checking",
        "The reader, seeing the technique named, would still feel respected",
        "You'd accept this message if you were the reader",
        "Their genuine interest overlaps the action you're urging",
    ],
    "It's manipulation if…", [
        "The scarcity, the anchor, or the social proof is invented",
        "It works only while the reader doesn't notice it",
        "You'd be angry receiving it",
        "It moves them toward YOUR interest against their own",
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "The chapter's closing audit, formalized — reversal test, visibility test, truth test, overlap test. Every technique in the deck passes or fails HERE, not in its conversion rate.")

s = takeaways_slide(prs, [
    "Persuasion earns decisions from readers free to refuse — their interests are the only fuel.",
    "Balance ethos, pathos, logos; diagnose failed pitches by the missing leg.",
    "Run the pipeline: reader-owned hook, accurate interest, evidence-built desire, calibrated ask.",
    "Concede the strongest real objection; prune the weak arguments that dilute your best.",
    "Climb the ladder — small dated yeses — and frame cost against the cost of doing nothing.",
    "Every lever passes the truth test, or it passes nothing for long.",
], D, nxt(), site_note="Practice now: course site → Chapter 8 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap. Unit 3 complete.")

s = quote_slide(prs, "Worth keeping",
    "The reader is free to refuse. Everything in this chapter is just respect for that freedom, organized.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Bring the best persuasive message you ever received. Which single choice made it work?",
    "Which Cialdini lever does your industry overuse into self-parody — and what has that cost it?",
    "Defend or attack: “Name your price early — always.” Use the two-sided research.",
    "Build the commitment ladder for something you actually want this term, with dates.",
    "Where is the line between calibrating to an audience and pandering? Construct the test.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 8 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 8 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Apply:", "This chapter is the written theory of your Influencing Positively work — bring the pipeline to it."),
    ("Read:", "The Chapter 8 Study Guide — both cases, the dilution research, and the before/after pitch autopsy."),
    ("Coming next:", "Unit 4 — Chapter 9: informal reports, where evidence gets sections and headings."),
], D, nxt())
notes(s, "Delivery-neutral closing. Unit 3 complete.")

out = os.path.join(os.path.dirname(__file__), "..", "ch08-persuasive-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
