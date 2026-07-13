# Chapter 17 study guide — Strategy for Communicators (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(17, 'Strategy for Communicators',
    'Where the value comes from · willingness to pay, willingness to sell · and proposals that speak the language of both')

h1(doc, 'Why this chapter exists')
para(doc, 'This is the capstone chapter, and it exists to answer a question every other chapter in this '
    'course has left implicit: why does any of this writing skill matter to the organizations that pay '
    'for it? The answer is value-based strategy — in the tradition of the value-stick framework taught '
    'in strategy courses at leading business schools — presented here in original language and original '
    'examples, so that the proposals, reports, and pitches this course has taught you to write can speak '
    'directly in the vocabulary the people funding them actually use.')
para(doc, 'Most professionals never learn where profit comes from, so their proposals argue in '
    'currencies leadership does not spend: effort, fairness, enthusiasm. The proposal that instead '
    'names its lever — does this raise willingness to pay, cut real cost, or lower willingness to '
    'sell? — gets funded at rates that look, from outside, like luck. It is not luck. It is a '
    'communicator who learned to translate every ask into the language the decision-maker was already '
    'thinking in. That translation is this chapter’s entire content, and it closes the course by '
    'returning to its opening claim: communication skill is not separate from strategy. It is how '
    'strategy actually gets executed.')

h1(doc, 'The value stick')
figure(doc, os.path.join(FIG, 'ch17_valuestick.png'),
    'Figure 1. The value stick — four points on a line that explain almost everything about where profit comes from.',
    'A vertical stick with four labeled sections: willingness to pay at top, price, cost, and willingness to sell at '
    'the bottom, with brackets showing customer delight (WTP minus price), firm margin (price minus cost), and '
    'supplier/employee surplus (cost minus WTS), and the note that value created equals WTP minus WTS.')
para(doc, 'Four points on a single line explain nearly everything this chapter has to teach. '
    'Willingness to pay (WTP) is the most a customer would ever pay for something, set entirely by the '
    'value they get from it. Price is what they actually pay — the point where the customer’s share of '
    'the stick gets split from everyone else’s. Cost is what the firm spends to deliver. And '
    'willingness to sell (WTS) is the least suppliers and employees would accept — set by how good the '
    'deal genuinely feels to them. Value created is simply WTP minus WTS, and everything else — the '
    'firm’s profit, the customer’s delight, the employee’s satisfaction — is just a slice of that one '
    'stick: customer delight is WTP minus price, firm margin is price minus cost, and supplier or '
    'employee surplus is cost minus WTS.')
para(doc, 'Creating value and capturing it are different acts, and the distinction matters more than '
    'it first appears. A firm can create enormous value and capture almost none of it — a price war '
    'gives customers everything and the firm nothing — or capture value briefly without creating any, '
    'until customers notice and leave. Durable profit requires both a wide stick (a large gap between '
    'WTP and WTS) and a defensible way of splitting it. This is why price alone is never a strategy: '
    'it only moves where the split happens on a stick whose width someone else determined. The '
    'deepest strategic insight in the whole framework is that the best-run firms compete by WIDENING '
    'the stick — more delight, better jobs — rather than fighting harder over a stick whose width is '
    'fixed. And the same physics governs communication: the proposal that widens the stick ("this '
    'raises WTP") outcompetes the proposal that only claims a bigger slice ("we should charge more") '
    'because the first one is positive-sum and the second is a fight.', bold_lead='Created versus captured.')

h1(doc, 'The only three levers')
figure(doc, os.path.join(FIG, 'ch17_levers.png'),
    'Figure 2. The only three levers — raise WTP, cut real cost, or lower WTS — locate every initiative or call it activity.',
    'Three boxes: raise WTP (make customers’ lives better), cut real cost (same value, less spend), and lower WTS '
    '(make working with you better), with the warning that moving price alone captures differently but creates nothing.')
para(doc, 'Every business initiative, properly understood, does one of exactly three things to the '
    'stick — and an initiative that does none of them is not strategy, whatever it is called in the '
    'meeting where it was proposed. Raising WTP means making customers’ lives genuinely better: '
    'quality that shows up in their outcomes, convenience, risk removed, status and belonging. Cutting '
    'real cost means delivering the same value for less spend — through scale, learning, or better '
    'operations, never through quietly degrading the value the customer actually receives. And '
    'lowering WTS means making it better to work with you or supply you — for employees, this is '
    'flexibility, growth, meaning, and respect; for suppliers, it is reliable forecasts, fast payment, '
    'and honest specifications. Moving price captures value differently but creates none of it — the '
    'lever that looks like strategy in a slide deck and is not one at all. The three-lever test '
    'becomes, once learned, impossible to unlearn: for any initiative, project, or proposal, ask which '
    'lever it pulls. An initiative that cannot be located on the stick is activity wearing strategy’s '
    'clothes.')

h1(doc, 'Raising willingness to pay')
para(doc, 'WTP rises whenever a customer’s actual outcomes improve, and the discipline is naming the '
    'outcome rather than the feature that produces it — Chapter 8’s "outcomes, not features" rule, '
    'here given its strategic foundation. Quality that shows up in the customer’s own results (the '
    'instrument that cuts audit findings raises WTP by the value of the findings avoided, not by the '
    'elegance of its spec sheet), convenience (every friction point removed adds to WTP, because '
    'friction is a hidden cost the customer already pays), risk removed (guarantees and pilots are '
    'WTP additions, because certainty is a feature customers will pay for directly), and status or '
    'belonging (social WTP is still WTP — dismissing it as vanity leaves real margin on the table).')
para(doc, 'Complements — products that make YOUR product more valuable — are a WTP lever worth '
    'naming explicitly, because they explain pricing patterns visible everywhere once you know to '
    'look for them: firms give away or subsidize a complement specifically because a cheaper '
    'complement widens their own core product’s stick. Substitutes work in the opposite direction, '
    'capping WTP from below, and any honest proposal names both. And near-customers — people who '
    'value the product but do not buy, because price sits above their WTP or one friction blocks '
    'them — are frequently where the easiest growth hides: a simpler tier, a financing option, or a '
    'single removed friction can convert an entire segment at once, and finding them is market-scale '
    'audience analysis (Chapter 2), not a separate skill.')

h1(doc, 'Cutting cost, lowering WTS')
para(doc, 'Cost cutting is honest only when it delivers the same value for less spend; when a cut '
    'quietly moves cost onto customers (degraded service, lowering their WTP) or onto employees '
    '(burnout, raising WTS), the stick has not shrunk — it has shifted, and it will shrink for real '
    'soon after, in churn and turnover. The test for any proposed cut: what happens to WTP and WTS as '
    'a result? A cut that pays for itself in attrition and lost customers was a loan against the '
    'future, not a genuine saving, and proposals should be written in exactly that language: "this cut '
    'leaves WTP untouched — same turnaround, same quality — verified as follows" (Chapter 10’s '
    'evidence standard).')
