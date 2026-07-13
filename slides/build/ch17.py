# Chapter 17 — Strategy for Communicators (38 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 17"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Strategy for Communicators",
    "Where value comes from · willingness to pay, willingness to sell · and proposals that speak the language of both", D)
notes(s, "Chapter 17: the capstone. Value-based strategy essentials — in the tradition of the value-stick framework taught at Harvard Business School — so students' proposals and career decisions speak the language leadership actually uses.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Explain", "where profit actually comes from: the gap between willingness to pay and willingness to sell."),
    ("Analyze", "any business move as raising WTP, cutting cost, or lowering WTS — the only three levers there are."),
    ("Write", "proposals in value language: every ask translated into the drivers leadership already funds."),
    ("Read", "your own organization's strategy well enough to aim your work at it."),
    ("Apply", "the same arithmetic to your career: your personal WTP, and what raises it."),
], D, nxt())
notes(s, "Objectives map to the Chapter 17 practice bank. Attribution note: the value stick framework is associated with value-based strategy scholarship at HBS (Oberholzer-Gee and colleagues) — presented here in original words with original examples.")

s = stat_slide(prs, "Why a communication course ends with strategy", "$",
    "Every document you've learned to write — the proposal, the report, the pitch — is ultimately read by someone asking one question: does this create value?",
    [("Most professionals can't say where value comes from,", "so their proposals argue features, effort, and fairness — currencies leadership doesn't spend."),
     ("The writer who CAN say it", "aims every ask at willingness to pay or cost — and gets funded at rates that look like luck."),
     ("This chapter is the decoder ring:", "one framework, three levers, and the writing habits that use them."),
    ], D, nxt())
notes(s, "The motivation slide: strategy literacy as a communication skill. The 'currencies leadership doesn't spend' line frames the whole chapter.")

s = section_slide(prs, "01", "The value stick",
    "Four points on a line explain almost everything.", D, nxt())
notes(s, "Section 1: the core framework.")

s = flow_slide(prs, "The value stick, top to bottom", [
    ("WTP", "Willingness to pay: the MOST a customer would ever pay — set by the value they get"),
    ("PRICE", "What they actually pay — the split point of the customer's share"),
    ("COST", "What the firm spends to deliver"),
    ("WTS", "Willingness to sell: the LEAST suppliers and employees would accept — set by how good the deal feels to them"),
], D, nxt(), note_text="Value created = WTP minus WTS. The firm's profit, the customer's delight, and the employee's satisfaction are all just SLICES of that one stick.")
notes(s, "The stick in one slide. Customer delight = WTP − price; firm margin = price − cost; supplier/employee surplus = cost − WTS. Total value = WTP − WTS. Everything else in the chapter is applications.")

s = bullets_slide(prs, "Value created vs. value captured", [
    ("Creating value and capturing it are different acts:", "a firm can create enormous value and keep none (price wars), or capture briefly without creating (until customers notice)."),
    ("Durable profit needs BOTH:", "a wide stick (big WTP-to-WTS gap) and a defensible split — which is why price alone is never a strategy."),
    ("The deepest insight:", "the best firms compete by WIDENING the stick — more delight, better jobs — not by fighting harder over a fixed one."),
    ("Communication runs on the same physics:", "the proposal that widens the stick ('this raises WTP') beats the one that just claims a bigger slice ('we should charge more')."),
], D, nxt())
notes(s, "Create-vs-capture is the framework's ethical core and its practical one: positive-sum moves are more durable AND easier to sell internally.")

s = bullets_slide(prs, "Willingness to pay: the customer's ceiling", [
    ("WTP is the maximum they'd pay before walking —", "not the price, and not the budget: the point of indifference between buying and not."),
    ("Everything that improves their life raises it:", "quality, convenience, status, risk removed, time returned — WTP is where 'value' stops being abstract (Chapter 4's ladder: it has a number)."),
    ("You can't see WTP on an invoice;", "you find it in behavior: what they trade off, what they complain about, what the audit costs them (Chapter 9's research methods)."),
    ("The proposal implication:", "'this saves your team 30 hours a month' is a WTP argument — it names what the customer's ceiling is made of."),
], D, nxt())
notes(s, "WTP operationalized. The invoice-vs-behavior point connects to primary research from Chapter 9 — WTP is discoverable, not mystical.")

