# Chapter 7 Study Guide — Negative Messages
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(7, 'Negative Messages',
    'Saying no, delivering bad news, and apologizing — the messages that test everything you know, at the moment it matters most.')

h1(doc, 'How to use this guide')
para(doc, 'Bad news is where communication skill stops being cosmetic. A clumsy request costs a round '
    'trip; a clumsy refusal costs a relationship, and a clumsy layoff memo makes the news. This '
    'chapter gives you the indirect pattern in full, the craft of the news sentence itself, the '
    'anatomy of a real apology, and the discipline of delivering bad news early. Read it twice: once '
    'as a writer, once as the person who will someday receive every message in it.')

h1(doc, 'When the direct pattern would wound')
para(doc, 'Chapter 3 established the decision rule: direct for receptive readers, indirect for '
    'resistance and bad news. Here is the psychology under the rule. A blunt opening no triggers the '
    'reader’s defense before your reasons get a hearing — they read the rest of the message as '
    'opposition research, hunting flaws in your logic rather than following it. Reasons delivered '
    'first, to a mind not yet wounded, get read as reasons. The indirect pattern is therefore not '
    'evasion; it is sequencing for a listener you are about to hurt. Every fact still arrives — '
    'in the order a human can hear it.')
figure(doc, os.path.join(FIG, 'ch7_indirect.png'),
    'Figure 1. The indirect pattern: buffer, reasons, the news once, pivot forward.',
    'Indirect pattern in four stages: a buffer of honest common ground that promises no yes; the reasons before the refusal so the no arrives pre-justified; the news itself delivered once, clearly and briefly without euphemism; and a forward pivot to alternatives and next steps.')
para(doc, 'Scope note: the indirect pattern is for consequential bad news — refusals that matter, '
    'decisions that cost the reader something real. Routine small nos (“we’re out of the blue ones”) '
    'take direct treatment; wrapping trivial disappointments in ceremony is its own insult, and '
    'Chapter 3 already named the abuse: indirect as fog.', bold_lead='Scope.')

h1(doc, 'Buffers: honest common ground, never false hope')
figure(doc, os.path.join(FIG, 'ch7_buffers.png'),
    'Figure 2. Five buffer types — agreement, appreciation, facts, good news first, understanding.',
    'Five buffer types with examples: agreement (you are right that turnaround time matters), appreciation (thank you for the careful proposal), facts (the committee reviewed all fourteen applications), good news first (your first request is approved; on the second…), and understanding (I know how much planning went into the March date).')
para(doc, 'The buffer’s job is narrow: one or two sentences of true, relevant common ground that let '
    'the reader settle before the turbulence. Its failure modes are both fatal. A false-hope buffer '
    '(“Great news about your application process!”) converts disappointment into betrayal — the '
    'reader replays your cheerful opening as mockery. A padded buffer (three paragraphs of weather) '
    'reads as the writer stalling, which the reader correctly interprets as dread — and dread is '
    'contagious. True, relevant, brief: “Thank you for the careful proposal — the cost analysis '
    'was thorough” is a buffer; “We received your document” is a timestamp; “Wonderful news '
    'inside!” is a lie with a salutation.')

h1(doc, 'Reasons: the load-bearing middle')
para(doc, 'The reasons section is where refusals are actually won or lost. Three disciplines. First, '
    'give the real reason when you can — readers detect boilerplate, and a true constraint '
    '(“the fund covers certifications only, and the conference is classified as travel”) respects '
    'them enough to argue with. Second, frame reasons around facts and shared interests, not '
    'personal judgment: “the budget closed in March” survives scrutiny; “your request wasn’t a '
    'priority” starts a war. Third, resist the apology-excuse blend: reasons explain the no; they '
    'do not beg forgiveness for it. If the decision is defensible, defend it plainly; if it is not '
    'defensible, the problem is the decision, not the paragraph.')

h1(doc, 'The news sentence: once, clear, brief')
figure(doc, os.path.join(FIG, 'ch7_news.png'),
    'Figure 3. The news sentence between its two failure modes: evasion and cruelty.',
    'The news sentence craft shown between two failure modes: evasion (it may prove difficult at this juncture to accommodate — the reader cannot even find the no) and cruelty (denied; your proposal failed on multiple criteria — the no weaponized). The craft: we cannot fund the March cohort this year — once, clear, brief, then pivot forward.')
para(doc, 'After the reasons, the news itself — and here the indirect pattern briefly becomes '
    'direct. Say it once: repetition grinds the wound. Say it clearly: the reader must never have to '
    'ask “wait, is this a no?” — euphemism that obscures the decision (“it may prove difficult to '
    'accommodate”) forces them to seek the rejection twice. Say it briefly: subordinate-clause '
    'placement softens without hiding (“Although the committee couldn’t fund the March cohort, the '
    'September session…”). And say it without the passive camouflage Chapter 3 flagged — “a '
    'decision has been made” fools no one and owns nothing.')

h1(doc, 'The pivot: every no carries whatever yes exists')
figure(doc, os.path.join(FIG, 'ch7_pivot.png'),
    'Figure 4. Four pivots: the alternative, the partial yes, the path back, the referral.',
    'Four forward pivots: the alternative (the September cohort has space, a seat held until Friday), the partial yes (we can fund two of the three positions), the path back (reapply after six months with specific strengtheners named), and the referral (another lab runs exactly this analysis).')
para(doc, 'The close of a negative message faces forward. If an alternative exists — a later '
    'cohort, a partial grant, a referral, a path back — it belongs here, concretely: “I can hold a '
    'September seat until Friday” is a pivot; “feel free to reach out in the future” is upholstery. '
    'If genuinely nothing exists, close with respect and without manufactured silver linings — '
    'dignity survives an honest no far better than a decorated one. Never close by re-apologizing '
    'for the decision you just defended; it reopens the question and teaches the reader to appeal.')

h1(doc, 'Apologies: the negative message about yourself')
figure(doc, os.path.join(FIG, 'ch7_apology.png'),
    'Figure 5. Apology anatomy: own it, name the impact, repair and prevent, stop.',
    'Apology anatomy in four stages: own it (I missed the deadline I committed to, with no mistakes-were-made and no if-you-were-offended), name the impact (which delayed your review by a week), repair and prevent (what is being done now and what stops a repeat), and stop (no third apology, no self-flagellation tour).')
