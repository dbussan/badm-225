# Chapter 8 — Persuasive Messages (22 slides, delivery-neutral)
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
