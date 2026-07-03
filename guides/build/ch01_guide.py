# Chapter 1 Study Guide (expanded ~20pp) — Communicating in Today's Workplace
# Original text; verified references; original figures with alt text.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(1, "Communicating in Today's Workplace",
    'Communication foundations, listening, nonverbal signals, culture, ethics, and professionalism.')

h1(doc, 'How to use this guide')
para(doc, 'Read it once straight through, then keep it open while you work the practice questions on the '
    'course site. Each section ends with an "Apply it" box — those are not decoration; they are the '
    'chapter converted into behavior. The self-check quiz near the end tells you whether you are ready '
    'for the graded homework. Everything here is original instructor material, and every source in the '
    'reference list is a real, published work you can follow up on.')

h1(doc, 'Why this skill compounds')
para(doc, 'Ask employers what they want most in new graduates and the answer has barely changed in '
    'decades: people who can solve problems, work in teams, and communicate. In the National Association '
    'of Colleges and Employers’ most recent Job Outlook survey, roughly nine in ten employers said they '
    'look for evidence of problem-solving, and roughly seven in ten or more want written and verbal '
    'communication skills (NACE, 2025). Notice something about that list: communication is not just one '
    'item on it — it is the medium through which the others become visible. Nobody can see your '
    'problem-solving until you explain a solution. Nobody experiences your teamwork except through how '
    'you speak, write, and listen. Your work does not speak for itself; you speak for it.')
para(doc, 'Communication also compounds in a way technical skills often do not. Software versions expire; '
    'the ability to make yourself understood transfers to every role you will ever hold, in every industry, '
    'at every level. Strong communicators get trusted with bigger audiences and bigger decisions, which '
    'produces more practice, which produces stronger communicators. That flywheel is the quiet engine '
    'behind many careers — and it is available to anyone willing to treat communication as a skill with '
    'technique and reps, rather than a personality trait you either have or lack.')
para(doc, 'Consider two new analysts with identical technical ability. One writes status updates her '
    'manager can forward without edits; the other writes updates the manager must decode and rewrite. '
    'Within a year, the first analyst is presenting to clients — not because her analysis is better, but '
    'because her communication makes everyone above her faster. That is what "communication skills" '
    'means in practice: you become an amplifier for your team instead of friction.', bold_lead='A tale of two analysts.')
bullets(doc, [
    ('Apply it:', 'find one message you sent this week that needed a follow-up question to be understood. '
     'Rewrite it so the question would never have been asked. That gap — between what you sent and what '
     'was needed — is the exact skill this course trains.'),
])

h1(doc, 'How communication actually works')
para(doc, 'The scientific study of communication as a process traces to Claude Shannon’s work on '
    'information transmission (Shannon, 1948), and the human version keeps his basic anatomy: a sender '
    'has an idea, encodes it into words or symbols, transmits it through a channel, and a receiver '
    'decodes it and — if the sender is lucky — responds with feedback. The picture looks tidy. '
    'The reality is that every stage is a place where meaning leaks.')
figure(doc, os.path.join(FIG, 'process.png'),
    'Figure 1. The communication process. Meaning is reconstructed by the receiver — feedback is the only way to learn what actually landed.',
    'Diagram of the communication process: sender has an idea, encodes it into words, transmits via a channel, receiver decodes it, and meaning is reconstructed. A feedback loop returns from receiver to sender, and noise can strike at every stage.')
para(doc, 'The most important idea in this chapter — maybe in this course — hides in the last box of '
    'Figure 1. Meaning is not delivered; it is rebuilt by the receiver out of your words plus everything '
    'they already know, fear, expect, and assume. The message that matters is not the one you sent but '
    'the one they reconstructed. Professionals therefore treat every important message as unconfirmed '
    'until feedback proves otherwise. Amateurs assume; professionals check.')
