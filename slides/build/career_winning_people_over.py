# Winning People Over — influence & people skills (Carnegie-inspired, all original text)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Career Series"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "INSTRUCTOR’S CAREER SERIES",
    "Winning People Over",
    "Influence, likability, and leading without resentment — people skills as a professional discipline", D)
notes(s, "Career-series lecture on influence and people skills. Inspired by the principles Dale Carnegie popularized; every word here is original.")
nxt()

s = bullets_slide(prs, "Why people skills decide careers", [
    ("Technical skill gets you hired.", "People skills get you promoted — leadership is influence, and influence is a people skill."),
    ("Every deliverable has a human on the other end.", "Reports persuade, emails negotiate, meetings build or burn trust."),
    ("Influence is learnable.", "Like listening and writing, it is technique plus practice — not a personality you were born with."),
    ("The stakes compound.", "The colleague you win over today is the reference, ally, or hiring manager of your next decade."),
], D, nxt())
notes(s, "Framing: influence as career capital. Connect to students' group work experiences.")

s = quote_slide(prs, "A classic worth knowing",
    "You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.",
    "Dale Carnegie, How to Win Friends and Influence People (1936)", D, nxt())
notes(s, "Brief quotation with attribution. Carnegie's 1936 classic popularized the principles this lecture builds on; the treatment and examples that follow are original. Recommend the book as optional reading.")

s = section_slide(prs, "01", "Handling people without bruising them",
    "The foundation: nobody was ever argued into liking you.", D, nxt())
notes(s, "Section 1: the foundational habits.")

s = two_col_slide(prs, "Criticism feels productive — and almost never is",
    "What criticism actually does", [
        "Triggers defense, not reflection — people justify, they don't reconsider",
        "Wounds pride and creates a quiet enemy",
        "Teaches people to hide mistakes from you",
        "Feels satisfying to give; costs you influence you can't see",
    ],
    "What works instead", [
        ("Get curious first.", "“Walk me through what happened” beats “why did you do that?”"),
        ("Critique the work, never the person.", "“This section needs sources” vs. “you're careless.”"),
        ("Assume a reason.", "Most 'incompetence' is a missing fact, tool, or instruction."),
    ], D, nxt())
notes(s, "The psychology: criticism activates self-justification. People rarely blame themselves — plan your communication around that reality rather than resenting it.")

s = two_col_slide(prs, "Appreciation vs. flattery — only one builds influence",
    "Flattery", [
        "Generic: “great job, team!”",
        "Insincere — and people can tell",
        "About getting something",
        "Cheap to give, worth nothing",
    ],
    "Honest appreciation", [
        "Specific: “your cost table made the decision easy for the committee”",
        "True — you actually noticed",
        "About the other person's real contribution",
        "Costs attention, compounds into loyalty",
    ], D, nxt())
notes(s, "Rule of thumb: if you couldn't name the specific thing, it isn't appreciation yet. One specific sentence of recognition outweighs a page of adjectives.")

s = bullets_slide(prs, "Frame it in their interests — the master key", [
    ("The amateur asks:", "“How do I get what I want?”"),
    ("The professional asks:", "“Why would this be good for them?” — and leads with that."),
    ("Weak:", "“I need your data by Friday for my report.”"),
    ("Strong:", "“If I get your data by Friday, your team's results go in front of the VP in Monday's report.”"),
    ("This is not manipulation —", "it is finding the genuine overlap between what you need and what they value. If there is no overlap, influence isn't your problem; the proposal is."),
], D, nxt())
notes(s, "This single reframe — from my request to their benefit — is the highest-leverage habit in the deck, and it's also the 'you-view' from our writing chapters applied to persuasion.")

s = section_slide(prs, "02", "Becoming someone people say yes to",
    "Likability isn't charm. It's attention, reliably paid.", D, nxt())
notes(s, "Section 2: likability as technique.")

s = icon_rows_slide(prs, "The small habits that make people like working with you", [
    ("❤", "Be genuinely interested", "Ask about their project, their constraint, their weekend — and actually listen to the answer."),
    ("☺", "Warmth is visible", "A greeting with energy — in person, on camera, even in an email's first line — sets the entire exchange."),
    ("✍", "Names matter", "Learn them, spell them right, pronounce them right. A misspelled name in an email is a small insult."),
    ("⚙", "Remember the details", "“How did the inspection go?” three weeks later tells someone they exist in your world."),
], D, nxt())
notes(s, "Keep brief notes after conversations if memory is weak — the follow-up question weeks later lands as extraordinary because almost nobody does it.")

s = bullets_slide(prs, "Listening is the most underrated influence tool", [
    ("People trust those who hear them.", "Being truly listened to is rare enough that it creates instant goodwill."),
    ("Let them talk more than you.", "The person doing the talking feels the conversation went well — use that math."),
    ("Their interests are the agenda.", "Open with what they care about, not with your pitch."),
    ("Make them feel important — honestly.", "Ask their advice in their area of strength. “You've run more of these projects than anyone — what am I missing?”"),
], D, nxt())
notes(s, "Connect to the active-listening techniques from Chapter 1: attend, paraphrase, question, pause. Same skills, aimed at influence.")

s = section_slide(prs, "03", "Winning agreement",
    "You cannot win an argument — even when you win it.", D, nxt())
notes(s, "Section 3: persuasion.")

