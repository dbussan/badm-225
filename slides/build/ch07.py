# Chapter 7 — Negative Messages (22 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 7"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Negative Messages",
    "Saying no · delivering bad news · apologizing — the messages that test everything, when it matters most", D)
notes(s, "Chapter 7: bad news craft. Companion guide has both cases in full.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Stage", "the indirect pattern: honest buffer, reasons first, the no once, a concrete pivot."),
    ("Craft", "the news sentence between its two failure modes — evasion and cruelty."),
    ("Apologize", "with anatomy: own the act, name the impact, prevent, stop."),
    ("Beat", "the MUM effect: report problems small and early, paired with a plan."),
    ("Pair", "channels for consequential news: rich conversation first, written record same day."),
], D, nxt())
notes(s, "Objectives map to the bad-news-to-customers assignment.")

s = section_slide(prs, "01", "The indirect pattern",
    "Sequencing for a reader you are about to hurt.", D, nxt())
notes(s, "Section 1.")

s = flow_slide(prs, "Buffer → Reasons → News → Pivot", [
    ("BUFFER", "True common ground. One or two sentences. Promises NOTHING."),
    ("REASONS", "The real why, before the no — reaching a mind not yet defending itself."),
    ("THE NEWS", "Once. Clear. Brief. Owned."),
    ("PIVOT", "Whatever yes exists: alternative, partial, path back, referral."),
], D, nxt(), note_text="Not evasion — sequencing. Every fact arrives, in the order a human can hear it. Scope: consequential news only; trivial nos stay direct.")
notes(s, "The psychology: a blunt opening no turns the rest of your message into opposition research.")

s = two_col_slide(prs, "Buffers: the two fatal failure modes",
    "False hope", [
        "“Great news about your application process!”",
        "Converts disappointment into betrayal",
        "The reader replays your cheer as mockery",
    ],
    "Padding", [
        "Three paragraphs of weather before the point",
        "Reads as the writer stalling",
        "Stalling reads as dread — and dread is contagious",
        ("The craft:", "true · relevant · brief"),
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "Working buffers: agreement, appreciation, facts, good-news-first, understanding.")

s = bullets_slide(prs, "Reasons: the load-bearing middle", [
    ("Give the real reason when you can.", "Readers detect boilerplate; a true constraint respects them enough to argue with."),
    ("Frame on facts and shared interests,", "not personal judgment: “the budget closed in March” survives scrutiny; “not a priority” starts a war."),
    ("Explain — don't beg.", "If the decision is defensible, defend it plainly. If it isn't, the problem is the decision, not the paragraph."),
], D, nxt())
notes(s, "Refusals are won or lost here.")

s = two_col_slide(prs, "The news sentence: between evasion and cruelty",
    "The failure modes", [
        ("Evasion:", "“It may prove difficult at this juncture to accommodate…” — the reader must hunt for their own rejection"),
        ("Cruelty:", "“Denied. Your proposal failed on multiple criteria.” — the no, weaponized"),
        ("Camouflage:", "“A decision has been made” — owns nothing, fools no one"),
    ],
    "The craft", [
        "“We can't fund the March cohort this year.”",
        "Once — repetition grinds the wound",
        "Clear — never make them ask “is this a no?”",
        ("Softening that works:", "the subordinate clause — “Although we couldn't fund March, September…”"),
    ], D, nxt())
notes(s, "The one place the indirect pattern briefly becomes direct.")

s = icon_rows_slide(prs, "The pivot: every no carries whatever yes exists", [
    ("↪", "The alternative", "“September has space — I can hold a seat until Friday.”"),
    ("½", "The partial yes", "“We can fund two of the three positions.”"),
    ("🛤", "The path back", "“Resubmission opens August 1 — Q3 data would make yours lead the cycle.”"),
    ("→", "The referral", "“Meridian Labs runs exactly this analysis; ask for Dr. Chen.”"),
], D, nxt(), kicker="Concrete or nothing: “feel free to reach out in the future” is upholstery, not a pivot.")
notes(s, "If genuinely nothing exists, close with respect — no manufactured silver linings.")

s = section_slide(prs, "02", "Apologies",
    "The negative message about yourself — where directness IS the respect.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "Apology anatomy (Lazare, 2004)", [
    ("OWN IT", "“I missed the deadline I committed to.” No “mistakes were made.” No “if you were offended.”"),
    ("NAME THE IMPACT", "“…which delayed your review a week.” Proof you understand the cost."),
    ("REPAIR + PREVENT", "What's happening now — and what stops a repeat. THE trust sentence."),
    ("STOP", "No third apology. The reader needs the fix, not your feelings."),
], D, nxt(), note_text="Most failed apologies fail at step one. “If you were offended” relocates the offense into the reader's sensitivity.")
notes(s, "One clean apology outperforms five grovels.")

s = section_slide(prs, "03", "Early and upward",
    "The MUM effect — and the career advantage of beating it.", D, nxt())