para(doc, 'Lowering employee WTS is the framework’s most underused lever and the one this chapter '
    'insists deserves equal billing with the more visible WTP and cost levers. Every improvement in '
    'how work actually feels — autonomy, flexibility, growth, a manager who runs Chapter 16’s '
    'principles — lowers the compensation a person would accept to stay, which means retained '
    'employees, lower recruiting spend, and preserved institutional knowledge, all as consequences of '
    'a single lever pulled well. This is precisely why "soft" initiatives are hard strategy: the '
    'mentoring program is not a perk, it is a WTS lever with a measurable financial effect, and '
    'writing it up in THAT language, rather than as a nicety, is frequently the difference between a '
    'funded initiative and a shelved one. Supplier WTS follows the identical logic in the other '
    'direction: suppliers price the relationship, not merely the order, and a chaotic buyer pays for '
    'that chaos inside every quote it receives. Reliable forecasts, clean specifications, and prompt '
    'payment lower supplier WTS and are, not incidentally, made almost entirely of business writing — '
    'this chapter’s lever is, in the end, largely a communication lever.')

h1(doc, 'Strategy in practice')
figure(doc, os.path.join(FIG, 'ch17_tradeoffs.png'),
    'Figure 3. Strategy is choosing what to be bad at — trade-offs versus straddling.',
    'Two panels: straddling (chasing every value driver, averaging the proposition into "fine") and trade-offs '
    '(picking the drivers to compete on and accepting visible weakness on the rest), with the test that a real '
    'strategy tells you what to stop doing.')
para(doc, 'No firm can be best on every driver simultaneously — the cheapest, fastest, most premium, '
    'and most personal option all at once describes four different companies, not one. Strategy is '
    'the discipline of picking the drivers to compete on and accepting visible weakness on the rest, '
    'deliberately: the discount airline is proudly bad at legroom, and that weakness is the strategy '
    'functioning correctly, not a flaw in its execution. Straddling — chasing every driver at once — '
    'averages the value proposition into "fine," and fine commands the willingness to pay of a shrug. '
    'The practical test, worth running on any initiative: does it tell you what to STOP doing? A '
    'genuine strategy always does; if nothing became harder to justify as a result of adopting it, no '
    'strategy was actually made, only an aspiration.')
para(doc, 'Reading an organization’s actual strategy — as opposed to its stated mission — means '
    'watching the money rather than the poster on the wall: what gets funded without a fight, who '
    'gets promoted, which customers get kept even when they are difficult. The revealed strategy, '
    'discovered this way, is frequently different from the stated one, and it is the revealed version '
    'that determines which proposals get funded. Locating one’s own role on the stick — does this job '
    'raise WTP, cut cost, or lower WTS? — is worth doing explicitly, because a performance review is '
    'implicitly graded in exactly this language whether or not it is ever stated aloud. And strategy '
    'is not the same activity as planning: a plan is a list of dated activities, while a strategy is '
    'a theory of value — "we win here, for these customers, because our stick is wider" — and the '
    'communicator’s upgrade, worth the extra page, is writing the actual theory before writing the '
    'plan that executes it.')

h1(doc, 'Case study: the regional lab chain')
para(doc, 'A twelve-location lab chain was being squeezed simultaneously by national discounters on '
    'price and boutique competitors on service — the textbook straddle, failing slowly and politely. '
    'A stick analysis, run for the first time in the company’s history, found that its most loyal '
    'customers’ actual WTP driver was turnaround time: results delivered a day faster than any '
    'competitor, made possible by a courier schedule nobody inside the company had ever named as a '
    'competitive asset.')
para(doc, 'The strategic choice, once the driver was named, became straightforward rather than '
    'agonizing: fund the driver directly — a third daily courier run, overnight processing — and '
    'raise prices 8% to match the now-explicit value being delivered, while dropping several '
    'money-losing service lines the actual strategy did not need to defend. Two years later: fewer '
    'services offered, higher prices charged, and record margins achieved. The strategy, in a real '
    'sense, had been operating successfully and invisibly for years before anyone wrote it down. The '
    'strategic act, in the end, was an act of writing — naming a driver that had always been there and '
    'converting it from an accident into a deliberate plan.')

h1(doc, 'Writing with strategy')
figure(doc, os.path.join(FIG, 'ch17_proposal.png'),
    'Figure 4. Writing proposals in value language — name the lever, price the status quo, show the arithmetic.',
    'A three-step flow: name the lever (WTP up, cost down, or WTS down), price the status quo (no is never free), '
    'and show the arithmetic (breakeven, not just effort), with the note that one lever per proposal, argued deep, '
    'avoids the dilution effect.')
para(doc, 'Every proposal this course has taught you to write improves the moment it names its lever '
    'explicitly and early: "this raises client WTP by cutting their audit prep time" or "this is a '
    'pure cost lever — same output, thirty fewer hours a month" (Chapter 10’s problem section, '
    'upgraded with the vocabulary this chapter supplies). Price the status quo in the same terms: '
    '"doing nothing keeps our WTS high — we are losing technicians to labs with better systems" prices '
    'inaction the way Chapter 8 taught, now with a framework behind the number rather than just an '
    'assertion. Quantify the lever itself, never merely the effort spent pursuing it — leadership '
    'funds moved sticks, not busy calendars, and "$18K of annual rework avoided" persuades where '
    '"significant team effort invested" does not. And argue one lever per proposal, in depth: an '
    'initiative claiming to move all three levers at once usually convinces on none of them, because '
    'the dilution effect from Chapter 8 governs value claims exactly as it governs persuasive '
    'arguments generally.')

h1(doc, 'Case study: two proposals, one budget line')
para(doc, 'Proposal A requested a $30,000 training program because, in its own words, "our people '
    'deserve investment and morale is suffering." True, sincerely felt, and unfunded. Proposal B '
    'requested the identical $30,000 for the identical program, framed differently: "exit interviews '
    'name growth as our top loss driver. Replacing one technician costs $22,000. This program targets '
    'the three roles with the worst churn — breakeven at 1.4 retentions, and we lose four a year." '
    'Same program, same price, equally sincere intent behind both requests — but B named the lever '
    '(lowering WTS), priced the status quo, and ran the breakeven arithmetic in the vocabulary of the '
    'people holding the budget pen.')
