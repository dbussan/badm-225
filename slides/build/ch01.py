# Chapter 1 — Communicating in Today's Workplace (36 slides, original content)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 1"
prs = new_deck()
i = 0

def nxt():
    global i; i += 1; return i

# 1 — title
s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Communicating in Today's Workplace",
    "Communication foundations · listening · nonverbal signals · ethics · professionalism", D)
notes(s, "Welcome to Chapter 1. This deck covers why communication is the most portable career skill, how the communication process works, and the habits of professional communicators.")
nxt()

# 2 — objectives
s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Explain", "the communication process and identify where messages break down."),
    ("Choose", "the right channel for a message based on richness, sensitivity, and the need for a record."),
    ("Listen", "actively — and prove it with paraphrase and follow-up questions."),
    ("Read", "nonverbal signals and manage the ones you send, in person and on camera."),
    ("Apply", "quick ethics tests to everyday workplace decisions."),
    ("Present", "yourself professionally in every channel, including social media."),
], D, nxt())
notes(s, "Learning objectives. Each maps to a section of this deck and to the practice questions on the course site.")

# 3 — why it pays
s = stat_slide(prs, "The most portable skill you will ever build", "#1",
    "Communication consistently tops employer surveys of the skills they want most — across industries and job titles.",
    [("It travels.", "Technical tools change; the ability to write, speak, and listen clearly moves with you to every job you will ever hold."),
     ("It compounds.", "Strong communicators get trusted with bigger audiences, bigger decisions, and bigger teams."),
     ("It is visible.", "Most of what your manager and colleagues know about your thinking arrives through what you write and say."),
    ], D, nxt())
notes(s, "Employer surveys — NACE and similar — routinely place communication at or near the top of desired skills. The point is not one statistic; it is that this skill is portable, compounding, and visible.")

# 4 — section 1
s = section_slide(prs, "01", "How communication actually works",
    "A message seems simple — until you watch how many places it can fail.", D, nxt())
notes(s, "Section 1: the communication process model.")

# 5 — the model
s = flow_slide(prs, "The communication process", [
    ("Sender has an idea", "You know what you mean — the idea exists only in your head."),
    ("Encode", "You translate the idea into words, images, numbers, or gestures."),
    ("Transmit via channel", "Email, call, meeting, chat, report — the carrier of the message."),
    ("Decode", "The receiver translates your words back into meaning — through their frame of reference."),
    ("Feedback", "The receiver responds; only now do you learn what actually landed."),
], D, nxt(), note_text="Meaning is never 'sent.' It is reconstructed by the receiver — which is why skilled communicators check what landed instead of assuming.")
notes(s, "Walk each stage. Emphasize: the receiver reconstructs meaning; the message that matters is the one that was received, not the one that was sent.")

# 6 — frame of reference
s = two_col_slide(prs, "Frame of reference: why the same memo reads two ways",
    "What shapes a frame of reference", [
        "Education, training, and vocabulary",
        "Experience with the topic — expert vs. first-timer",
        "Culture, language, and generation",
        "Mood, workload, and history with the sender",
    ],
    "What skilled senders do about it", [
        ("Anticipate.", "Ask: what does this reader already know? What do they fear or want?"),
        ("Translate.", "Replace jargon with the reader's vocabulary."),
        ("Test.", "For high-stakes messages, have an outsider read it first."),
        ("Invite feedback.", "Make it easy for the receiver to ask, push back, or confirm."),
    ], D, nxt())
notes(s, "Two employees can decode one memo differently because each decodes through their own experience. The fix is sender-side: anticipate, translate, test, invite feedback.")

# 7 — noise
s = icon_rows_slide(prs, "Noise: everything that degrades the message", [
    ("🔊", "Physical noise", "A loud HVAC unit on the call, a glitchy connection, a cluttered slide — interference in the channel itself."),
    ("📖", "Semantic noise", "Jargon, vague wording, or a term the audience decodes differently than you intended."),
    ("🧠", "Psychological noise", "Stress, distraction, bias, or a bad history with the sender — static inside the receiver."),
], D, nxt(), kicker="Diagnose which kind of noise you are fighting — each has a different fix.")
notes(s, "Physical noise: fix the environment or channel. Semantic: fix the wording. Psychological: fix timing, tone, and trust. Ask students for one example of each from their own week.")

