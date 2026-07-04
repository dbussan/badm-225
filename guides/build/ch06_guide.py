# Chapter 6 Study Guide — Positive and Neutral Messages
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(6, 'Positive and Neutral Messages',
    'Requests, replies, claims, adjustments, and goodwill — the everyday mail that quietly builds your reputation.')

h1(doc, 'How to use this guide')
para(doc, 'This chapter covers the messages you will send most and think about least: asking for '
    'things, answering people, granting requests, fixing problems, and saying thank you. None of them '
    'is hard, which is exactly why they are diagnostic — everyone can see whether yours are good. '
    'Read with the direct strategy from Chapter 3 in hand; every pattern here is a variation on it.')

h1(doc, 'The direct request: asking so people can say yes')
figure(doc, os.path.join(FIG, 'ch6_request.png'),
    'Figure 1. The direct request pattern: ask, explain, detail, close with a date.',
    'Direct request pattern in four steps: open with the ask, explain briefly why and why this person, detail what is needed as a scannable list, and close with a date and goodwill.')
para(doc, 'Requests fail two ways: the buried ask (three paragraphs of context before the reader '
    'learns what is wanted — Chapter 3’s buried lead in request costume) and the incomplete ask '
    '(the reader must reply with questions before they can comply). The pattern in Figure 1 prevents '
    'both. Open with the ask in question form — questions politely demand answers in a way '
    'statements do not. Explain briefly why, and why them: “you ran last year’s audit” tells the '
    'reader they are chosen, not spammed. Detail what compliance requires — format, scope, access '
    '— as a list they can work down. Close with the deadline and its reason. A request that can be '
    'satisfied without a single clarifying question is a professional artifact; count yours.')

h1(doc, 'Replies: answer first, then anticipate')
figure(doc, os.path.join(FIG, 'ch6_reply.png'),
    'Figure 2. The reply skeleton: answer first, details next, extras they did not ask for, forward close.',
    'Reply skeleton: answer first (yes, the room is yours Friday 2–4), then details they will ask next such as access and setup, then extras they did not ask about but need such as the projector code, then a forward-looking close.')
para(doc, 'When someone asks a yes/no question, the first word of your reply should be yes or no — '
    'everything before it is suspense nobody ordered. After the answer, anticipate: what will they '
    'ask next? Answer it now, in the same message, and you have saved a round trip (the '
    'answerable-asynchronously rule from Chapter 1 in action). The bar to clear: your reply should '
    'end the thread, not extend it. And when the answer is partly no — you can have the room but '
    'not the projector — lead with the yes you can give: “The room is yours; the projector is '
    'booked, but here are two options.” That is not spin; it is Chapter 2’s positive framing doing '
    'honest work.')

h1(doc, 'Claims: complaining like a professional')
figure(doc, os.path.join(FIG, 'ch6_claim.png'),
    'Figure 3. Claim anatomy: the record, the problem, the remedy, the deadline — delivered calm.',
    'Claim message anatomy: what and when (order numbers, dates, the verifiable record), what went wrong (facts stated calmly with evidence attached), what you want (the specific remedy such as refund, replacement, or repair), and by when, with a tone of confidence in resolution.')
para(doc, 'A claim is a request wearing a grievance, and the request part is what gets results. The '
    'anatomy: open with the verifiable record (order number, date, product — the reader must be '
    'able to find you in their system from sentence one); state what went wrong in facts, with '
    'evidence attached; name the specific remedy you want — sellers grant specific requests and '
    'stall vague unhappiness; close with a reasonable deadline and confident courtesy. The tone '
    'discipline matters most: anger feels powerful and reads as noise. The customer-service '
    'representative reading your claim did not break your product — make it easy for them to become '
    'your advocate. Confidence (“I’m sure you’ll want to make this right”) recruits; sarcasm '
    'entrenches.')

h1(doc, 'Adjustments: granting claims so the customer stays')
figure(doc, os.path.join(FIG, 'ch6_adjust.png'),
    'Figure 4. The adjustment grant: lead with the fix, explain without excuses, repair confidence, restore the relationship.',
    'Adjustment message flow: grant immediately (a replacement ships today, free), explain what went wrong briefly and without blame, repair confidence by naming what prevents a repeat, and restore the relationship with a forward-looking close and no groveling.')
para(doc, 'When you are granting a claim, the news is good — so the message is direct: the grant in '
    'sentence one. Delay it and the customer reads your explanation as the wind-up to a refusal, '
    'experiencing thirty seconds of manufactured dread you then bill as service. After the grant: '
    'explain what happened briefly and without the blame opera (customers want competence, not '
    'someone punished), say what prevents a repeat — this is the sentence that actually restores '
    'confidence — and close forward, without groveling. Over-apology (“we deeply regret the '
    'unacceptable failure…”) keeps the spotlight on the failure; the confident version keeps it on '
    'the fix. Research on reciprocity explains why generous adjustments pay: people repay treatment '
    'in kind, and a customer rescued gracefully often becomes more loyal than one never '
    'disappointed (Cialdini, 2021).')

h1(doc, 'Goodwill messages: the highest-return mail you will ever send')
figure(doc, os.path.join(FIG, 'ch6_5s.png'),
    'Figure 5. The five-S test for goodwill messages: specific, sincere, short, spontaneous, selfless.',
    'Five S test for goodwill messages: specific (names the exact act and its effect), sincere (no flattery or smuggled agenda), short (five sentences beat five paragraphs), spontaneous (sent promptly, not at review season), selfless (about them, with no reply requested).')
para(doc, 'Thanks, congratulations, and sympathy are the messages nobody requires and everybody '
    'remembers. The five-S test keeps them potent. Specific: “your triage of Saturday’s outage saved '
    'the launch” — the named act is the proof you actually noticed (the appreciation-versus-flattery '
    'line from Chapter 16). Sincere: no agenda in the envelope; a thank-you that pivots to a favor '
    'was an invoice all along. Short, spontaneous, selfless complete the set. Two notes on the hard '
    'one: sympathy. Send it — silence from colleagues wounds more than clumsy words ever could; keep '
    'it brief, warm, and unhurried (“no reply needed”); and handwrite it if the relationship '
    'warrants, because in a digital century, ink is the costly signal. This is also the one message '
    'category AI should never draft (Chapter 15): the entire content is that a human paused.')