para(doc, 'Where exactly do messages break?')
bullets(doc, [
    ('Encoding failures.', 'The idea in your head gets translated into words that do not carry it — jargon the audience does not share, vagueness that feels efficient to write and is expensive to read, or a frame that makes sense only from your side of the desk.'),
    ('Channel failures.', 'The right message dies in the wrong medium: a sensitive conversation attempted by text message, a binding agreement left verbal, a complex procedure buried in a chat thread.'),
    ('Decoding failures.', 'The receiver reads through their own frame of reference — training, mood, history with you, workload — and honestly derives a different meaning than you intended.'),
    ('Feedback failures.', 'No confirmation loop exists, so nobody discovers the misunderstanding until the deadline arrives with the wrong deliverable attached.'),
])
h2(doc, 'Mini-case: the safety memo nobody followed')
para(doc, 'A safety engineer emails dense technical instructions to office staff. A week later, compliance '
    'is near zero. Diagnose it with Figure 1 before reading on. The encoding failed — the memo used '
    'specialist vocabulary the audience could not decode. The channel failed — one mass email for a '
    'behavior change that needed discussion and demonstration. And the feedback loop failed — no '
    'confirmation step, so the sender learned about the breakdown a week late. The fix was unglamorous '
    'and completely effective: a plain-language rewrite, a five-minute demonstration at the staff meeting, '
    'and a one-question reply to confirm understanding. Most real communication failures are multi-point '
    'failures like this one; the model gives you a checklist for finding every leak.')
para(doc, 'One more foundational idea, from the classic clinical literature: one cannot not communicate '
    '(Watzlawick, Beavin & Jackson, 1967). Silence is a message. A three-day email delay is a message. '
    'Who you copied — and who you left off — is a message. Formatting is a message. You do not get to '
    'choose whether you are communicating; you only get to choose whether your signals are deliberate.')

h1(doc, 'Noise and frames of reference')
para(doc, 'Noise is anything that degrades a message between the idea and its reconstruction. Diagnosing '
    'the type matters, because each has a different fix.')
figure(doc, os.path.join(FIG, 'noise.png'),
    'Figure 2. Three kinds of noise — and where the fix lives in each case.',
    'Diagram of three types of noise: physical (environment problems like a loud vent, fixed by changing the environment or channel), semantic (word choice problems like jargon, fixed by rewording for the audience), and psychological (internal problems like stress or bias, fixed through timing, tone, and trust).')
para(doc, 'Physical noise interferes with the channel itself: the loud HVAC unit during the call, the '
    'glitchy connection, the cluttered slide. Fix the environment or move channels. Semantic noise lives '
    'in the words: technical terms your reader decodes differently or not at all. Fix the wording — for '
    'this audience, not for yourself. Psychological noise is static inside the receiver: stress, '
    'distraction, bias, or a bad history with the sender. No rewording fixes that; timing, tone, and '
    'rebuilt trust do.')
para(doc, 'Closely related is the frame of reference — the personal lens each of us decodes through. '
    'Your education, your experience with the topic, your culture and generation, your mood, and your '
    'history with the sender all shape what a message means to you. Two employees can read one memo and '
    'derive two honest, different meanings. Skilled senders do four things about it: they anticipate the '
    'audience (what does this reader already know, want, fear?), they translate jargon into the reader’s '
    'vocabulary, they test high-stakes messages on an outsider first, and they invite feedback so decode '
    'errors surface early and cheaply.')
bullets(doc, [
    ('Apply it:', 'take one sentence of jargon from your own field and rewrite it for a smart '
     'twelve-year-old. If you cannot, you have found the limit of your own understanding — which is '
     'exactly what your least-technical reader experiences every time you skip this step.'),
])

h1(doc, 'Choosing the channel')
para(doc, 'Channels differ in richness — how many cues they carry and how quickly feedback returns. '
    'Face-to-face conversation is the richest: words, tone, facial expression, and instant response all '
    'travel together. Video calls preserve most of that. The phone keeps tone but loses the face. Email '
    'and memos are lean — but they create the permanent, searchable record that rich channels do not. '
    'Chat is the fastest and the easiest to misread; nuance dies in it daily.')
figure(doc, os.path.join(FIG, 'richness.png'),
    'Figure 3. The media richness continuum, from richest to leanest.',
    'Horizontal continuum of communication channels from richest to leanest: face-to-face, video call, phone call, email or memo, then text or chat. Richest channels carry tone, expression, and instant feedback; leanest are fast and documented but easily misread.')
para(doc, 'Richer is not better — richer is richer. Calling a meeting to announce that timesheets are '
    'due Friday wastes twelve people’s hour; texting someone that their project is cancelled wounds them '
    'and you. The skill is matching the channel to the message, and the two questions that decide it are '
    'sensitivity and the need for a record.')