para(doc, 'Leadership was not being heartless in declining Proposal A. Proposal A never told them '
    'what the program was actually worth in terms the budget process could evaluate; Proposal B did, '
    'in three sentences. The lesson generalizes directly from Chapter 13’s two-candidates case: '
    'identical content, identical sincerity, and the entire outcome turned on the writing. That '
    'pattern — content equal, writing decisive — has now appeared at three different stakes across '
    'this course, from a job application to a training budget, and it is close to the course’s single '
    'most important recurring finding.')

h1(doc, 'Your personal value stick')
para(doc, 'The framework turns inward for a graduating class in a way worth making explicit rather '
    'than leaving implicit. Every employer has a WTP for you, set by the problems you can '
    'demonstrably solve — and every skill this course has built raises that number, because '
    'communication is specifically the skill that makes your other skills visible to the people '
    'deciding whether to hire or promote you (Chapter 13’s entire case rests on exactly this point). '
    'You also have a WTS — the least you would accept for a given role — and it moves with growth, '
    'flexibility, meaning, and the quality of the management you report to (Chapter 16, once again). '
    'When negotiating an offer, negotiate the whole gap rather than only the salary line (Chapter '
    '14): development budget and flexibility are value for you that frequently cost an employer less '
    'than an equivalent amount of cash, which makes them easier concessions to obtain. And career '
    'strategy is, in the end, stick strategy: choosing roles that raise your future WTP — through '
    'skills gained, evidence accumulated, and networks built — even at equal current pay, because a '
    'widening stick compounds over a career in a way that a merely well-paid flat one never does.')

h1(doc, 'A closing note on humility: what this framework does not explain')
para(doc, 'It would be dishonest to close a capstone chapter without naming the framework’s limits. '
    'The value stick explains where economic value comes from and how to argue for resources in its '
    'language; it does not, by itself, explain everything worth valuing. Some worthwhile work — pure '
    'research with no clear near-term application, care for people that produces no measurable '
    'retention benefit, art and culture pursued for reasons unrelated to any customer’s willingness '
    'to pay — sits partly or entirely outside this chapter’s vocabulary, and forcing every human '
    'activity into stick language would itself be a kind of category error, the same error this '
    'chapter warned against when discussing nonprofit mission and ethical limits.')
para(doc, 'The honest scope of the claim: within the domain of organizational resource allocation — '
    'which proposal gets funded, which initiative gets prioritized, which role gets the next '
    'headcount — this framework describes the actual mechanism with unusual clarity, and learning to '
    'speak its language measurably improves a communicator’s ability to get good work funded. It does '
    'not describe, and was never meant to describe, why the work is worth doing in some deeper sense. '
    'That question belongs to the person doing the work, not to the stick. This course has taught you '
    'to argue for what you believe in more effectively. It has not told you what to believe in — that '
    'choice, appropriately, remains entirely yours.')

h1(doc, 'The last worked comparison: a career built on the floor versus a career built on the stick')
para(doc, 'Two graduates, same program, same GPA, same starting title at comparable companies. Both '
    'are competent, reliable, and well-liked. Five years on, one has been promoted twice; the other, '
    'equally hardworking, has been promoted once and has begun quietly job-searching out of a sense '
    'that her contributions go unnoticed. The difference, traced back, was never effort.')
para(doc, 'The first graduate learned, somewhere in his first two years, to translate his work into '
    'the vocabulary this chapter has spent its pages building: his project updates named which lever '
    'each initiative pulled, his proposals priced the status quo before asking for budget, and his '
    'self-advocacy during review season pointed to that history NAMED, not merely performed. The '
    'second graduate did equally strong work and described it, consistently, in effort and activity '
    'language — "I worked really hard on this," "I put in a lot of hours" — which is honest and '
    'sympathetic and, as this entire course has shown from Chapter 13 onward, simply not the currency '
    'that funding and promotion decisions are made in.')
para(doc, 'Neither graduate was dishonest, lazy, or less capable. One had learned to speak the '
    'language the decisions were actually made in; one had not yet learned that such a language '
    'existed to be learned. That is the gap this course, and this final chapter specifically, exists '
    'to close — not by making anyone work harder, but by giving the work a vocabulary that the people '
    'funding it already speak.')

h1(doc, 'What to do Monday morning, in whatever role you hold')
para(doc, 'This chapter, and this course, close with the most practical possible question: what does '
    'any of this mean for the specific job a reader is about to start or already holds? A short, '
    'role-general answer, sized for a first Monday.')
numbered(doc, [
    'Learn your organization’s revealed strategy within the first month — watch what gets funded, '
    'not what the mission statement claims — before proposing anything that might collide with it '
    'unknowingly.',
    'Locate your own role on the stick as soon as you can articulate it honestly: does the work you '
    'do raise WTP, cut cost, or lower WTS? If you genuinely cannot tell, that is itself worth raising '
    'with a manager, framed as a question rather than a complaint.',
    'The next time you want something funded — a tool, a training budget, a process change — write '
    'the one-page strategy memo from this chapter before writing anything longer. It will tell you, '
    'often within the first paragraph, whether the ask is ready to make.',
    'Keep the three-question closing frame from Chapter 16 and the value-lever test from this chapter '
    'as a permanent pair: one governs how you treat people under pressure, the other governs how you '
    'argue for resources. Together they cover most of what a career actually requires beyond '
    'technical competence.',
    'Revisit this course’s materials when the stakes are real, not just during the term you took it. '
    'A study guide read once during a semester and never again is notes; the same guide reopened '
    'before an actual high-stakes proposal, interview, or crisis is a genuine professional resource.',
])

h1(doc, 'A final worked example: from raw idea to funded proposal')
para(doc, 'To make the whole chapter concrete, here is one initiative walked from a vague hallway idea '
    'to a fundable one-page memo, using every tool this chapter has supplied in sequence.')
para(doc, 'The raw idea, as first mentioned in a hallway conversation: "we should probably get better '
    'project-management software; the current one is kind of a pain." Vague, unpriced, unlikely to '
    'survive a budget meeting in this form — closer to a complaint than a proposal.', bold_lead='Stage one.')
para(doc, 'Applying the measurement discipline: instead of guessing at the pain, the proposer pulled '
    'actual data — hours per week the team spent on manual status updates the current software should '
    'have automated, and one near-miss where a missed deadline traced directly to a scheduling '
    'conflict the software failed to flag. This is behavioral evidence, not a survey of feelings about '
    'the software.', bold_lead='Stage two.')
para(doc, 'Naming the lever: the case is a cost lever, not a WTP or WTS story — "same project '
    'outcomes, six fewer hours per week of manual status-chasing across a five-person team." Precise, '
    'and importantly, NOT inflated into a WTS claim about team morale that the data did not actually '
    'support.', bold_lead='Stage three.')