figure(doc, os.path.join(FIG, 'ch6_capital.png'),
    'Figure 6. Goodwill capital compounds: small deposits, made promptly, for years.',
    'Rising curve of goodwill capital over time: a thank-you, a congratulations note, credit given publicly, a favor before any ask, the unrequested reference, and finally the door that opens itself.')
para(doc, 'Organizational research finds that habitual givers — people who help, credit, and thank '
    'without keeping score — end up disproportionately represented at the top of success '
    'distributions, provided they pair generosity with boundaries (Grant, 2013). Goodwill messages '
    'are the five-minute version of that strategy: deposits in Chapter 16’s influence account, made '
    'before any withdrawal is imagined.')

h1(doc, 'Instructions: messages people can follow with their hands')
figure(doc, os.path.join(FIG, 'ch6_steps.png'),
    'Figure 7. Instructions that work: one step per line, preconditions first, checkpoints after key steps, warnings before the step they protect.',
    'Instruction-writing pattern: one step, one action, one line, numbered with imperative verbs first; preconditions listed before step one; results after key steps as confirmation checkpoints; warnings placed before the step they protect, never after.')
para(doc, 'Instructional messages — how to submit the expense report, how to book the lab — are '
    'judged by a brutal metric: the support questions they generate. The craft: number the steps and '
    'start each with an imperative verb (“Click… Enter… Save…”); one action per step, because two '
    'actions in one line is where readers fall off; list preconditions before step one (the VPN '
    'password needed at step six is a landmine if discovered at step six); insert checkpoints '
    '(“you’ll see a green banner”) so readers know they are still on the path; and place warnings '
    'before the step they protect — a caution after the damage line is an autopsy. Test on one real '
    'novice before shipping to fifty; their first confusion is your revision list.')

h1(doc, 'Deep dive: requests upward, downward, and sideways')
para(doc, 'The direct request pattern is universal; its calibration is directional. Upward requests '
    '(to managers, sponsors, senior stakeholders) compress everything: the ask and its '
    'decision-relevant context must survive a phone-screen skim, options beat open questions '
    '(“A or B?” outperforms “what should we do?” — you are buying a decision, so package it for '
    'purchase), and the cost of what you are asking should arrive pre-counted (“needs two hours of '
    'Dana’s week through March”). Downward requests carry authority whether you invoke it or not, '
    'which is exactly why Chapter 16’s ask-don’t-order discipline matters most here: the request '
    'that preserves choice recruits judgment, while the order recruits compliance — and you want '
    'the judgment. Explain the why even when you could skip it (“the client moved the audit, so I '
    'need the logs Thursday instead of Monday”): people execute reasons better than instructions, '
    'and the habit compounds into a team that can act without you. Sideways requests — peers who '
    'owe you nothing — run entirely on the account balance from the goodwill section: lead with '
    'acknowledgment of the imposition (“I know month-end is your crunch”), size the ask precisely '
    'so it can be evaluated (“about twenty minutes, before Friday”), and make returning the favor '
    'easy to invoke. The pattern is identical in all three directions; what changes is which line '
    'carries the persuasive weight.')

h1(doc, 'Deep dive: the request stack — sequencing multiple asks')
para(doc, 'One message, one job — but real work sometimes requires several related asks of one '
    'person. The stack disciplines: never bury asks in prose where they compete for survival; '
    'number them, each with its own deadline, so the reply can address them by number (“1: done; '
    '2: Thursday; 3: need to check”); order by deadline, not importance, unless one ask blocks the '
    'others — then lead with the blocker and say so (“#1 gates the rest”); and cap the stack at '
    'three, because the fourth ask converts a request into a workload negotiation that deserves a '
    'conversation instead. If the asks serve different purposes (one needs action, one needs '
    'information, one needs a decision), label them so: “Decision needed: … / FYI only: … / '
    'Action requested: …” — the reader triages instantly, and nothing dies of ambiguity. The '
    'anti-pattern to retire: the paragraph containing three implicit asks, none marked, followed '
    'six days later by “per my last email…” — the fossil that blames the reader for the '
    'writer’s buried cargo.')

h1(doc, 'Research corner: why granting well beats never failing')
para(doc, 'The counterintuitive finding behind adjustment strategy is that well-recovered failures '
    'can leave customers more loyal than uninterrupted service — the recovery demonstrates the '
    'relationship’s value in a way routine transactions never test. The mechanism is reciprocity, '
    'among the most robust findings in influence research: humans feel obligated to return good '
    'treatment, and a generous, fast, unbegrudging fix is good treatment delivered at the moment of '
    'maximum attention (Cialdini, 2021). The practical rules it generates: err generous on '
    'borderline claims (the margin on one order is smaller than the value of the relationship); '
    'grant fast, because speed is read as sincerity; and never make the customer litigate — a grant '
    'delivered grudgingly (“as a one-time courtesy, although our records show…”) spends the money '
    'and forfeits the credit.')

h1(doc, 'Deep dive: confirmations — the message that prevents the dispute')
para(doc, 'The confirmation is the positive message most often skipped, because at sending time it '
    'feels redundant — everyone was there, everyone agreed, why write it down? Chapter 5 gave the '
    'template; this chapter supplies the genre’s full logic. A confirmation converts a fragile '
    'shared memory into a durable shared artifact, and its three properties do the work: it is '
    'numbered (three points, addressable by number in any future discussion), it is complete '
    '(dates, amounts, owners — the future reader has no context, per the record-purpose rules '
    'from Chapter 2), and it is self-ratifying (“corrections welcome — otherwise this stands as '
    'our plan” converts silence into agreement, gently and legitimately). Send it the same day '
    'while memories still match; a confirmation sent Friday for Monday’s call invites the very '
    'divergence it exists to prevent. And notice the relationship effect, which is why this genre '
    'belongs in the goodwill chapter: consistent confirmers are experienced as trustworthy rather '
    'than bureaucratic, because the confirmation protects BOTH parties — the colleague who '
    'benefits from your record the first time a dispute dissolves against it becomes its second '
    'adopter. Institutional memory is built by exactly this habit, one same-day message at a '
    'time.')

