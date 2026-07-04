# Chapter 5 Study Guide — Short Workplace Messages and Digital Media
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(5, 'Short Workplace Messages and Digital Media',
    'Email that works, chat that coordinates, and the digital professionalism that follows your name everywhere.')

h1(doc, 'How to use this guide')
para(doc, 'Unit 3 begins here: the foundation chapters meet the inbox. Everything from Chapters 1–4 '
    'now gets applied to the messages you will actually send most — email, chat, and texts — plus '
    'the digital citizenship that surrounds them. Read with your own sent folder open; the best '
    'practice material for this chapter is the last twenty messages you wrote.')

h1(doc, 'Email: still the workplace’s official language')
para(doc, 'Decades after its predicted death, email remains where business happens: it is the channel '
    'of record, the external interface, and the medium wrapped around every attachment and decision. '
    'Analysts at McKinsey estimated years ago that interaction workers spent roughly 28 percent of '
    'the workweek reading and answering email (Chui et al., 2012) — and worldwide volume has only '
    'grown since, with hundreds of billions of messages daily (Radicati Group, 2024). The '
    'professional consequence is arithmetic: everyone you write to is drowning. The writer who costs '
    'the reader the least time wins the reputation.')
figure(doc, os.path.join(FIG, 'ch5_email.png'),
    'Figure 1. Anatomy of a working email — six parts, each with one job.',
    'Email anatomy: subject line stating the message’s job; greeting matched to the relationship; sentence one carrying the main point; body support in lists or short paragraphs within one screen; call to action with a specific act and date standing at the end; signature block with name, title, organization, and phone.')
para(doc, 'Every part of Figure 1 executes a foundation chapter. The subject line and sentence one are '
    'Chapter 3’s frontloading. The one-screen body is Chapter 4’s conciseness. The call to action '
    'with act-plus-date is Chapter 2’s planning. The signature block is Chapter 1’s professionalism. '
    'Short messages are not a new skill — they are all your skills, compressed.')

h1(doc, 'Subject lines: five words that decide everything')
figure(doc, os.path.join(FIG, 'ch5_subject.png'),
    'Figure 2. Subject-line formulas: action, information, question, and the thread rescue.',
    'Four subject line formulas with examples: action (verb plus object plus date, “Approve vendor list by Thu”), information (topic plus takeaway, “Server migration done — all normal”), question (the actual question, “OK to move standup to 9:30?”), and thread rescue (new topic gets a new subject).')
para(doc, 'A subject line has three careers: it gets the message opened today, it gets the message '
    'found next quarter, and it tells a skimming reader what is owed. All three careers reward the '
    'same design — the message’s job, stated in front-loaded specifics. “Quick question” has no '
    'careers at all: it does not say what is owed, and no search will ever find it again. The '
    'formulas in Figure 2 cover most traffic; the habit worth building is writing the subject line '
    'last, after the message has told you what it turned out to be about.')

h1(doc, 'The one-screen rule and the shape of short messages')
para(doc, 'If an email scrolls, it is competing with reports — and losing to neither. The internal '
    'shape that keeps messages inside a screen: main point in sentence one; support as a short list '
    'or two brief paragraphs (Chapter 3’s chunking); the ask standing alone at the end where the '
    'F-pattern terminates (Nielsen, 2006). When content genuinely will not fit — procedures, '
    'analyses, anything with sections — the email’s job changes: it becomes a one-paragraph cover '
    'note for an attachment, and the attachment carries the weight. “Details attached; the decision '
    'needed is X by Friday” serves every reader at every altitude.')

h1(doc, 'Threads, copies, and the ecology of the inbox')
figure(doc, os.path.join(FIG, 'ch5_threads.png'),
    'Figure 3. Thread hygiene: reply-all discipline, new-topic-new-thread, To versus CC, and the BCC exit ramp.',
    'Four thread hygiene rules: reply-all only when every name needs every word; a new topic gets a new thread instead of hiding in an old subject line; people in the To line act while people in CC are informed; and BCC as an exit ramp when moving someone off a thread with thanks.')
para(doc, 'Email is a shared ecosystem, and etiquette is its pollution control. Reply-all belongs '
    'only where every recipient needs every word — the reply-all “thanks!” to forty people is a '
    'micro-tax on forty attention budgets. The To and CC lines are a work assignment: To means act, '
    'CC means know; blurring them is why nobody is sure who owns the task (Chapter 16’s '
    'accountability lesson, in miniature). And when a thread’s topic drifts — the budget thread now '
    'negotiating a hire — give the new topic a new subject line, or next quarter’s search will find '
    'nothing where the decision lives.')

h1(doc, 'Chat, Teams, and Slack: coordination at conversation speed')
figure(doc, os.path.join(FIG, 'ch5_channels.png'),
    'Figure 4. The channel etiquette matrix: what each medium owes and expects.',
    'Channel etiquette matrix comparing email, chat, and text: response windows (about one business day for email, minutes to hours for chat, minutes for urgent texts), formality levels, best uses (records and decisions for email, quick coordination for chat, time-critical logistics for text), and never-fors (email for instant needs, chat for decisions needing records, text for anything confidential or complex).')
para(doc, 'Chat is the hallway, digitized: perfect for the quick question, the coordination ping, '
    'the “running five minutes late.” Its etiquette differs from email in speed and shape — short '
    'turns, conversational register, threads to contain topics, @mentions used like a hand on a '
    'shoulder rather than an air horn. Two disciplines keep chat professional. First, front-load '
    'even here: “Quick one: can the demo move to 2:00?” beats the naked “hey” that takes a hostage '
    'and reveals no ransom. Second, know chat’s ceiling: the moment a conversation becomes a '
    'decision with consequences, it graduates to email — “confirming what we agreed in chat” — '
    'because decisions need the channel of record (Chapter 1’s pairing, again).')

h1(doc, 'Texting and after-hours: the boundary channels')
figure(doc, os.path.join(FIG, 'ch5_response.png'),
    'Figure 5. Response-time norms: what each channel and audience customarily owes.',
    'Response time expectations: client or external email deserves same-business-day acknowledgment; a manager’s direct question deserves hours not days; a team chat mention deserves a response within the working session; FYI and CC traffic owes no reply; after-hours messages owe a next-business-day response unless the role requires otherwise.')