para(doc, 'When the bad news is your own error, the pattern inverts: directness is the respect. '
    'Psychiatrist Aaron Lazare, who studied apology for decades, found that effective apologies '
    'share recognizable anatomy — acknowledgment of the specific offense, explanation without '
    'excuse, expressed remorse, and reparation — and that most failed apologies fail by omitting '
    'the first element (Lazare, 2004). The workplace translation is Figure 5: own the specific act '
    '(“I missed the deadline I committed to” — no “mistakes were made,” no “if you were '
    'offended,” which relocates the offense into the reader’s sensitivity); name the impact, which '
    'proves you understand the cost; state repair and prevention; and stop. The prevention sentence '
    'does the trust repair — the same sentence that restores customers in Chapter 6 restores '
    'colleagues here. One clean apology outperforms five grovels, because the reader needs the fix, '
    'not your feelings about yourself.')

h1(doc, 'Delivering bad news upward and early: the MUM effect')
figure(doc, os.path.join(FIG, 'ch7_mum.png'),
    'Figure 6. The MUM effect: bad news travels slowest exactly when it matters most (Rosen & Tesser, 1970).',
    'Downward curve showing how a small fixable problem, delayed by reluctance to report — next week, after the demo — grows until it surfaces itself, large and public. Labeled the MUM effect after Rosen and Tesser 1970.')
para(doc, 'More than fifty years ago, psychologists documented what every workplace confirms: people are '
    'reluctant to transmit bad news — they delay it, soften it, or route it to someone else, even '
    'when they bear no blame for the news itself (Rosen & Tesser, 1970). The MUM effect is why your '
    'manager hears about problems six weeks late and why Chapter 1’s upward filter exists. Beating '
    'it in your own career is a competitive advantage with a simple protocol: report the problem '
    'while it is small, pair it with a plan (own it, cause in one line, '
    'recovery plan, ask), and calibrate honestly — “yellow, trending red” beats both silence and '
    'panic. The professionals leaders trust with big things are the ones who told the truth about '
    'small things, early, on purpose.')

h1(doc, 'Channel and timing: the pairing, again')
figure(doc, os.path.join(FIG, 'ch7_pairing.png'),
    'Figure 7. Serious bad news is a pairing: rich conversation first, written record second.',
    'Channel pairing for serious bad news: rich channel first (conversation or call carrying empathy, absorbing questions, protecting dignity), then lean channel second (a written follow-up the same day carrying the record, the terms, and next steps).')
para(doc, 'Chapter 1’s pairing rule reaches its most important application here. Consequential '
    'personal bad news — a role eliminated, a project cancelled under someone, a serious claim '
    'denied — is delivered rich first: conversation or call, where empathy has bandwidth, questions '
    'get absorbed in real time, and the person’s reaction happens in private rather than in a '
    'reply-all. The written version follows the same day: terms, dates, next steps — the record. '
    'Email-only for such news reads as cowardice because it usually is. Timing discipline completes '
    'the craft: bad news is delivered as early as certainty allows (the MUM effect is the enemy), '
    'never on a Friday at 4:55 as avoidance, and never “after the holidays” when the decision is '
    'already made and the reader is planning around a fiction.')

h1(doc, 'Deep dive: refusing by relationship — customers, colleagues, bosses, friends')
para(doc, 'The indirect pattern is constant; its execution bends by relationship. Refusing '
    'customers is the most-scripted case (Case 2 below), where the pivot carries the commercial '
    'weight: what you CAN do is the difference between a lost sale and a converted one, and the '
    'refusal that teaches (“the reinforced case prevents exactly this break”) leaves the customer '
    'more capable than it found them. Refusing colleagues is a relationship transaction: the '
    'reason must be real and checkable (they will see your calendar), the pivot should share the '
    'load you cannot carry (a name, a brief, an offer to onboard your replacement), and the '
    'refusal must arrive fast — a slow no steals the time they needed to find someone else, which '
    'converts your scheduling problem into their crisis. Refusing upward is a delicate art: '
    'almost never a flat no, almost always a constraint surface — “I can '
    'deliver A by Friday or B by Friday; which should lead?” hands the trade-off to its owner '
    'without refusing anything, and “yes, and here’s what it displaces” is a yes that carries its '
    'own invoice. Refusing friends-at-work adds one hazard: the relationship tempts you to skip '
    'the structure and improvise on warmth — which is exactly how good friendships acquire vague '
    'resentments. The pattern protects friendships precisely because it is impersonal: honest '
    'buffer, real reason, clean no, generous pivot, same as anyone — plus the one sentence '
    'friendship earns: “I hate saying no to you specifically.”')

h1(doc, 'Deep dive: the language of bad news — words that wound and words that work')
para(doc, 'Below the pattern level, individual word choices carry disproportionate weight in '
    'negative messages, because wounded readers read closely. The lexicon of unnecessary pain: '
    '“unfortunately” (the most overused word in refusals — it performs sympathy while adding '
    'none; the reasons should make the regret evident); “policy” as a standalone reason (“per '
    'company policy” is where accountability goes to hide — cite the policy’s REASON or expect '
    'the reader to appeal past you); “you claim / you state” (converts their report into an '
    'accusation of lying); “must understand / need to realize” (commands aimed at feelings never '
    'land); and any repetition of the wound’s vocabulary — a rejection letter that uses '
    '“rejected/rejection” four times grinds where once informed. The working lexicon: “although / '
    'while” (subordination that softens without hiding); “what we can do” (the pivot’s native '
    'tongue); “going forward” deployed honestly (future-facing, but only after the past is dealt '
    'with — premature pivoting reads as evasion); and the reader’s own words for their situation, '
    'echoed accurately in the buffer (proof of listening, Chapter 1’s cheapest trust move). One '
    'revision drill covers all of it: reread your draft refusal marking every word the reader '
    'could experience as a second cut, and ask of each whether it carries information or just '
    'edge. Information stays. Edge goes.')