figure(doc, os.path.join(FIG, 'matrix.png'),
    'Figure 4. A channel-choice matrix: let sensitivity and the need for documentation pick the medium.',
    'Two-by-two matrix for channel choice. Axes are sensitivity/complexity and need for a permanent record. Routine with no record needed: chat or a quick call. Routine with record needed: email or memo. Sensitive or complex: rich channel first, face-to-face or video. Sensitive and binding: rich conversation followed by written confirmation.')
para(doc, 'The professional pairing in the lower-right cell deserves emphasis: deliver hard news rich, '
    'confirm lean. The conversation carries the empathy and absorbs the questions; the written follow-up '
    'creates the record and prevents the "that’s not what you said" dispute. One channel cannot do both '
    'jobs; two channels in the right order can.', bold_lead='The pairing.')
h2(doc, 'You make the call')
numbered(doc, [
    'A performance problem with a teammate → rich first: private face-to-face or video conversation; written summary afterward.',
    'New parking policy effective next month → lean: email or intranet post. Routine, factual, needs a record.',
    'Department restructuring announcement → rich first (live meeting with questions), written follow-up for the record.',
    'Reminder that timesheets are due Friday → lean and brief: chat or email. Nobody needs a meeting for this.',
])

h1(doc, 'How information moves inside organizations')
para(doc, 'Formal communication flows in three directions, and each fails in a signature way. Downward '
    'communication (leadership to staff: goals, policies, feedback) tends to arrive vaguer than it left — '
    'each management layer compresses and reinterprets. Upward communication (status, problems, ideas) '
    'gets filtered, because nobody enjoys carrying bad news to the person who writes their review; '
    'organizations that punish messengers end up surprised by problems everyone below already knew about. '
    'Lateral communication (peer to peer, across teams) snags on turf and inconsistent records.')
para(doc, 'Around all of it runs the grapevine — the informal network of hallway conversations, direct '
    'messages, and lunch tables. Three things are reliably true of it: it is fast, it is inevitable, and '
    'it fills every silence leadership leaves. You cannot eliminate a grapevine; you can only outrun it '
    'with formal communication that is faster and more honest than the rumor. For your own career, '
    'treat the grapevine as a listening post, not a broadcasting station: what you hear there is useful '
    'context; what you say there travels with your name attached.')

h1(doc, 'Listening like a professional')
para(doc, 'In one of the most cited articles ever published on the subject, Ralph Nichols and Leonard '
    'Stevens reported that immediately after hearing someone talk, listeners retained only about half of '
    'what was said — and within eight hours, roughly a third (Nichols & Stevens, 1957). Their central '
    'argument has aged remarkably well: hearing is passive, listening is a learnable skill with visible '
    'technique, and almost nobody is ever trained in it. In a course full of writing instruction, '
    'remember that professionals spend more of their day listening than doing anything else with '
    'language.')
figure(doc, os.path.join(FIG, 'listening.png'),
    'Figure 5. The stages of listening. The middle stages fail silently.',
    'Five-stage listening process: hear (passive), focus (attention chooses), interpret (meaning assigned), evaluate (fact versus opinion), respond and retain (what you keep). Callout notes that listening fails silently in the middle stages — you can nod while interpreting wrongly.')
para(doc, 'The stages explain the two classic failure points. Focus fails because minds process words '
    'several times faster than people speak, and the spare capacity wanders — to your phone, your reply, '
    'your lunch. Interpretation fails because it runs through your frame of reference, quietly assigning '
    'meanings the speaker never intended, while your face keeps nodding. Both failures are invisible '
    'from the outside, which is why the fix must be visible technique:')
bullets(doc, [
    ('Attend fully.', 'Devices down, body turned toward the speaker, eye contact on. Attention is visible — and so is its absence. Spend the spare mental capacity summarizing and anticipating instead of drifting.'),
    ('Capture, don’t transcribe.', 'Note key points, decisions, and commitments. Writing everything means processing nothing.'),
    ('Paraphrase.', '“So the deadline moves only if the client signs by Tuesday — did I get that right?” Ten words that catch misunderstanding at the cheapest possible moment: immediately, while the speaker is still in the room.'),
    ('Ask real questions.', 'Open questions that explore (“what led to that?”), not leading questions that steer (“don’t you think we should…?”).'),
    ('Let silence work.', 'Pause before replying. Speakers routinely add their most important sentence into that space — the concern, the caveat, the real reason.'),
])
para(doc, 'A manager who paraphrases in meetings gives everyone else permission to do it, and within '
    'weeks "let me play that back" becomes the team’s cheapest quality-control system. Technique '
    'spreads — model it.', bold_lead='Culture note.')