h1(doc, 'Deep dive: the reference pair — asking for one, writing one')
para(doc, 'Two connected genres every professional faces from both sides. Asking for a '
    'recommendation or reference is a direct request with elevated stakes and one governing '
    'kindness: make the yes easy and the no graceful. The craft: ask early (three weeks minimum '
    '— a rushed reference is a weak reference); ask with an escape hatch (“if your schedule or '
    'familiarity with my work makes this a bad fit, no explanation needed” — a lukewarm reference '
    'hurts more than none, so you WANT the graceful exit used); and arm the writer — attach the '
    'posting, your resume, and three bullet reminders of specific shared work (“the Q3 validation '
    'project where we cut turnaround 40%”). You are not flattering yourself; you are doing their '
    'prewriting, and every recommender alive is grateful for it.')
para(doc, 'Writing one reverses the seat. Say yes only when you can write specifics — the '
    'five-S logic applies: a recommendation made of adjectives (“hardworking, reliable, a '
    'pleasure”) is read by every experienced recipient as polite noise, while one concrete story '
    '(“when the calibration drift appeared mid-audit, she caught it, retraced two weeks of logs, '
    'and presented the correction to the assessor herself”) outweighs a page of praise. Structure: '
    'your relationship and its duration (the credibility line), two or three specific '
    'accomplishments with visible stakes, one honest dimension of growth if the context permits '
    'candor (it strengthens everything else), and an unambiguous bottom line (“I would hire her '
    'again without hesitation” — hedged closings are read at full volume). Decline gracefully '
    'when you cannot clear that bar: “I don’t think I’m the strongest reference for this '
    'particular role — you deserve someone who has seen that side of your work” is a kindness '
    'wearing a refusal (Chapter 7’s craft, deployed for the requester’s own good).',
    bold_lead='The writing seat.')

h1(doc, 'Deep dive: announcements — informing at scale without spin')
para(doc, 'The announcement is a positive/neutral genre with a built-in temptation: because it '
    'goes to everyone, it gets written for no one, and because it represents the institution, it '
    'drifts toward promotion. The disciplines: lead with the reader’s operative fact, not the '
    'institution’s pride (“Starting March 1, submit expenses in Concur” beats “We are excited to '
    'announce our digital transformation journey continues”); put what-changes-for-you above '
    'how-we-got-here (the history paragraph, if it survives at all, goes last); answer the three '
    'questions every announcement reader asks — what changed, when, what must I do — in the '
    'first three sentences, visibly; and anticipate the anxious stakeholder (Chapter 2): if the '
    'announcement touches jobs, money, or workload, address the personal-impact question '
    'explicitly, because “what does this mean for me?” unanswered becomes the grapevine’s opening '
    'act (the wellness-memo case, permanently on file). Two operational habits: give every '
    'announcement a single named owner for questions (“questions → Dana Reyes,” not '
    '“contact the team”), and archive announcements where future searchers will look — the '
    'announcement that cannot be found six months later generates the exact confusion it existed '
    'to prevent.')

h1(doc, 'Deep dive: the shared-fault claim')
para(doc, 'Chapter 6’s claim anatomy assumes clean hands; reality is often messier — the '
    'equipment was mishandled AND the packaging was inadequate; the deadline was missed partly '
    'because your specs arrived late. Claims with shared fault require one addition and one '
    'discipline. The addition: acknowledge your share first, briefly and specifically (“our team '
    'stored the unit outside the recommended range for two days before discovering the fault”), '
    'because the reader’s file has your fingerprints in it anyway and preemption converts a '
    'gotcha into a credibility deposit (Chapter 8’s two-sided logic in claim form). The '
    'discipline: keep the remedy request proportionate to THEIR share — asking for full '
    'replacement when you contributed to the failure invites the itemized rebuttal; asking for '
    'the repair at cost, or the split, signals the fairness that makes a yes easy. The same '
    'geometry governs responses to shared-fault claims from the other side: grant your share '
    'fully and immediately, name the customer’s contribution once and without relish, and let '
    'the prevention sentence cover both parties’ next time (“the updated handling card ships '
    'with every unit — and we’ve reinforced the housing”). Shared fault handled cleanly often '
    'builds MORE trust than clean-hands cases, because both sides watched each other be fair '
    'under ambiguity — which is the only condition where fairness is informative.')

h1(doc, 'Worked examples: four everyday messages, done properly')
h2(doc, '1. The complete request')
para(doc, '“Could you send me the Q2 vendor performance report by Thursday noon? I’m compiling the '
    'renewal recommendation (due Friday) and yours is the last dataset. What I need: the summary '
    'tab as PDF plus the raw sheet — same format as Q1. Thursday noon keeps the review on '
    'schedule; thank you!” Ask, why-and-why-them, detail, dated close: nothing to clarify, easy to '
    'grant.')
h2(doc, '2. The reply that ends the thread')
para(doc, '“Yes — the conference room is yours Friday 2:00–4:00. Details: your badge opens it from '
    '1:30; the projector code is 4417; capacity is 14. You didn’t ask, but parking validation is at '
    'the front desk if your clients drive. Anything else before Friday, just ask.” Answer first, '
    'anticipations included, thread closed.')
h2(doc, '3. The adjustment grant')
para(doc, '“A replacement unit ships today by expedited freight, at no charge — you’ll have it '
    'Wednesday. The damage happened in transit; we’ve switched your account to the reinforced '
    'packaging we use for lab equipment so this doesn’t recur. Thanks for the clear photos, which '
    'made this fast. We appreciate the chance to make it right.” Grant, cause without opera, '
    'prevention, forward close.')
h2(doc, '4. The confirmation after a verbal agreement')
para(doc, '“Confirming our hallway conversation: (1) I’ll draft the SOP revision by Wednesday; '
    '(2) you’ll route it to QA the same day; (3) we present jointly at the safety meeting on the '
    '19th. Corrections welcome — otherwise this is our plan.” Thirty seconds after any decision '
    'made aloud; the hallway evaporates, the record remains.')
h2(doc, '5. The order acknowledgment that prevents the ticket')
para(doc, '“Order 4471 confirmed: one Beckman Coulter Allegra X-30R, $28,570 installed, delivery '
    'week of Aug 11 (exact date confirmed 48 hours ahead). To change anything before Aug 1, reply '
    'here; after Aug 1, call Dana Reyes at 555-0114. Your quote and warranty terms are attached '
    'for your records.” Every follow-up question answered before it forms.')