h1(doc, 'Deep dive: bad news to groups — layoffs, changes, and the all-hands')
para(doc, 'When bad news addresses many people at once — restructurings, benefit cuts, program '
    'cancellations — the pattern holds but three dynamics intensify. Fairness perception '
    'dominates: groups process bad news by comparing (why our team? why not theirs?), so the '
    'reasons section must address the selection logic explicitly or the grapevine will supply a '
    'worse one. Survivors are an audience: the layoff message is read most closely by the people '
    'staying, who are learning what this organization does to people — the dignity you extend '
    'the affected is the loyalty pitch you are making to the rest. And timing compresses: with '
    'groups, the rich-first pairing becomes a same-hour sequence (live meeting with questions → '
    'written version → manager talking points), because gaps between tellings create '
    'first-class and second-class recipients, and the second class finds out from the first '
    'within minutes. Two group-specific disciplines: never let logistics carry the emotional '
    'load (the calendar invite titled “Org Update — mandatory” has already delivered the bad '
    'news, badly), and prepare the FAQ before the announcement, not after — the questions are '
    'predictable, and “we’ll get back to you” on the obvious ones reads as either unprepared or '
    'evasive. Groups forgive hard decisions delivered well with remarkable consistency; what '
    'they file permanently is carelessness about the delivery.')

h1(doc, 'Worked examples: three refusals, done properly')
h2(doc, '1. Refusing a colleague’s request')
para(doc, '“Thanks for thinking of me for the interview panel — I’ve enjoyed the past two rounds. '
    'This month I’m committed to the audit closeout through the 22nd, and panel prep deserves real '
    'attention, so I have to pass this cycle. Dana ran the rubric with me last year and would be '
    'excellent; I’m glad to brief whoever steps in.” Buffer (true), reason (concrete), no (clear, '
    'once), pivot (a named alternative plus an offer).')
h2(doc, '2. Refusing a customer’s claim')
para(doc, '“Thank you for the photos and the quick report — they made review easy. The damage shown '
    'is consistent with a drop after delivery rather than transit handling, which our carrier '
    'coverage and warranty don’t extend to. We can’t replace the unit at no cost. Here’s what we '
    'can do: our repair service can restore it for $180 — about a third of replacement — and I can '
    'schedule it this week. Either way, the reinforced case on page 12 prevents exactly this '
    'break.” Reasons before refusal, the no in one clean sentence, a concrete partial yes.')
h2(doc, '3. Declining an internal proposal')
para(doc, '“Your automation proposal was the most complete the committee saw this quarter — the '
    'payback math held up under finance review. The budget can fund two initiatives this cycle, and '
    'the two ranked ahead tie directly to the compliance deadline. We can’t fund yours this round. '
    'It ranked third of nine; with Q3 volume data added, I’d expect it to lead the next cycle — '
    'resubmission opens August 1, and I’ll flag it for the chair.” Honest praise, real reasons, '
    'clear no, and a path back specific enough to act on.')

h1(doc, 'Case study 1: the same denial, twice')
para(doc, 'A regional manager must deny an employee’s tuition-reimbursement request for an executive '
    'workshop. Version A, sent by email: “Your request has been denied as the program does not meet '
    'eligibility criteria. Please consult the policy manual for details. Future requests should be '
    'submitted with closer attention to program classifications.” Version B, delivered in a brief '
    'conversation and confirmed in writing: “Your development plan is exactly what the fund exists '
    'for, and the workshop choice makes sense for where you’re headed. The fund is restricted to '
    'certificate-granting programs — the workshop is classified as a conference, which the policy '
    'excludes and I can’t override. So I can’t approve this one. Two things I can do: the fall '
    'Certified Manager program is covered at 100% and closes enrollment in June; and if you want '
    'the workshop anyway, the department can cover your two travel days as work time. Worth '
    'fifteen minutes Thursday?”')
numbered(doc, [
    'Map both versions against Figure 1. Which stages does Version A skip, and what does each omission cost?',
    '“Future requests should be submitted with closer attention…” — analyze that sentence’s tone. What does the employee hear?',
    'Version B contains the identical no. List every craft element that changes its reception.',
    'The manager spent eleven extra minutes on Version B. Argue the return on those minutes using Chapter 16’s influence framework.',
])
h2(doc, 'Case analysis')
para(doc, 'Version A is a no wearing a policy citation: no buffer, no reasons (a pointer to a manual '
    'is homework, not an explanation), a passive-adjacent verdict, and a closing sentence that '
    'converts a denial into a reprimand — the employee hears “you were careless,” and the '
    'relationship books the loss. Version B delivers the same refusal with every stage intact: a '
    'true buffer that affirms the person’s trajectory, the real constraint stated plainly enough to '
    'be checked, the no in one unambiguous sentence with ownership (“I can’t approve this one”), '
    'and a pivot carrying two concrete yeses. The eleven-minute return is Chapter 16 arithmetic: '
    'Version B leaves an employee who tells colleagues “she fought for me and the policy blocked '
    'it” — deposit; Version A leaves one who tells them “don’t bother asking” — withdrawal, '
    'compounding through the grapevine (Chapter 1) forever.')

h1(doc, 'Case study 2: the slipping launch')
para(doc, 'A product team discovers in week three that a client launch will miss its date by roughly '
    'a month — a vendor component failed certification. The account lead argues for waiting: “We’ll '
    'know more after the retest in two weeks; why alarm them with maybes?” The project manager '
    'overrules and calls the client that afternoon: here’s what we know, here’s what we don’t, '
    'here’s the recovery plan, here’s the date we’ll confirm the new date. Two weeks later the '
    'retest fails too; the slip lengthens. The client, briefed at each step, extends the contract '
    'anyway — and later tells the PM’s boss it was the vendor management that convinced them. A '
    'competing team at the same company, facing an identical slip on another account, waited for '
    'certainty. Their client learned the truth four days before the launch date, from their own '
    'integration team.')