s = bullets_slide(prs, "Willingness to sell: the floor nobody watches", [
    ("WTS is the least a supplier — or an employee — would accept", "and still say yes: the floor of the stick, and the most neglected lever in business."),
    ("For employees, WTS falls when work gets BETTER:", "flexibility, growth, meaning, respect — people accept less total compensation for jobs they'd choose again (and stay longer, which is the cost lever wearing a culture costume)."),
    ("For suppliers, WTS falls when you're a better customer:", "reliable forecasts, fast payment, honest specs — being easy to sell to is a discount nobody invoices."),
    ("The insight leaders miss:", "lowering WTS creates value WITHOUT squeezing anyone — the opposite of the beat-them-down purchasing playbook."),
], D, nxt())
notes(s, "WTS is the framework's freshest idea for students. The employee application (better jobs = lower WTS = value created) reframes 'culture' as arithmetic.")

s = two_col_slide(prs, "The only three levers there are",
    "Widen the stick", [
        ("Raise WTP:", "make customers' lives better — quality, convenience, complements"),
        ("Lower WTS:", "make working with you better — for employees and suppliers",),
        "Positive-sum: someone gains, nobody must lose",
    ],
    "Or work the middle", [
        ("Cut cost:", "deliver the same value for less spend — scale, learning, operations"),
        ("Move price:", "captures differently, creates NOTHING — the lever that looks like strategy and isn't"),
        ("Test any initiative:", "which lever is this? 'None' = it's not strategy, it's activity"),
    ], D, nxt())
notes(s, "The three-lever test is the chapter's workhorse: every project, proposal, and initiative can be located on the stick — or exposed as unlocated.")

s = section_slide(prs, "02", "Raising willingness to pay",
    "The top of the stick: delight, complements, and the near-customer.", D, nxt())
notes(s, "Section 2: WTP applications.")

s = bullets_slide(prs, "What actually raises WTP", [
    ("Quality that shows up in THEIR outcomes:", "the instrument that cuts audit findings raises the lab's WTP by the findings' cost — not by the spec sheet's elegance (Chapter 8's outcomes-not-features)."),
    ("Convenience is quality:", "every step removed, every integration that just works — WTP rises with friction removed (the same physics as Chapter 8's ask design)."),
    ("Risk removed is WTP added:", "guarantees, pilots, reliability records — certainty is a product feature customers pay for (Chapter 8's risk reversal, priced)."),
    ("Status and belonging are real:", "the brand on the badge, the tool the good labs use — social WTP is still WTP; snobbery about it is margin left on the table."),
], D, nxt())
notes(s, "Four WTP drivers, each tied back to persuasion machinery — the frameworks converge because they describe the same buyer.")

s = bullets_slide(prs, "Complements: the products that raise YOUR value", [
    ("A complement makes YOUR product more valuable:", "the app that makes the instrument easy, the training that makes the software sticky — WTP for one rises with the other."),
    ("Cheap complements are strategy:", "when the complement gets cheaper, YOUR stick widens — which is why firms give away what makes their core product shine."),
    ("Spot them by the pairing question:", "'what do customers use WITH this?' — then ask who controls it and what it costs."),
    ("Substitutes work in reverse:", "cheaper alternatives cap your WTP from below — the honest proposal names both (Chapter 9's completeness)."),
], D, nxt())
notes(s, "Complements/substitutes with the pairing heuristic. The give-away-the-complement logic explains pricing students see everywhere (razors, printers, platforms).")