para(doc, 'Pricing the status quo and the alternative: six hours a week across five people, at a '
    'blended rate, comes to a concrete annual figure — compared honestly against the new software’s '
    'licensing cost, yielding a breakeven inside the first quarter. The near-miss deadline, priced '
    'separately as a risk rather than folded dishonestly into the routine-hours savings, strengthens '
    'the case without overstating it.', bold_lead='Stage four.')
para(doc, 'Naming the honest trade-off: adopting the new tool means a two-week migration period '
    'during which the team’s reported hours-saved will temporarily go negative — stated up front, '
    'rather than left for a skeptical reviewer to discover and use against the proposal’s credibility.',
    bold_lead='Stage five.')
para(doc, 'The final one-page memo, assembled from stages two through five, reads nothing like the '
    'original hallway complaint and everything like the two-proposals case study earlier in this '
    'chapter: a clear lever, real evidence, an honest cost of inaction, and a stated trade-off. The '
    'idea did not change between the hallway and the memo. The communication of it did — and that '
    'gap, demonstrated one final time, is this entire course.', bold_lead='Stage six.')

h1(doc, 'Case study: the consultant who separated signal from noise')
para(doc, 'An operations consultant was hired by a mid-size distributor to "improve customer '
    'satisfaction," a mandate vague enough to justify almost any initiative. Rather than starting '
    'with a survey (which the client had already run three times, at declining response rates and '
    'increasingly generic results), she began with the value stick: what specifically was the '
    'distributor’s customers’ WTP built on, and was it actually declining, or was a different metric '
    'being mistaken for it?')
para(doc, 'Behavioral data — order patterns, complaint logs, actual account cancellations — told a '
    'sharper story than the surveys had. Satisfaction scores had drifted downward slightly across the '
    'board, but cancellations were concentrated almost entirely among one customer segment: accounts '
    'placing frequent small emergency orders, whose real WTP driver was delivery speed under time '
    'pressure, not the broad "satisfaction" the surveys measured. The distributor’s standard delivery '
    'window — perfectly adequate for the majority of accounts placing routine orders — was actively '
    'failing this smaller, higher-value segment, and their departures were dragging down the average '
    'satisfaction score enough to look like a company-wide problem.')
para(doc, 'The fix was narrow and cheap compared to the company-wide "improve satisfaction" initiative '
    'originally envisioned: a rush-order tier with a different fulfillment path, priced to reflect its '
    'genuinely higher WTP, offered only to the segment that needed it. Overall satisfaction scores '
    'recovered within two quarters — not because service broadly improved, but because the specific '
    'driver actually losing customers got addressed directly, while the majority of accounts noticed '
    'no change at all because none was needed for them. The consultant’s closing memo to the client '
    'board made the point this whole chapter has been making: "you asked us to fix satisfaction. The '
    'real question was always which customers, driven by which value, and the survey couldn’t tell '
    'you that. Behavior could."')

h1(doc, 'Pricing: the split point, and why it deserves its own care')
para(doc, 'Price sits in the exact middle of the stick and gets more organizational attention than '
    'any other point on it, often at the expense of the WTP and WTS work that actually determines how '
    'much room a price has to move within. A few pricing principles follow directly from the '
    'framework and are worth stating for any communicator who will someday write a pricing '
    'recommendation or justify one to a client.')
bullets(doc, [
    ('Price below WTP always, or the sale never happens.', 'This sounds obvious stated plainly, yet '
     'pricing decisions routinely get anchored to cost-plus formulas that ignore what the customer '
     'would actually pay — Chapter 8’s anchoring principle, run internally: the first number in a '
     'pricing conversation is often the cost structure, when it should be the customer’s value.'),
    ('A price near WTP captures more value but converts fewer customers;', 'a price near cost converts '
     'more customers but captures less value per sale. This trade-off has no universally correct '
     'answer — it depends entirely on whether the strategic goal is margin or market share, which is '
     'itself a strategic choice deserving the same explicit trade-off treatment as any other.'),
    ('Price communicates a claim about value whether or not that claim is intended.', 'A price set '
     'too low relative to genuine quality can depress WTP directly, because customers use price as a '
     'quality signal in the absence of other information — the "credence good" problem familiar from '
     'markets where quality is hard to verify before purchase.'),
    ('Discounting is a WTS conversation in disguise, aimed at the customer instead of an employee.',
     'A discount is, functionally, lowering the price the customer must pay to say yes — which is '
     'sometimes the right lever to pull and sometimes a signal that the actual problem is inadequate '
     'WTP, being papered over with a price cut that erodes margin without fixing the underlying issue.'),
])
para(doc, 'None of this is a pricing course. It is the minimum vocabulary a communicator needs to '
    'participate credibly in a pricing conversation, rather than treating price as a number handed '
    'down from finance with no connection to the value arguments the rest of this chapter has built.')

h1(doc, 'The one-page strategy memo: a template')
para(doc, 'Chapter 10 taught the executive summary; this section supplies its strategic counterpart — '
    'a one-page memo any communicator can write to clarify (for themselves, first, and for leadership '
    'second) exactly where an initiative’s value comes from before drafting the full proposal around '
    'it.')
numbered(doc, [
    'The driver, named in one sentence: "This raises client WTP by cutting audit-prep time" or "This '
    'lowers technician WTS by removing the worst-rated shift rotation." One lever, stated plainly, '
    'no hedging across all three.',
    'The evidence, in two sentences: the measurement (behavioral, not just surveyed) that supports '
    'the claimed driver — a pilot result, an exit-interview pattern, a documented near-customer '
    'segment.',
    'The status quo, priced: what continuing to do nothing costs, in the same units as the proposed '
    'investment, so the two numbers can be compared on one line.',
    'The trade-off, named honestly: what this initiative means saying no to, or being worse at, as a '
    'direct consequence — the discomfort that proves a real strategic choice is being made rather '
    'than a wish list being assembled.',
    'The breakeven, shown: the arithmetic connecting cost to return, in the plainest possible form — '
     '"pays back in 14 months" or "breakeven at 1.4 retentions a year."',
])
para(doc, 'Five sentences, one page, and — worth noting explicitly — the discipline of writing it '
    'often reveals that a favored initiative does not actually have a clear driver, clear evidence, or '
    'an honest trade-off attached, which is more useful to discover before the full proposal than '
    'after it has been rejected for reasons that were never quite explained.')

h1(doc, 'Reading a company for value drivers before you interview there')
para(doc, 'Chapter 13 taught researching an employer before applying; this chapter supplies the '
    'specific lens that research should run through. Before an interview, try to answer: what is this '
    'company’s actual value driver — the thing on the stick they compete on — and is the role being '
    'discussed positioned to serve it?')