s = stat_slide(prs, "The argument paradox", "Lose–lose",
    "Win the argument and you've usually lost the person — they walk away embarrassed, resentful, and unconvinced.",
    [("Avoid the head-on collision.", "State your view once, clearly; repetition at higher volume converts no one."),
     ("Respect the other opinion out loud.", "“I can see why you'd read it that way” costs nothing and lowers every defense."),
     ("Admit your errors fast and first.", "Beating others to your own mistake converts a weakness into credibility."),
    ], D, nxt())
notes(s, "Distinguish argument (ego contest) from disagreement (idea comparison). Professionals disagree constantly without arguing.")

s = bullets_slide(prs, "Build a path to yes", [
    ("Open friendly.", "Tone in the first ten seconds — or first sentence of the email — decides the temperature of everything after."),
    ("Start where you agree.", "Stack the easy agreements first; momentum toward 'yes' is real psychology."),
    ("Ask questions instead of asserting.", "“What would it take to hit Friday?” beats “This must be done Friday.”"),
    ("Let them do most of the talking.", "Their objections, spoken aloud, often answer themselves."),
    ("Let the idea become theirs.", "“Building on what Maria said…” — shared ownership beats sole credit, every time."),
], D, nxt())
notes(s, "The 'their idea' move is the advanced version: influence that doesn't need the credit gets the outcome plus an ally.")

s = section_slide(prs, "04", "Leading without resentment",
    "Correcting people while keeping them — the manager's hardest skill.", D, nxt())
notes(s, "Section 4: leadership application.")

s = icon_rows_slide(prs, "Changing behavior without making an enemy", [
    ("★", "Open with honest praise", "Real appreciation first — it proves the critique comes from an ally, not an attacker."),
    ("↷", "Correct indirectly where you can", "“Let's tighten the sourcing in section two” beats a public autopsy of who wrote it."),
    ("♟", "Your mistakes first", "“I made this exact error my first year…” makes the lesson receivable."),
    ("?", "Ask, don't order", "“Could we try it with the summary up front?” preserves ownership and dignity."),
    ("⌂", "Always leave a face-saving exit", "Let people retreat with dignity and they'll follow you again; corner them and they'll fight you forever."),
], D, nxt())
notes(s, "Leadership variant of every earlier principle: influence under authority. Authority makes these habits MORE necessary, not less.")

s = bullets_slide(prs, "Praise progress — loudly, specifically, publicly", [
    "Catch people doing it right; behavior you spotlight repeats.",
    "Give a reputation to live up to: “you're the most careful reviewer we have” recruits their identity to the standard.",
    "Make the fault seem fixable — “you're 90% there” motivates; “this is all wrong” paralyzes.",
    ("Credit generously.", "“That was Jordan's catch” costs you nothing and gains two allies: Jordan, and everyone who watched you do it."),
], D, nxt())
notes(s, "Public credit is the cheapest, most reliable influence investment available to anyone — student or CEO.")

s = two_col_slide(prs, "The ethical line: influence vs. manipulation",
    "Influence (build on this)", [
        "Genuine interest, honest appreciation",
        "Finding real overlap between your goal and theirs",
        "Both parties better off — and both would agree if the method were visible",
    ],
    "Manipulation (never)", [
        "Fake warmth deployed to extract something",
        "Framing designed to hide the real cost",
        "You win, they lose — and it works only until they notice",
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "The visibility test: if the other person could see your technique, would they still feel respected? Carnegie's own insistence: sincerity is the whole game.")

s = bullets_slide(prs, "In this course — and in your inbox", [
    ("Your 'Influencing Positively' assignment", "is exactly this skill set in writing: frame the request in the reader's interests, open friendly, make yes easy."),
    ("Complaint handling:", "let the customer talk, respect the frustration out loud, fix what's fixable, and leave them a dignified exit."),
    ("Persuasive messages (Chapter 8):", "attention → interest → desire → action is Carnegie's overlap-hunting, formalized."),
    ("Every email is a rep.", "You get a dozen chances a day to practice one of these habits in a low-stakes sentence."),
], D, nxt())
notes(s, "Tie directly to the course's Influencing Positively and complaint-handling assignments and Chapter 8 persuasion.")

s = takeaways_slide(prs, [
    "Criticism triggers defense; curiosity triggers change.",
    "Appreciation is specific and true — flattery is neither.",
    "Frame every request in the other person's interests; find the genuine overlap.",
    "You cannot win an argument — build agreements instead, and let ideas become theirs.",
    "Correct with praise first, questions instead of orders, and a face-saving exit.",
    "The visibility test keeps influence honest: would they feel respected if they saw your technique?",
], D, nxt(), site_note="Optional reading: Dale Carnegie, How to Win Friends and Influence People (1936) — the classic behind this lecture.")
notes(s, "Recap plus the book recommendation.")

s = discussion_slide(prs, "Discussion questions", [
    "Recall a time criticism changed your behavior — and one where it just made you defensive. What was different?",
    "Rewrite this request in the reader's interests: “I need everyone's status updates by 3 PM.”",
    "Which is harder for you — admitting error first, or letting someone else take credit? Why?",
    "Where's the line between adapting to your audience and manipulating them? Give an example of each.",
    "Pick one habit from this deck to practice for one week. How will you know it's working?",
], D, nxt())
notes(s, "Good async discussion-board prompts; question 2 doubles as a writing exercise.")

out = os.path.join(os.path.dirname(__file__), "..", "career", "winning-people-over.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