numbered(doc, [
    'The account lead’s argument is the MUM effect wearing a strategy costume. Name its flaws using Figure 6.',
    'Script the PM’s first call using the crisis structure: known, unknown, plan, next update.',
    'Why did the news getting WORSE not damage the first client relationship?',
    'The second team’s client found out from the integration team. Using Chapter 1’s grapevine rule, explain why that channel was inevitable — and what it cost.',
])
h2(doc, 'Case analysis')
para(doc, '“Why alarm them with maybes” fails on both of its own terms: the maybes were already '
    'facts (the component had failed once), and the alarm grows with every day of silence — bad '
    'news early is a resource the client can plan with; bad news late is a betrayal they must '
    'recover from. The PM’s structure is the calm-clarity formula: what we know (component failed '
    'certification), what we don’t (whether the retest passes), the plan (parallel-sourcing started '
    'today), and the promised cadence (update every Tuesday) — that last element converting a '
    'crisis into a managed process. The worsening news didn’t damage trust because trust was never '
    'staked on the outcome; it was staked on the reporting, which held. And the second team '
    'demonstrated the immutable law: the client always finds out. The only variable under your '
    'control is whether they find out from you, early, with a plan — or from the grapevine, late, '
    'with a grievance.')

h1(doc, 'Deep dive: rejections that recruit — declining candidates')
para(doc, 'The hiring rejection is the negative message organizations send most and invest in '
    'least — a template so hollow (“we received many qualified applications…”) that its arrival '
    'is a small insult. The craft opportunity is real: rejected candidates become customers, '
    'referrers, and future applicants, and research on candidate experience consistently finds '
    'the rejection’s quality shapes all three. The upgrades, in ascending investment: speed '
    '(the rejection that arrives promptly respects the candidate’s search; the one that arrives '
    'after their start date elsewhere announces they never mattered); specificity where scale '
    'allows (finalists earn a human sentence — “the committee was impressed by your validation '
    'portfolio; the offer went to a candidate with direct FDA-submission experience” — which '
    'converts a door slam into a data point); the honest pivot (“we’d welcome your application '
    'for the QC lead posting in the fall” only when true — the reflexive “we’ll keep your resume '
    'on file” is the false-hope buffer’s cousin); and the door left open with dignity regardless. '
    'What never belongs: feedback on the candidate’s interview performance unless requested '
    '(unsolicited critique in a rejection reads as justification), and any sentence implying the '
    'decision was hard if it was not. For your own job search, the mirror lesson: read rejections '
    'as calibration data where they offer any, and never as verdicts — Chapter 13 takes that '
    'thread.')

h1(doc, 'Deep dive: when the bad news is public — crisis statements')
para(doc, 'Sometimes the audience for bad news is everyone: the recall, the breach, the outage, '
    'the public mistake. External crisis statements compress this chapter into its highest-stakes '
    'form, and the structure is settled craft: acknowledge fast (the vacuum fills with '
    'speculation at internet speed — a holding statement within hours beats a polished one '
    'tomorrow: “we are aware, we are investigating, next update by 6 p.m.”); state what happened '
    'in plain declarative language (every hedge — “alleged,” “apparent,” “may have” — will be '
    'read aloud on the news with raised eyebrows; if you know, say; if you don’t, say that); own '
    'your share without the passive camouflage (“we misconfigured the transfer” — companies that '
    'write “mistakes were made” become case studies titled Mistakes Were Made); center the '
    'affected before the institution (the statement that leads with “our reputation for quality” '
    'while customers hold recalled product has chosen its priority publicly); and carry the '
    'prevention sentence at institutional scale — what specifically changes, by when, verified '
    'how. The internal corollary: employees hear the public statement too, and they know the '
    'facts — a public statement that spins converts the whole staff into fact-checkers with '
    'group chats. One honest rule covers both audiences: write the statement you could defend '
    'line-by-line at the deposition, because that is now a standard scenario, not a paranoid '
    'one.')

h1(doc, 'Deep dive: documenting performance — when the bad news needs a paper trail')
para(doc, 'A specialized genre sits at the intersection of this chapter and HR reality: the '
    'written record of a performance problem. Its double audience defines it — the employee, who '
    'deserves clarity and a path; and the file, which may someday need to demonstrate fairness. '
    'The craft threads that needle with behavioral specificity: “missed the March 3 and March 17 '
    'reporting deadlines after two verbal reminders” is checkable, fair, and file-worthy; '
    '“continues to display a poor attitude toward deadlines” is an opinion wearing a verdict, '
    'unfair to the employee and useless to the file. The structure mirrors the adjustment letter '
    'inverted: the concern stated plainly (once, per the news-sentence rules), the expectation '
    'made explicit with dates and measures, the support offered concretely (training, check-ins, '
    'resources — the path back is not optional decoration; it is the document’s legitimacy), '
    'and the consequences of no change stated without threat theater. Tone discipline is '
    'absolute: the document will be reread by its subject many times and possibly by lawyers '
    'once — write it so both readings find the same fair author. And pair it (rich first, '
    'always): the conversation happens before the memo arrives; a written warning that IS the '
    'first notice converts a performance process into an ambush, and ambushes teach organizations '
    'nothing except fear.')
para(doc, 'The behavioral-specificity habit above has a name worth learning: SBI — Situation, '
    'Behavior, Impact. State the situation concretely (“in Tuesday’s client call”), the observed '
    'behavior without adjectives (“the pricing slide had last quarter’s numbers”), and the impact '
    'it had (“the client caught it, and we spent ten minutes rebuilding credibility”). SBI is what '
    'converts feedback from a character verdict into a checkable, fixable fact pattern — the same '
    'discipline this chapter’s documentation genre already runs, given a label you can carry into '
    'any feedback conversation, not just the written ones.', bold_lead='SBI, named.')