# 8 — one message, many failures (scenario)
s = bullets_slide(prs, "Case: the safety memo nobody followed", [
    ("The situation:", "A safety engineer emails dense technical instructions to office staff. A week later, compliance is near zero."),
    ("Encoding failure —", "the memo used specialist vocabulary the audience could not decode (semantic noise)."),
    ("Channel failure —", "one mass email for a behavior change that needed discussion and demonstration."),
    ("Feedback failure —", "no confirmation loop, so the sender learned about the breakdown a week late."),
    ("The fix:", "plain-language rewrite, a five-minute demo at the staff meeting, and a one-question reply to confirm understanding."),
], D, nxt())
notes(s, "Run this as a diagnosis exercise before revealing the bullets: where did this message break down? Most real communication failures are multi-point failures.")

# 9 — section 2
s = section_slide(prs, "02", "Choosing the channel",
    "The same words succeed in one channel and fail in another.", D, nxt())
notes(s, "Section 2: channel selection and media richness.")

# 10 — richness continuum
s = flow_slide(prs, "The richness continuum", [
    ("Face-to-face", "Richest: words + tone + expression + instant feedback."),
    ("Video call", "Nearly as rich; watch for camera and connection limits."),
    ("Phone call", "Tone and immediacy, but no visual cues."),
    ("Email / memo", "Lean but permanent — creates the record."),
    ("Text / chat", "Fast, informal, easily misread; no nuance."),
], D, nxt(), note_text="Richer is not always better. Routine facts belong in lean, documented channels; sensitive or complex topics need rich ones.")
notes(s, "Richness = capacity to carry multiple cues and immediate feedback. The skill is matching the channel to the message, not defaulting to your comfort channel.")

# 11 — channel decision
s = two_col_slide(prs, "Match the channel to the message",
    "Choose a RICH channel when…", [
        "The topic is sensitive, emotional, or personal",
        "The message is complex or likely to raise questions",
        "You need immediate feedback or negotiation",
        "Trust is low or the news is bad",
    ],
    "Choose a LEAN channel when…", [
        "The content is routine and factual",
        "You need a permanent, searchable record",
        "Many people need identical information",
        "The receiver needs time to process before responding",
    ], D, nxt())
notes(s, "Classic pairing: deliver hard news rich (conversation), then confirm lean (written follow-up). You get empathy AND a record.")

# 12 — practice scenarios
s = icon_rows_slide(prs, "You make the call", [
    ("1", "Performance problem with a teammate", "Rich first: private face-to-face or video conversation; written summary afterward."),
    ("2", "New parking policy, effective next month", "Lean: email or intranet post — routine, factual, needs a record."),
    ("3", "Department restructuring announcement", "Rich first (live meeting with Q&A), written follow-up for the record."),
    ("4", "Reminder: timesheets due Friday", "Lean and brief: chat or email; nobody needs a meeting for this."),
], D, nxt(), kicker="For each situation: rich or lean — and in what order?")
notes(s, "Have students commit to an answer before revealing. The pattern: emotional impact and complexity push rich; routine and documentation push lean.")

# 13 — information flows
s = icon_rows_slide(prs, "How information moves inside an organization", [
    ("↓", "Downward", "Leadership to staff: goals, policies, feedback. Risk: sounds clear at the top, arrives vague at the bottom."),
    ("↑", "Upward", "Staff to leadership: status reports, problems, ideas. Risk: bad news gets filtered on the way up."),
    ("→", "Lateral", "Peer to peer across teams: coordination, requests. Risk: turf friction and inconsistent records."),
    ("◎", "The grapevine", "The informal network. Fast, inevitable, mostly accurate — and it fills every silence leadership leaves."),
], D, nxt())
notes(s, "The grapevine cannot be eliminated, only outrun: fast, honest formal communication shrinks the space rumors grow in. Upward filtering is why leaders must actively reward bad news delivered early.")

# 14 — section 3
s = section_slide(prs, "03", "Listening like a professional",
    "Most people listen to reply. Professionals listen to understand.", D, nxt())
notes(s, "Section 3: listening.")

# 15 — cost of poor listening
s = bullets_slide(prs, "Poor listening is expensive", [
    "Instructions repeated, work redone, deadlines missed — the tax on every misheard detail.",
    "Customers who feel unheard leave quietly; colleagues who feel unheard stop offering ideas.",
    "Most people retain only a fraction of what they hear — attention drifts, memory edits, assumptions fill gaps.",
    ("The upside:", "listening is a learnable skill with visible technique — not a personality trait."),
], D, nxt())
notes(s, "Frame listening as a professional skill with technique and reps, exactly like writing. The next slides give the technique.")