bullets(doc, [
    ('Read the careers page and recent news for WTP language.', 'Does the company talk about being '
     'faster, cheaper, higher-quality, more convenient, or more prestigious? That language reveals '
     'which driver leadership believes it competes on, whether or not the belief is accurate.'),
    ('Ask directly in the interview:', '"what does this team’s work do for the company’s core value '
     'proposition?" — Chapter 14’s recommended interview questions, now aimed specifically at '
     'locating the role on the stick. A hiring manager who cannot answer this clearly is revealing '
     'something about the role’s actual strategic weight.'),
    ('Watch for straddle symptoms during the interview process itself.', 'A company whose interviewers '
     'describe conflicting priorities (be the cheapest AND the most premium; move fast AND never make '
     'mistakes) may be straddling internally, which frequently shows up later as organizational '
     'friction and unclear priorities for whoever takes the role.'),
])
para(doc, 'Locating a prospective employer’s actual strategy before accepting an offer is not merely '
    'academic interest — Chapter 14’s offer-evaluation matrix improves considerably when "does this '
    'role serve a real, well-understood value driver" is one of the weighted criteria, alongside '
    'manager quality, path, and compensation.')

h1(doc, 'Case study: the acquisition that failed the trade-off test')
para(doc, 'A regional accounting firm, strong in small-business tax and bookkeeping services, acquired '
    'a boutique forensic-audit practice specializing in litigation support — a service with a '
    'genuinely different client base, different staff expertise, and a completely different sales '
    'cycle. The acquisition’s stated logic was growth: "more services means more revenue." Eighteen '
    'months later, the combined firm’s core small-business clients reported declining satisfaction, '
    'the forensic-audit partners had left for a competitor, and overall margins had fallen despite '
    'higher total revenue.')
para(doc, 'A stick analysis conducted after the fact — the kind that should have been run before the '
    'acquisition, not after — revealed the mechanism plainly. The firm’s original small-business '
    'clients had a WTP driven by responsiveness and simplicity: same-day answers, plain-language '
    'explanations, predictable flat fees. Absorbing the forensic-audit practice pulled senior '
    'partner attention toward complex, high-stakes litigation matters that paid more per engagement '
    'but demanded exactly the kind of extended availability and specialized language that eroded the '
    'core clients’ experience. The firm had, without naming it, straddled two genuinely different '
    'value propositions and served both worse as a result — this chapter’s central warning, executed '
    'via acquisition rather than internal feature creep, with the identical outcome.')
para(doc, 'The eventual fix was a trade-off made explicit and public: the forensic-audit practice was '
    'spun off as an independent affiliate with its own brand and partner structure, allowed to serve '
    'its different WTP driver (expertise and discretion, not speed) without diluting the core firm’s '
    'promise. Both halves, separated, recovered their original margins within a year. The lesson for '
    'any communicator asked to write the case for a merger, acquisition, or "any inch we can get more '
    'revenue from" proposal: growth that fails the trade-off test is not growth. It is dilution '
    'wearing a bigger number.')

h1(doc, 'The course, in one closing frame')
para(doc, 'Seventeen chapters ago, this course opened with a claim: communication is the most '
    'portable skill a career can hold, because it is the medium through which every other skill '
    'becomes visible, actionable, and valuable to the people who depend on it. This closing chapter '
    'has tried to make that claim literal rather than aspirational, by showing exactly where value '
    'comes from in any organization and how communication pulls each of the three levers directly.')
para(doc, 'A brief accounting of what the seventeen chapters actually built, seen now as one '
    'integrated system rather than a syllabus. The foundation chapters (1–4) built the raw mechanics: '
    'how communication succeeds or fails, how to plan a message before writing it, how to organize '
    'and draft it, how to revise it into something that survives scrutiny. The genre chapters (5–10) '
    'applied those mechanics to the documents a career actually requires: the short message, the '
    'positive and negative message, the persuasive pitch, the report, the formal proposal. The '
    'professional-practice chapters (11–14) extended the same discipline to the settings and '
    'transitions a career moves through: the team, the meeting, the podium, the job search, the '
    'interview. And this final unit (15–17) supplied the tools a career now runs alongside — the AI '
    'that drafts, the leadership moment that tests everything at once, and the strategic vocabulary '
    'that explains why any of it was worth learning to an organization deciding what to fund.')
para(doc, 'The recurring finding, surfacing in nearly identical form across chapters that otherwise '
    'shared nothing — two résumé candidates, two interview follow-ups, two training proposals, two '
    'plant managers, two software companies — deserves to be named once, plainly, as the course '
    'closes: identical substance produces wildly different outcomes based on how it is communicated. '
    'Not because communication is decoration applied after the real work is done, but because for '
    'nearly every kind of value this course has discussed — a candidate’s worth, a team’s trust, an '
    'organization’s strategy — the communication of it IS a substantial part of the value itself. '
    'That is the sentence this entire course has been building toward, seventeen chapters at a time.')

h1(doc, 'Five myths, retired')
para(doc, 'Retired by the value stick itself: cost and price sit in the MIDDLE of the stick, not at '
    'its center of gravity. A strategy built purely on being cheaper is a strategy that has ceded the '
    'entire WTP side of the equation to whatever the product happens to already deliver — durable '
    'advantage lives in the WTP and WTS ends, where competitors find it hardest to simply match a '
    'number.', bold_lead='Myth: strategy is fundamentally about being cheaper than competitors.')
para(doc, 'Retired by the nonprofit section above: WTP and WTS apply to donor gifts, volunteer time, '
    'and mission-driven retention exactly as they apply to customer purchases and employee '
    'compensation. The vocabulary changes; the arithmetic of where value comes from does not.',
    bold_lead='Myth: value-based strategy only applies to for-profit companies.')
para(doc, 'Retired by the trade-offs section: a strategy that never requires giving anything up was '
    'never a strategy, only a wish list. The discomfort of explicitly declining a market segment or a '
    'feature request is not a sign the strategy is wrong — it is frequently the sign that a real '
    'choice was actually made.', bold_lead='Myth: a good strategy should please every stakeholder.')
para(doc, 'Retired by the ethics section immediately above: the durable, positive-sum version of '
    'every lever makes the other party genuinely better off. A lever pulled through squeeze rather '
    'than genuine improvement fails Chapter 16’s ethical test and typically proves unstable the '
    'moment alternatives appear.', bold_lead='Myth: lowering WTS just means paying people less.')
