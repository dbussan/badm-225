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
para(doc, 'Fifty years ago, psychologists documented what every workplace confirms: people are '
    'reluctant to transmit bad news — they delay it, soften it, or route it to someone else, even '
    'when they bear no blame for the news itself (Rosen & Tesser, 1970). The MUM effect is why your '
    'manager hears about problems six weeks late and why Chapter 1’s upward filter exists. Beating '
    'it in your own career is a competitive advantage with a simple protocol: report the problem '
    'while it is small, pair it with a plan (Chapter 16’s formula — own it, cause in one line, '
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

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Frances Frei, “How to build (and rebuild) trust” (TED).', 'Authenticity, logic, empathy — and why trust repair starts with naming the wobble. The apology section’s theory, live.'),
    ('Adam Galinsky, “How to speak up for yourself” (TED).', 'The range of acceptable assertiveness and how to expand yours — directly useful for delivering unwelcome truths upward.'),
    ('Susan David, “The gift and power of emotional courage” (TED).', 'Why discomfort tolerance — yours — is the hidden prerequisite for every honest hard conversation.'),
])

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

h1(doc, 'Journal prompts')
numbered(doc, [
    'Recall the worst-delivered bad news you ever received. Map it against Figure 1 — what was missing, and what did the delivery add to the injury?',
    'Write the refusal you have been avoiding (a request, an invitation, a commitment you must exit). Full pattern. Sending is optional; drafting is not.',
    'Recall a time you sat on bad news. What did the MUM effect whisper, how long did you wait, and what did the delay cost?',
    'Find a public corporate apology (recall, outage, scandal). Grade it against Figure 5: what does it own, what does it dodge, and where does the passive voice hide?',
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
    ('The indirect pattern exists because:', ['Bad news should be hidden','Reasons delivered before the no reach a mind not yet defending itself','It is more formal','Length softens everything']),
    ('A buffer must be:', ['Optimistic','True, relevant, and brief — promising nothing','At least a paragraph','An apology']),
    ('“Great news about your application process!” before a rejection is:', ['A strong buffer','A false-hope buffer — disappointment converted to betrayal','Required courtesy','A forward pivot']),
    ('The reasons section works best when it:', ['Cites the policy manual and stops','States the real constraint in checkable facts','Blames the committee','Apologizes repeatedly']),
    ('The news sentence should be:', ['Repeated for emphasis','Findable, unambiguous, said once','Implied rather than stated','In the postscript']),
    ('“It may prove difficult at this juncture to accommodate…” fails because:', ['Too short','The reader cannot even find the no — and must seek their rejection twice','Too direct','Wrong salutation']),
    ('A forward pivot is:', ['A second apology','The concrete alternative, partial yes, path back, or referral','A subject line','A buffer']),
    ('An apology that says “if you were offended”:', ['Shows sensitivity','Relocates the offense into the reader’s feelings instead of owning the act','Is legally safer','Meets Lazare’s anatomy']),
    ('The sentence that repairs trust in an apology is:', ['The remorse sentence','The prevention sentence — what stops a repeat','The greeting','The third apology']),
    ('The MUM effect (Rosen & Tesser, 1970) describes:', ['Quiet offices','Reluctance to transmit bad news, producing delay and distortion','A meeting format','Email overload']),
    ('Beating the MUM effect in your career means:', ['Never reporting problems','Reporting problems small and early, paired with a plan','Waiting for certainty','Routing news through colleagues']),
    ('Consequential personal bad news should be delivered:', ['Email only, for the record','Rich channel first, written record the same day','On Fridays at 4:55','After the holidays']),
    ('In the tuition case, “future requests should be submitted with closer attention…” converted the denial into:', ['A pivot','A reprimand — the relationship books the loss','A buffer','A partial yes']),
    ('The slipping-launch case shows that client trust was staked on:', ['The outcome never worsening','The reporting — which held even as the news worsened','The contract terms','The account lead’s optimism']),
], ['b','b','b','b','b','b','b','b','b','b','b','b','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'When is directness the kinder structure for bad news? Build the decision rule with two examples from your own experience.',
    'Find a rejection you received that was well done. What did the writer do that you would steal?',
    'Why do organizations reward MUM-effect behavior even while claiming to want transparency? What would actually change the incentive?',
    'Take a public corporate apology and rewrite its worst sentence to pass Figure 5.',
    'Your team must announce a price increase to loyal customers. Draft the structure: what buffers, reasons, and pivots honestly exist?',
])

references(doc, [
    'Lazare, A. (2004). On apology. Oxford University Press.',
    'Rosen, S., & Tesser, A. (1970). On reluctance to communicate undesirable information: The MUM effect. Sociometry, 33(3), 253–263.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch07-study-guide.docx')
finish(doc, os.path.abspath(out))