s = bullets_slide(prs, "The near-customer: growth hiding in plain sight", [
    ("Near-customers value the product but don't buy —", "the price sits above THEIR WTP, or one friction blocks them: complexity, access, a missing complement."),
    ("Ask what blocks them, not what's wrong with them:", "the lab that 'can't afford it' may really mean 'can't spare the validation downtime' — different problem, solvable."),
    ("Small WTP moves recruit whole segments:", "the simpler tier, the financing option, the turnkey install — each converts a band of near-customers at once."),
    ("Every business writer should know their near-customer:", "it's the audience-analysis question (Chapter 2), asked about the whole market."),
], D, nxt())
notes(s, "The near-customer concept — one of value-based strategy's most actionable — framed as market-scale audience analysis.")

s = section_slide(prs, "03", "Cutting cost, lowering WTS",
    "The bottom of the stick: operations, and the jobs people would choose again.", D, nxt())
notes(s, "Section 3: the lower levers.")

s = bullets_slide(prs, "Cost: the honest lever", [
    ("Real cost reduction delivers the SAME value for less:", "scale spreading fixed costs, learning curves compounding, waste engineered out (the barcode pilot was a cost lever all along)."),
    ("Fake cost reduction just moves the cost:", "onto customers (worse service = WTP falls), onto employees (burnout = WTS rises) — the stick doesn't shrink; it shifts, and then it shrinks."),
    ("The test for any cut:", "'what happens to WTP and WTS?' — a cut that pays for itself in churn and turnover was a loan, not a saving."),
    ("Write cost cases in stick language:", "'this cut leaves WTP untouched — same turnaround, same quality — and here's the verification' (Chapter 10's evidence rules)."),
], D, nxt())
notes(s, "The real-vs-fake cut distinction gives students the analytical vocabulary for the cost proposals they'll write and endure.")

s = bullets_slide(prs, "Lowering employee WTS: culture as arithmetic", [
    ("Every improvement in how work FEELS lowers WTS:", "autonomy, flexibility, growth, a manager who runs Chapter 16 — people stay for less than competitors must pay to poach them."),
    ("The savings are real and layered:", "lower churn, cheaper recruiting, retained knowledge — turnover is the cost line that hides in four other budgets."),
    ("This is why 'soft' initiatives are hard strategy:", "the mentoring program isn't a perk; it's a WTS lever with a measurable stick effect — WRITE it that way and watch it get funded."),
    ("The caution:", "perks nobody wants lower nothing — WTS falls when work actually improves, which requires asking (Chapter 9's surveys, Chapter 1's listening)."),
], D, nxt())
notes(s, "The chapter's most useful reframe for future managers: culture initiatives argued in WTS language survive budget season; argued as niceness, they don't.")

s = bullets_slide(prs, "Supplier WTS: be the customer they'd discount for", [
    ("Suppliers price the RELATIONSHIP, not just the order:", "chaotic buyers pay for their chaos — rush orders, spec churn, and slow payment all arrive back inside the quote."),
    ("Lower their cost of serving you, and WTS follows:", "reliable forecasts, clean specs (Chapter 6's complete-ask, at contract scale), payment on time."),
    ("Share the widened stick deliberately:", "long-term partners who co-invest beat auctioned vendors on everything but the first invoice."),
    ("The communicator's role is the whole lever:", "supplier WTS is moved almost entirely by the quality of what your organization WRITES to them — forecasts, specs, confirmations (Chapter 6)."),
], D, nxt())
notes(s, "Supplier WTS closes the stick tour — and lands on the thesis that the lever is literally made of business communication.")

s = section_slide(prs, "04", "Strategy in practice",
    "Trade-offs, value maps, and the difference between strategy and planning.", D, nxt())
notes(s, "Section 4: using the framework on real decisions.")