para(doc, 'Retired by nearly this entire course: Chapter 13’s two-candidates case, Chapter 14’s '
    'silver-medalist case, and this chapter’s two-proposals case all show identical substance '
    'producing wildly different outcomes based purely on how it was communicated. Strategy without '
    'the ability to articulate it in the funding audience’s own language does not get funded, however '
    'sound the underlying logic.', bold_lead='Myth: a good strategy speaks for itself and needs no persuasive writing.')

h1(doc, 'Frequently asked questions')
para(doc, 'Both, and the framework is agnostic about which — what matters is that the theory of value '
    '(where does OUR advantage in this market come from) exists and is written down before the '
    'quarterly activities are planned. A strategy discovered from bottom-up initiatives still needs '
    'to be named and defended once discovered, exactly as the regional lab case shows.',
    bold_lead='Does strategy have to come from the top of an organization, or can it be built bottom-up?')
para(doc, 'Start with the customer-facing WTP question, since it is usually more measurable and less '
    'politically fraught than an internal WTS conversation. Once a real WTP driver is identified and '
    'validated, the trade-off conversation (what do we stop doing to fund this) becomes concrete '
    'rather than abstract, which makes it much easier to have productively.',
    bold_lead='My organization has no explicit strategy at all. Where do I even start applying this framework?')
para(doc, 'Yes, provided the argument is honest: naming a real lever, with real evidence, is '
    'legitimate persuasion (Chapter 8); inventing a plausible-sounding lever with fabricated support is '
    'the same integrity violation Chapter 9 and Chapter 15 both warn against, just wearing this '
    'chapter’s vocabulary instead.', bold_lead='Can this framework be used to make a weak proposal sound stronger than it is?')

h1(doc, 'Case study: the software company that chose its enemy')
para(doc, 'A mid-size project-management software company faced a strategic crossroads familiar to '
    'many growing firms: expand upmarket to compete with enterprise incumbents, or stay focused on '
    'small teams where they had started. Every recent product request pulled toward "enterprise-grade" '
    'features — SSO integration, advanced permissions, compliance certifications — each individually '
    'reasonable, each collectively pulling the product toward exactly the straddle this chapter warns '
    'against.')
para(doc, 'The founding team ran a stick analysis on their actual customer base rather than their '
    'loudest feature requests (the vocal-minority warning from the measurement section above, applied '
    'directly): their highest-WTP, highest-retention customers were small teams who valued speed of '
    'setup and simplicity above all else, and their WTP for the product dropped, not rose, as '
    'complexity increased. The enterprise features, largely requested by a small number of prospective '
    'customers who had never actually purchased, were solving a problem the company’s real customer '
    'base did not have.')
para(doc, 'The strategic choice, once the driver was correctly identified, was a deliberate trade-off: '
    'explicitly decline the enterprise market, remove several in-progress "enterprise-readiness" '
    'features from the roadmap, and double down on onboarding speed as the company’s defining driver — '
    'a public commitment ("set up your team in under five minutes, guaranteed") that would have been '
    'impossible to sustain while also serving enterprise complexity requirements. Two competitors who '
    'chose to straddle both markets simultaneously saw their onboarding times creep upward over the '
    'following two years as feature complexity accumulated; the company that chose its enemy '
    '(enterprise incumbents, deliberately not competed with) grew faster in its chosen segment than '
    'either straddling competitor grew in total.')
para(doc, 'The lesson generalizes past software specifically: choosing a trade-off means choosing who '
    'you will NOT serve, explicitly and often publicly, which is uncomfortable in a way that '
    '"we serve everyone" never is — and precisely why so few organizations do it, and why the ones '
    'that do gain a durable advantage over the ones that merely say they have a strategy.')

h1(doc, 'A note on ethics: value creation is not value extraction')
para(doc, 'This chapter’s framework can be, and occasionally is, misused to justify squeezing value '
    'from employees or suppliers rather than creating it — lowering WTS through worse working '
    'conditions rather than through genuinely better ones, for instance, technically "moves the '
    'lever" while violating the entire spirit of the framework. Worth stating directly: a WTS '
    'reduction achieved by making people’s lives WORSE and leaving them no better alternative is '
    'extraction, not the value creation this chapter describes, and it typically proves unstable — '
    'the moment a better alternative appears, the "savings" evaporate in a wave of departures, often '
    'at the worst possible moment for the organization.')
para(doc, 'The durable version of every lever in this chapter is positive-sum: WTP rises because '
    'customers are genuinely better off; WTS falls because employees and suppliers are genuinely '
    'better off working with you. Chapter 16’s ethical-influence test applies with full force here: '
    'would the person on the other side of this lever, seeing exactly how and why it was pulled, '
    'still feel the arrangement was fair? A value-stick argument that fails this test is not a '
    'strategic insight. It is a euphemism for something this course’s ethics content, threaded through '
    'every chapter from Chapter 1 onward, would call by its plainer name.')

h1(doc, 'Competitive strategy and the communicator’s role')
para(doc, 'Beyond the value stick’s internal arithmetic, communicators need a working vocabulary for '
    'how firms position against rivals, because proposals and pitches routinely have to argue not just '
    '"this creates value" but "this creates MORE value than the alternative," including the '
    'alternative of doing nothing and the alternative of a competitor’s offer.')
bullets(doc, [
    ('Differentiation versus cost leadership.', 'A firm competing on differentiation wins by raising '
     'WTP higher than rivals can match at a similar cost; a firm competing on cost leadership wins by '
     'delivering acceptable WTP at a cost rivals cannot match. Confusing which game your organization '
     'is playing is a common and costly proposal-writing error — a cost-leader’s internal pitch '
     'should rarely lead with premium features, and a differentiator’s pitch should rarely lead with '
     'being the cheapest option.'),
    ('Sustainable advantage requires a reason competitors can’t simply copy it.', 'A wider stick that '
     'rivals can replicate within a quarter is a temporary advantage, not a strategic one — the '
     'communicator’s question worth asking before writing an enthusiastic proposal: what stops a '
     'competitor from doing this too, next month?'),
    ('Switching costs affect both WTP and WTS calculations.', 'A customer already invested in your '
     'system has an effectively higher WTP for your NEXT offering, because switching away carries a '
     'real cost — proposals for existing customers can legitimately account for this, while '
     'proposals for net-new customers cannot assume it.'),
])
para(doc, 'None of this requires a full strategy course to apply usefully — it requires knowing '
    'enough to ask "compared to what, and why can’t they just copy us?" before finalizing any pitch '
    'that claims competitive advantage as part of its case.')

h1(doc, 'How communication itself moves the value stick')
para(doc, 'This course’s central, load-bearing claim gets its final statement here: communication is '
    'not merely a tool for describing value that strategy created elsewhere. Communication frequently '
    'IS the value-creating act itself, on all three levers at once.')