para(doc, 'Texting a colleague’s personal number is entering their kitchen: appropriate for '
    'time-critical logistics with people who invited you, and for nothing confidential, complex, or '
    'contractual. After-hours messaging deserves special care — Chapter 1 taught that response '
    'timing is nonverbal communication, and a 9 p.m. message from a senior person reads as a demand '
    'whatever the sender intended. The professional habits: schedule-send for the morning, or say '
    'explicitly “no response needed tonight.” Norms you protect for others tend to be protected for '
    'you.')

h1(doc, 'The permanence gradient: write like legal reads it')
figure(doc, os.path.join(FIG, 'ch5_permanence.png'),
    'Figure 6. The permanence gradient — employer systems are logged, retained, and discoverable.',
    'Permanence gradient across workplace channels: email and documents are discoverable and archived; chat platforms are logged and exportable; even so-called disappearing messages survive as screenshots. Workplace systems are employer property with logging, retention, and legal discovery.')
para(doc, 'Everything on workplace systems is the employer’s property and, in disputes, the court’s '
    'reading material: email archives, chat exports, edit histories. The practical rule is not '
    'paranoia but posture — write every workplace message as if a future third party will read it, '
    'because the mechanism for exactly that is already installed. The venting that felt private in a '
    'DM becomes a screenshot; the “joke” becomes the exhibit. Chapter 1’s publicity test is not '
    'hypothetical on digital channels; it is the literal operating condition.')

h1(doc, 'Your digital presence: the profile that interviews first')
figure(doc, os.path.join(FIG, 'ch5_presence.png'),
    'Figure 7. The professional presence pyramid: public posts, work platforms, professional profiles, private channels.',
    'Professional presence pyramid: public posts (assume permanent and employer-visible), work platforms (employer property, logged and exportable), professional profiles like LinkedIn (a standing portfolio to curate), and private channels (still one screenshot from public).')
para(doc, 'Recruiters and clients meet your digital presence before they meet you, so curate the '
    'layer built for that meeting: a professional profile with a competent photo, a headline that '
    'says what you do, and activity that demonstrates judgment. The other layers follow the '
    'gradient: public posts are permanent and employer-visible (assume both), and private channels '
    'sit one screenshot from public. None of this demands blandness — thoughtful professional '
    'presence is an asset, the standing portfolio from Chapter 1. It demands only that the person '
    'visible online and the person in the interview be colleagues, not strangers.')

h1(doc, 'Deep dive: digital body language')
para(doc, 'Chapter 1 established that nonverbal signals ride on every channel; digital channels have '
    'evolved their own nonverbal vocabulary, and professionals read it whether or not senders manage '
    'it. Response latency is the loudest signal: answering a peer in four minutes and their '
    'teammate in four days announces a hierarchy nobody wrote down. Latency should track message '
    'priority, not sender politics — and when it can’t (travel, deadline crunch), the two-line '
    'acknowledgment resets the signal honestly. Message length carries tone: the one-word “Fine.” '
    'under a five-paragraph proposal reads as contempt even when it means consent; match '
    'investment, or explain the brevity (“Short answer from the road: yes — details Monday”). '
    'Punctuation is expression: the period at the end of a one-line chat message (“ok.”) has '
    'measurably chilled a generation of readers; the exclamation point, in moderation, is simply '
    'how warmth survives compression. Read receipts and online-status indicators broadcast '
    'availability claims you may not intend — the “seen at 9:14, unanswered” gap is a message you '
    'sent without typing. None of this requires paranoia; it requires the same awareness the '
    'in-person version does. Your digital posture is being read. Stand accordingly.')

h1(doc, 'Deep dive: the acknowledgment economy')
para(doc, 'The highest-leverage habit in digital communication costs fifteen seconds: closing '
    'loops. Every request launched into silence generates uncertainty the sender must manage — did '
    'it arrive? is it happening? should I follow up or would that nag? The acknowledgment kills the '
    'whole cascade: “Got it — full answer by Friday” or even “On it” converts an open loop into a '
    'scheduled one. Professionals who acknowledge reliably get described with the highest '
    'compliment an inbox can award: “you never have to wonder with them.”')
para(doc, 'The craft points: acknowledge with a commitment, not just receipt — “received” answers '
    'arrival; “by Friday” answers the question the sender actually has. Calibrate the promise '
    'honestly and then beat it quietly (the reverse — bold promise, silent slip — is how trust '
    'leaks). For requests you cannot serve soon, say so at acknowledgment time: “this is behind two '
    'client deliverables; realistic date is the 22nd — flag me if that breaks something” is '
    'Chapter 7’s early-bad-news discipline at inbox scale. And when YOU are the requester, design '
    'for acknowledgment: end with a question that invites the fifteen-second reply (“will Friday '
    'work?”) rather than a mute period. Loops close twice as fast when both ends are built for '
    'closing.', bold_lead='The craft.')

h1(doc, 'Deep dive: the three-reply rule — when threads should die')
para(doc, 'Some conversations degrade in text: each reply adds a sub-question, a tone wobble, a new '
    'CC — and by reply seven the thread is a committee meeting conducted at typing speed. The '
    'working heuristic: when a thread passes three substantive back-and-forths without converging, '
    'convert channels — a ten-minute call, then one email confirming what was decided (the pairing, '
    'as always). The math is stark: a six-person thread with eleven replies has consumed more '
    'collective minutes than the meeting everyone was avoiding, and produced a worse record. '
    'Convert-triggers beyond the count: visible tone escalation (each reply slightly sharper — '
    'voice de-escalates what text inflames), genuine complexity (interdependent decisions need '
    'working memory that threads fragment), and anything approaching conflict (Chapter 16’s '
    'territory — nobody has ever been argued out of a position by reply-all). The inverse rule '
    'also holds: meetings that exist to transfer information one-way should have been messages. The '
    'channel test is interaction density — high interaction, meet; low interaction, write. Most '
    'organizations get both wrong in both directions, which makes the professional who converts '
    'correctly look like a time wizard.')