h2(doc, '6. The goodwill note that costs five minutes')
para(doc, '“Dana — your catch on the calibration drift saved us a failed audit finding; the '
    'assessor specifically noted the logs were clean. I’ve told Dr. Reyes the same. Thank you.” '
    'Specific act, named effect, credit passed upward, no agenda. Five sentences would have been '
    'fine; three are better.')

h1(doc, 'Case study 1: the refund that built a customer')
para(doc, 'A small analytical-instruments supplier ships a $1,900 pH-meter kit to a university lab; '
    'it arrives with a cracked electrode housing. The lab manager emails a textbook claim (record, '
    'photos, specific remedy: replacement by month-end, before a teaching practicum). The supplier’s '
    'first-draft reply, written by a new hire, opens: “While our packaging meets industry standards '
    'and damage of this kind is typically carrier-caused, we are willing on this occasion to…” The '
    'sales director intercepts it and rewrites: replacement ships same day with a loaner electrode '
    'included, packaging upgraded for the account, a thanks for the photos, and one forward '
    'sentence about the practicum. Cost of the intercept: about $60 in freight. Eighteen months '
    'later the lab has standardized on the supplier for three courses, citing “how they handle '
    'problems” in the department’s vendor review.')
numbered(doc, [
    'Diagram both drafts against Figure 4. Where does the first draft violate each stage?',
    '“While our packaging meets industry standards…” — what is this sentence doing, who is it for, and what does the customer hear?',
    'The rewrite added a loaner and upgraded packaging unprompted. Using reciprocity (Cialdini, 2021), explain the economics.',
    'Draft the same grant for a case where the customer is partly at fault — what changes, and what must not?',
])
h2(doc, 'Case analysis')
para(doc, 'The first draft is a refusal’s skeleton wearing a grant’s conclusion: it opens by '
    'defending the company (an audience-of-one message — the writer’s own anxiety), implies the '
    'customer’s claim is dubious (“on this occasion”), and buries the yes where the dread has '
    'already done its damage. The rewrite is Figure 4 executed: the grant leads, the cause is one '
    'clause, the prevention sentence (“upgraded packaging for your account”) does the confidence '
    'repair, and the practicum sentence proves a human read the claim. The $60 arithmetic is the '
    'whole strategy: the supplier bought, at freight cost, an outcome no marketing spend reliably '
    'produces — a customer who retells the story. When the customer is partly at fault, the grant '
    'can shrink (repair at cost, say) but the tone rules hold absolutely: no litigating the past, '
    'and the prevention sentence becomes a shared one — “here’s a setup step that protects the '
    'housing” — which teaches without indicting.')

h1(doc, 'Case study 2: the instructions that generated forty tickets')
para(doc, 'Facilities emails all staff: “We are pleased to announce the rollout of the new visitor '
    'management system. Visitors must now be pre-registered via the portal accessible through the '
    'intranet under Services, after which a QR code will be generated for the visitor which should '
    'be presented at the kiosk, though for visitors arriving by vehicle the parking module must '
    'first be completed, noting that international visitors require the extended form, and hosts '
    'should allow additional time accordingly.” Within a week the help desk logs forty tickets, '
    'three VIP visitors are stranded in the lobby, and Facilities sends a follow-up beginning “To '
    'clarify our previous communication…”')
numbered(doc, [
    'Count the actions hiding in the announcement’s single sentence. What does Figure 7 say each needed?',
    'Identify the three distinct audiences with three different paths (standard visitor, vehicle, international). How should the message have handled them?',
    'Rewrite the announcement: subject line, one-line purpose, then the numbered procedure(s). Where do the preconditions and the warning about extra time belong?',
    'What testing step would have caught all forty tickets before they existed?',
])
h2(doc, 'Case analysis')
para(doc, 'One 68-word sentence contains five actions, two branches, and a warning — each of which '
    'Figure 7 assigns its own numbered line. The rewrite: subject “Registering visitors — new '
    'required steps (2 minutes)”; purpose line; then a numbered path for the standard case (1. Open '
    'Services → Visitor Portal. 2. Enter the visitor’s name and date — you’ll see a QR code '
    'generate. 3. Forward the code; they scan it at the kiosk), with the branches as labeled '
    'variants (“Arriving by car? Complete the parking module first — before step 1” — the warning '
    'placed before the step it protects) and the international form flagged with its time cost up '
    'front. The testing step is Figure 7’s last line: one real novice — any staff member outside '
    'Facilities — walking the instructions cold would have hit the parking landmine and the buried '
    'QR-forward step in the first five minutes. Forty tickets are what “test on one novice” costs '
    'when skipped.')

h1(doc, 'Deep dive: goodwill across the org chart')
para(doc, 'The five-S test is universal; the deployment is positional. Thanks upward is the '
    'trickiest register — it must never scan as flattery, which means the specific-and-true bar '
    'rises: thank managers for particular decisions and their concrete effects (“the deadline '
    'extension let us re-run the failed batch — the client got clean data”), never for qualities '
    '(“your great leadership”). Credit upward, meanwhile, is the professional’s quiet art: when '
    'your manager’s suggestion worked, saying so in the room where it matters (“this was Dana’s '
    'catch”) costs nothing and is remembered disproportionately. Thanks downward and sideways is '
    'the highest-yield deployment and chronically undersupplied — the analyst who stays late, the '
    'peer who covered the demo; these are the notes that get kept in desk drawers. Public versus '
    'private is its own calibration: praise publicly when the achievement is public-safe and the '
    'person tolerates spotlight (some genuinely don’t — ask once, remember forever); correct '
    'privately, always (Chapter 16). And the register nobody teaches: thanks to the invisible — '
    'the coordinator, the technician, the person whose name is on no slide. Consistent, specific '
    'gratitude to people who can do nothing for your career is, besides being decent, the single '
    'most-watched behavior in any workplace: colleagues who see it extend you trust on credit. '
    'The receptionist test from your instructor’s book applies to email exactly as it applies to '
    'lobbies.')