# 16 — listening process
s = flow_slide(prs, "What happens between hearing and remembering", [
    ("Hear", "Sound reaches you — this part is passive."),
    ("Focus", "You choose what gets attention; multitasking ends listening here."),
    ("Interpret", "You assign meaning — through your frame of reference."),
    ("Evaluate", "You judge: credible? complete? What's opinion vs. fact?"),
    ("Respond & retain", "You confirm, ask, act — and what you processed is what you keep."),
], D, nxt(), note_text="Listening fails silently at the middle stages. You can be nodding while interpreting wrongly — which is why confirmation matters.")
notes(s, "Hearing is passive; listening is five active stages. Where do most failures happen for you? Usually focus (distraction) or interpretation (assumption).")

# 17 — barriers to listening
s = two_col_slide(prs, "What gets in the way",
    "External barriers", [
        "Noise, interruptions, uncomfortable settings",
        "Devices — the open laptop during meetings",
        "Speed gap: minds process faster than people talk, so attention wanders",
    ],
    "Internal barriers", [
        "Rehearsing your reply while they're still talking",
        "Prejudging the speaker or dismissing the topic early",
        "Emotional triggers — a word lands wrong and you stop processing",
        "Faking it: nodding along while mentally absent",
    ], D, nxt())
notes(s, "The speed gap is real: we process words several times faster than people speak. Skilled listeners spend the spare capacity summarizing and anticipating, not drifting.")

# 18 — active listening techniques
s = icon_rows_slide(prs, "Active listening: the visible techniques", [
    ("👁", "Attend fully", "Devices down, eye contact on, body turned toward the speaker. Attention is visible."),
    ("✎", "Capture, don't transcribe", "Note key points and commitments — writing everything means processing nothing."),
    ("↺", "Paraphrase", "“So the deadline moves only if the client signs by Tuesday — did I get that right?” Confirms meaning on the spot."),
    ("?", "Ask real questions", "Open questions that explore, not leading questions that steer."),
    ("⏸", "Let silence work", "Pause before replying. The speaker often adds the most important sentence into that silence."),
], D, nxt())
notes(s, "Paraphrase is the highest-value habit: it catches misunderstanding at the cheapest possible moment — immediately.")

# 19 — section 4
s = section_slide(prs, "04", "Nonverbal communication",
    "Your body is broadcasting whether you script it or not.", D, nxt())
notes(s, "Section 4: nonverbal signals.")

# 20 — nonverbal categories
s = icon_rows_slide(prs, "The channels you're always transmitting on", [
    ("😐", "Face & eyes", "Expression and eye contact carry attitude and confidence — the first thing audiences read."),
    ("🧍", "Posture & gesture", "Open posture signals engagement; folded arms and turned shoulders read as resistance."),
    ("🗣", "Voice (paralanguage)", "Tone, pace, volume, and pauses — how you say it can invert what you say."),
    ("⏰", "Time", "Punctuality, response speed, and how long you give someone signal respect — or its absence."),
    ("🪑", "Space & appearance", "Distance, setting, dress, and your video background all frame the message before a word lands."),
], D, nxt())
notes(s, "Nonverbal cues are continuous and mostly involuntary — which is exactly why audiences trust them.")

# 21 — when words and body conflict
s = stat_slide(prs, "When words and body language disagree", "Body wins",
    "When verbal and nonverbal signals conflict, listeners overwhelmingly believe the nonverbal one.",
    [("Why:", "nonverbal signals are harder to fake, so audiences treat them as the honest channel."),
     ("Implication for you:", "a confident report delivered with slumped shoulders and a flat voice reads as doubt."),
     ("The fix is alignment:", "prepare your delivery like you prepare your content — posture, voice, and eye contact rehearsed alongside the words."),
    ], D, nxt())
notes(s, "Avoid fake precision (the old '93% of meaning is nonverbal' myth misquotes narrow studies). The defensible claim: in conflicts, nonverbal usually wins.")

# 22 — virtual nonverbals
s = two_col_slide(prs, "Nonverbal signals on camera and in writing",
    "On video calls", [
        "Camera at eye level; look at the lens when speaking",
        "Frame yourself: face visible, decent light, tidy background",
        "Mute discipline and patient turn-taking replace body language",
        "Being visibly present — not typing — is the new eye contact",
    ],
    "In writing (yes, text has nonverbals)", [
        "Response time signals priority",
        "Formatting is posture: clean structure reads as competence",
        "ALL CAPS, terse one-liners, and exclamation marks!!! carry tone",
        "Emoji: match the norms of the room; when unsure, leave them out",
    ], D, nxt())