h1(doc, 'Nonverbal communication')
para(doc, 'Your face, eyes, posture, gestures, voice, timing, distance, and appearance broadcast '
    'continuously, whether you script them or not. Audiences read these channels constantly and — when '
    'verbal and nonverbal signals conflict — tend to believe the nonverbal ones, on the sensible theory '
    'that they are harder to fake. A confident report delivered with slumped shoulders and a flat voice '
    'reads as doubt, whatever the words say.')
para(doc, 'A caution about a famous number: the oft-quoted claim that “93 percent of meaning is '
    'nonverbal” misreads Albert Mehrabian’s narrow experiments about feelings and liking under '
    'contradictory signals (Mehrabian, 1971). Real communication does not obey a fixed percentage. The '
    'defensible lesson is a priority, not a statistic: align your delivery with your words, because '
    'misalignment is what audiences believe.', bold_lead='About that 93% myth.')
h2(doc, 'The channels, briefly')
bullets(doc, [
    ('Face and eyes.', 'Expression and eye contact carry attitude and confidence — the first thing audiences read, and the thing cameras crop or exaggerate.'),
    ('Posture and gesture.', 'Open posture signals engagement; folded arms and turned shoulders read as resistance whether or not you mean them that way.'),
    ('Voice.', 'Tone, pace, volume, and pauses — paralanguage — can invert the literal meaning of a sentence (“great job”).'),
    ('Time.', 'Punctuality, response speed, and how much time you give someone are read as respect or its absence.'),
    ('Space and appearance.', 'Distance, setting, dress, and your video background frame a message before a single word lands.'),
])
h2(doc, 'On camera and in writing')
para(doc, 'Video meetings compress the nonverbal channels into a rectangle: camera at eye level, decent '
    'light, visible attention (not visible typing), mute discipline, and patient turn-taking do the work '
    'that posture and eye contact do in a room. And writing — yes — has nonverbals too: response time '
    'signals priority; formatting is posture (a clean, structured email is the digital equivalent of '
    'standing up straight); ALL CAPS, terse one-liners, and stacked exclamation marks carry tone you may '
    'not intend. Emoji follow the norms of the room; when unsure, leave them out.')

h1(doc, 'Communicating across cultures')
para(doc, 'Anthropologist Edward T. Hall distinguished low-context cultures, where meaning lives mainly '
    'in the explicit words, from high-context cultures, where meaning rides on relationship, tone, and '
    'situation (Hall, 1976). In low-context settings, directness is respect and the contract carries the '
    'weight; in high-context settings, indirectness is respect and trust carries the weight. Neither '
    'style is better. Each decodes the other as rude or evasive — the blunt email reads as hostile in '
    'one direction, the diplomatic non-answer reads as slippery in the other.')
figure(doc, os.path.join(FIG, 'context.png'),
    'Figure 6. Hall’s context continuum. Neither end is “correct” — but each misreads the other.',
    'Continuum from low-context to high-context communication styles based on Edward T. Hall. Low-context: meaning lives in explicit words, directness equals respect, contracts carry the weight. High-context: meaning rides on relationship, tone, and situation; indirectness equals respect; trust carries the weight.')
para(doc, 'Working strategies for global and diverse teams:')
bullets(doc, [
    ('Slow down the judgment.', 'When a message reads as rude or evasive, first ask whether you are watching a style difference rather than a character flaw.'),
    ('Write plainly.', 'Short sentences; no idioms or sports metaphors — “touch base,” “home run,” and “punt” do not travel.'),
    ('Confirm in writing.', 'After spoken agreements, a short written summary catches decode errors gently, before they compound.'),
    ('Respect the calendar and the clock.', 'Holidays, workweeks, and punctuality norms differ; assume nothing.'),
    ('Ask, don’t assume.', '“How do you prefer to receive feedback?” is a professional question, not an awkward one — and the answers will surprise you.'),
])