h1(doc, 'Deep dive: urgency signaling — spend it like money')
para(doc, 'Every channel has an urgency register — the URGENT tag, the red exclamation, the '
    '@here, the text message itself as a channel choice — and urgency signals obey strict '
    'inflation economics: each unearned use devalues every future one. The sender who marks routine '
    'mail urgent trains recipients to discount the marker exactly once — permanently. The '
    'disciplines: reserve the register for genuine time-criticality (a decision needed today, not a '
    'preference for attention); put the deadline and its reason in the subject instead of the '
    'adrenaline (“Approve by 3 p.m. — vendor hold expires” outperforms “URGENT!!”); and never '
    'escalate channels as a first move — the text message about a non-urgent work matter spends '
    'relationship capital on postage. When everything from someone is urgent, nothing is; when '
    'nothing is, the one urgent message they ever send moves a whole office. Be the second person.')

h1(doc, 'Deep dive: findability — writing for future search')
para(doc, 'Every workplace message has a second audience Chapter 2 didn’t name: future searchers, '
    'including future you. Six months from now, someone — probably you — will need this decision, '
    'this number, this agreement, and will hunt it with keywords. Write for that hunt: put the '
    'searchable nouns in the subject line (project names, vendor names, PO numbers — “Re: that '
    'thing from the call” is unfindable by design); keep one topic per thread so the found thread '
    'contains the whole story; restate context when threads resume after a gap (“picking up the '
    'March decision on the Beckman purchase…” re-anchors both the reader and the search index); '
    'and name attachments as their finders will look for them (“Okafor-Proposal-2026-07.pdf,” '
    'never “final_v2 (3).pdf”). Organizations run on retrieved decisions; the writer whose messages '
    'surface cleanly in search is contributing to institutional memory with every send — and '
    'collecting the quiet reputation that goes with being the person whose email always settles '
    'the dispute about what was agreed.')

h1(doc, 'Research corner: the cost of the ping')
para(doc, 'The always-on workplace has a measured cost. Interaction workers already spent over a '
    'quarter of the workweek inside email a decade ago (Chui et al., 2012), and psychologists '
    'studying conversation argue that continuous partial attention — the phone on the table, the '
    'chat window blinking — degrades even the interactions we stay in (Turkle, 2015). For '
    'communicators the implication is double. As a sender: every message you emit spends someone '
    'else’s focus, so batch the small stuff and make each message complete enough to be answered '
    'without a follow-up (“answerable asynchronously,” Chapter 1’s remote-work rule). As a '
    'receiver: process email in scheduled blocks rather than at each ping — triage (act now if under '
    'two minutes, schedule if longer, file or delete otherwise), and protect at least one daily '
    'stretch of unpinged work. Inbox management is attention management wearing a work costume.')

h1(doc, 'Deep dive: the memo — the format that refuses to die')
para(doc, 'Chapter 2 introduced format signals; the memo deserves its own examination, because it '
    'keeps outliving its obituaries. A memo — whether printed, PDF’d, or living as a formatted '
    'page in a shared drive — is defined by its header block (To / From / Date / Subject) and its '
    'promise: this document is complete in itself, addressed to a defined audience, and built to be '
    'filed. Email carries conversation; memos carry position. That is why policies, formal '
    'recommendations, decision records, and anything that will be referenced by people outside the '
    'original conversation still deserve memo form: the format tells every future reader “this was '
    'considered, this is official, this stands alone.”')
para(doc, 'The craft mirrors everything this course has built: subject line as the document’s job; '
    'a one-line summary or recommendation up top (the direct pattern in its natural habitat); '
    'informative headings; and — memo-specific — a distribution line that is itself a message '
    '(who is on it, and who conspicuously is not, will be read as carefully as paragraph one). One '
    'specialized species matters to know: the memo-to-file, addressed to the record itself — '
    'written after significant meetings, decisions, or incidents, filed where the team files such '
    'things. Nobody asks for it; everybody who has ever needed one wishes it existed. When a '
    'dispute surfaces fourteen months later, the person who wrote the memo-to-file owns the '
    'authoritative version of events — a quiet form of institutional power available to anyone '
    'with ten spare minutes and the habit.', bold_lead='The craft, and the file.')

h1(doc, 'Deep dive: shared documents — writing where everyone can see you type')
para(doc, 'A growing share of workplace writing happens inside shared documents and wikis, where '
    'drafting, commenting, and deciding collapse into one surface. The etiquette layer: comment on '
    'the work, at the right altitude, and declare it (Chapter 4’s reviewer rules apply verbatim); '
    'use suggestion/tracked mode in documents you don’t own — direct edits to someone else’s '
    'draft-in-progress read as marking territory; resolve comment threads when addressed rather '
    'than leaving archaeology for the next reader; and never conduct a side-argument in the margin '
    'of a document the whole team reads — comment threads are the most public private conversation '
    'in the building.')
para(doc, 'The ownership layer matters more: every living document needs a named owner, or it '
    'quietly becomes true-ish — edited by many, vouched for by none. The owner’s job is Chapter '
    '4’s pass three at the document level: periodic verification that the page still matches '
    'reality, a visible “last reviewed” date, and ruthless archiving of superseded versions. A wiki '
    'nobody owns is a rumor with formatting. And for documents that decide things — specs, '
    'policies, runbooks — freeze decisions OUT of the living surface into dated records (the memo '
    'habit again), because a decision that lives only in an editable page is a decision anyone can '
    'silently re-decide.', bold_lead='Ownership.')

h1(doc, 'Deep dive: availability is a message — OOO, calendars, and status')
para(doc, 'Your availability signals are a communication channel you are always broadcasting on. '
    'The out-of-office reply is the most-written, least-designed message in business; the good one '
    'answers the sender’s three questions in three lines: when you return (“back Monday, July 14”), '
    'who covers what meanwhile (“urgent lab scheduling: Dana Reyes; everything else waits for '
    'me”), and what happens to their message (“I’ll reply within two days of returning” — which '
    'also licenses you not to triage from the beach). Skip the apology; absence isn’t a failing. '
    'Calendar hygiene communicates too: blocks labeled honestly (“focus work” is a legitimate '
    'appointment), meeting invitations carrying agendas (an inviteless meeting request is the '
    'naked “hey” of scheduling), and declines with one-line reasons (“conflict with client audit '
    '— send notes and I’ll comment”) that respect both the meeting and your absence from it. '
    'Status indicators round it out: set them truthfully or not at all, because a green dot that '
    'means nothing teaches colleagues to ping and hope — the exact uncertainty all this signaling '
    'exists to remove.')