h1(doc, 'Deep dive: form responses that don’t feel like forms')
para(doc, 'Recurring requests deserve template responses — and templates deserve engineering, '
    'because a response that FEELS templated subtracts the goodwill it was built to deliver. The '
    'craft: write the skeleton once, at your best (the complete answer, the anticipations, the '
    'forward close), then personalize three points per use — the name (verified, Chapter 4), one '
    'sentence that proves you read THEIR message (“since your cohort starts in March, the timing '
    'works”), and the closing line. Sixty seconds of personalization on a five-minute template '
    'beats both alternatives: the fully-artisanal reply (unsustainable at volume) and the naked '
    'boilerplate (readable as such from orbit, especially when it answers questions the sender '
    'didn’t ask while missing the one they did — the tell of every unread-message template). '
    'Maintain the fleet like code: when a template generates the same follow-up question twice, '
    'the template has a bug; fix it at the source. And never template the untemplatable: '
    'condolences, apologies, and anything Chapter 6’s five-S test governs — the entire value of '
    'those messages is that they could not have been reused.')

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Adam Grant, “Are you a giver or a taker?” (TED).', 'The research behind goodwill capital — and why givers with boundaries finish first (Grant, 2013).'),
    ('Laura Trice, “Remember to say thank you” (TED).', 'Three minutes on why people secretly need the praise they never request — the case for sending the note you keep drafting mentally.'),
    ('Drew Dudley, “Everyday leadership” (TED).', 'The “lollipop moment”: the outsized impact of small acknowledgments — this chapter’s thesis in a story.'),
])

h1(doc, 'Deep dive: the everyday message and AI — where drafting help belongs')
para(doc, 'This chapter’s genres are the safest territory in the book for AI-assisted drafting — '
    'and the clearest illustration of its boundaries. Requests, replies, confirmations, '
    'announcements, and transactional mail are structural genres: an assistant given the pattern '
    'and the facts drafts them competently, and the templates appendix above works beautifully as '
    'a prompt library (“draft a reference request using this structure, with these three '
    'accomplishments”). The verification load stays yours (Chapter 15): every name, date, figure, '
    'and commitment in an AI draft gets checked against sources, because fluent wrongness is the '
    'failure mode — the draft that confidently promises Wednesday delivery nobody offered. The '
    'personalization stays yours too: the one sentence proving you read THEIR message is exactly '
    'what generic drafting cannot supply, and its absence is what makes AI-scented mail feel like '
    'AI-scented mail. And the exclusion zone stands absolute: sympathy, personal congratulations, '
    'apologies — the five-S genres where the entire payload is that a human paused. The clean '
    'division: let tools accelerate the structural genres so you can spend the recovered minutes '
    'on the human ones. That trade — machine speed purchasing human presence — is this whole '
    'course’s AI position in a single sentence.')

h1(doc, 'Deep dive: saying yes well — the underrated art')
para(doc, 'Chapter 7 will spend twenty pages on saying no; saying yes deserves at least one, '
    'because a yes can be delivered so poorly it functions as a debit. The grudging yes (“fine, I '
    'suppose I can squeeze it in”) grants the favor and forfeits the credit — the adjustment-'
    'letter mistake at conversational scale; if you are going to spend the time anyway, deliver '
    'the yes with both hands (“glad to — the timing actually works”). The vague yes (“sure, at '
    'some point this week”) obligates you while informing no one; a yes is only complete when it '
    'carries the same specifics a good ask does — what, by when, at what scope (“yes: summary '
    'tab plus raw sheet, Thursday noon”). The overloaded yes — agreeing beyond your actual '
    'capacity — is the most dangerous species, because it converts today’s goodwill into next '
    'week’s missed deadline plus a Chapter 7 conversation; the partial yes exists precisely for '
    'this (“I can do the analysis but not the deck — does that still help?”), and colleagues '
    'trust the person whose yes means yes far more than the person whose yes means probably. '
    'Finally, the yes with visible cost: when granting something genuinely expensive, letting the '
    'cost be quietly visible — not performed, just honest (“I’ll move my Thursday block to fit '
    'this”) — prices the favor accurately and keeps the reciprocity ledger truthful. Say yes the '
    'way this chapter says everything else: first, specifically, and on time.')

h1(doc, 'Deep dive: timing — when positive messages land hardest')
para(doc, 'Content and structure decided, one variable remains: when. Positive-message timing has '
    'its own physics. Speed multiplies goodwill — the congratulations sent within hours of the '
    'announcement participates in the moment; the same note three weeks later is an apology '
    'wearing a compliment (five-S’s “spontaneous,” given a clock). Grants accelerate for the same '
    'reason: an adjustment approved in one day reads as conviction; the identical grant after '
    'eleven days of silence reads as reluctant surrender — speed IS part of the message '
    '(reciprocity research consistently finds promptness read as sincerity; Cialdini, 2021). '
    'Requests, inversely, respect the reader’s calendar: the complete-ask sent during their '
    'month-end close, however perfect, arrives as a burden — where timing is free, spend it '
    '(Tuesday morning beats Friday 4 p.m. for anything needing thought). Two calendar habits '
    'formalize the advantage: a beat sheet of your recurring goodwill occasions (work '
    'anniversaries, project completions, the audit your colleague dreads annually), and the '
    'two-minute Friday scan for the week’s unmarked wins — the promotion buried in a memo, the '
    'defense passed, the first client call survived. The professionals people describe as '
    '“thoughtful” are mostly just people with a system; the thought is real, but the system is '
    'what delivers it on time.')

h1(doc, 'Deep dive: transactional mail — orders, receipts, and the automated voice')
para(doc, 'A last positive-message species runs mostly on rails: order confirmations, shipping '
    'notices, appointment reminders, payment receipts. Most are automated — and someone writes '
    'the automation, which makes this a writing genre with a hidden author: possibly you. The '
    'principles compress everything in this chapter to system scale. Completeness: the '
    'confirmation that answers every follow-up question (what, when, how much, how to change it, '
    'who to contact) prevents thousands of support tickets — the complete-ask test, inverted and '
    'multiplied. Findability: transactional messages get retrieved months later; subject lines '
    'carry order numbers and dates (Chapter 5’s search rules, at volume). Tone: even automated '
    'mail has a register — “Your order shipped!” and “SHIPMENT NOTIFICATION #4471-B” describe '
    'the same event in two company voices; choose one deliberately, then hold it everywhere. And '
    'the human handoff: the automated message’s most important line is the one that says how to '
    'reach a person when the rails fail — burying it is the corporate equivalent of the '
    'unfindable no. When you inherit responsibility for transactional messaging — and in a small '
    'organization, everyone eventually does — audit it against these four; the fixes are '
    'one-time and the returns are permanent.')