h1(doc, 'Ethics at typing speed')
para(doc, 'Most workplace ethics decisions are not dramatic boardroom moments; they happen at typing '
    'speed — how to word the status update, whether to copy the manager, how to describe the delay. '
    'Start by distinguishing an ethical dilemma from an ethical lapse. A dilemma is two defensible '
    'values in genuine conflict: honesty to a customer versus a confidentiality promise; transparency '
    'versus a teammate’s privacy. Dilemmas deserve careful reasoning, consultation, and documentation. '
    'A lapse is a clear wrong, chosen anyway, and usually rationalized in the moment: “everyone does '
    'it,” “just this once,” “nobody will check.” Lapses deserve a flat no — and most career-ending '
    'events are lapses that started small.')
para(doc, 'Because these choices arrive mid-keystroke, keep quick tests within reach:')
bullets(doc, [
    ('The publicity test.', 'Would you be comfortable if this message appeared in the news, or in front of your family? If not, stop.'),
    ('The reversal test.', 'Would you accept being on the receiving end of this?'),
    ('The whole-truth test.', 'Is it literally true but designed to mislead? Deception by selection is still deception.'),
    ('The sleep test.', 'Will you still defend it comfortably tomorrow morning? Discomfort is data.'),
])

h1(doc, 'Professionalism: the daily behaviors that build trust')
para(doc, 'Professionalism is not formality — it is predictability plus respect, demonstrated in small '
    'repeated behaviors. Reliability: deadlines met, promises kept, meetings attended on time; trust is '
    'built on boring consistency. Responsiveness: messages acknowledged within a business day, even when '
    'the full answer comes later. Polish: everything proofread — a typo in your email is a smudge on '
    'your credibility, fair or not. Composure: never send angry; draft it if you must, then wait, edit, '
    'or delete. Discretion: what colleagues tell you in confidence stays in confidence.')
para(doc, 'Treat everything you post as public and permanent — because functionally it is. Screenshots '
    'outlive deletions; the delete button removes your copy, not everyone else’s; and employers look. '
    'The same permanence cuts the other way, though: a thoughtful professional presence is a standing '
    'portfolio that can demonstrate judgment and expertise before you ever walk into the interview.',
    bold_lead='Social media.')
para(doc, 'Remote and hybrid work raise the stakes on all of this. Distributed teams cannot see effort, '
    'so visible written updates replace the hallway; decisions made in calls need two-line written '
    'summaries or they evaporate; messages should be answerable hours later without a clarifying '
    'question. Workplace research consistently ties employee engagement — built largely through '
    'day-to-day communication with managers — to performance and wellbeing (Gallup, 2025). '
    'Communication climate is not a soft extra; it is the operating system of modern work.',
    bold_lead='Remote work.')
para(doc, 'One more thing about the modern workplace: AI writing tools now draft emails, summaries, and '
    'reports in seconds. Used well, they raise the floor of writing quality — but the judgment layer '
    'stays human: knowing your reader, verifying facts, and owning what goes out under your name. '
    'Chapter 15 of this course covers using AI professionally, in depth.', bold_lead='A note on AI.')

h1(doc, 'Worked examples: three everyday messages, fixed')
h2(doc, '1. The email makeover')
para(doc, 'Before: “Per my last email, the aforementioned deliverables remain outstanding. It is '
    'imperative that all stakeholders effectuate completion of their respective action items at their '
    'earliest convenience, as failure to do so may negatively impact downstream timelines.”')
para(doc, 'Diagnose it: semantic noise everywhere (“effectuate,” “aforementioned”), no clear actor, no '
    'clear deadline, and a passive-aggressive opener (“per my last email”) that adds psychological noise '
    'for anyone who missed the first message. The reader must decode who owes what by when — which '
    'means many readers will not.')
para(doc, 'After: “Hi team — three items from the March plan are still open: the budget table (Sam), '
    'the vendor quotes (Priya), and the draft slides (me). Could we each post ours to the shared folder '
    'by Thursday noon? That keeps Friday’s review on schedule. Thanks!” Same facts. Named owners, one '
    'deadline, one reason, zero decoding required — and the tone builds the relationship instead of '
    'taxing it.')