h1(doc, 'Deep dive: designing group chat that stays useful')
para(doc, 'Team chat degrades by default — channels multiply, topics smear, and the important '
    'drowns in the social. Design fights the entropy. Channels get names that state their scope '
    '(#proj-beckman-rollout, not #stuff) and a pinned purpose line including what does NOT belong; '
    'the social channel exists so the work channels don’t absorb the memes — containment, not '
    'prohibition. Threading discipline keeps parallel conversations parallel: reply in thread, '
    'start new topics at top level, and resist the instinct to answer a threaded question in the '
    'main channel (it forks the record). The @-register follows urgency economics: @person for '
    'their action, @here sparingly for the working-now, @channel almost never — it is the fire '
    'alarm, and fire alarms that ring weekly get ignored. And chat needs a decision-export habit: '
    'anything decided in-channel gets its one-line confirmation in the channel AND its durable '
    'record in email or the project doc, because chat search is where decisions go to become '
    'arguments. A team that adopts even half of this discipline recovers hours a week; the team '
    'that adopts none conducts its business inside a slot machine.')

h1(doc, 'Worked example: the escalation email')
para(doc, 'When the three-reply rule triggers but a call isn’t possible — or the thread must be '
    'escalated to someone senior — the professional move is the escalation summary: a fresh email '
    '(new subject, per thread hygiene) that compresses the mess into a decision package. The '
    'template: “Subject: Decision needed by Thu: Beckman install date. [1] Situation: install '
    'slipped twice; vendor now offers Aug 2 or Aug 16. [2] The disagreement: Ops prefers Aug 2 '
    '(before audit prep); Lab prefers Aug 16 (after method validation). [3] What’s been tried: '
    'both threads attached; no convergence after six replies. [4] Recommendation: Aug 16 — '
    'validation risk outweighs audit-prep inconvenience, mitigations below. [5] Ask: your call by '
    'Thursday, so we hold whichever slot.” Five numbered moves: situation, conflict, history, '
    'recommendation, dated ask. Note what it never does: relitigate the thread, characterize '
    'colleagues’ motives, or forward forty messages with “thoughts?” — the decider gets a '
    'briefing, not homework. Executives fund this format’s author with something better than '
    'budget: they start routing hard things through them.')

h1(doc, 'Worked examples: three short-message makeovers')
h2(doc, '1. The naked “hey”')
para(doc, 'Before (chat): “hey” … “you there?” … “quick question.” Three pings, zero information, '
    'and a colleague now held hostage to an unnamed ask. After: “Quick one: client demo — OK to '
    'move it to 2:00 so Priya can join? Need to confirm by 11.” One ping, complete, answerable from '
    'a phone in nine seconds.')
h2(doc, '2. The scrolling update')
para(doc, 'Before: four paragraphs narrating a project’s week, with the schedule slip mentioned in '
    'paragraph three. After: “Sprint update — on track except one item. Done: API tests, vendor '
    'docs. Slipping: data migration (3 days — vendor file was corrupt; fix due Wed). Need from you: '
    'nothing yet; escalation call Thursday if the fix misses.” The forwardable format from Chapter '
    '2, in five lines.')
h2(doc, '3. The thanks that taxed forty people')
para(doc, 'Before: reply-all “Thanks everyone!!” to the entire division. After: reply (sender only) '
    '“Thanks, Dana — the turnaround saved us.” Gratitude got MORE personal by getting narrower; '
    'thirty-nine inboxes got nothing, which was exactly what they were owed.')

h1(doc, 'Deep dive: external email — writing to clients and strangers')
para(doc, 'Everything in this chapter tightens one notch when the recipient is outside your '
    'organization, because external email carries three loads internal mail doesn’t. It represents '
    'the institution: your signature block says the company’s name, and the reader generalizes '
    'freely — one sloppy message from you is “they’re sloppy over there.” It lacks shared context: '
    'the acronyms, personalities, and history that lubricate internal mail are walls externally; '
    'spell out what any insider would compress (project names, role titles, even which “Friday” — '
    'time zones are a hidden audience). And it is discoverable by the OTHER side’s legal team too: '
    'the permanence gradient runs in both directions, so commitments phrased casually (“we can '
    'probably get you 10% off next round”) are commitments, and hedges must be real hedges '
    '(“subject to the written quote”).')
para(doc, 'The craft additions for strangers specifically: earn the open with a subject line '
    'carrying THEIR interest, not your introduction (“Question about your March webinar on LIMS '
    'validation” beats “Introduction — Jamie Chen”); establish the connection in sentence one '
    '(Chapter 2’s opening playbook — the referral, the shared context, the reason for THIS '
    'person); and make the first ask small (Chapter 8’s ladder applies to relationships too — '
    'fifteen minutes, one question, not “pick your brain sometime,” which prices itself as '
    'unlimited). First messages to strangers get exactly one reading and no benefit of the doubt: '
    'they are the highest-revision-tier messages of their size in your professional life '
    '(Chapter 4’s budgets apply).', bold_lead='Cold craft.')

h1(doc, 'Deep dive: the recurring update — cadence as communication')
para(doc, 'The status update is the most repeated message in professional life, and its secret is '
    'that the CADENCE is half the message: an update that arrives every Friday at 4:00, '
    'identically formatted, communicates control before a word is read — and the Friday it fails '
    'to arrive communicates louder than anything in it. Design the recurring update once, then let '
    'the format compound: a fixed skeleton (On track / Slipping / Need from you / Next milestone), '
    'the same order every time so readers’ eyes learn the layout, deltas over restatements '
    '(“unchanged from last week” is a complete and excellent line item), and honest color-coding '
    'discipline — the project that goes red only after death has trained everyone to ignore its '
    'green (Chapter 7’s calibration rule, on a schedule). Two temptations to resist: the '
    'novel-length update that proves effort instead of reporting status (nobody rereads last '
    'week’s essay; everybody scans this week’s skeleton), and cadence inflation — daily updates '
    'nobody asked for teach recipients to filter you. Agree the cadence with the audience once, '
    'deliver it like a metronome, and break format only when something has genuinely broken: on '
    'that day, the format break itself is your siren.')