bullets(doc, [
    ('Communication raises WTP directly.', 'A customer’s willingness to pay depends heavily on '
     'understanding what they are buying — the clearest explanation of a complex service often raises '
     'WTP more than a feature added to the service itself, because confusion is a tax on WTP that '
     'clear writing removes for free (Chapter 8’s outcomes-language, doing literal economic work).'),
    ('Communication cuts real cost.', 'Chapter 9’s entire report-writing apparatus — the pyramid, the '
     'honest yellow, decision minutes — exists to prevent the costliest failure mode in organizations: '
     'work redone because the first version was never clearly specified or clearly reported. Every '
     'hour saved from a miscommunication that didn’t happen is a real cost-lever pull.'),
    ('Communication lowers WTS.', 'Chapter 16’s entire leadership-communication apparatus — clarity '
     'over reassurance, honest correction, genuine appreciation — is, in value-stick terms, a direct '
     'WTS lever: people accept less to work somewhere they are treated with this kind of respect and '
     'clarity, and organizations that communicate this way pay a real, measurable retention dividend.'),
])
para(doc, 'This is why a course about writing memos, reports, and pitches ends on strategy rather than '
    'on a separate, unrelated subject. The two were never separate. Every chapter has been teaching a '
    'lever.')

h1(doc, 'Measuring WTP and WTS in the real world')
para(doc, 'WTP and WTS are not visible on any invoice, which is precisely why they get ignored in '
    'favor of price and cost — the numbers that already appear in a spreadsheet. Finding them requires '
    'the research discipline Chapter 9 already taught, aimed at a specific question.')
bullets(doc, [
    ('For WTP: watch behavior, not stated preference.', 'What customers actually trade off — driving '
     'further for a better price, tolerating a worse feature to get a needed one — reveals more than '
     'a survey question asking "how much would you pay?" (which respondents answer strategically, '
     'not honestly). Chapter 9’s primary-research methods apply directly: pilots, A/B tests, and '
     'observed switching behavior are stronger evidence than self-reported willingness.'),
    ('For WTS: exit interviews and near-miss departures are the richest source.', 'What an employee '
     'who almost left says was the deciding factor — flexibility, a bad manager, a missed promotion — '
     'is a direct WTS data point. Aggregated across many exits, a pattern in exit-interview language '
     'is essentially a market research report on your own organization’s WTS drivers.'),
    ('For suppliers: ask directly what would lower their price.', 'Suppliers frequently know exactly '
     'what makes a customer expensive or cheap to serve — inconsistent order volume, late payment, '
     'shifting specifications — and asking "what would make us easier to work with?" often produces '
     'a straightforward, actionable answer that pure negotiation never surfaces.'),
    ('Beware the vocal minority.', 'The loudest customer feedback is rarely representative of the '
     'median customer’s actual WTP; Chapter 9’s denominator discipline (report the response rate, not '
     'just the responses) applies directly to avoid mistaking noise for signal.'),
])
para(doc, 'The unifying point: WTP and WTS are empirical questions, answerable with the same research '
    'rigor this course has taught for any other claim, not values to be guessed at in a strategy '
    'offsite. Guessing produces strategy statements that sound right and mean nothing; measuring '
    'produces ones a communicator can actually write a defensible proposal around.')

h1(doc, 'Strategy in mission-driven and nonprofit organizations')
para(doc, 'The value-stick framework is often assumed to apply only to for-profit firms, and this is a '
    'mistake worth correcting directly, because a large share of this course’s students will work in '
    'or communicate for mission-driven organizations at some point in a career.')
bullets(doc, [
    ('WTP has a direct nonprofit analog: donor and beneficiary value.', 'A donor’s "willingness to '
     'pay" is measured in the size and frequency of gifts they will make for a given outcome — Chapter '
     '8’s fundraising case (the $180-per-student ask) is precisely a WTP argument, translated. A '
     'beneficiary’s WTP is measured in their willingness to participate, travel for, or prioritize a '
     'program over competing uses of their scarce time.'),
    ('WTS applies directly to volunteers and mission-driven staff,', 'who frequently accept lower pay '
     'in exchange for meaning, impact, and alignment with values — a real and measurable WTS discount '
     'that mission-driven organizations depend on and should not take for granted or exploit '
     'indefinitely (Chapter 16’s ethical-influence line applies here with real force).'),
    ('The three levers still apply, translated:', 'raising "WTP" means demonstrating clearer, more '
     'credible impact per dollar donated; cutting real cost means genuine operational efficiency, not '
     'quietly reducing service to beneficiaries; lowering "WTS" means making mission-driven work '
     'itself more sustainable and less burnout-prone for the people delivering it.'),
    ('Trade-offs apply with, if anything, MORE force,', 'because mission-driven organizations face '
     'constant pressure to serve every possible need — the straddling failure mode, applied to a '
     'nonprofit’s program list instead of a firm’s product line, with the identical "fine" outcome '
     'and the identical fix: naming the actual driver of impact and funding it deliberately.'),
])
para(doc, 'The translation matters for anyone drafting a grant proposal, an annual appeal, or a board '
    'presentation: the language changes (impact, not margin; donors, not customers), but the '
    'underlying arithmetic — where does the value actually come from, and what does the honest cost '
    'of the status quo look like — survives the translation completely.')

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Run the three-lever test on three visible initiatives at your workplace, internship, or student '
    'organization. Which lever does each pull — or is at least one simply activity with no lever '
    'attached?',
    'Name a firm that is proudly bad at something. What does that visible weakness buy it on the '
    'drivers it actually competes on?',
    'Find the WTS lever in a job you have held: what single change would have made you willing to '
    'stay for less total compensation, and what would it plausibly have cost the employer to make '
    'that change?',
    'Take a real or imagined proposal and rewrite its opening paragraph in value language: name the '
    'lever, price the status quo, and show the breakeven arithmetic.',
    'Draw your own value stick for a target role: what sets your WTP ceiling, what sets your WTS '
    'floor, and which single skill would move your WTP furthest this year?',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Run the three-lever test on your university’s (or employer’s) most visible recent initiative. '
    'Which lever, if any, does it actually pull — and how would you know if it were pure activity '
    'instead?',
    'Value-based strategy argues that widening the stick beats fighting over a fixed one. Construct '
    'the strongest counterargument: when IS fighting over a fixed stick the rational strategic choice?',
    'The chapter argues that soft initiatives (mentoring, flexibility) are hard strategy once framed '
    'in WTS language. Where does this framing risk reducing genuine care for employees to pure '
    'instrumental calculation — and does that risk matter if the outcomes are the same?',
    'Compare the regional lab case to a real-world example you know of a company straddling multiple '
    'value drivers. What would a genuine trade-off decision look like for that company?',
    'Draw your own value stick for your intended career path five years out. Which lever do you '
    'expect to be pulling primarily, and what does that imply about the skills worth prioritizing now?',
])