h2(doc, '2. The confirmation email (the rich-then-lean pairing in practice)')
para(doc, 'You just finished a difficult conversation — a scope change, a missed deadline, a '
    'performance concern. Within a few hours, send the lean half of the pairing: “Thanks for talking '
    'this through today. Confirming what we agreed: (1) the delivery date moves to May 12; (2) I’ll '
    'send revised specs by Friday; (3) we’ll check in briefly each Monday until launch. If I’ve '
    'misstated anything, tell me and I’ll correct it.” Three numbered points, one invitation to correct '
    'the record. This template converts a fragile verbal understanding into a durable shared one, and '
    'the closing line is the feedback loop from Figure 1, built directly into the message.')
h2(doc, '3. The status update your manager can forward')
para(doc, 'Weak: “Working on the report, going okay, some issues with the data but handling it.” '
    'Nothing here can be acted on, forwarded, or remembered. Strong: “Report is 70% drafted, on track '
    'for Friday. One risk: the Q2 data from vendor feed has gaps; I’ve requested the corrected file '
    '(due Wednesday) and will flag by Thursday if it slips.” Progress, date, named risk, plan, and a '
    'promise about when you will communicate next. Upward communication that carries bad news early and '
    'specifically is rare enough that it becomes your reputation.')

h1(doc, 'Your first 90 days: a communication playbook')
para(doc, 'Every principle in this chapter compresses into a routine you can run in any new job, '
    'internship, or team:')
numbered(doc, [
    'Week one, listen deliberately: in every meeting, capture who owns what and paraphrase once. You will learn the team’s real map faster than any org chart shows it.',
    'Learn the channel culture before you assert your own: does this team decide in meetings, in email, or in chat? Match it first; suggest improvements after you have credibility.',
    'Find each key person’s frame of reference: ask your manager “how do you prefer updates — format and frequency?” It is one question, and almost nobody asks it.',
    'Establish your reliability signature early: acknowledge every request within a business day, and never let a deadline pass silently — communicate slips before they land.',
    'Write your first status updates in the forwardable format above. You are training the organization in what to expect from your name in an inbox.',
    'Apply the publicity test to everything you post or send during your probation period — and after it.',
])

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('Assuming the message arrived intact.', 'Fix: build the feedback loop into the message itself — “reply with your date” beats “let me know.”'),
    ('Choosing channels by personal comfort.', 'Fix: choose by sensitivity and need-for-record (Figure 4), not by what feels easiest to you.'),
    ('Writing for yourself instead of the reader.', 'Fix: before sending, reread once as the least-informed person on the thread.'),
    ('Listening to reply instead of to understand.', 'Fix: paraphrase before you respond; it forces processing.'),
    ('Sending while emotional.', 'Fix: draft, wait, edit — anger is a drafting tool, never a sending strategy.'),
    ('Treating culture-style differences as character flaws.', 'Fix: curiosity first; Hall’s continuum before judgment.'),
])

h1(doc, 'Case study: the Riverside account')
para(doc, 'Read the case, answer the four questions, then compare with the analysis that follows.')
para(doc, 'Dana manages the Riverside account at a mid-size consulting firm. On Monday, a senior '
    'analyst tells her in the hallway that the client’s data migration is “behind, but probably fine.” '
    'Dana, buried in another project, replies “okay, keep me posted” and moves on. On Wednesday, the '
    'analyst sends a long technical email describing schema conflicts; Dana skims it between meetings, '
    'decodes “schema conflicts” as routine engineering noise, and files it. On Friday morning, the '
    'client’s operations director calls Dana’s boss directly: the migration has slipped two weeks, '
    'month-end reporting is at risk, and “nobody told us.” By noon, Dana is in a conference room '
    'explaining what happened. The analyst is upset too — “I did tell her. Twice.”')
numbered(doc, [
    'Trace the failures using the communication process model. Where did encoding, channel, decoding, and feedback each break down?',
    'What kinds of noise were involved in the Wednesday email?',
    'Who should have chosen a richer channel, and when?',
    'Draft the two-sentence message Dana should have sent the client on Wednesday.',
])
h2(doc, 'Case analysis')
para(doc, 'The hallway update failed at encoding (“behind, but probably fine” carries no size, cause, or '
    'date) and at feedback — Dana’s “keep me posted” confirmed nothing. The Wednesday email failed on '
    'channel (a two-week slip is not an FYI email; it is a conversation) and on semantic noise: “schema '
    'conflicts” encoded a business problem in engineering vocabulary, so Dana decoded it as routine. '
    'Both parties own part of the breakdown: the analyst never said the consequence — “this slips '
    'month-end reporting by two weeks” — and Dana never paraphrased or asked the question that would '
    'have surfaced it (“what does this mean for the client’s deadline?”). And the client heard nothing '
    'at all, which converted a manageable delay into a trust problem: the grapevine — in this case, the '
    'client’s own escalation — outran the formal channel. Dana’s Wednesday message should have been '
    'the rich-then-lean pairing: a call to the operations director, then two sentences in writing: '
    '“Following up on our call: the migration is running about two weeks behind due to data-structure '
    'conflicts we found this week. Here is the recovery plan and revised timeline; I will update you '
    'every Tuesday until we are back on track.” Bad news, early, with a plan — the most trust-building '
    'message in business.')