h1(doc, 'Put it to work this week')
numbered(doc, [
    'Send one request built to the complete-ask standard and count the clarifying questions it generates. Zero is the score to beat.',
    'Answer your next yes/no question with the answer as the first word. Notice the thread end.',
    'Send one five-S goodwill note — a real one, to a real person, today.',
    'Write the confirmation for the next thing your team decides aloud. Watch who starts relying on it.',
    'Draft — not necessarily send — the follow-up you have been avoiding, using the good-faith template. Notice what the tone rule changes.',
])

h1(doc, 'Deep dive: how routine mail is actually scored')
para(doc, 'Nobody grades your everyday messages — and everybody scores them. The scoring is '
    'implicit, cumulative, and category-based: colleagues unconsciously file you as someone whose '
    'requests are effortless or extractive, whose replies end threads or extend them, whose thanks '
    'mean something or nothing. Three properties of this ledger are worth knowing. It is '
    'asymmetric: one incomplete request costs more than three complete ones earn, because friction '
    'is remembered and smoothness is invisible — the tax of the everyday genres is that '
    'excellence merely avoids debits. It is transitive: your scores travel through the grapevine '
    'ahead of you (“just forward it to Dana, she actually answers”) — meaning your everyday mail '
    'is recruiting or repelling future collaborators you have never met. And it compounds at '
    'promotion time: when managers describe someone as “easy to work with” or “high-maintenance,” '
    'they are usually summarizing hundreds of routine messages, not any single event. This is the '
    'quiet answer to “why does a communication course spend a chapter on ordinary email”: the '
    'ordinary is where reputations are actually manufactured, keystroke by keystroke, while '
    'everyone’s attention is on the extraordinary.')

h1(doc, 'Deep dive: the follow-up — nudging without nagging')
para(doc, 'Every request writer eventually faces the silence, and the follow-up is its own '
    'positive-message genre with a narrow path between doormat and pest. The timing rule: follow '
    'up after the stated deadline passes, or after a week for undated asks — sooner reads as '
    'pressure, much later reads as your own indifference. The tone rule: assume good faith, '
    'always and explicitly — “resending in case this got buried” (Chapter 2’s playbook) '
    'attributes the silence to the inbox, not the person, and leaves every exit dignified. The '
    'content rule: make the second message EASIER to answer than the first — restate the ask in '
    'one line (never “see below,” which assigns homework), narrow it if possible (“even a yes/no '
    'on the date would unblock us”), and re-anchor the deadline with its reason. The arithmetic '
    'rule: two follow-ups, then change something — the channel (a thirty-second call resolves '
    'what three emails couldn’t), the ask (smaller), or the recipient (the escalation summary '
    'from Chapter 5, without heat: “flagging that this is now blocking the March validation — '
    'how should we route it?”). What never works: the guilt ledger (“as per my previous THREE '
    'emails”), which converts your legitimate claim on their attention into their legitimate '
    'grievance about your tone. Persistence is professional; scorekeeping is not.')

h1(doc, 'Deep dive: goodwill across cultures')
para(doc, 'The five-S test is universal; its execution crosses Hall’s continuum (Chapter 1) with '
    'predictable adjustments. In high-context settings, goodwill messages carry MORE relational '
    'weight and less optional character — the congratulations skipped, the holiday greeting '
    'unsent, the thanks unwritten register as statements, not omissions; build the calendar '
    'awareness (local holidays, naming conventions, gift-and-greeting norms) that lets you '
    'participate correctly. Formality floors differ: the first-name warmth that reads as friendly '
    'in one business culture reads as presumption in another — when unsure, one register more '
    'formal, and let them lower it first (the same asymmetry rule as Chapter 5’s greetings). '
    'Directness of praise varies too: public individual praise delights some cultures and '
    'mortifies others where the team is the honored unit — praise the team publicly, the '
    'individual privately, until you know. And sympathy crosses cultures on the same principle '
    'everywhere — presence over eloquence — but its forms (flowers, donations, silence, food, '
    'attendance) are intensely local: when a colleague from another culture suffers a loss, the '
    'one-line question to a mutual colleague (“what would be right?”) is itself an act of '
    'respect. The constant across all of it: sincerity survives translation; formula doesn’t.')

h1(doc, 'Templates appendix: five to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. The reference request')
para(doc, '“Dr. Alvarez — I’m applying for the QC supervisor role at Meridian (posting attached), '
    'and your view of my validation work would carry real weight. Would you be willing to serve as '
    'a reference? Three reminders that might help: the Q3 audit-trail project, the 40% turnaround '
    'improvement, and the retraining program I ran after the calibration incident. The form takes '
    'about ten minutes; deadline is the 25th. And if your schedule or familiarity makes this a bad '
    'fit, no explanation needed — I appreciate you either way.”')
h2(doc, '2. The congratulations that lands')
para(doc, '“Dana — saw the announcement: lead on the Meridian account. Nobody worked harder for '
    'it, and the client is getting the person who caught the drift error everyone else missed. '
    'Congratulations.” (Specific, sincere, short, prompt, selfless — and no “let’s catch up '
    'sometime” smuggled in.)')
h2(doc, '3. The sympathy note')
para(doc, '“Jamie — I was so sorry to hear about your father. No reply needed, and nothing at work '
    'requires a thought from you right now — we have it covered. You and your family are in my '
    'thoughts.” (Brief, warm, unhurried; the coverage line is the practical gift.)')
h2(doc, '4. The adjustment grant')
para(doc, '“A replacement ships today by expedited freight at no charge — arriving Wednesday. The '
    'damage occurred in transit; your account now ships in the reinforced packaging we use for lab '
    'equipment, so this doesn’t recur. Thank you for the clear photos — they made this fast.” '
    '(Grant, cause, prevention, gratitude. No opera.)')
h2(doc, '5. The graceful follow-up')
para(doc, '“Resending in case this got buried in the month-end crunch: could you confirm the '
    'vendor list by Thursday? Even a yes/no on TechServe alone would unblock the renewal. '
    'Thursday keeps us inside the discount window — thank you!” (Good faith assumed, ask '
    'restated and narrowed, deadline re-anchored to its reason.)')

