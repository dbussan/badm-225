# Chapter 1 Study Guide — Communicating in Today's Workplace (original text, verified references)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

doc = new_doc(1, "Communicating in Today's Workplace",
    'Communication foundations, listening, nonverbal signals, culture, ethics, and professionalism.')

h1(doc, 'Why this skill compounds')
para(doc, 'Ask employers what they want most in new graduates and the answer has barely changed in '
    'decades: people who can solve problems, work in teams, and communicate. In the National Association '
    'of Colleges and Employers’ most recent Job Outlook survey, roughly nine in ten employers said they '
    'look for evidence of problem-solving, and roughly seven in ten or more want written and verbal '
    'communication skills (NACE, 2025). Notice something about that list: communication is not just one '
    'item on it — it is the medium through which the others become visible. Nobody can see your '
    'problem-solving until you explain a solution; nobody experiences your teamwork except through how '
    'you speak, write, and listen.')
para(doc, 'Communication also compounds in a way technical skills often do not. Software versions expire; '
    'the ability to make yourself understood transfers to every role you will ever hold. Strong '
    'communicators get trusted with bigger audiences and bigger decisions, which produces more practice, '
    'which produces stronger communicators. That flywheel is the quiet engine behind many careers — '
    'and this course is where you start it.')

h1(doc, 'How communication actually works')
para(doc, 'The scientific study of communication as a process traces to Claude Shannon’s work on '
    'information transmission (Shannon, 1948), and the human version keeps his basic anatomy: a sender '
    'has an idea, encodes it into words or symbols, transmits it through a channel, and a receiver '
    'decodes it and — if the sender is lucky — responds with feedback. Each stage is a place '
    'where meaning can leak.')
bullets(doc, [
    ('Encoding failures.', 'The idea in your head is translated into words that do not carry it — jargon, vagueness, or a frame the reader does not share.'),
    ('Channel failures.', 'The right message dies in the wrong medium: a sensitive conversation attempted by text, a binding agreement left verbal.'),
    ('Decoding failures.', 'The receiver reconstructs your words through their own frame of reference — their training, mood, history, and expectations — and builds a different meaning than you sent.'),
    ('Feedback failures.', 'No confirmation loop exists, so nobody discovers the misunderstanding until the deadline arrives.'),
])
para(doc, 'Two vocabulary items matter here. Noise is anything that degrades the message: physical noise '
    '(a loud vent, a bad connection), semantic noise (words the audience decodes differently than you '
    'intended), and psychological noise (stress, bias, or distraction inside the receiver). Frame of '
    'reference is the personal lens each of us decodes through. Two employees can read one memo and '
    'honestly derive two meanings — which is why skilled senders anticipate the audience, translate '
    'jargon, and invite feedback rather than assuming the message arrived intact.', bold_lead='Noise and frames.')
para(doc, 'A useful summary from the classic literature: one cannot not communicate (Watzlawick, Beavin '
    '& Jackson, 1967). Silence, delay, formatting, even who is copied on an email — all of it carries '
    'meaning to somebody. The only choice you have is whether the signals you send are deliberate.')

h1(doc, 'Choosing the channel')
para(doc, 'Channels differ in richness — how many cues they carry and how fast feedback returns. '
    'Face-to-face conversation is the richest: words, tone, expression, and instant response. Video calls '
    'come close; phone preserves tone but loses the face; email and memos are lean but create the '
    'permanent, searchable record; chat is fastest and easiest to misread.')
bullets(doc, [
    ('Choose rich channels when', 'the topic is sensitive, emotional, complex, or likely to need negotiation — bad news, performance concerns, genuine disagreement.'),
    ('Choose lean channels when', 'content is routine and factual, many people need identical information, or you need documentation.'),
    ('The professional pairing:', 'deliver hard news rich (a conversation), then confirm lean (a written summary). You get empathy and a record.'),
])

h1(doc, 'How information moves inside organizations')
para(doc, 'Formal communication flows downward (leadership to staff: goals, policies, feedback), upward '
    '(staff to leadership: status, problems, ideas), and laterally (peer to peer across teams). Each has a '
    'signature failure: downward messages arrive vaguer than they left; upward messages get filtered '
    'because nobody enjoys carrying bad news; lateral messages snag on turf. Around all of it runs the '
    'grapevine — the informal network. It is fast, inevitable, and fills every silence leadership '
    'leaves. You cannot eliminate it; you can only outrun it with fast, honest formal communication.')

h1(doc, 'Listening like a professional')
para(doc, 'In one of the most cited articles ever published on the subject, Ralph Nichols and Leonard '
    'Stevens reported that immediately after hearing someone talk, listeners retained only about half of '
    'what was said — and within eight hours, roughly a third (Nichols & Stevens, 1957). Their argument '
    'still stands: hearing is passive, but listening is a skill with technique, and hardly anyone is '
    'trained in it.')
para(doc, 'Listening runs through stages — you hear, focus, interpret, evaluate, and respond — and '
    'it fails silently in the middle: you can nod along while interpreting wrongly. The visible techniques '
    'of active listening are the fix:')