h1(doc, 'Listening self-assessment')
para(doc, 'Score yourself honestly: 2 = usually, 1 = sometimes, 0 = rarely. Total below.')
numbered(doc, [
    'In conversations, my devices are down and out of reach.',
    'I can restate the other person’s main point to their satisfaction before I argue with it.',
    'I take brief notes on decisions and commitments, not transcripts.',
    'I ask at least one open question before offering my view.',
    'I let a beat of silence pass after someone finishes speaking.',
    'I catch myself when I start rehearsing my reply mid-sentence — and return to listening.',
    'I check my interpretation of emotionally loaded messages before acting on them.',
    'I remember and follow up on things people told me weeks ago.',
    'In video meetings, I am visibly attentive (camera on, not typing).',
    'People bring me bad news early — a sign they expect to be heard, not punished.',
])
para(doc, 'Scoring: 16–20, you are the listener people describe when they praise a colleague; keep '
    'modeling it. 10–15, solid foundation — pick the two lowest items and practice only those for two '
    'weeks. Below 10, start with items 1 and 2 alone; they carry most of the value. Retake this after '
    'the course’s midpoint and compare.')

h1(doc, 'Channel playbook: common messages, recommended channels')
bullets(doc, [
    ('Routine reminder or logistics.', 'Chat or brief email. No meeting.'),
    ('Weekly status to your manager.', 'Email in a forwardable format (progress, date, risk, plan).'),
    ('Bad news to a client or stakeholder.', 'Call or meeting first, written confirmation the same day.'),
    ('Performance feedback.', 'Private, face-to-face or video; written summary only if formal.'),
    ('Policy or process change (minor).', 'Email or intranet post; anticipate the top three questions in it.'),
    ('Policy change (major or emotional).', 'Live meeting with Q&A first, then the written version.'),
    ('Brainstorming or genuine disagreement.', 'Live conversation; chat threads escalate and harden positions.'),
    ('Binding agreements, scope, or money.', 'Always ends in writing, whatever channel it started in.'),
    ('Recognition and thanks.', 'Public channel for the praise; specifics make it land.'),
    ('Anything you drafted angry.', 'No channel today. Reread tomorrow.'),
])

h1(doc, 'Put it to work this week')
numbered(doc, [
    'In your next conversation that matters, paraphrase once before replying. Notice what it catches.',
    'Audit your last ten sent messages: for each, was the channel chosen or just habitual? Move one recurring message type to a better channel.',
    'Find the semantic noise: rewrite one jargon-heavy sentence from your field for a general reader.',
    'Watch one speaker you admire and list two nonverbal habits worth stealing.',
    'Run the publicity test on one message before sending it. If it changes what you write, sit with that.',
])