h1(doc, 'Everyday-message self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'My requests open with the ask, in question form.',
    'My requests can be satisfied without a clarifying question.',
    'My replies answer in the first word or sentence.',
    'My replies anticipate the next question and end the thread.',
    'My claims include the record, the evidence, and a specific remedy.',
    'I keep claim tone confident — the reader becomes my advocate, not my adversary.',
    'When granting, the grant is my first sentence.',
    'My adjustment messages include the prevention sentence.',
    'I send goodwill notes promptly — and they pass the five-S test.',
    'My instructions are numbered, imperative, one action per line, tested on a novice.',
    'I confirm verbal decisions in writing the same day.',
    'My follow-ups assume good faith and narrow the ask.',
    'My yeses are specific — what, by when, at what scope — and sized to my real capacity.',
    'I check AI-drafted routine mail for names, dates, figures, and the one personal sentence.',
])
para(doc, 'Scoring: 16–20, your everyday mail is building a reputation on purpose. 10–15, adopt '
    '“answer first” and the five-S habit this week. Below 10, start with one rule: the ask or the '
    'answer goes in sentence one. Retake at midterm.')

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find the last request you sent that generated a clarifying question. What was missing against Figure 1, and what did the round trip cost?',
    'Recall the best complaint outcome you ever got. Which elements of Figure 3 were present — and which tone choices helped?',
    'Write (and actually send) one five-S goodwill note this week. Record what it cost you and what came back.',
    'Take instructions you recently struggled to follow. Autopsy them against Figure 7: where were the preconditions, checkpoints, and warnings?',
    'Ask two colleagues (or classmates) what it is like to receive requests from you — really ask, and don’t defend. Compare their answers against this chapter’s ledger categories.',
    'Write the recommendation letter you hope someone could honestly write about you in two years. What specific stories would it need — and which of them exist yet?',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'These are the messages the course rubric was built for: routine, sendable, judged '
    'instantly. Top-band work here means the ask or answer in sentence one, completeness that ends '
    'threads, remedies and deadlines made specific, grants that lead with the grant, and goodwill '
    'that passes five-S. The introductory-letter assignment in this unit is graded exactly on '
    'Figure 1’s pattern plus Chapter 4’s zero-error standard.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('Burying the ask under context.', 'Fix: ask first, in question form; context gets two lines after.'),
    ('Requests that require a reply-before-compliance.', 'Fix: detail format, scope, access — the complete-ask test.'),
    ('The suspense reply.', 'Fix: yes or no is the first word; reasons follow.'),
    ('Angry claims.', 'Fix: record, facts, remedy, deadline — confidence recruits the reader; anger is leverage wasted.'),
    ('The defensive grant.', 'Fix: if you’re saying yes, say it first. “While our packaging meets standards…” is a refusal’s opening on a grant’s body.'),
    ('Goodwill with an agenda.', 'Fix: if there’s an ask inside, it’s an invoice. Send the ask separately, later.'),
    ('Paragraph-prose instructions.', 'Fix: numbered, imperative, one action per line, warnings first, tested on a novice.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Isn’t answer-first blunt for sensitive replies?”', 'If the answer is genuinely bad news, it’s not this chapter — it’s Chapter 7, and the indirect pattern applies. The test: will the reader’s day get worse? If it’s routine, answer first; if it wounds, buffer first.'),
    ('“How generous is too generous on adjustments?”', 'Set policy by customer lifetime value, not order margin — then let front-line writers grant to policy without escalation. Grudging grants cost double: the money and the credit.'),
    ('“Handwritten notes: charming or outdated?”', 'For milestone goodwill — a mentor’s retirement, a colleague’s loss — ink is the costly signal that lands hardest precisely because it’s rare. For routine thanks, fast beats fancy: send the email today rather than the card never.'),
    ('“Can AI draft these?”', 'Requests, replies, instructions: yes, with your verification (Chapter 15). Adjustment grants: draft carefully — tone is the product. Sympathy and personal goodwill: no. The entire message is that a human paused.'),
    ('“What if my claim deadline passes with no response?”', 'Escalate one level with the original attached, same calm anatomy, new sentence: “I’d like to resolve this before involving [card issuer / consumer bureau].” Confidence, not threat — you’re still recruiting an advocate, now a more senior one.'),
    ('“Isn’t all this goodwill machinery just transactional niceness?”', 'Only if you run it transactionally. The five-S test’s “sincere” and “selfless” are load-bearing: notes sent to be owed something are invoices, and readers can smell the ledger. Send because the act deserved marking; the compounding is a byproduct you never mention — including to yourself.'),
    ('“How do I decline being a reference without burning the bridge?”', 'The graceful exit you offer others, used on yourself: “I don’t think I’m the strongest reference for this role — my view of your work is mostly [X], and this job is about [Y]; you deserve a recommender who has seen that side.” True, kind, and it hands them a better strategy instead of a wound.'),
    ('“My company requires legal-approved language for adjustments. Doesn’t that kill the craft?”', 'It constrains the middle, not the ends. The grant can still lead, the prevention sentence usually survives review, and the human close is yours. Within any template, sequence and warmth remain writer’s choices — which is why two agents with identical scripts produce opposite customer reviews.'),
    ('“I sent a five-S note and got no response. Was it wasted?”', 'No — “selfless” means no response was owed; requesting one (even silently) converts the gift back into a transaction. The note was received, filed in the ledger, and will surface in ways you won’t trace. Send the next one on the same terms, or examine whether you were sending notes or invoices.'),
    ('“Which everyday genre should I master first?”', 'The reply, answer-first. It is the highest-volume genre, the fastest habit to install, and the most immediately visible — colleagues feel a thread-ending replier within a week. Requests second, confirmations third; goodwill throughout, because the calendar won’t wait for your curriculum.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 6).', 'Request patterns, reply order, adjustment stages, and goodwill judgment calls.'),
    ('Introductory letter assignment.', 'A direct request wearing letter formatting: Figure 1 plus Chapter 2’s you-view plus Chapter 4’s zero errors.'),
    ('Complaint-handling presentations.', 'The claim and adjustment patterns are the written half of the “Influencing Positively / complaint handling” work in this course.'),
    ('Next chapter.', 'Chapter 7 — negative messages: when the answer is no, and the reader’s day is about to get worse.'),
    ('The lecture deck.', 'The Chapter 6 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Direct request pattern', 'ask (as a question), explain briefly, detail completely, close with a dated goodwill line.'),
    ('Complete-ask test', 'the request can be satisfied without a single clarifying question.'),
    ('Answer-first reply', 'yes or no leads; details and anticipations follow; the thread ends.'),
    ('Claim', 'a request wearing a grievance: record, facts, specific remedy, deadline, calm confidence.'),
    ('Adjustment', 'the response granting a claim: grant first, explain without excuses, prevent, restore.'),
    ('Prevention sentence', 'the line naming what stops a repeat — the sentence that actually restores confidence.'),
    ('Goodwill message', 'thanks, congratulations, or sympathy passing the five-S test: specific, sincere, short, spontaneous, selfless.'),
    ('Reciprocity', 'the robust human tendency to repay treatment in kind (Cialdini, 2021) — the economics of generous adjustments.'),
    ('Giver advantage', 'habitual, boundaried generosity predicting long-run success (Grant, 2013).'),
    ('Checkpoint', 'the “you’ll see a green banner” line telling instruction-followers they are still on the path.'),
    ('Confirmation', 'the same-day, numbered, self-ratifying record of anything decided aloud.'),
    ('Request stack', 'multiple asks of one person: numbered, dated, capped at three, blocker first.'),
    ('Graceful exit', 'the escape hatch built into high-stakes asks — a lukewarm yes is worse than a clean no.'),
    ('Follow-up arithmetic', 'deadline passes → good-faith nudge → narrowed second nudge → change channel, ask, or recipient.'),
    ('The reputation ledger', 'the implicit, cumulative, transitive scoring of your everyday messages — where “easy to work with” is manufactured.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Everyday messages are diagnostic: everyone can see whether yours are good, and reputations compound from them.',
    'Requests: ask first in question form, explain why-and-why-them, detail to the complete-ask standard, close with a dated reason.',
    'Replies: answer in the first word, anticipate the next question, end the thread.',
    'Claims: record, facts, specific remedy, deadline — delivered with the confidence that recruits an advocate.',
    'Adjustments: grant first, explain without opera, include the prevention sentence, close forward. Generosity is economics (Cialdini, 2021).',
    'Goodwill: five-S — specific, sincere, short, spontaneous, selfless. Send it; ink for milestones; never AI (the pause is the message).',
    'Instructions: numbered, imperative, one action per line, preconditions first, checkpoints included, warnings before the step — tested on one novice.',
])