h1(doc, 'Deep dive: mobile-first means thumb-first')
para(doc, 'A majority of business email gets its first reading on a phone, and many messages get '
    'their ONLY reading there — which imposes design constraints stricter than any this chapter '
    'has named. The phone screen shows roughly your subject line plus thirty words before scrolling '
    'begins; that preview either wins the open or loses it, and either carries the point or wastes '
    'the reader’s only glance. The disciplines: front-load harder than desktop habits suggest '
    '(subject + first sentence must survive alone); prefer short paragraphs and lists even more '
    'aggressively (a five-line desktop paragraph is a twelve-line phone wall); place the ask where '
    'a thumb-scroller decelerates — the end — AND flag it early (“decision needed by Thu — '
    'details below”); and never bury required action inside an attachment a phone reader will '
    'defer opening (“see attached” as the whole message is a desktop assumption wearing '
    'confidence). Test your own high-stakes messages by sending them to yourself and reading on '
    'your phone first: if the point doesn’t survive the preview, it doesn’t survive the morning '
    'commute triage where messages live or die.')

h1(doc, 'Deep dive: reactions and emoji — the smallest messages')
para(doc, 'The thumbs-up reaction is now a load-bearing piece of workplace infrastructure, and it '
    'deserves two minutes of actual thought. Reactions solve a real problem — acknowledgment '
    'without inbox noise (a 👍 on “meeting moved to 3” closes the loop at zero cost, better than '
    'six “ok!” replies). Their limits: a reaction confirms receipt, not commitment — “can you own '
    'the vendor follow-up?” answered with 👍 is ambiguous exactly where ambiguity is expensive; '
    'anything with a deliverable deserves words. Emoji in prose follow the register rules from '
    'Chapter 2: they scale warmth in channels that have adopted them, they never carry load-bearing '
    'meaning alone, and they exit entirely for first contact, external formality, bad news '
    '(Chapter 7 — a 😊 near a refusal reads as mockery), and anything that might be forwarded '
    'upward. The meta-rule: mirror the register of the specific room, one notch more conservative '
    'than the median. Nobody was ever marked down for warmth delivered in words.')

h1(doc, 'Case study 1: the reply-all storm')
para(doc, 'An HR coordinator sends a benefits reminder to an all-company list — 1,400 names — with '
    'the list itself in the To line. A warehouse employee replies “please remove me,” to everyone. '
    'Six more “remove me too” follow, then the fatal genre: “STOP REPLYING ALL,” sent reply-all, '
    'eleven times, from eleven people, each certain they were the voice of reason. Within an hour '
    'the thread has 900 messages; the email system slows; IT locks the list. The person most '
    'discussed at the next leadership meeting is not the coordinator — it is the sales director '
    'whose all-caps “EVERYONE SHUT UP” is now a screenshot on the company meme channel.')
numbered(doc, [
    'Assign responsibility across the storm: the list configuration, the first replier, the “stop replying” repliers, the director. Who bears what?',
    'What single technical choice by the coordinator would have prevented everything?',
    'Using Figure 6, explain how the director’s message changed careers even though the thread was internal.',
    'Write the one message that could legitimately have gone to the full list mid-storm — from IT — and say why it works where “stop replying” failed.',
])
h2(doc, 'Case analysis')
para(doc, 'The technical fix is one line: mass announcements go BCC (or through a no-reply '
    'distribution tool), which makes reply-all structurally impossible — prevention beats etiquette '
    'every time you can get it. The behavioral layer is Figure 3’s rule failing at scale: every '
    '“stop replying all” author correctly diagnosed the problem and became it, because they answered '
    '“who needs this?” with their irritation instead of the To line. The director’s screenshot '
    'demonstrates the permanence gradient: internal is not private, and composure (Chapter 1’s '
    'professionalism) is most visible exactly when everyone else loses it. The legitimate mid-storm '
    'message exists and is IT’s: “We’ve locked this thread; no further replies will deliver. '
    'Benefits questions → this form.” It works because it changes the system, not just the plea.')

h1(doc, 'Case study 2: the screenshot')
para(doc, 'Two analysts share a private chat channel. After a tense meeting, one vents: “honestly K '
    'has no idea what she’s doing, that budget is fantasy math.” The colleague, meaning to forward a '
    'different message to a teammate, forwards the vent — to a group channel that includes K’s '
    'manager. Apologies are exchanged; the channel goes quiet. Three months later, K is promoted to '
    'lead the analyst’s team. The old message, screenshotted by someone at the time “just in case,” '
    'begins circulating again the week the new org chart posts.')
numbered(doc, [
    'The analyst’s vent was private, informal, and arguably accurate. Walk it through the publicity test and the permanence gradient: where did the risk actually live?',
    'What should the analyst do in the first hour after the misforward — and what should they NOT do?',
    'K saw the message twice: once at the incident, once at promotion. Draft the note the analyst should send K in week one of the new reporting relationship.',
    'What venting channels are actually safe for workplace frustration — and what does Chapter 16 suggest about the underlying disagreement itself?',
])
h2(doc, 'Case analysis')
para(doc, 'The risk lived at the moment of typing, not the moment of forwarding: once frustration '
    'became text on a logged platform, every future was possible and none was controllable — the '
    'permanence gradient is about who controls copies, and the answer on digital channels is never '
    'you. The first-hour move is direct ownership: a short, unhedged apology to K in person or by '
    'voice (rich channel for a wound — Chapter 1), no re-litigation of the budget, no “if you were '
    'offended.” The week-one note under the new org chart is harder and more important: brief, '
    'unprompted, forward-facing — “Before we start working together: that message was unfair to '
    'you, I regret it, and you’ll have my full support on the Q3 plan.” Face the debt before it '
    'faces you. As for the venting itself: the safe channel for workplace frustration is voice, off '
    'platform, with someone outside the org chart — and the disagreement that powered it deserved a '
    'Chapter 16 move at the time: a question in the meeting (“walk me through the revenue '
    'assumptions?”) instead of a verdict in a chat window.')

h1(doc, 'Watch list: three short talks worth your time')
bullets(doc, [
    ('Adam Alter, “Why our screens make us less happy” (TED).', 'A behavioral scientist on what always-on channels do to attention — the receiver’s side of this chapter.'),
    ('Cal Newport, “Quit social media” (TEDx).', 'Deliberately provocative; whether or not you follow the advice, his framing of attention as career capital is this chapter’s economics.'),
    ('Tristan Harris, “How a handful of tech companies control billions of minds” (TED).', 'A former design ethicist on why the ping is engineered — useful for designing your own defenses.'),
])

