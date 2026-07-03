# Business Strategy Essentials — original treatment of value-based strategy concepts
# Concepts credited to Felix Oberholzer-Gee (Better, Simpler Strategy, HBR Press 2021)
# and the HBS Online Business Strategy course the instructor completed. All text original.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Professional Development"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "PROFESSIONAL DEVELOPMENT · INSTRUCTOR'S NOTES FROM HARVARD BUSINESS SCHOOL ONLINE",
    "Business Strategy Essentials",
    "Value-based strategy — where profit actually comes from, and why it matters to everyone who writes a proposal", D)
notes(s, "Original lecture built from what the instructor studied in HBS Online's Business Strategy course (Prof. Felix Oberholzer-Gee). Concepts credited; every slide's text is original.")
nxt()

s = bullets_slide(prs, "Why a strategy lecture in a communication course?", [
    ("Strategy is an argument.", "Every strategy lives or dies by how clearly it can be explained — to employees, investors, and customers."),
    ("You will pitch ideas your whole career.", "Understanding where value comes from turns 'I have an idea' into 'here is why this wins.'"),
    ("It sharpens every proposal you write.", "The frameworks in this deck give you the vocabulary decision-makers already think in."),
    ("Your instructor studied this at HBS Online", "and this deck shares the ideas that most changed how he evaluates plans — with pointers to the original sources at the end."),
], D, nxt())
notes(s, "Set expectations: this is the instructor's synthesis, not Harvard's materials. The final slide sends students to the primary sources.")

s = quote_slide(prs, "The core idea, in one sentence",
    "Great strategy is simpler than you think: create more value for customers, employees, and suppliers than your rivals do — and the profit follows.",
    "the central argument of value-based strategy, as developed in Felix Oberholzer-Gee's Better, Simpler Strategy (Harvard Business Review Press, 2021)", D, nxt())
notes(s, "Attribution slide. Oberholzer-Gee's book is the backbone of the HBS Online course; recommend it as the single best follow-up read.")

s = section_slide(prs, "01", "The value stick",
    "One picture that explains where profit comes from.", D, nxt())
notes(s, "Section 1: WTP, WTS, and value creation.")

s = flow_slide(prs, "Four numbers that decide every business", [
    ("Willingness to pay (WTP)", "The MOST a customer would ever pay for your product. Delight raises it."),
    ("Price", "What you actually charge. The gap below WTP is the customer's happy surplus."),
    ("Cost", "What you pay for labor and inputs. The gap above WTS is your suppliers' and employees' surplus."),
    ("Willingness to sell (WTS)", "The LEAST employees and suppliers would accept. Better jobs and partnerships lower it."),
], D, nxt(), note_text="Total value created = WTP minus WTS. Strategy has exactly two jobs: raise WTP or lower WTS. Everything else is decoration.")
notes(s, "The value stick: draw it vertically on the board — WTP on top, WTS on the bottom. Firms compete on the size of the wedge they create, not just the price they charge.")

s = two_col_slide(prs, "Raising WTP vs. lowering WTS — the only two moves",
    "Raise willingness to pay", [
        "Make the product genuinely better or more delightful",
        "Make it easier to buy, use, and love",
        "Add complements that make it more valuable",
        ("Example:", "a phone gets more valuable with every great app"),
    ],
    "Lower willingness to sell", [
        "Make jobs better so great people accept fair pay — passion, flexibility, respect",
        "Make suppliers more productive so they can charge you less profitably",
        "Share data, training, and forecasts with partners",
        ("Example:", "a stable schedule is worth real money to an hourly worker"),
    ], D, nxt())
notes(s, "Lowering WTS is NOT squeezing people — it's making the relationship more valuable so both sides win. That distinction is the ethical heart of the framework.")