h1(doc, 'Deep dive: receiving bad news like a professional')
para(doc, 'You will receive every message this chapter teaches, and the receiving seat has its '
    'own craft. When the no arrives: respond — silence after a refusal reads as sulking, while '
    'the gracious acknowledgment (“understood — thanks for the clear reasons and the September '
    'option”) is so rare it gets remembered; mine the reasons — a well-built refusal contains a '
    'map of what would change the answer (the path back is yours to walk); and never make the '
    'refuser pay for honesty, because the colleague punished for a clean no learns to deliver '
    'foggy ones. When criticism arrives: the counterintuitive move is to extract the useful core '
    'BEFORE processing the sting — “what specifically would make this sendable?” converts even '
    'clumsy criticism into specification; defensiveness, however justified, teaches the critic to '
    'route future feedback around you, which is how professionals end up surprised at review '
    'time (the MUM effect, aimed at you personally). And when the bad news is big — the role '
    'eliminated, the project killed — the professional receipt is composure plus one day: '
    'acknowledge, ask what you need to know now, and schedule the substantive conversation for '
    'tomorrow, when the questions you ask will be the ones you actually need answered. How you '
    'receive bad news is watched as closely as how you deliver it — and it is the cheaper '
    'reputation to build, because the opportunities arrive free.')

h1(doc, 'Refusal workshop: five repairs (answers follow)')
para(doc, 'Diagnose each against the pattern before checking the answers. Name the failing stage '
    '— buffer, reasons, news, or pivot — as you go.')
numbered(doc, [
    '“Great news! While we were extremely impressed with your proposal, unfortunately after careful consideration we have decided not to move forward at this juncture. We wish you the best of luck!”',
    '“Your request for remote work has been denied per section 4.2 of the employee handbook. Please direct any questions to HR.”',
    '“I’m so sorry, I feel terrible about this, I know I should have told you sooner, I’m the worst — the report isn’t done and honestly I’ve just been drowning, I’m really really sorry.”',
    '“We can’t issue a refund. We also can’t offer store credit at this time. The warranty doesn’t apply. Thank you for being a valued customer!”',
    '“Due to circumstances, it may prove difficult to accommodate the March cohort as originally envisioned, though every effort will be made going forward.”',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    'The false-hope buffer (“Great news!”), an unfindable size-zero reason (“careful consideration” explains nothing), and a luck-wish where a pivot belongs. Repair: true buffer about the proposal’s specific strength, the real constraint, one clear no, and a path back with coordinates.',
    'A no wearing a citation: no buffer, the policy invoked without its reason, and the pivot outsourced to HR. Repair: the reason BEHIND 4.2 (coverage requirements, precedent), an owned no, and whatever partial yes exists — hybrid days, a review date, the criteria that would change the answer.',
    'The apology anatomy inverted: five apologies, zero impact statement, zero fix, zero prevention — the reader must now manage the writer’s feelings AND the missing report. Repair: “The report is two days late, which delayed your review. It arrives tomorrow noon; I’ve moved my Thursday block to finish it, and you’ll hear from me the day any future deadline wobbles — not after.”',
    'Three nos and a fossil, no reasons, no pivot — the reader learns what is impossible and nothing else. Repair: reasons for the warranty boundary, then the pivot that exists (repair at cost? replacement discount? the prevention accessory?) — and if genuinely nothing exists, a respectful close without the “valued customer” garnish on a bare refusal.',
    'Pure evasion: the reader cannot find the no, the size of it, or the date of anything. Repair: “We can’t fund the March cohort. September has space, and I can hold a seat until Friday” — eleven words of news, ten of pivot, zero fog.',
])

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Frances Frei, “How to build (and rebuild) trust” (TED).', 'Authenticity, logic, empathy — and why trust repair starts with naming the wobble. The apology section’s theory, live.'),
    ('Adam Galinsky, “How to speak up for yourself” (TED).', 'The range of acceptable assertiveness and how to expand yours — directly useful for delivering unwelcome truths upward.'),
    ('Susan David, “The gift and power of emotional courage” (TED).', 'Why discomfort tolerance — yours — is the hidden prerequisite for every honest hard conversation.'),
])

h1(doc, 'Worked example: the price increase, start to finish')
para(doc, 'The price increase letter is the negative-message genre every business eventually '
    'writes, and it rewards the full machinery. The draft nobody should send: “Dear Valued '
    'Customer, Due to unprecedented increases in raw material and logistics costs, we are '
    'unfortunately compelled to adjust our pricing effective immediately. We appreciate your '
    'understanding.” Every failure in one paragraph: the fossil salutation, the passive '
    'compulsion (“we are compelled” — by whom?), the unfindable size of the increase, the '
    'effective-immediately ambush, and a closing that requests understanding while offering '
    'none.')
para(doc, 'The rebuilt version: “Dear Dr. Alvarez — For three years we’ve held your reagent '
    'pricing flat while carrier surcharges and solvent costs rose around it. [buffer: true, '
    'relevant, and quietly establishing the credit the request draws on] We can’t absorb the gap '
    'any longer: effective September 1, catalog prices increase 6% — your typical monthly order '
    'moves from $2,340 to about $2,480. [the news: findable, sized in THEIR numbers, dated with '
    'runway] Two things stay unchanged: your locked contract pricing through its December '
    'renewal, and same-week delivery. [what survives — the anxious reader’s question, answered] '
    'If it helps your budgeting, orders placed before September 1 hold current pricing, and '
    'annual contracts lock the new rate against further changes. [the pivot: two real levers '
    'handed to the reader] Questions on your specific pricing → me directly, this week. '
    '[named owner, dated availability]” The anatomy is Chapter 7 complete: honest buffer, '
    'checkable reasons, one clear no (to the old price), survivors named, pivots real, and '
    'runway that converts an ambush into a plannable event. Customers leave price increases over '
    'the delivery far more often than over the digits.')

h1(doc, 'Deep dive: the strategic no — refusing good ideas')
para(doc, 'The hardest refusals are not of bad requests but of good ones: the genuinely promising '
    'project that doesn’t fit this year’s three priorities, the strong candidate for the wrong '
    'role, the improvement worth doing that would displace something worth more. Strategy IS '
    'refusal (Chapter 17’s simplicity discipline — ten priorities equal none), which makes the '
    'strategic no a leadership genre. Its distinct requirements: honor the idea explicitly and '
    'mean it (“this is the best automation proposal the committee has seen” — the buffer here is '
    'not softening but justice); locate the refusal in the portfolio, not the proposal (“the two '
    'funded initiatives tie to the compliance deadline” — the idea lost to context, not to '
    'quality, and the difference determines whether its author proposes again); preserve the '
    'idea’s future concretely (the resubmission date, the data that would strengthen it, your '
    'flag to the chair — Case 3’s path back, with real coordinates); and protect the proposer’s '
    'standing in the room where the no lands (“I want this back in front of us in Q3” said '
    'publicly costs nothing and keeps a good thinker thinking). Organizations that refuse good '
    'ideas badly train their best people to stop having them — the innovation death spiral '
    'nobody schedules a meeting about. The strategic no, delivered with this care, does the '
    'opposite: it teaches the organization that ideas are safe here even when budgets are '
    'finite.')