s = bullets_slide(prs, "Trade-offs: strategy is choosing what to be bad at", [
    ("No firm can top every driver:", "the cheapest, fastest, highest-touch, most premium lab-services company is four different companies."),
    ("Great strategies pick their drivers", "and accept visible weakness on the rest — the discount airline is PROUDLY bad at legroom; that's the strategy working."),
    ("Straddling kills:", "chasing every driver averages the value proposition into 'fine' — and 'fine' has the WTP of a shrug."),
    ("The writing implication:", "a proposal that improves an off-strategy driver is well-meant noise — know which drivers YOUR firm competes on before you draft (next slide)."),
], D, nxt())
notes(s, "Trade-offs as the discipline of strategy. The off-strategy-proposal warning sets up the strategy-reading slide.")

s = bullets_slide(prs, "Reading your own organization's strategy", [
    ("Ignore the mission statement; watch the money:", "what gets funded without a fight, who gets promoted, which customers get fired — revealed strategy beats stated strategy."),
    ("Find the value drivers in the wild:", "what do YOUR loyal customers say they'd miss most? That answer is the strategy, whatever the poster says."),
    ("Locate your own work on the stick:", "does your role raise WTP, cut cost, or lower WTS? If you can't answer, your performance review is being graded in a language you haven't learned."),
    ("Then aim your proposals at the live drivers:", "the initiative that serves the actual strategy needs half the persuasion (Chapter 8) of the one that fights it."),
], D, nxt())
notes(s, "Strategy-reading as an employee survival skill. The 'locate your own work' question is the career pivot the last section completes.")

s = bullets_slide(prs, "Strategy is not planning", [
    ("A plan is a list of activities with dates;", "a strategy is a theory of value: 'we win because our stick is wider HERE, for THESE customers.'"),
    ("The test:", "a strategy tells you what to STOP doing; a plan never does — if nothing got harder to justify, no strategy was made."),
    ("Both are needed, in order:", "theory first, activities second — a brilliant plan for an unlocated position is fast travel in a random direction."),
    ("Communicators inherit the confusion:", "most 'strategy documents' you'll be asked to write are plans. Writing the actual theory in one page first (Chapter 10's one-pager) is the upgrade nobody asks for and everyone funds."),
], D, nxt())
notes(s, "The strategy-vs-planning distinction, with the stop-doing test. The one-page-theory habit is the practical takeaway.")

s = bullets_slide(prs, "Case: the regional lab chain", [
    ("Twelve locations, squeezed by national discounters on price", "and boutique labs on service — the classic straddle, dying politely."),
    ("The stick analysis:", "their loyal customers' WTP driver was TURNAROUND — results a day faster than anyone, because couriers ran twice daily. Nobody inside had named it."),
    ("The choice:", "fund the driver (third courier run, overnight processing) and RAISE prices 8%; drop the money-losing services the strategy didn't need."),
    ("Two years on: fewer services, higher prices, record margins.", "The strategy was always there — someone finally wrote it down. That someone was a communicator with a framework."),
], D, nxt())
notes(s, "The worked case: diagnosis (unnamed driver), trade-off (dropped services), and the punchline — the strategic act was an act of writing.")

s = section_slide(prs, "05", "Writing with strategy",
    "Value language in proposals — and the arithmetic of your own career.", D, nxt())
notes(s, "Section 5: bringing it home to documents and careers.")

s = bullets_slide(prs, "The proposal, rewritten in value language", [
    ("Every ask maps to a lever, named early:", "'this raises client WTP by cutting their audit prep' or 'this is a pure cost lever: same output, 30 fewer hours' (Chapter 10's problem section, upgraded)."),
    ("Price the status quo in stick terms:", "'doing nothing keeps our WTS high — we're losing techs to labs with better systems' (Chapter 8's status-quo move, with a framework behind it)."),
    ("Quantify the lever, not the effort:", "leadership doesn't fund busy; it funds moved sticks — '$18K of annual rework' beats 'significant team effort' every time (Chapter 4)."),
    ("One lever per proposal, argued deep:", "the initiative that claims all three levers usually moves none — the dilution effect (Chapter 8) applies to value claims too."),
], D, nxt())
notes(s, "The chapter's practical payload: four habits that convert competent proposals into funded ones.")