notes(s, "Students underestimate written nonverbals: response latency, formatting, and punctuation all get read as attitude.")

# 23 — section 5
s = section_slide(prs, "05", "Communicating across cultures",
    "The rules you consider universal are local.", D, nxt())
notes(s, "Section 5: intercultural communication.")

# 24 — high/low context
s = two_col_slide(prs, "High-context vs. low-context communication",
    "Low-context cultures", [
        "Meaning lives in the explicit words",
        "Directness is respect; vagueness is confusing",
        "Contracts and written detail carry the weight",
        "“Say what you mean, mean what you say”",
    ],
    "High-context cultures", [
        "Meaning lives in relationships, tone, and situation",
        "Indirectness is respect; blunt refusals can insult",
        "Trust and history carry the weight",
        "“Read the room; hear what wasn't said”",
    ], D, nxt())
notes(s, "Neither style is better; each decodes the other as rude or evasive. Global teams need explicit norms about which style the team will use.")

# 25 — practical strategies
s = bullets_slide(prs, "Working across cultures without stepping on rakes", [
    ("Slow down the judgment.", "When something reads as rude or evasive, first ask whether it's a style difference."),
    ("Write plainly.", "Short sentences, no idioms or sports metaphors — “touch base” and “home run” don't travel."),
    ("Confirm in writing.", "After spoken agreements, send a short summary — it catches decode errors gently."),
    ("Watch the calendar and the clock.", "Holidays, workweeks, and norms about punctuality differ; assume nothing."),
    ("Ask, don't assume.", "“How do you prefer to receive feedback?” is a professional question, not an awkward one."),
], D, nxt())
notes(s, "Diverse teams communicate better with explicit norms. The professional move is curiosity before judgment.")

# 26 — section 6
s = section_slide(prs, "06", "Ethics and professionalism",
    "Your reputation is built one message at a time — and spent the same way.", D, nxt())
notes(s, "Section 6: ethics and professionalism.")