h1(doc, 'Digital professionalism self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'My subject lines state the message’s job in front-loaded specifics.',
    'My routine emails fit one screen, with the ask standing at the end.',
    'I use To for action and CC for information — deliberately.',
    'I reply-all only when every name needs every word.',
    'I move drifted topics to new threads with new subjects.',
    'In chat, my first message contains the actual question.',
    'I graduate consequential chat decisions to email confirmations.',
    'I acknowledge external email the same business day.',
    'I schedule-send after-hours messages, or mark them no-response-needed.',
    'Nothing I have typed on a workplace system this month would embarrass me as a screenshot.',
])
para(doc, 'Scoring: 16–20, your digital footprint is an asset — maintain it. 10–15, adopt the two '
    'lowest items; subject lines and reply-all discipline pay fastest. Below 10, start with one '
    'habit: write the subject line last, and make it the message’s job. Retake at midterm.')

h1(doc, 'Deep dive: attachments and links — the cargo layer')
para(doc, 'Messages increasingly exist to deliver cargo — files and links — and the cargo layer '
    'has its own etiquette. Announce what you attach and why it matters (“Attached: the signed '
    'quote — the $28,570 figure on page 2 is the one we verified”), because an unexplained '
    'attachment demands the reader open it to learn whether they needed to. Choose attachment '
    'versus link deliberately: attachments freeze a moment (right for records, quotes, anything '
    'that must not drift) while links point at living documents (right for collaboration, wrong '
    'for “the version we agreed to” — a link to a living doc is a moving target wearing a '
    'timestamp). Check link permissions BEFORE sending — the “request access” bounce is the most '
    'common self-inflicted delay in modern work, and it always lands at the worst moment. Name '
    'files for their finders (the recipient’s conventions, not your desktop chaos), keep sizes '
    'courteous (compress or link anything over a few megabytes — mobile readers pay for your '
    'attachment twice), and never let required action live ONLY inside the cargo: the message body '
    'carries the ask and the deadline; the attachment carries the detail. The last-thing check '
    '(Chapter 4) already guards the classic failure — the missing attachment — but its modern '
    'sibling deserves equal billing: the wrong-permissions link is the missing attachment that '
    'looks attached.')

h1(doc, 'Deep dive: the weekly reset — maintenance for your communication system')
para(doc, 'Triage handles the daily flow; a weekly fifteen-minute reset keeps the whole system '
    'honest. The ritual, ideally Friday afternoon: sweep the inbox for open loops YOU owe — every '
    'message where someone awaits your answer gets its acknowledgment-with-commitment now, even if '
    'the commitment is “next Wednesday”; sweep for loops OWED you that have gone quiet — one '
    'gentle, assumption-of-good-faith nudge each (“resending in case this got buried”); clear the '
    'flag/star backlog, because a flagging system where everything is flagged is a decoration '
    'scheme; file or archive the settled threads so Monday’s search space is clean; and — the '
    'compounding step — harvest the week into your systems: decisions worth a memo-to-file get '
    'one, recurring questions worth a template get drafted once, and anything you explained twice '
    'this week becomes a document you link next time. Fifteen minutes. The professionals whose '
    'inboxes never seem to own them are not faster typists; they run maintenance on a schedule, '
    'the way labs calibrate instruments — because an uncalibrated communication system drifts '
    'exactly the same way, just less visibly.')

h1(doc, 'Templates appendix: five messages to steal')
para(doc, 'Adapt freely — the structure is the value.')
h2(doc, '1. The acknowledgment with a commitment')
para(doc, '“Got it — thanks. Full answer by Thursday noon; flag me if you need it sooner.” '
    '(Receipt, date, escape valve. Fifteen seconds; closes the loop completely.)')
h2(doc, '2. The out-of-office that actually helps')
para(doc, '“I’m out through Monday, July 14. Urgent lab scheduling: Dana Reyes (dreyes@…). '
    'Everything else: I’ll reply within two days of returning.” (Return date, coverage by topic, '
    'expectation set. No apology — absence isn’t a failing.)')
h2(doc, '3. The cold contact')
para(doc, '“Subject: Question about your March webinar on LIMS validation. Dr. Alvarez — your '
    'segment on audit trails answered a problem my lab has fought for a year, except one piece: '
    'how do you handle amendment logs under 21 CFR 11? If you have fifteen minutes in the next two '
    'weeks, I’d value the answer — happy to work around your calendar.” (Their work first, one '
    'specific question, one small dated ask.)')
h2(doc, '4. The decision confirmation')
para(doc, '“Confirming today’s call: (1) install moves to Aug 16; (2) I’ll send revised validation '
    'specs by Friday; (3) weekly check-ins each Tuesday until launch. Corrections welcome — '
    'otherwise this stands as our plan.” (Numbered, complete, self-ratifying. The pairing’s written '
    'half, every time anything is decided aloud.)')
h2(doc, '5. The channel-convert move')
para(doc, '“This thread has outgrown email — six replies and we’re circling. Ten minutes at 2:00 '
    'to settle it? I’ll send the confirmation after.” (Names the pattern without blame, proposes '
    'the fix, promises the record. The three-reply rule, operationalized in two sentences.)')

h1(doc, 'The short-message playbook')
bullets(doc, [
    ('Routine ask →', 'email, one screen, subject = the job, act+date at the end.'),
    ('Two-minute question to a teammate →', 'chat, complete in the first message.'),
    ('Decision reached anywhere →', 'email confirmation, three numbered points (Chapter 1’s pairing).'),
    ('Mass announcement →', 'BCC or distribution tool; replies routed to a form or owner.'),
    ('Time-critical logistics →', 'text, if invited into that channel; nothing sensitive.'),
    ('Frustration →', 'voice, off platform, outside the org chart — or a walk.'),
    ('Anything you hesitated before sending →', 'that hesitation is data. Cool it overnight (Chapter 4).'),
    ('Thread past three rounds →', 'convert to voice; confirm in writing after (template 5).'),
    ('Anything decided aloud →', 'the decision confirmation, same day (template 4).'),
    ('Friday afternoon →', 'the fifteen-minute reset: close loops, nudge loops, harvest templates.'),
])