bullets(doc, [
    ('Attend fully.', 'Devices down, body turned toward the speaker. Attention is visible, and its absence is too.'),
    ('Capture, don’t transcribe.', 'Note key points and commitments; writing everything means processing nothing.'),
    ('Paraphrase.', '“So the deadline moves only if the client signs by Tuesday — did I get that right?” Confirms meaning at the cheapest possible moment: immediately.'),
    ('Ask real questions.', 'Open questions that explore, not leading questions that steer.'),
    ('Let silence work.', 'Pause before replying; speakers often add their most important sentence into that space.'),
])

h1(doc, 'Nonverbal communication')
para(doc, 'Your face, eyes, posture, gestures, voice, timing, distance, and appearance broadcast '
    'continuously, whether you script them or not. When verbal and nonverbal signals conflict, audiences '
    'tend to believe the nonverbal ones — they are harder to fake. A caution about a famous number: '
    'the oft-quoted claim that “93 percent of meaning is nonverbal” misreads Albert Mehrabian’s '
    'narrow experiments on feelings and liking (Mehrabian, 1971); the defensible lesson is not a '
    'percentage but a priority — align your delivery with your words, because misalignment reads as '
    'doubt or dishonesty.')
para(doc, 'Nonverbal communication now extends to screens: camera at eye level, decent light, visible '
    'attention on video calls; response time, formatting, and punctuation in writing. A clean, structured '
    'email is the digital equivalent of good posture.', bold_lead='On camera and in writing.')

h1(doc, 'Communicating across cultures')
para(doc, 'Anthropologist Edward T. Hall distinguished low-context cultures, where meaning lives mainly '
    'in explicit words, from high-context cultures, where meaning rides on relationships, tone, and '
    'situation (Hall, 1976). Neither style is better; each decodes the other as rude or evasive. '
    'Practical strategies: slow down the judgment when something reads as blunt or vague; write plainly '
    'and skip idioms and sports metaphors, which do not travel; confirm spoken agreements in writing; and '
    'ask people how they prefer to receive feedback — a professional question, not an awkward one.')

h1(doc, 'Ethics and professionalism')
para(doc, 'Distinguish an ethical dilemma — two defensible values in genuine conflict, such as honesty '
    'to a customer versus a confidentiality promise — from an ethical lapse: a clear wrong, chosen '
    'anyway, usually rationalized as “everyone does it.” Dilemmas deserve careful reasoning and '
    'consultation. Lapses deserve a flat no.')
para(doc, 'Because most workplace ethics decisions happen at typing speed, keep quick tests within reach:')
bullets(doc, [
    ('The publicity test.', 'Comfortable if this message appeared in the news or before your family? If not, stop.'),
    ('The reversal test.', 'Would you accept being on the receiving end?'),
    ('The whole-truth test.', 'Literally true but designed to mislead is still deception.'),
    ('The sleep test.', 'Still defending it comfortably tomorrow? Discomfort is data.'),
])
para(doc, 'Professionalism, finally, is not formality — it is predictability plus respect, shown in '
    'small repeated behaviors: deadlines met, messages acknowledged within a business day, work '
    'proofread, anger never sent, confidences kept. And treat everything you post on social media as '
    'public and permanent, because functionally it is: screenshots outlive deletions, and employers look. '
    'Worker engagement research suggests how much this everyday communication climate matters — '
    'Gallup’s global workplace studies consistently tie engagement, which is built largely through '
    'day-to-day communication with managers, to performance and wellbeing (Gallup, 2025).')

keyterms(doc, [
    ('Encoding / decoding', 'translating an idea into symbols, and reconstructing meaning from them.'),
    ('Feedback', 'the receiver’s response that tells the sender what actually landed.'),
    ('Noise', 'physical, semantic, or psychological interference that degrades a message.'),
    ('Frame of reference', 'the personal lens of experience and expectation through which each person decodes.'),
    ('Media richness', 'a channel’s capacity to carry multiple cues and immediate feedback.'),
    ('Grapevine', 'the informal, unofficial communication network in every organization.'),
    ('Active listening', 'listening with visible technique: attending, capturing, paraphrasing, questioning, pausing.'),
    ('High-context / low-context cultures', 'cultures where meaning rides mainly on situation and relationship versus mainly on explicit words (Hall, 1976).'),
    ('Ethical dilemma vs. lapse', 'two rights in conflict versus a wrong chosen anyway.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Communication is the skill employers most consistently demand — and the medium through which every other skill becomes visible.',
    'Meaning is reconstructed by the receiver, not transmitted intact; check what landed instead of assuming.',
    'Match the channel to the message: rich for sensitive and complex, lean for routine and documented — and pair them for hard news.',
    'Listening is a technique, not a trait: attend, capture, paraphrase, question, pause. Retention without technique is poor — about half, fading fast.',
    'Align nonverbal signals with words, in rooms and on screens; misalignment is believed over the words themselves.',
    'Across cultures, assume style differences before rudeness; write plainly and confirm in writing.',
    'Ethics at typing speed: publicity, reversal, whole-truth, and sleep tests. Professionalism is small behaviors, repeated.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Describe a message you sent that was decoded very differently than you intended. Which stage of the process failed, and what kind of noise was involved?',
    'What channel does your workplace or team overuse? What belongs somewhere else, and why?',
    'Which active-listening technique would change your next important conversation the most — and what makes it hard for you personally?',
    'Rewrite one jargon-heavy sentence from your field for a general audience. What semantic noise did you remove?',
    'A colleague asks you to “soften” disappointing numbers in a status update. Dilemma or lapse? Apply at least two of the four quick tests and defend your call.',
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