h1(doc, 'Templates appendix: five refusals to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. Declining a meeting invitation')
para(doc, '“Thanks for including me — the agenda looks useful. I can’t contribute much to the '
    'vendor discussion and I’m protecting Thursday for the audit prep, so I’ll pass this round. '
    'Dana has the current pricing context if you need that thread covered; send me the notes and '
    'I’ll flag anything from my side.” (Honest reason, named alternative, loop kept closed.)')
h2(doc, '2. Refusing a discount request')
para(doc, '“Thanks for the direct question — I’d rather give you a straight answer than a slow '
    'one. We can’t move on the unit price; it’s set by volume tiers we apply uniformly, which is '
    'also your protection as a customer. What I can do: waive the installation fee ($900) at your '
    'current volume, and the price drops automatically at 50 units if your usage grows. Want me '
    'to model both paths?” (Reason with a principle behind it; two real pivots; forward '
    'question.)')
h2(doc, '3. The candidate rejection, finalist version')
para(doc, '“Thank you for the time and preparation you brought to three rounds — the committee '
    'was genuinely impressed by your validation portfolio. We’ve offered the role to a candidate '
    'with direct FDA-submission experience, and they’ve accepted. That was the deciding factor, '
    'and it’s a narrow one: if the QC lead posting opens this fall as expected, we’d welcome '
    'your application, and I’m glad to be a reference contact for your search in the meantime.” '
    '(Specific praise, honest reason, true pivot, dignity intact.)')
h2(doc, '4. Saying no upward')
para(doc, '“I can get you the full validation package by Friday, or the summary plus the raw '
    'data by Wednesday — but not the full package by Wednesday without pulling Dana off the '
    'audit. Which trade works better for the client meeting?” (No refusal anywhere; the '
    'constraint surfaced, the decision routed to its owner.)')
h2(doc, '5. The apology for a real error')
para(doc, '“I missed the deadline I committed to for the stability data, which held up your '
    'submission by two days. The gap was mine — I underestimated the reprocessing time and '
    'didn’t flag it when I knew. The data is attached now; going forward I’m building a '
    'half-day buffer into anything touching submissions, and you’ll hear from me the day a '
    'timeline wobbles, not after. Thanks for your patience with this one.” (Own, impact, fix, '
    'prevention, stop. No third apology.)')

h1(doc, 'Bad-news self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'I choose indirect structure for consequential bad news — and direct for trivial nos.',
    'My buffers are true and promise nothing.',
    'I give the real reason when one exists, framed on facts rather than judgment.',
    'My news sentences pass the test: findable, unambiguous, said once.',
    'My refusals carry whatever yes exists — concretely.',
    'My apologies own the specific act, without “if you were offended.”',
    'My apologies include the prevention sentence — and then stop.',
    'I report problems while they are small, paired with a plan.',
    'I deliver consequential personal bad news rich-first, record-second.',
    'I never schedule bad news for Friday 4:55 as avoidance.',
])
para(doc, 'Scoring: 16–20, you are the person organizations trust with hard messages — a genuinely '
    'rare asset. 10–15, drill the news sentence and the early-reporting habit. Below 10, adopt one '
    'rule: the reader must be able to find the no, and hear it only once. Retake at midterm.')

h1(doc, 'Deep dive: after the no — managing the aftermath')
para(doc, 'The message sends; the episode doesn’t end. Three aftermath disciplines complete the '
    'craft. Hold the line kindly: some recipients appeal — new arguments, escalations, emotional '
    'renegotiation — and the professional response distinguishes new information (which honestly '
    'reopens the question) from new pressure (which doesn’t): “if the Q3 data changes the '
    'payback math, bring it to me — but the budget constraint itself won’t move this cycle” '
    'respects both the person and the decision. Repair the temperature: after a hard refusal, '
    'the next routine interaction carries outsized weight — the ordinary friendly message about '
    'ordinary business, sent within days, tells the recipient the no was about the request, not '
    'the relationship (goodwill capital, Chapter 6, deployed at the exact moment it matters '
    'most). And audit your own aftermath: if a refusal keeps generating appeals, the reasons '
    'section failed; if recipients keep being surprised, the buffer overpromised or the news '
    'sentence hid; if relationships keep cooling, the pivots weren’t real. Bad news is the one '
    'genre where the feedback arrives reliably — every response to your refusals is a grade on '
    'your delivery. Read them.')

h1(doc, 'Deep dive: bad news across cultures')
para(doc, 'Hall’s continuum (Chapter 1) bends every stage of the indirect pattern. In high-context '
    'settings, the buffer and reasons carry more of the message — a no may never be spoken '
    'directly at all, arriving instead as “this presents difficulties” or “we will study it,” '
    'phrases that ARE the refusal to a fluent reader; demanding a blunter no (“so is that a yes '
    'or a no?”) forces a face-loss that damages the relationship past the transaction. Reading '
    'indirect refusals is therefore a skill: delay, deflection to committees, and enthusiasm that '
    'never converts to dates are answers. In low-context settings, the inverse hazard: your '
    'carefully-buffered indirect refusal may simply not register as a no, generating follow-ups '
    'you experience as pressure and they experience as diligence — with such readers, the news '
    'sentence must be findable even at the cost of feeling abrupt to you. Apologies vary even '
    'more: in some business cultures apology is relational maintenance offered freely and '
    'implying little fault; in others it is a formal admission spent carefully — calibrate '
    'before you export your default. The meta-rule survives everywhere: reasons before refusal, '
    'dignity throughout, the pivot forward. The dial settings are local; the machine is not.')