quiz(doc, [
    ('A direct request should open with:', ['Background context','The ask, in question form','The writer’s credentials','An apology for asking']),
    ('The complete-ask test is passed when:', ['The request is under 100 words','The reader can comply without asking a clarifying question','The deadline is generous','The tone is warm']),
    ('A reply to a yes/no question should begin with:', ['Context','The answer','A greeting paragraph','The reasons']),
    ('A good reply ends the thread by:', ['Being brief','Anticipating and answering the reader’s next question now','Promising to follow up','CCing a manager']),
    ('The first element of a professional claim is:', ['The emotional impact','The verifiable record — order number, dates, product','A threat to escalate','The remedy']),
    ('Claims name a specific remedy because:', ['It’s legally required','Sellers grant specific requests and stall vague unhappiness','It shortens the message','Templates require it']),
    ('When granting a claim, the grant belongs:', ['After the explanation','In sentence one — delay reads as the wind-up to a refusal','In the postscript','In a separate message']),
    ('The sentence that actually restores customer confidence is:', ['The apology','The prevention sentence — what stops a repeat','The discount offer','The greeting']),
    ('“While our packaging meets industry standards, we are willing on this occasion…” fails because:', ['It’s too short','It defends the company first and makes the grant grudging — spending the money and forfeiting the credit','It lacks a signature','It’s passive voice']),
    ('Generous adjustments pay because of:', ['Tax deductions','Reciprocity — customers repay treatment in kind (Cialdini, 2021)','Legal precedent','Faster shipping']),
    ('The five-S test for goodwill messages is:', ['Specific, sincere, short, spontaneous, selfless','Smart, swift, simple, safe, signed','Subject, salutation, summary, signature, send','Specific, serious, structured, standard, sent']),
    ('The one message category AI should never draft is:', ['Meeting recaps','Instructions','Personal sympathy and goodwill — the pause is the message','Routine requests']),
    ('In instructions, warnings belong:', ['At the end, as notes','Before the step they protect','After the step, as review','In an appendix']),
    ('The cheapest way to catch instruction failures is:', ['Longer review meetings','Testing on one real novice before shipping to fifty','Adding more warnings','A FAQ section']),
], ['b','b','b','b','b','b','b','b','b','b','a','c','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Bring a real request you received that failed the complete-ask test. What round trips did it cause, and what would Figure 1 have saved?',
    'When has a company’s handling of your complaint changed your loyalty — in either direction? Map their message against Figure 4.',
    'Why do so few professionals send goodwill notes, when everyone agrees they matter? Name the frictions honestly — and the one you’ll remove for yourself.',
    'Find instructions in your workplace or university that generate repeated questions. Which Figure 7 element is missing?',
    'Debate: “Companies should empower front-line staff to grant borderline claims without approval.” Costs, risks, and the reciprocity math.',
    'The reputation ledger is asymmetric — friction remembered, smoothness invisible. Is that unfair, and does it matter? What follows for how you budget effort across message types?',
    'Automated transactional mail increasingly speaks for organizations. Find one automated message you received recently that failed this chapter’s standards, and rewrite its worst two sentences.',
])

h1(doc, 'A closing word: the ordinary as practice field')
para(doc, 'Every skill this course teaches gets its daily repetitions in this chapter’s genres. The '
    'direct strategy is rehearsed in every request; audience analysis in every reply; revision '
    'discipline in every message that matters slightly; goodwill in every note you remember to '
    'send. Musicians have scales; communicators have routine mail. The professionals whose '
    'high-stakes documents impress were not saving their skill for the big occasions — they were '
    'practicing on the small ones, dozens of times a day, until the habits held under pressure '
    'automatically. Treat your ordinary inbox as the practice field it is, and the extraordinary '
    'moments will find you already trained.')

references(doc, [
    'Cialdini, R. B. (2021). Influence, new and expanded: The psychology of persuasion. Harper Business.',
    'Grant, A. (2013). Give and take: Why helping others drives our success. Viking.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch06-study-guide.docx')
finish(doc, os.path.abspath(out))