keyterms(doc, [
    ('Encoding / decoding', 'translating an idea into symbols, and reconstructing meaning from them.'),
    ('Feedback', 'the receiver’s response that reveals what actually landed.'),
    ('Noise', 'physical, semantic, or psychological interference that degrades a message.'),
    ('Frame of reference', 'the personal lens of experience and expectation through which each person decodes.'),
    ('Media richness', 'a channel’s capacity to carry multiple cues and immediate feedback.'),
    ('Downward / upward / lateral communication', 'formal information flows from leadership, to leadership, and across peers — each with its signature failure.'),
    ('Grapevine', 'the informal, unofficial communication network in every organization — fast, inevitable, and fed by silence.'),
    ('Active listening', 'listening with visible technique: attending, capturing, paraphrasing, questioning, pausing.'),
    ('Paralanguage', 'the vocal nonverbals — tone, pace, volume, pause — that ride on top of words.'),
    ('High-context / low-context cultures', 'cultures where meaning rides mainly on situation and relationship versus mainly on explicit words (Hall, 1976).'),
    ('Ethical dilemma vs. lapse', 'two defensible values in conflict, versus a clear wrong chosen anyway.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Communication is the skill employers most consistently demand — and the medium through which every other skill becomes visible (NACE, 2025).',
    'Meaning is reconstructed by the receiver, not transmitted intact. Check what landed; never assume.',
    'Noise comes in three types — physical, semantic, psychological — and each has a different fix.',
    'Match the channel to the message: rich for sensitive and complex, lean for routine and documented; pair them (rich then lean) for hard news.',
    'Information flows down, up, and laterally, each failing in signature ways; the grapevine fills every silence leadership leaves.',
    'Listening is technique, not temperament: attend, capture, paraphrase, question, pause. Untrained retention is poor — about half, fading fast (Nichols & Stevens, 1957).',
    'When words and body language conflict, audiences believe the body. Align them — in rooms, on camera, and in text.',
    'Across cultures, assume style differences before rudeness; write plainly and confirm in writing (Hall, 1976).',
    'Ethics at typing speed: publicity, reversal, whole-truth, and sleep tests. Professionalism is small behaviors, repeated.',
])

quiz(doc, [
    ('The receiver’s verbal or nonverbal response to a message is called:', ['Encoding','Feedback','Channel noise','Decoding']),
    ('A manager must discuss a sensitive performance problem. The best first channel is:', ['A text message','A group email','A face-to-face or video conversation','A comment in team chat']),
    ('Jargon that the audience cannot decode is an example of:', ['Physical noise','Semantic noise','Psychological noise','Feedback failure']),
    ('“One cannot not communicate” means:', ['Everyone must speak in meetings','Silence, delay, and formatting also carry meaning','Communication is impossible','Email is mandatory']),
    ('The professional pairing for delivering hard news is:', ['Lean then rich','Rich conversation, then written confirmation','Written memo only','Announce it on the grapevine']),
    ('Nichols and Stevens (1957) found that immediately after listening, people retain about:', ['90 percent','Two-thirds','Half','Ten percent']),
    ('When verbal and nonverbal signals conflict, listeners usually believe:', ['The words','The nonverbal signals','Neither','Whichever came first']),
    ('In a high-context culture, meaning relies most on:', ['Explicit written words','Relationships, tone, and situation','Legal contracts','Bullet points']),
    ('An ethical dilemma differs from a lapse because a dilemma involves:', ['A clearly illegal act','Two defensible values in genuine conflict','Simple carelessness','No consequences']),
    ('The upward communication flow most commonly fails because:', ['Leaders talk too much','Bad news gets filtered on its way up','Email is slow','Staff have no opinions']),
], ['b','c','b','b','b','c','b','b','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Describe a message you sent that was decoded very differently than you intended. Which stage of the process failed, and what kind of noise was involved?',
    'What channel does your workplace or team overuse? What belongs somewhere else, and why?',
    'Which active-listening technique would change your next important conversation the most — and what makes it hard for you personally?',
    'Rewrite one jargon-heavy sentence from your field for a general audience. What semantic noise did you remove?',
    'A colleague asks you to “soften” disappointing numbers in a status update. Dilemma or lapse? Apply at least two of the four quick tests and defend your call.',
    'Where does your own communication sit on Hall’s context continuum — and how does that shape how you read people from the other end of it?',
])

references(doc, [
    'Gallup. (2025). State of the Global Workplace: 2025 report. Gallup Press. https://www.gallup.com/workplace/',
    'Hall, E. T. (1976). Beyond culture. Anchor Press/Doubleday.',
    'Mehrabian, A. (1971). Silent messages. Wadsworth.',
    'National Association of Colleges and Employers. (2025). Job Outlook 2025. NACE. https://www.naceweb.org/',
    'Nichols, R. G., & Stevens, L. A. (1957, September). Listening to people. Harvard Business Review, 35(5), 85–92. https://hbr.org/1957/09/listening-to-people',
    'Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27(3), 379–423.',
    'Watzlawick, P., Beavin, J. H., & Jackson, D. D. (1967). Pragmatics of human communication: A study of interactional patterns, pathologies, and paradoxes. W. W. Norton.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch01-study-guide.docx')
finish(doc, os.path.abspath(out))