h1(doc, 'Put it to work this week')
numbered(doc, [
    'Deliver one small refusal you have been avoiding, using the full pattern. Notice which stage was hardest — that stage is your growth edge.',
    'Report one problem to its stakeholder while it is still small, paired with a plan. Log what the early telling cost versus what you feared.',
    'Write (send optional) the apology anatomy for something real: own, impact, prevention, stop.',
    'Practice one gracious receipt: acknowledge a no, mine its reasons, thank the refuser for the clarity.',
    'Find your organization’s or university’s last public bad-news statement and grade it against the crisis structure.',
])

h1(doc, 'Journal prompts')
numbered(doc, [
    'Recall the worst-delivered bad news you ever received. Map it against Figure 1 — what was missing, and what did the delivery add to the injury?',
    'Write the refusal you have been avoiding (a request, an invitation, a commitment you must exit). Full pattern. Sending is optional; drafting is not.',
    'Recall a time you sat on bad news. What did the MUM effect whisper, how long did you wait, and what did the delay cost?',
    'Find a public corporate apology (recall, outage, scandal). Grade it against Figure 5: what does it own, what does it dodge, and where does the passive voice hide?',
    'Recall a no you received that you still respect. Reconstruct its anatomy — then recall one you still resent, and locate the exact sentence where it went wrong.',
    'Which seat is harder for you: delivering bad news or receiving it? What does your answer suggest about which deep dive to reread?',
    'You must someday deliver bad news you disagree with. Write the version you could deliver honestly — and identify what conversation you’d need with your own manager first.',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'The supervisor test is sternest here: a badly handled refusal is the message most likely '
    'to get forwarded, screenshotted, or read aloud in someone’s kitchen. Top-band negative messages '
    'in this course show the full pattern — honest buffer, real reasons, a findable once-only no, a '
    'concrete pivot — plus tone that survives the angriest possible reader. The '
    'bad-news-to-customers assignment in this unit is graded exactly on those elements.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('The false-hope buffer.', 'Fix: true and neutral common ground. Cheer that precedes a no reads as mockery in the replay.'),
    ('Reasons after the no.', 'Fix: reasons first — a wounded reader reads your logic as opposition research.'),
    ('The unfindable no.', 'Fix: one clear sentence. If the reader must ask “is this a no?”, they suffer it twice.'),
    ('The repeated no.', 'Fix: once. Repetition grinds the wound without adding information.'),
    ('“Mistakes were made” apologies.', 'Fix: own the specific act, name the impact, prevent, stop.'),
    ('Sitting on bad news until certain.', 'Fix: early with a plan beats certain and late — the MUM effect is the career trap (Rosen & Tesser, 1970).'),
    ('Email-only for personal bad news.', 'Fix: rich first, record second — the pairing is the professionalism.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Isn’t the buffer manipulative?”', 'A true buffer is sequencing, not deception — every fact arrives. The manipulation line is crossed by false hope, hidden decisions, or missing reasons, not by kindness in the opening.'),
    ('“What if the real reason is unflattering — budget politics, a stronger candidate?”', 'Give the truest reason you can state professionally, at the useful altitude: “the committee funded initiatives tied to the compliance deadline” is true without an autopsy of the politics. Never invent a tidier reason; invented reasons get checked.'),
    ('“How do I say no to my boss?”', 'As a constraint conversation, not a refusal: “I can deliver A by Friday or B by Friday — which should lead?” You are not declining; you are surfacing the trade-off they are implicitly choosing. Chapter 16’s question-not-order, aimed upward.'),
    ('“Should apologies ever be public?”', 'Match the audience to the injury: private errors get private apologies; public errors (the reply-all, the meeting comment) get their repair in the same room. Never wider than the wound — a broadcast apology for a private slight re-injures.'),
    ('“Can AI draft bad news?”', 'It can structure a draft — the pattern is mechanical. But tone under stress is the product, the empathy must be real, and for personal bad news the human authorship IS part of the message (Chapters 6 and 15). Draft with help if you must; deliver as yourself, always.'),
    ('“The recipient will be angry no matter how well I write it. Why bother?”', 'Because the anger has a half-life, and the delivery determines what remains after it decays: a grievance about the decision, or a grievance about YOU. Well-delivered bad news is regularly forgiven; badly-delivered good news sometimes isn’t. You are writing for the reader they’ll be in three weeks.'),
    ('“How much emotion belongs in my apology?”', 'Enough to be human, less than would make the reader manage YOUR feelings. “I’m genuinely sorry” carries; a paragraph of self-recrimination transfers the emotional labor to the injured party — the apology equivalent of the blame opera. The fix and the prevention are where sincerity shows.'),
    ('“What if I disagree with the decision I must deliver?”', 'Deliver it honestly and own the delivery without theatrical distance (“they decided…” with an eye-roll buys you nothing and costs the organization coherence). You may say a decision was contested where true and useful; you may not recruit the recipient into your dissent. If you can’t deliver it without deception, that’s a Chapter 1 ethics conversation with your own manager — before the delivery, not during it.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 7).', 'Pattern staging, buffer judgment, news-sentence craft, and apology anatomy.'),
    ('“Effective Strategies for Delivering Bad News to Customers” assignment.', 'This chapter is that assignment’s toolkit — Figures 1 through 4 in particular.'),
    ('Complaint-handling work.', 'Chapter 6 granted claims; this chapter denies them without losing the customer.'),
    ('Next chapter.', 'Chapter 8 — persuasive messages: moving readers who could say no toward yes.'),
    ('The lecture deck.', 'The Chapter 7 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Indirect pattern', 'buffer → reasons → news once → forward pivot; sequencing for a reader about to be hurt.'),
    ('Buffer', 'one or two sentences of true, relevant common ground that promise nothing.'),
    ('False-hope buffer', 'cheer preceding a no — converts disappointment into betrayal.'),
    ('The news sentence', 'the refusal itself: findable, unambiguous, said once, owned.'),
    ('Subordinate-clause softening', 'placing the no in a dependent clause (“Although we couldn’t fund…”) — softening without hiding.'),
    ('Forward pivot', 'the alternative, partial yes, path back, or referral that every no should carry if one exists.'),
    ('Apology anatomy', 'own the act, name the impact, repair and prevent, stop (Lazare, 2004).'),
    ('MUM effect', 'the documented reluctance to transmit bad news, producing delay and distortion (Rosen & Tesser, 1970).'),
    ('Rich-first pairing', 'conversation for the delivery, same-day writing for the record.'),
    ('Calm-clarity structure', 'known · unknown · plan · next update — bad news as a managed process.'),
    ('Strategic no', 'refusing a good idea for portfolio reasons — honored, located in context, given a path back.'),
    ('Holding statement', 'the fast public acknowledgment that fills the vacuum before the full statement can: aware, investigating, next update at [time].'),
    ('Behavioral specificity', 'documenting performance in checkable acts and dates, never traits — fair to the person, useful to the file.'),
    ('Survivor audience', 'the people watching how bad news treats its recipients — the loyalty pitch inside every layoff message.'),
    ('The gracious receipt', 'acknowledging a refusal, mining its reasons, and never punishing the honesty — the reputation built for free.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Indirect structure is sequencing for a reader about to be hurt: reasons reach an unwounded mind; every fact still arrives.',
    'Buffers are true, relevant, and brief — never false hope, never padding.',
    'Give the real reason at a professional altitude; facts and shared interests, not personal judgment.',
    'The news sentence: findable, unambiguous, once, owned. Euphemism makes the reader hunt for their own rejection.',
    'Every no carries whatever yes exists — concretely, or not at all.',
    'Apologies own the specific act, name the impact, prevent, and stop (Lazare, 2004).',
    'The MUM effect delays bad news exactly when speed matters most — report small, early, with a plan (Rosen & Tesser, 1970).',
    'Consequential personal bad news is a pairing: rich conversation first, written record the same day.',
])

quiz(doc, [
    ('The indirect pattern exists because:',
     ['Bad news should be hidden', 'Reasons delivered before the no reach a mind not yet defending itself',
      'It is more formal', 'Length softens everything']),
    ('A buffer must be:',
     ['Optimistic', 'An apology',
      'At least a paragraph', 'True, relevant, and brief — promising nothing']),
    ('“Great news about your application process!” before a rejection is:',
     ['A false-hope buffer — disappointment converted to betrayal', 'A strong buffer',
      'Required courtesy', 'A forward pivot']),
    ('The reasons section works best when it:',
     ['Cites the policy manual and stops', 'Blames the committee',
      'States the real constraint in checkable facts', 'Apologizes repeatedly']),
    ('The news sentence should be:',
     ['Repeated for emphasis', 'Findable, unambiguous, said once',
      'Implied rather than stated', 'In the postscript']),
    ('“It may prove difficult at this juncture to accommodate…” fails because:',
     ['Too short', 'Wrong salutation',
      'Too direct', 'The reader cannot even find the no — and must seek their rejection twice']),
    ('A forward pivot is:',
     ['The concrete alternative, partial yes, path back, or referral', 'A second apology',
      'A subject line', 'A buffer']),
    ('An apology that says “if you were offended”:',
     ['Shows sensitivity', 'Is legally safer',
      'Relocates the offense into the reader’s feelings instead of owning the act', 'Meets Lazare’s anatomy']),
    ('The sentence that repairs trust in an apology is:',
     ['The remorse sentence', 'The prevention sentence — what stops a repeat',
      'The greeting', 'The third apology']),
    ('The MUM effect (Rosen & Tesser, 1970) describes:',
     ['Quiet offices', 'Email overload',
      'A meeting format', 'Reluctance to transmit bad news, producing delay and distortion']),
    ('Beating the MUM effect in your career means:',
     ['Reporting problems small and early, paired with a plan', 'Never reporting problems',
      'Waiting for certainty', 'Routing news through colleagues']),
    ('Consequential personal bad news should be delivered:',
     ['Email only, for the record', 'On Fridays at 4:55',
      'Rich channel first, written record the same day', 'After the holidays']),
    ('In the tuition case, “future requests should be submitted with closer attention…” converted the denial into:',
     ['A pivot', 'A reprimand — the relationship books the loss',
      'A buffer', 'A partial yes']),
    ('The slipping-launch case shows that client trust was staked on:',
     ['The outcome never worsening', 'The account lead’s optimism',
      'The contract terms', 'The reporting — which held even as the news worsened']),
], ['b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'When is directness the kinder structure for bad news? Build the decision rule with two examples from your own experience.',
    'Find a rejection you received that was well done. What did the writer do that you would steal?',
    'Why do organizations reward MUM-effect behavior even while claiming to want transparency? What would actually change the incentive?',
    'Take a public corporate apology and rewrite its worst sentence to pass Figure 5.',
    'Your team must announce a price increase to loyal customers. Draft the structure: what buffers, reasons, and pivots honestly exist?',
    'The chapter claims survivors read layoff messages more closely than the laid-off. Test the claim against any organizational bad news you’ve witnessed: what did the watchers learn?',
    'Is the strategic no genuinely different from an ordinary refusal, or just a flattering frame? Argue from the proposer’s side of the desk.',
])

h1(doc, 'A closing word: the messages that define you')
para(doc, 'Nobody remembers who wrote the smooth announcement in a good quarter. The messages '
    'that get retold — in exit interviews, at retirement dinners, in the stories organizations '
    'tell about themselves — are disproportionately this chapter’s: the layoff handled with '
    'dignity, the refusal that kept a door open, the apology that owned everything, the bad news '
    'delivered early when hiding was available. That is not because negative messages matter '
    'more than positive ones; it is because they are the only messages written under conditions '
    'that reveal character — when the writer’s interests and the reader’s comfort genuinely '
    'diverge, and craft is the only bridge. Every technique in this chapter is learnable in an '
    'afternoon and practicable for a career. The professionals who master them are not the ones '
    'who enjoy delivering bad news; they are the ones who decided that if it must be delivered, '
    'it will be delivered well — and were quietly promoted, decade after decade, by the people '
    'who received it.')

references(doc, [
    'Lazare, A. (2004). On apology. Oxford University Press.',
    'Rosen, S., & Tesser, A. (1970). On reluctance to communicate undesirable information: The MUM effect. Sociometry, 33(3), 253–263.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch07-study-guide.docx')
finish(doc, os.path.abspath(out))