# 27 — ethics: dilemma vs lapse
s = two_col_slide(prs, "Ethical dilemma vs. ethical lapse — know the difference",
    "Ethical DILEMMA", [
        "Two defensible values in genuine conflict",
        "Honesty to a customer vs. loyalty to a teammate",
        "Transparency vs. a confidentiality promise",
        ("Response:", "reason carefully, consult, document"),
    ],
    "Ethical LAPSE", [
        "A clear wrong, chosen anyway",
        "Inflating numbers, taking credit, hiding an error",
        "Usually rationalized: “everyone does it,” “just this once”",
        ("Response:", "don't. And speak up when you see it."),
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "A dilemma is choosing between two rights; a lapse is choosing wrong over right. Most career-ending events are lapses that started as small rationalizations.")

# 28 — quick ethics tests
s = icon_rows_slide(prs, "Four quick tests before you hit send", [
    ("📰", "The publicity test", "Comfortable if this message appeared in the news or before your family? If not, stop."),
    ("🔁", "The reversal test", "Would you accept being on the receiving end of this?"),
    ("🧾", "The whole-truth test", "Is it literally true but designed to mislead? Deception by selection is still deception."),
    ("🌙", "The sleep test", "Still defending it comfortably tomorrow morning? Discomfort is data."),
], D, nxt())
notes(s, "Fast, memorable filters for everyday choices — expense wording, status report spin, whom to CC. Most ethics failures happen at typing speed, not in big dramatic moments.")

# 29 — professionalism
s = bullets_slide(prs, "Professionalism: the daily behaviors that build trust", [
    ("Reliability.", "Deadlines met, promises kept, meetings attended on time — trust is built on boring consistency."),
    ("Responsiveness.", "Acknowledge messages within a business day, even if the full answer comes later."),
    ("Polish.", "Proofread everything; a typo in your email is a smudge on your credibility."),
    ("Composure.", "Never send angry. Draft it, sleep on it, edit it — or delete it."),
    ("Discretion.", "What colleagues tell you in confidence stays in confidence."),
], D, nxt())
notes(s, "Professionalism is not formality — it is predictability plus respect, demonstrated in small repeated behaviors.")

# 30 — social media permanence
s = stat_slide(prs, "Social media: the permanent record you're writing", "∞",
    "Assume everything you post is public and permanent — regardless of your settings.",
    [("Screenshots outlive deletions.", "The delete button removes your copy, not everyone else's."),
     ("Employers look.", "Recruiters routinely review candidates' public profiles — before the interview."),
     ("The flip side:", "a thoughtful professional presence is an asset: it can demonstrate judgment, expertise, and communication skill before you ever walk in."),
    ], D, nxt())
notes(s, "Not a scare slide — a strategy slide. The same permanence that makes careless posts dangerous makes thoughtful posts a standing portfolio.")

# 31 — remote work habits
s = bullets_slide(prs, "Communicating when nobody can see you working", [
    ("Overcommunicate status.", "Distributed teams can't see effort — visible written updates replace the hallway."),
    ("Default to writing.", "Decisions made in calls get a two-line written summary; unwritten decisions evaporate."),
    ("Respect asynchrony.", "Write messages that can be answered hours later without a follow-up question."),
    ("Guard the rich channels.", "Use live meetings for what actually needs them: conflict, complexity, connection."),
    ("Be reachable predictably.", "Published working hours and response norms beat 24/7 availability."),
], D, nxt())
notes(s, "Remote work turns communication from a soft skill into the operating system of the job.")

# 32 — AI preview
s = bullets_slide(prs, "A word about AI — your new co-writer (and its limits)", [
    ("AI drafts fast.", "Modern AI tools produce competent first drafts of emails, summaries, and reports in seconds."),
    ("You still own the message.", "AI doesn't know your reader, your history, or your intent — the judgment layer is yours."),
    ("Verify before you trust.", "AI states errors with confidence. Facts, numbers, names: check them."),
    ("Disclose honestly.", "Follow your instructor's and employer's rules for AI use and attribution."),
    ("Coming in Chapter 15:", "using AI and AI agents professionally — as a skill, not a shortcut."),
], D, nxt())
notes(s, "Preview of Chapter 15. Framing: AI raises the floor of writing quality; your judgment sets the ceiling.")

# 33 — takeaways
s = takeaways_slide(prs, [
    "Meaning is reconstructed by the receiver — check what landed, not what you sent.",
    "Match the channel to the message: rich for sensitive and complex, lean for routine and documented.",
    "Listening is a technique: attend, capture, paraphrase, question, pause.",
    "When words and body language conflict, audiences believe the body — align them.",
    "Ethics at typing speed: publicity test, reversal test, whole truth, sleep test.",
    "Professionalism is small behaviors, repeated: reliable, responsive, polished, composed, discreet.",
], D, nxt(), site_note="Practice now: course site → Chapter 1 → Practice, then the graded homework when you're ready.")
notes(s, "Recap. Direct students to the practice site for Chapter 1 questions and writing prompts.")

# 34 — quote
s = quote_slide(prs, "Worth keeping",
    "The single biggest problem in communication is the illusion that it has taken place.",
    "attributed to George Bernard Shaw", D, nxt())
notes(s, "Widely attributed to Shaw; attribution noted as such. A good closing frame: assume the illusion, then verify.")

# 35 — discussion
s = discussion_slide(prs, "Discussion questions", [
    "Describe a message you sent that was decoded very differently than you intended. Which stage of the process failed?",
    "What channel does your workplace or team overuse? What belongs somewhere else?",
    "Which active-listening technique would change your next meeting the most — and what makes it hard to do?",
    "Find the semantic noise: rewrite one jargon-heavy sentence from your field for a general audience.",
    "A colleague asks you to 'soften' bad numbers in a status update. Dilemma or lapse? Apply the four tests.",
], D, nxt())
notes(s, "Use in live session or as async discussion-board prompts.")

# 36 — next steps (delivery-neutral: works for async, online, or in-person sections)
s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 1 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 1 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Write:", "Try one Chapter 1 writing prompt and self-check it against the model guidance."),
    ("Reflect:", "Watch one speaker you admire this week — list two nonverbal habits worth stealing."),
    ("Coming next:", "Chapter 2 — planning messages: purpose, audience, and the choices before you write a word."),
], D, nxt())
notes(s, "Delivery-neutral closing slide (no 'next class' phrasing — works for asynchronous sections). Standard pattern across all chapter decks: practice, graded work, writing, reflection, preview.")

out = os.path.join(os.path.dirname(__file__), "..", "ch01-communicating-in-todays-workplace.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", len(prs.slides.__iter__.__self__._sldIdLst))