keyterms(doc, [
    ('Value stick', 'the four-point model — willingness to pay, price, cost, willingness to sell — '
     'that locates customer delight, firm margin, and supplier/employee surplus as slices of one '
     'created-value total.'),
    ('Willingness to pay (WTP)', 'the maximum a customer would ever pay before walking away — set '
     'entirely by the value they receive, not by the price charged.'),
    ('Willingness to sell (WTS)', 'the minimum a supplier or employee would accept and still say yes '
     '— set by how good the arrangement genuinely feels, and the framework’s most neglected lever.'),
    ('Value created versus captured', 'the distinction between widening the stick (creating value, '
     'positive-sum) and merely shifting where it splits (capturing value, zero-sum) — durable '
     'strategy requires both, in that order.'),
    ('The three levers', 'raise WTP, cut real cost, or lower WTS — the only three ways an initiative '
     'can genuinely create value; moving price alone captures without creating.'),
    ('Complements and substitutes', 'products that raise (complements) or cap (substitutes) a '
     'product’s own WTP — explaining why firms subsidize complements and must account for substitutes '
     'honestly.'),
    ('Near-customers', 'people who value a product but do not buy, blocked by price or friction — '
     'often the cheapest source of growth once identified.'),
    ('Trade-offs versus straddling', 'strategy as deliberately choosing which value drivers to '
     'compete on and accepting weakness elsewhere, versus chasing every driver into an averaged, '
     'forgettable "fine."'),
    ('Revealed strategy', 'what an organization’s funding and promotion patterns actually show, as '
     'distinct from its stated mission — the version that determines which proposals get funded.'),
    ('Value language (in proposals)', 'naming the specific lever a proposal pulls, pricing the cost '
     'of the status quo, and showing breakeven arithmetic — the upgrade that converts a sincere ask '
     'into a fundable one.'),
])

quiz(doc, [
    ('On the value stick, "value created" is defined as:',
     ['Price minus cost', 'Willingness to pay minus willingness to sell', 'Revenue minus expenses', 'Cost minus willingness to sell']),
    ('A firm that captures value without creating any (e.g., a pure price increase with no change in '
     'delivered quality) will eventually:',
     ['Sustain profits indefinitely', 'See the effect erode as customers notice and the stick fails to widen', 'Automatically raise WTS', 'Improve its cost structure']),
    ('The three genuine value-creating levers are:',
     ['Price, cost, and marketing', 'Raise WTP, cut real cost, lower WTS', 'Revenue, profit, and market share', 'Advertising, sales, and distribution']),
    ('Lowering employee WTS means:',
     ['Paying employees less', 'Making work genuinely better so people accept less total compensation to stay',
      'Reducing headcount', 'Increasing required work hours']),
    ('"Straddling" in strategy refers to:',
     ['Diversifying into multiple industries', 'Chasing every value driver at once, averaging the proposition into "fine"',
      'Merging with a competitor', 'Focusing only on cost leadership']),
    ('The test for whether a genuine strategy has been made is:',
     ['Revenue grows year over year', 'The strategy tells you what to STOP doing', 'A mission statement exists', 'Competitors react to it']),
    ('A proposal written in "value language" should, above all:',
     ['Use as many financial terms as possible', 'Name the specific lever it pulls and price the status quo',
      'Avoid mentioning cost entirely', 'Claim to move all three levers at once']),
    ('The "two proposals" case study shows that Proposal A was rejected because:',
     ['The training program itself was flawed', 'It never translated its ask into a lever leadership could evaluate, unlike Proposal B',
      'It requested too little money', 'Leadership opposed employee training on principle']),
    ('Complements raise a product’s WTP because:',
     ['They are always cheaper to produce', 'They make the original product more valuable to use, which is why firms often subsidize them',
      'They replace the need for the original product', 'They are required by regulation']),
    ('Applying the value stick to one’s own career, the chapter argues that career strategy should '
     'prioritize:',
     ['Maximizing current salary above all else', 'Roles that raise future WTP (skills, evidence, network) even at equal current pay',
      'Staying in one role as long as possible', 'Minimizing employer willingness to sell']),
], ['b','b','b','b','b','b','b','b','b','b'])

references(doc, [
    'Besanko, D., Dranove, D., Shanley, M., & Schaefer, S. (2017). Economics of strategy (7th ed.). Wiley.',
    'Brandenburger, A. M., & Stuart, H. W. (1996). Value-based business strategy. Journal of '
    'Economics & Management Strategy, 5(1), 5–24.',
    'Ghemawat, P., & Rivkin, J. W. (2006). Creating competitive advantage. Harvard Business School '
    'background note.',
    'Oberholzer-Gee, F. (2021). Better, simpler strategy: A value-based guide to exceptional '
    'performance. Harvard Business Review Press.',
    'Porter, M. E. (1996). What is strategy? Harvard Business Review, 74(6), 61–78.',
    'Porter, M. E. (1985). Competitive advantage: Creating and sustaining superior performance. Free Press.',
])

h1(doc, 'Closing')
para(doc, 'Seventeen chapters, one course, one repeated finding: the value of what you know, what you '
    'have built, and what you have done is realized only through the communication of it — clearly, '
    'honestly, and in the language of whoever needs to fund, hire, follow, or believe it. Write '
    'accordingly, for the rest of a career this course was built to serve.')
para(doc, 'Keep the practice sets, the study guides, and the decks after the term ends. None of it '
    'was built to expire with a final grade — a career runs far longer than a semester, and the '
    'documents you will need to write for it, from the first cover letter to the strategy memo that '
    'gets a real initiative funded, are exactly the ones this course rehearsed.')
para(doc, 'Good luck. Write well, verify what you claim, treat people the way this course has '
    'described, and know exactly which lever your work is pulling before you ask anyone to fund it.')
para(doc, 'And when you eventually find yourself training someone newer than you — a junior '
    'colleague, an intern, a direct report — pass along what turned out to matter most from this '
    'course, in whatever words fit the moment. Not the terminology, which will drift and update long '
    'after this specific edition is out of print, but the underlying habit: that clear, honest, '
    'well-aimed communication is not a soft skill layered on top of the real work. For nearly '
    'everyone in nearly every organization, it is a very large part of the real work itself.')

out = os.path.join(os.path.dirname(__file__), '..', 'ch17-study-guide.docx')
finish(doc, os.path.abspath(out))
