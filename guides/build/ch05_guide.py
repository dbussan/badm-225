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

h1(doc, 'The short-message playbook')
bullets(doc, [
    ('Routine ask →', 'email, one screen, subject = the job, act+date at the end.'),
    ('Two-minute question to a teammate →', 'chat, complete in the first message.'),
    ('Decision reached anywhere →', 'email confirmation, three numbered points (Chapter 1’s pairing).'),
    ('Mass announcement →', 'BCC or distribution tool; replies routed to a form or owner.'),
    ('Time-critical logistics →', 'text, if invited into that channel; nothing sensitive.'),
    ('Frustration →', 'voice, off platform, outside the org chart — or a walk.'),
    ('Anything you hesitated before sending →', 'that hesitation is data. Cool it overnight (Chapter 4).'),
])

h1(doc, 'Journal prompts')
numbered(doc, [
    'Audit your last twenty sent messages against Figure 1. Which part is your weakest — subject, sentence one, or the call to action? Repair the three worst.',
    'Track one workday’s interruptions: every ping, every check. What did the always-on tax cost you, and which two defenses from this chapter would recover the most?',
    'Find the oldest message of yours still retrievable (any platform). Apply the permanence gradient: what does it teach you about the next ten years of your digital writing?',
    'Describe a reply-all storm, group-chat misfire, or screenshot incident you have witnessed. Which rule in this chapter was the missing one?',
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
])

references(doc, [
    'Chui, M., Manyika, J., Bughin, J., Dobbs, R., Roxburgh, C., Sarrazin, H., Sands, G., & Westergren, M. (2012). The social economy: Unlocking value and productivity through social technologies. McKinsey Global Institute.',
    'Nielsen, J. (2006). F-shaped pattern for reading web content. Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/',
    'Radicati Group. (2024). Email statistics report, 2024–2028. The Radicati Group, Inc. https://www.radicati.com/',
    'Turkle, S. (2015). Reclaiming conversation: The power of talk in a digital age. Penguin Press.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch05-study-guide.docx')
finish(doc, os.path.abspath(out))