notes(s, "Section 3.")

s = stat_slide(prs, "Bad news travels slowest when it matters most", "MUM",
    "People delay, soften, and reroute bad news — even when blameless for it (Rosen & Tesser, 1970). It's why managers hear about problems six weeks late.",
    [("The protocol:", "report while it's small · pair it with a plan · calibrate honestly (“yellow, trending red”)."),
     ("The formula:", "own it → cause in one line → recovery plan with a date → the ask."),
     ("The career math:", "leaders trust big things to the people who told the truth about small things, early, on purpose."),
    ], D, nxt())
notes(s, "Fifty-five years of replication. Chapter 1's upward filter, explained.")

s = bullets_slide(prs, "Channel and timing for consequential news", [
    ("Rich first:", "conversation or call — empathy has bandwidth, questions get absorbed, dignity stays private."),
    ("Record second, same day:", "terms, dates, next steps in writing."),
    ("Email-only for personal bad news reads as cowardice", "— because it usually is."),
    ("Timing:", "as early as certainty allows. Never Friday 4:55 as avoidance. Never “after the holidays” while they plan around a fiction."),
], D, nxt())
notes(s, "Chapter 1's pairing at its highest-stakes application.")

s = bullets_slide(prs, "Case: the same denial, twice", [
    ("Version A (email):", "“Your request has been denied as the program does not meet eligibility criteria. Consult the policy manual. Future requests should be submitted with closer attention…”"),
    ("What the employee hears:", "“you were careless” — a denial converted into a reprimand."),
    ("Version B (conversation + confirmation):", "true buffer, the real constraint stated checkably, an owned no — and two concrete yeses (covered fall program; travel days as work time)."),
    ("Eleven extra minutes.", "One version books a withdrawal that compounds through the grapevine; the other, a deposit: “she fought for me and the policy blocked it.”"),
], D, nxt())
notes(s, "Identical no; opposite relationships.")

s = bullets_slide(prs, "Case: the slipping launch", [
    ("Week 3: launch will slip a month.", "Account lead: “Why alarm them with maybes? Wait for the retest.” PM overrules — calls the client that afternoon."),
    ("The structure:", "known · unknown · recovery plan · “new date confirmed by Tuesday; updates weekly.”"),
    ("The retest fails too. The slip grows.", "The client extends the contract anyway — citing the vendor management."),
    ("The control group:", "an identical slip on another account, held for certainty. That client learned four days out — from their own integration team."),
], D, nxt())
notes(s, "Trust was staked on the reporting, not the outcome — and the reporting held. The client ALWAYS finds out; the only variable is from whom.")

s = two_col_slide(prs, "Two refusals you can reuse this week",
    "To a colleague", [
        "“Thanks for thinking of me — I've enjoyed the past two panels.",
        "I'm committed to the audit closeout through the 22nd, and panel prep deserves real attention, so I have to pass this cycle.",
        "Dana ran the rubric with me last year and would be excellent; happy to brief whoever steps in.”",
    ],
    "To a customer (claim denial)", [
        "“Thanks for the photos — they made review easy.",
        "The damage is consistent with a post-delivery drop, which warranty and carrier coverage don't extend to. We can't replace at no cost.",
        "What we can do: repair at $180 — a third of replacement — scheduled this week. And the reinforced case on p. 12 prevents exactly this break.”",
    ], D, nxt())
notes(s, "Both from the guide's worked examples: buffer, reasons, one no, concrete pivot.")

s = takeaways_slide(prs, [
    "Indirect structure is sequencing, not evasion: reasons reach an unwounded mind; every fact arrives.",
    "Buffers: true, relevant, brief — never false hope, never padding.",
    "The news sentence: findable, unambiguous, once, owned.",
    "Every no carries whatever yes exists — concretely, or not at all.",
    "Apologies: own the act, name the impact, prevent, stop.",
    "Beat the MUM effect: small, early, with a plan. Rich first, record second, never Friday 4:55.",
], D, nxt(), site_note="Practice now: course site → Chapter 7 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The reader always finds out. The only variable you control is whether they find out from you, early, with a plan — or from the grapevine, late, with a grievance.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "When is directness the KINDER structure for bad news? Build the decision rule with two real examples.",
    "Describe a rejection you received that was well done. What will you steal from it?",
    "Why do organizations reward MUM-effect behavior while claiming to want transparency? What changes the incentive?",
    "Take a public corporate apology and rewrite its worst sentence to pass the anatomy.",
    "Draft the structure for announcing a price increase to loyal customers: what buffers, reasons, and pivots honestly exist?",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 7 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 7 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Apply:", "This chapter IS the toolkit for the bad-news-to-customers assignment."),
    ("Read:", "The Chapter 7 Study Guide — both cases in full, plus the apology anatomy."),
    ("Coming next:", "Chapter 8 — persuasive messages: moving readers who could say no toward yes."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch07-negative-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