s = bullets_slide(prs, "Case: two proposals, one budget line", [
    ("Proposal A asked for a $30K training program", "because 'our people deserve investment and morale is suffering.' True, heartfelt, unfunded."),
    ("Proposal B asked for the same $30K:", "'Exit interviews name growth as our top loss driver. Replacing one tech costs $22K. This program targets the three roles with the worst churn — breakeven at 1.4 retentions, and we lose 4 a year.'"),
    ("Same program. Same price. Same sincerity.", "B named the lever (WTS down), priced the status quo, and did the breakeven arithmetic — the language of the people holding the pen."),
    ("The lesson:", "leadership wasn't heartless in rejecting A. A never told them what it was worth. B did. That's the entire chapter — and most of the course."),
], D, nxt())
notes(s, "The closing case pairs with Chapter 13's two-candidates case deliberately: in both, the content was equal and the WRITING was the variable.")

s = bullets_slide(prs, "Your personal value stick", [
    ("Employers have a WTP for you:", "set by the problems you can solve — every skill in this course raises it, because communication is the skill that makes your other skills visible (Chapter 13's case)."),
    ("You have a WTS:", "the least you'd accept for THIS job — and it moves with growth, flexibility, meaning, and a manager who runs Chapter 16."),
    ("Negotiate the whole gap, not just salary (Chapter 14):", "when the price is fixed, development budget and flexibility are WTS moves — value for you that costs them less than cash."),
    ("Career strategy is stick strategy:", "pick roles that RAISE your future WTP (skills, evidence, network) even at equal pay — the wide stick compounds; the flat one just pays."),
], D, nxt())
notes(s, "The framework turned inward — the graduation slide. 'Communication makes your other skills visible' ties the whole course into the career arithmetic.")

s = takeaways_slide(prs, [
    "Value created = WTP minus WTS; profit, delight, and good jobs are slices of that one stick.",
    "Only three levers exist: raise WTP, cut real cost, lower WTS — locate every initiative or call it activity.",
    "WTS is the neglected lever: better jobs and better partnerships create value without squeezing anyone.",
    "Strategy is trade-offs — it tells you what to stop; watch the money, not the mission statement.",
    "Write proposals in lever language with the status quo priced — funded beats heartfelt, and both is best.",
    "Run the stick on your career: raise your WTP with skills and evidence; negotiate the whole gap.",
], D, nxt(), site_note="Practice now: course site → Chapter 17 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap. Course content complete.")

s = quote_slide(prs, "Worth keeping",
    "Value is created in the gap between what customers would pay and what it truly costs to serve them — and it is communicated, or it is lost.",
    "this chapter — after the value-based strategy tradition (Harvard Business School)", D, nxt())
notes(s, "Attributed framing paraphrase, flagged as 'after' the tradition rather than a verbatim quotation.")

s = discussion_slide(prs, "Discussion questions", [
    "Run the three-lever test on your employer's (or university's) last three visible initiatives. Which lever — or was it activity?",
    "Name a firm that is PROUDLY bad at something. What does that weakness buy on the drivers it competes on?",
    "Find the WTS lever in a job you've held: what change would have made you stay for less — and what did it cost the employer NOT to make it?",
    "Rewrite a real (or imagined) proposal ask in value language: lever named, status quo priced, breakeven shown.",
    "Draw your personal value stick for your target role: what sets your WTP, what sets your WTS, and which skill moves your WTP most this year?",
], D, nxt())
notes(s, "Async-ready. Question five doubles as a career-planning exercise.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 17 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 17 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Apply:", "Rewrite your capstone proposal's opening in value language — lever, status quo price, breakeven."),
    ("Reflect:", "You now own the full stack: plan, draft, revise, persuade, report, present, lead, and locate the value. Use it on something real this month."),
    ("The course site stays up:", "practice banks, study guides, and decks remain available — the toolkit doesn't expire with the term."),
], D, nxt())
notes(s, "Delivery-neutral closing. Course complete.")

out = os.path.join(os.path.dirname(__file__), "..", "ch17-strategy-for-communicators.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