h1(doc, 'Deep dive: when the channel IS the message')
para(doc, 'A closing synthesis: channel choice is never neutral, because the medium announces the '
    'weight before the words load. A phone call about a routine matter signals “this matters more '
    'than you thought”; an email about something you always discuss in person signals distance or '
    'documentation — and the recipient will wonder which; a calendar invitation titled “quick '
    'sync” from HR is an anxiety generator regardless of its innocent content. Skilled '
    'communicators read this second-order layer before sending: not just “which channel serves '
    'this message” (Figure 4’s matrix) but “what does choosing this channel SAY?” Three habitual '
    'checks: does the channel shift itself carry news (the manager who suddenly emails what she '
    'used to say in person is communicating something — make sure it’s intended)? does the '
    'formality of the container match the stakes of the content (a termination by chat, an FYI by '
    'certified letter — both are container-content mismatches that become the story)? and is the '
    'channel choice comfortable for you but costly for them (the classic: calling because typing '
    'is slower for you, interrupting because waiting is slower for you)? The reader experiences '
    'your channel choice as part of the message because it IS part of the message — the first '
    'part, delivered before a single word.')

h1(doc, 'Journal prompts')
numbered(doc, [
    'Audit your last twenty sent messages against Figure 1. Which part is your weakest — subject, sentence one, or the call to action? Repair the three worst.',
    'Track one workday’s interruptions: every ping, every check. What did the always-on tax cost you, and which two defenses from this chapter would recover the most?',
    'Find the oldest message of yours still retrievable (any platform). Apply the permanence gradient: what does it teach you about the next ten years of your digital writing?',
    'Describe a reply-all storm, group-chat misfire, or screenshot incident you have witnessed. Which rule in this chapter was the missing one?',
    'Read your last ten messages on your phone, as their recipients did. How many survive the preview test — subject plus thirty words carrying the point?',
    'Map your team’s channel ecology: what actually lives where, versus where each thing SHOULD live by the record/coordination/live split? Draft the one-paragraph channel charter you wish existed.',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'The supervisor test compresses perfectly at this scale: could your manager forward your '
    'email — or screenshot your chat message — anywhere, as-is? Short messages are graded in this '
    'course the way inboxes grade them in practice: subject line informative, point first, one '
    'screen, ask dated, tone dialed, zero errors (Chapter 4’s last-thing check applies doubly to '
    'messages written in thirty seconds). The email signature assignment and recruitment-letter work '
    'in this unit use exactly these criteria.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('“Quick question” subject lines.', 'Fix: the question IS the subject. Five front-loaded words.'),
    ('The naked “hey” in chat.', 'Fix: first message carries the ask — complete, answerable from a phone.'),
    ('Deciding things in chat, permanently.', 'Fix: decisions graduate to email confirmation. Chat coordinates; email records.'),
    ('Reply-all as social reflex.', 'Fix: does every name need every word? Usually the sender alone does.'),
    ('CC as political armor.', 'Fix: CC informs; it does not assign, threaten, or witness. Overuse reads exactly as intended — and is remembered.'),
    ('After-hours pings from habit.', 'Fix: schedule-send. The morning inbox reads identically; the evening boundary survives.'),
    ('Venting on logged platforms.', 'Fix: voice, off platform, outside the org chart. Typed frustration is a screenshot on layaway.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Are greetings and sign-offs still required?”', 'Match the relationship and the thread’s age: first contact gets full dress (“Hi Dana, … Best, Alex”); rapid ongoing threads can drop ceremony. When unsure, one register warmer than you think — down-shifting later is graceful; up-shifting is awkward.'),
    ('“Emoji in work messages?”', 'Follow the room’s norms and the relationship, never in first contact or external formality, and never carrying load-bearing meaning. A 👍 acknowledging a chat is mainstream; one in a client apology is not.'),
    ('“How fast must I really reply?”', 'Figure 5 is the custom: acknowledge external mail same-day even if the answer comes later; answer your manager in hours; owe nothing to CC. Predictability beats raw speed — the reputation that matters is “always closes the loop.”'),
    ('“Can AI write my email?”', 'It drafts well at exactly this scale — and every Chapter 15 rule applies: verify facts, own the tone, never paste confidential content into public tools. The subject line and the ask are still decisions, and those are yours.'),
    ('“Is my personal social media really my employer’s business?”', 'Legally it depends on jurisdiction and contract; practically, Figure 7 is the answer — public is public, screenshots are forever, and hiring managers look. Curate the layer you want doing the talking.'),
    ('“My manager sends one-word replies. Should I match?”', 'Match their channel and speed preferences; keep your own completeness standards. Senior brevity is a prerogative of context (they hold the background you must spell out) — mirroring it upward usually reads as underexplaining, not efficiency. Answer the question their one word asked, fully, in three lines.'),
    ('“How many channels is too many?”', 'When the team debates where to post instead of what to decide, consolidation is overdue. The working set is three: a record channel (email/docs), a coordination channel (chat), and a live channel (calls). Every additional platform must replace one, not join them — tools multiply; attention doesn’t.'),
    ('“What about voice notes?”', 'Rich in tone, hostile to search and skimming — the recipient must consume them linearly, at your pace, often unable to play them aloud. Fine for warmth among consenting colleagues; wrong for decisions, details, or anything a future reader must find. If it matters, it needs to be text somewhere.'),
    ('“I inherited a chaotic inbox/channel culture. Where do I start?”', 'With your own output only — model the subject lines, the acknowledgments, the confirmations, without a single sermon. Culture changes are adopted from examples that visibly work, not from etiquette memos (which this chapter’s reply-all case should make permanently suspicious). After a month of modeling, propose ONE norm, in the room’s own channel, framed as an experiment.'),
    ('“Does any of this matter if my team is five people who sit together?”', 'The volumes shrink; the physics don’t. Small teams skip the record-keeping because everyone “was there” — until someone leaves, someone new arrives, or two memories of the same decision diverge in month six. The decision confirmation and the memo-to-file are cheapest exactly when teams are small enough to think they don’t need them.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 5).', 'Channel choice, subject lines, thread etiquette, and digital professionalism — the bank mirrors this guide.'),
    ('Email signature assignment.', 'Figure 1’s signature block is the spec: name, title, organization, contact, tagline — professional design without decoration.'),
    ('Recruitment letter (Week 8 companion).', 'The one-screen shape and front-loaded ask apply directly.'),
    ('Next chapter.', 'Chapter 6: positive and neutral messages — requests, replies, goodwill, and the everyday mail that builds your reputation.'),
    ('The lecture deck.', 'The Chapter 5 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Channel of record', 'the medium whose messages are archived and authoritative — in most workplaces, email.'),
    ('Subject-line formulas', 'action (verb+object+date), information (topic+takeaway), question, and thread rescue.'),
    ('One-screen rule', 'routine emails fit without scrolling; longer content graduates to an attachment with a cover note.'),
    ('Thread hygiene', 'reply-all discipline, new-topic-new-thread, To=act / CC=know, and the BCC exit ramp.'),
    ('Response-time norms', 'the customary reply windows each channel and audience expects (Figure 5).'),
    ('Permanence gradient', 'the spectrum from archived email to “disappearing” messages — all of it one screenshot from public.'),
    ('Continuous partial attention', 'the divided state produced by always-on channels (Turkle, 2015).'),
    ('Triage', 'processing messages in batches: act (<2 min), schedule, file, delete.'),
    ('Schedule-send', 'composing now, delivering at a respectful hour — boundary maintenance built into the tool.'),
    ('Professional presence', 'the curated public layer — profile, headline, activity — that interviews before you do.'),
    ('Digital body language', 'the nonverbal layer of digital channels: latency, length, punctuation, read-receipts.'),
    ('Acknowledgment with commitment', '“got it — full answer Friday”: receipt plus a date; the fifteen-second trust builder.'),
    ('Three-reply rule', 'when a thread passes three substantive rounds without converging, convert to voice — then confirm in writing.'),
    ('Memo-to-file', 'the record written for the record: dated, filed, and authoritative when memory fails.'),
    ('Escalation summary', 'the fresh-thread decision package: situation, conflict, history, recommendation, dated ask.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Email remains the channel of record, and everyone is drowning in it — the writer who costs the reader least wins (Chui et al., 2012; Radicati, 2024).',
    'A working email has six parts with one job each; the subject line states the message’s job and the first sentence delivers it.',
    'One screen for routine mail; longer content becomes an attachment with a one-paragraph cover note.',
    'Thread hygiene — reply-all discipline, To/CC clarity, new-topic-new-thread — is pollution control for a shared ecosystem.',
    'Chat coordinates at conversation speed; decisions graduate to email. Texts are for invited, time-critical logistics only.',
    'Everything on workplace systems is logged, exportable, and discoverable: write as if legal reads it, because it can.',
    'Your public digital layer interviews before you do — curate it; and manage attention like the career capital it is (Turkle, 2015).',
])

quiz(doc, [
    ('The best subject line for a message needing budget approval by Friday is:', ['“Quick question”','“Budget”','“Approve Q3 budget rev by Fri 7/10”','“IMPORTANT!!!”']),
    ('The main point of a routine email belongs:', ['In the attachment','In sentence one','After the background','In the postscript']),
    ('People in the To line versus the CC line are expected to:', ['Act versus know','Reply versus forward','Read versus skim','Approve versus reject']),
    ('Reply-all is appropriate when:', ['You feel strongly','Every recipient needs every word','Thanking the sender','Correcting the sender publicly']),
    ('When a thread’s topic drifts to something new, you should:', ['Continue — history is useful','Start a new thread with a new subject','Switch to chat','BCC everyone']),
    ('A consequential decision reached in chat should be:', ['Left in chat — it’s logged','Confirmed by email — the channel of record','Texted to the manager','Screenshotted']),
    ('Mass announcements avoid reply-all storms primarily through:', ['Polite requests in the message','BCC or no-reply distribution tools','Shorter messages','Sending after hours']),
    ('The permanence gradient teaches that workplace chat is:', ['Private between participants','Logged, exportable, and discoverable','Deleted nightly','Legally protected venting']),
    ('“Continuous partial attention” (Turkle, 2015) refers to:', ['Multitasking productivity','The divided state produced by always-on channels','A meeting technique','An email filter']),
    ('The professional response to external client email is:', ['Reply within minutes always','Acknowledge the same business day, even if the full answer comes later','Reply within a week','No norm exists']),
    ('A senior employee messaging at 9 p.m. should:', ['Expect immediate replies','Schedule-send for morning or mark it no-response-needed','Use all caps for urgency','Call instead']),
    ('The safe channel for venting workplace frustration is:', ['A private DM','A group chat of allies','Voice, off platform, outside the org chart','A disappearing-message app']),
    ('In the reply-all storm, the “STOP REPLYING ALL” messages:', ['Solved the problem','Were the problem wearing a reasonable costume','Were required by policy','Came from IT']),
    ('Your public social layer matters professionally because:', ['Employers may not look','It interviews before you do — permanent and visible','It is legally private','Only LinkedIn counts']),
], ['c','b','a','b','b','b','b','b','b','b','b','c','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Pull your three most recent subject lines. Which of Figure 2’s formulas — if any — do they follow, and what would their repairs look like?',
    'Where does your team or workplace actually decide things: meetings, email, or chat? What gets lost in that channel, and what pairing would fix it?',
    'Argue both sides: “after-hours messages with schedule-send are considerate” versus “they still normalize after-hours work.” Where do you land, and why?',
    'What is your personal permanence-gradient policy — what will you never type on a logged platform? Be specific.',
    'Design the ideal company policy for mass email. What technical and behavioral rules does it need, in what order?',
    'Your team decides things in chat and loses them there. Design the decision-export habit: who confirms, where, in what format, triggered by what?',
    'Pick one template from the appendix and adapt it to your own voice and situation. What did you change, and what did you learn was load-bearing?',
])

references(doc, [
    'Chui, M., Manyika, J., Bughin, J., Dobbs, R., Roxburgh, C., Sarrazin, H., Sands, G., & Westergren, M. (2012). The social economy: Unlocking value and productivity through social technologies. McKinsey Global Institute.',
    'Nielsen, J. (2006). F-shaped pattern for reading web content. Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/',
    'Radicati Group. (2024). Email statistics report, 2024–2028. The Radicati Group, Inc. https://www.radicati.com/',
    'Turkle, S. (2015). Reclaiming conversation: The power of talk in a digital age. Penguin Press.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch05-study-guide.docx')
finish(doc, os.path.abspath(out))