s = bullets_slide(prs, "The simplicity test", [
    ("Strategy fails by addition.", "Ten initiatives, three visions, dashboards nobody reads — complexity is where strategies go to die."),
    ("The one-question filter:", "does this initiative raise customers' willingness to pay, or lower willingness to sell? If neither — why are we doing it?"),
    ("Communicators take note:", "if you cannot state a plan's value logic in one sentence, the plan probably doesn't have one."),
    ("This is your Chapter 2 lesson at company scale:", "purpose first, audience benefit first, everything else after."),
], D, nxt())
notes(s, "Bridge to course content: the same discipline as purpose-first writing.")

s = section_slide(prs, "02", "Customers",
    "Delight, near-customers, and learning what people actually value.", D, nxt())
notes(s, "Section 2: customer side of the stick.")

s = icon_rows_slide(prs, "Finding room to raise WTP", [
    ("★", "Create delight, not just satisfaction", "Satisfied customers shop around; delighted ones stay and recruit. Ask what would make someone cheer."),
    ("◔", "Hunt the near-customers", "People who ALMOST buy from you — the growth hiding in plain sight. One removed obstacle can unlock a whole segment."),
    ("⚖", "Measure real trade-offs", "Don't ask 'do you like it?' — force choices. Techniques like conjoint analysis reveal what people actually pay for versus what they say they value."),
    ("✂", "Cut what customers don't value", "Every feature costs something; features nobody pays for are pure WTS with no WTP."),
], D, nxt())
notes(s, "Near-customers question for the class: name a product you almost buy. What one change would convert you? That answer is strategy.")

s = section_slide(prs, "03", "Complements & network effects",
    "Why some products get stronger as the world around them grows.", D, nxt())
notes(s, "Section 3: complements and platforms.")

s = two_col_slide(prs, "Complements: the helpers that raise your value",
    "How complements work", [
        "A complement is a different product that raises YOUR product's WTP",
        "Cheaper, better complements = more valuable core product",
        "Apps make phones worth more; chargers make EVs practical",
        "Smart firms invest in their complements' success",
    ],
    "Friend or foe?", [
        "Today's complementor can become tomorrow's competitor",
        "Platform disputes (like app stores vs. developers) are fights over who captures the value both create",
        "Watch who controls the customer relationship",
        ("Lesson:", "map who makes you valuable — and who could replace you"),
    ], D, nxt())
notes(s, "Public example: the Epic Games v. Apple litigation was a complement relationship turned rivalrous — both made each other valuable, then fought over the split.")

s = stat_slide(prs, "Network effects and tipping points", "n²",
    "In network businesses, each new user makes the product more valuable for every other user — growth compounds.",
    [("Tipping:", "past a critical mass, markets can tip toward one winner — being early and dense beats being slightly better."),
     ("But networks aren't destiny:", "underdogs win by serving niches deeply, differentiating, or building local density the giant ignores."),
     ("Career note:", "your professional network works the same way — every genuine connection raises the value of the rest."),
    ], D, nxt())
notes(s, "Keep the math light: the point is compounding value, tipping dynamics, and the underdog playbook.")

s = section_slide(prs, "04", "People — the other half of the stick",
    "Value for employees and suppliers is strategy, not charity.", D, nxt())
notes(s, "Section 4: WTS side — employees and suppliers.")

s = bullets_slide(prs, "Value for employees: 'feeling heard' is a strategy", [
    ("People accept better jobs for less pay.", "Flexibility, respect, growth, and being heard all lower WTS — honestly."),
    ("Listening is a profit lever.", "Employees who feel heard stay longer, work better, and tell you the truth early — every one of those shows up in cost."),
    ("The communication tie-in is direct:", "Chapter 1's listening skills and Chapter 16's leadership habits are literally value-creating activities."),
    ("Same logic for suppliers:", "train them, share forecasts, pay promptly — a more productive partner can serve you better for less."),
], D, nxt())
notes(s, "This is where strategy and this course fully merge: communication quality changes WTS. It's measurable strategy, not soft skills.")

s = section_slide(prs, "05", "Execution",
    "A strategy nobody understands is a strategy that doesn't exist.", D, nxt())
notes(s, "Section 5: execution and measurement.")

s = icon_rows_slide(prs, "From idea to action: making strategy visible", [
    ("▦", "The Balanced Scorecard", "Track four views at once — financial, customer, internal process, and learning/growth — so 'success' isn't just last quarter's number. (Kaplan & Norton's classic framework.)"),
    ("→", "Connect the dots", "Every team should be able to say which value driver their work moves. If they can't, the strategy hasn't been communicated — it's been filed."),
    ("$", "Guide investment by value", "Fund what raises WTP or lowers WTS; starve what doesn't. Budgets are the strategy, whatever the slide deck says."),
    ("✎", "Write it simply", "The strategy that wins is the one every employee can repeat in one sentence."),
], D, nxt())
notes(s, "Balanced Scorecard credited to Kaplan & Norton (HBR, 1992). Execution failures are mostly communication failures — which is why this course matters to strategy.")

s = bullets_slide(prs, "Using this in BADM 225 — and in your first job", [
    ("Write value-first proposals.", "Lead with the value logic: 'This raises what customers will pay by…' or 'This lowers our costs by making the work better…'"),
    ("Frame for the reader's stick.", "Your boss thinks in WTP and WTS even if they've never heard the words. Speak margin, not features."),
    ("Use it in interviews.", "'Here's how I'd create value in this role' is a stronger answer than any list of duties."),
    ("Your feasibility study is a value argument.", "The executive summary should say, in one sentence, where the value comes from."),
], D, nxt())
notes(s, "Direct application to the course's market research and feasibility study assignments.")

s = takeaways_slide(prs, [
    "Value created = willingness to pay minus willingness to sell. Strategy raises the top or lowers the bottom.",
    "Delight raises WTP; near-customers are growth hiding in plain sight; measure trade-offs, not opinions.",
    "Complements raise your value — and can become rivals. Network effects compound and tip markets.",
    "Better jobs and stronger partners lower WTS honestly — listening is a profit lever.",
    "Execution is communication: scorecards, connected dots, and a strategy anyone can repeat.",
    "Every proposal you ever write should answer one question: where does the value come from?",
], D, nxt(), site_note="Try Chapter 17 on the course site — practice questions and writing prompts on exactly these ideas.")
notes(s, "Recap; point to the new Chapter 17 bank.")

s = bullets_slide(prs, "Go to the source — strongly recommended", [
    ("The book behind it all:", "Felix Oberholzer-Gee, Better, Simpler Strategy: A Value-Based Guide to Exceptional Performance (Harvard Business Review Press, 2021) — readable, practical, and the backbone of what you just saw."),
    ("The classic on measurement:", "Robert Kaplan & David Norton, “The Balanced Scorecard — Measures That Drive Performance,” Harvard Business Review (1992)."),
    ("Free reading:", "HBS Online's Business Insights blog (online.hbs.edu/blog) publishes open articles on these frameworks, including conjoint analysis."),
    ("The full experience:", "HBS Online's Business Strategy course — your instructor took it and recommends it; ask him about it."),
], D, nxt())
notes(s, "Genuine exposure to the HBS materials: send students to the primary, public sources rather than reproducing course content.")

s = discussion_slide(prs, "Discussion questions", [
    "Pick a product you love. What creates its willingness-to-pay premium — and what complement makes it better?",
    "Name a company you ALMOST buy from. What one change would convert you, and what would it cost them?",
    "How could your current (or future) employer lower willingness-to-sell for its best people without raising pay?",
    "Take any campus service and sketch one Balanced Scorecard measure for each of the four perspectives.",
    "Rewrite this feature-first pitch as value-first: “Our app now has 14 new settings and a dark mode.”",
], D, nxt())
notes(s, "Question 5 doubles as a writing exercise tying strategy to the course's persuasive writing skills.")

out = os.path.join(os.path.dirname(__file__), "..", "career", "business-strategy-essentials.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
