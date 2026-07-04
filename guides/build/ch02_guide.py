# Chapter 2 Study Guide — Planning Business Messages (original text, verified references)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(2, 'Planning Business Messages',
    'Purpose, audience analysis, reader benefits, tone, and the decisions that happen before you write a word.')

h1(doc, 'How to use this guide')
para(doc, 'This chapter is about the invisible half of writing — the thinking that happens before '
    'drafting. Read it once through, complete the message-planner worksheet on a real message you '
    'need to send this week, then work the Chapter 2 practice questions on the course site. The '
    'self-check quiz near the end tells you whether you are ready for the graded homework.')

h1(doc, 'The most expensive sentence in business')
para(doc, 'It is the sentence that has to be sent twice. Every unclear message generates a reply asking '
    'what you meant, a correction, a meeting to untangle the confusion, or — worst — silent '
    'wrong action. Multiply that by the dozens of messages professionals send daily and you find one of '
    'the quietest costs in any organization: rework caused by writing that was fast to send and slow to '
    'understand. Planning is how you buy back that time. The minutes spent deciding what you want, who '
    'you are asking, and why they would care are repaid every time the first version of your message '
    'does its job.')
para(doc, 'Writing research backs the intuition: skilled writers differ from novices less in vocabulary '
    'than in process — they spend far more effort setting goals, representing the audience, and '
    'planning before and during composition (Flower & Hayes, 1981). Novices start typing; experts start '
    'deciding.')
figure(doc, os.path.join(FIG, 'ch2_process.png'),
    'Figure 1. The three-phase writing process. Planning carries the most weight — drafting is the fast part.',
    'Three-phase writing process diagram: Plan (purpose, audience, benefit, channel) shown as the largest phase, then Draft (get it down, not perfect), then Revise (reader’s eyes, polish, proofread).')
para(doc, 'The three phases also unbundle three different mental jobs — deciding, generating, and '
    'judging — which is exactly why drafting improves when you refuse to edit while you write, and '
    'editing improves when the draft has cooled. Chapter 3 covers drafting and Chapter 4 covers '
    'revision; this chapter is about the phase that determines whether those chapters have good material '
    'to work with.')

h1(doc, 'Purpose: one message, one job')
para(doc, 'Before drafting anything, answer the only question that matters: what should the reader know '
    'or do after reading this? Not "what do I want to talk about" — what changes in the world if this '
    'message works. Most business messages have one of two purposes: to inform (the reader knows '
    'something new and needs no action) or to persuade (the reader does something — approves, buys, '
    'changes, replies). Many failed messages die of purpose overload: three asks, two announcements, and '
    'a question, all competing in one email. One message, one job.')
figure(doc, os.path.join(FIG, 'ch2_purpose.png'),
    'Figure 2. Anatomy of a working purpose statement: who must act, what exactly they should do, and why they would want to.',
    'Diagram showing three components of a purpose statement — who must act (the reader), what exactly they should do, and why they would want to — combining into an example sentence about a director approving a software license because it saves staff hours.')
h2(doc, 'Worked examples: purpose statements')
bullets(doc, [
    ('Weak:', '“Update everyone on the project.” No actor, no action, no test for success.'),
    ('Working:', '“So that my manager approves two extra days for testing, because shipping untested risks the client relationship.”'),
    ('Weak:', '“Tell the team about the new expense system.” Inform them of what, to what end?'),
    ('Working:', '“So that every team member submits May expenses in the new system by May 31, because late entries won’t be reimbursed until July.”'),
])
para(doc, 'Notice the template hiding in the working versions: so that [reader] does [specific act] '
    'because [their reason]. If you cannot complete that sentence, you are not ready to draft — and no '
    'amount of polished prose will rescue a message that does not know its job.', bold_lead='The template.')

h1(doc, 'Audience analysis: writing for the person who is actually there')
para(doc, 'Chapter 1 established that meaning is reconstructed through the receiver’s frame of '
    'reference. Planning is where you act on that: profile the audience before you draft. Three '
    'questions cover most of it. What do they already know? (Determines vocabulary and how much '
    'background to give.) How will they feel about this message? (Receptive, neutral, resistant — '
    'this decides your organization strategy in Chapter 3.) What do they need in order to act? '
    '(Deadlines, links, authority, reassurance.)')
figure(doc, os.path.join(FIG, 'ch2_audience.png'),
    'Figure 3. Your audience is bigger than your addressee: primary, secondary, gatekeeper, and hidden readers.',
    'Concentric rings diagram of audiences: primary reader in the center who acts on the message, secondary readers who read it later such as people it is forwarded to, gatekeepers who decide whether it reaches the primary reader, and hidden readers such as legal, HR, competitors, and the public record.')
para(doc, 'The rings in Figure 3 matter because business messages travel. The email you write to one '
    'teammate gets forwarded to their manager; the memo you write today becomes evidence in next year’s '
    'dispute; the report you address to your director is skimmed by her boss. Write to the primary '
    'reader, but write in the knowledge that secondary and hidden readers exist: define terms the '
    'forwarded-to reader will not know, and never put in writing what a hidden reader should not see. '
    'The forwardability test — “could this be forwarded, unedited, without embarrassing me?” — is '
    'audience analysis compressed into one question.')

h1(doc, 'Theory corner: the rhetorical situation')
para(doc, 'The planning discipline in this chapter has ancient and modern roots. Aristotle’s Rhetoric '
    'organized persuasion around three appeals — ethos (the credibility of the speaker), pathos (the '
    'emotions and values of the audience), and logos (the logic of the argument) — and insisted that '
    'the available means of persuasion depend on the audience at hand (Aristotle, trans. 2007). '
    'Twenty-three centuries later, Lloyd Bitzer formalized the idea that discourse arises from a '
    'rhetorical situation with three parts: an exigence (the problem that calls for words), an audience '
    '(the people capable of acting on it), and constraints (rules, relationships, deadlines, and beliefs '
    'that shape what can be said) (Bitzer, 1968).')
para(doc, 'The practical translation: every message you plan sits inside a situation you did not fully '
    'choose. The exigence tells you your purpose. The audience tells you your appeals — a numbers-first '
    'CFO wants logos; a burned-once team needs ethos rebuilt before logic lands. The constraints tell '
    'you your form: what the syllabus, the contract, the culture, or the moment allows. Planning is '
    'simply reading the situation before speaking into it — and writers who skip it are answering a '
    'question nobody asked, in a voice the room does not trust, at a length the moment will not bear.')

h1(doc, 'The you-view: the reader is the main character')
para(doc, 'The single most visible mark of a planned message is that it faces the reader. Writer-view '
    'prose reports what I did and we decided; you-view prose states what the reader gets, owes, or can '
    'do. It is not cosmetic — it is the purpose statement (“why would they want to?”) surfacing in the '
    'grammar.')
figure(doc, os.path.join(FIG, 'ch2_youview.png'),
    'Figure 4. Writer-view to you-view: the same facts, re-anchored on the reader.',
    'Before-and-after panel showing writer-view sentences transformed into you-view sentences. Example: “We are pleased to announce our new evening hours” becomes “You can now shop weeknights until 9 p.m.”; “I have approved your request” becomes “Your request is approved — your new hours begin Monday.”')
para(doc, 'Two cautions keep the you-view honest. First, it is not about sprinkling the word “you” — '
    'it is about organizing the content around reader benefit; “you will be terminated” is technically '
    'you-view and diplomatically radioactive. Second, in negative or accusatory contexts, competent '
    'writers pivot away from “you” precisely to avoid blame language (“the report needs sources” '
    'rather than “you forgot the sources”). The principle underneath both: face the reader’s '
    'interests, protect the reader’s dignity.')

h1(doc, 'Tone: one voice, dialed to the occasion')
para(doc, 'Tone is the reader’s impression of your attitude, and it is planned, not accidental. The '
    'reliable model is a dial, not a costume change: the same professional voice, adjusted for '
    'formality by occasion.')
figure(doc, os.path.join(FIG, 'ch2_tone.png'),
    'Figure 5. The formality dial. Same voice, adjusted to the occasion — never two personalities.',
    'Horizontal formality spectrum from most formal (formal report: no contractions, precise, documented) through client letter and internal email to most casual (team chat: contractions, first names, emoji if appropriate).')
bullets(doc, [
    ('Prefer positive framing.', '“Your order ships Friday” beats “We cannot ship before Friday” — identical facts, opposite experience.'),
    ('Retire the fossils.', '“Per my last email,” “as per,” “please be advised,” “enclosed please find” — inherited noise that adds formality without adding respect.'),
    ('Use bias-free language.', 'Gender-neutral job titles, person-first descriptions, and names/pronouns people actually use — precision and respect, which are the same professional value.'),
    ('Match the reader’s stakes, not your mood.', 'Cheerful tone on a message about someone’s billing error reads as indifference; measured tone earns trust.'),
])

h1(doc, 'Writing for the skeptical reader')
para(doc, 'Receptive audiences forgive planning shortcuts; skeptical ones punish them. When you '
    'anticipate resistance — budget requests, policy changes, anything that costs the reader time, '
    'money, or comfort — plan the objections before you draft.')
figure(doc, os.path.join(FIG, 'ch2_resistance.png'),
    'Figure 6. Planning for resistance: surface the objections early and answer the big ones inside the message.',
    'Four-step process for writing to skeptical readers: list their objections honestly before writing, address the two biggest inside the message, show evidence rather than claims, and make yes easy with a small ask and clear next step.')
para(doc, 'The counterintuitive move is naming the objection yourself: “This costs $2,400, and here is '
    'why it pays back in six weeks” outperforms hoping nobody notices the price. Readers trust writers '
    'who have obviously considered the other side — that is ethos, manufactured honestly. And '
    'psychology is on the side of modest asks: attention is scarce and effort is aversive '
    '(Kahneman, 2011), so a specific, small, deadline-bearing request (“reply with your preferred slot '
    'by Thursday”) converts far better than a vague large one (“let me know your thoughts”).')

h1(doc, 'Plain language is the law (really)')
para(doc, 'If planning for the reader ever feels optional, consider that for U.S. federal agencies it '
    'is legally required: the Plain Writing Act of 2010 obligates agencies to write public-facing '
    'documents in “clear, concise, well-organized” language suited to the audience (Plain Writing Act, '
    '2010; plainlanguage.gov). The private sector has no such statute — just the same economics: '
    'documents that readers understand the first time cost less, convert better, and generate fewer '
    'complaints. The federal guidelines at plainlanguage.gov are a free, excellent style reference for '
    'any business writer.')

h1(doc, 'Worked example: planning one real message')
para(doc, 'Situation: you coordinate a student org and need faculty volunteers to judge a case '
    'competition on a Saturday morning. Run the canvas (Figure 7):')
numbered(doc, [
    'Purpose: so that at least four faculty reply “yes, I’ll judge” by Friday, because judging showcases their expertise to 80 students and takes only three hours.',
    'Audience: busy faculty; receptive to student success, resistant to weekend time; they need the exact time commitment and what judging involves before they can say yes.',
    'Benefit: visible mentorship, listed program recognition, coffee and lunch provided — their reasons, stated early.',
    'Channel: individual emails (not a mass BCC — gatekeeper-free, personal, forwardable to their calendar).',
    'Opening: the ask and the date in sentence one; background afterward for those who read on.',
    'Call to action: “Could you reply by Friday with a yes/no? Judging runs 9–noon on the 14th; rubric and coffee provided.”',
])
figure(doc, os.path.join(FIG, 'ch2_planner.png'),
    'Figure 7. The six-box message planner. Two minutes here is cheaper than one misunderstood email.',
    'Message planner canvas with six boxes: purpose (what should the reader know or do), audience (what they know, feel, fear, want), benefit (why they would say yes), channel (rich or lean, record needed), opening (main point first), and call to action (specific act plus deadline).')

h1(doc, 'Deep dive: the four purposes, and the hidden fifth')
para(doc, 'The inform/persuade split from earlier deserves finer teeth, because misdiagnosing purpose '
    'is the most common root cause of failed messages. Business messages actually pursue four '
    'purposes, often in combination. Informing transfers knowledge and asks nothing: the outage '
    'notice, the schedule, the minutes. Its success test is comprehension — could the reader answer '
    'a quiz? Persuading seeks a decision the reader is free to refuse: the proposal, the request, '
    'the pitch. Its success test is behavior — did they do it? Building goodwill maintains the '
    'relationship itself: thanks, congratulations, the check-in note. Its test is affective — does '
    'the reader feel valued? And creating a record protects the future: the confirmation email, the '
    'documented decision, the memo-to-file. Its test may not arrive for years — will this document '
    'defend us when memory fails or disputes arise?')
para(doc, 'Each purpose has a signature architecture. Information wants maximal findability: '
    'frontloaded, chunked, skimmable. Persuasion wants sequenced benefit logic (Chapter 8 gives it a '
    'whole architecture). Goodwill wants brevity and specificity — ceremony smothers it. Records '
    'want completeness and precision: full names, full dates, exact figures, because the future '
    'reader has no context. Diagnose before drafting, because the architectures conflict: the '
    'precision that makes a good record makes a bloated goodwill note; the warmth that carries '
    'goodwill dilutes a record.')
para(doc, 'Then there is the hidden fifth purpose, the one nobody writes in a planning box: '
    'self-presentation. Every message you send is also a performance of your competence, and '
    'pretending otherwise is naive. The mature handling is to let self-presentation ride as a '
    'passenger, never drive: the message that exists mainly to display its writer — the '
    'jargon-dense reply-all, the unnecessary weigh-in — is read by everyone as exactly what it is. '
    'Paradoxically, the strongest professional image comes from messages ruthlessly organized around '
    'the reader; competence displayed through usefulness is the only display that does not look '
    'like one.', bold_lead='The fifth purpose.')

h1(doc, 'Deep dive: the audience analysis protocol')
para(doc, 'When stakes justify more than the 60-second plan, run the full protocol. Twelve questions, '
    'four clusters — the answers write half your message.')
h2(doc, 'Cluster 1: Knowledge')
numbered(doc, [
    'What does the reader already know about this topic? (Sets your starting altitude — background they have is insult to repeat, background they lack is a wall to hit.)',
    'What vocabulary is native to them? (Their words, not yours: a CFO hears “payback period,” a chemist hears “detection limit,” and each hears the other’s term as fog.)',
    'What do they think they know that is actually wrong? (Misconceptions must be dislodged gently BEFORE the new information has anywhere to land.)',
])
h2(doc, 'Cluster 2: Feelings')
numbered(doc, [
    'What is their likely first emotional reaction to this message? (Receptive, neutral, resistant — the strategy switch from Chapter 3.)',
    'What is their history with this topic — and with you? (A proposal that failed twice before does not arrive new; your last interaction is your current ethos.)',
    'What are they afraid of? (Fear unaddressed becomes the grapevine’s raw material — the wellness-memo lesson.)',
])
h2(doc, 'Cluster 3: Needs')
numbered(doc, [
    'What must they have in order to act — authority, budget, information, cover? (A reader who cannot act on your ask needed a different message, or a different reader.)',
    'What does saying yes cost them — time, money, risk, face? (Price the yes honestly; your message must be worth it.)',
    'What is their preferred format and channel? (Some readers decide from tables; some from narratives; asking once — “how do you like updates?” — pays for years.)',
])
h2(doc, 'Cluster 4: Context')
numbered(doc, [
    'When will they read this — and in what state? (Monday 8 a.m. triage differs from Thursday afternoon; month-end differs from mid-cycle.)',
    'Who else will see it? (The rings: secondary, gatekeeper, hidden.)',
    'What else is competing for their attention right now? (Your message is not read in a vacuum but in a stack; its design must survive the stack.)',
])
para(doc, 'The protocol’s value is not filling boxes — it is the question you cannot answer. Every '
    'blank is a finding: something to learn before sending, or a risk you are knowingly accepting. '
    'Experts do not know all twelve answers; they know WHICH answers they are missing.',
    bold_lead='Read the blanks.')

h1(doc, 'Deep dive: a taxonomy of reader benefits')
para(doc, 'The “which means” ladder ends at a reader benefit — but benefits come in four currencies, '
    'and matching the currency to the reader is its own skill.')
bullets(doc, [
    ('Economic benefits', '— money saved, revenue gained, budget protected. The currency of owners, executives, and anyone with a P&L. Strongest when concrete: “$1,800 per external review, twice a year.”'),
    ('Operational benefits', '— time saved, errors prevented, friction removed. The currency of managers and practitioners: “no more Friday reconstruction of the week.” Often more persuasive than money to the people who live the friction.'),
    ('Psychological benefits', '— pride, security, recognition, reduced anxiety. The currency of everyone, admitted by no one: “your team’s results go in front of the VP.” Handle with sincerity; manufactured flattery reads instantly.'),
    ('Political benefits', '— cover, credit, alliance, safe precedent. The currency of organizational life: “finance has already signed off on the framework” removes the risk of going first. Legitimate when true; toxic when fabricated.'),
])
para(doc, 'Mixed audiences need mixed currencies — the proposal skimmed by an executive (economic), '
    'implemented by a manager (operational), and lived by a team (psychological) should carry all '
    'three, each where its reader will look. And note the ethical constant across currencies: a '
    'benefit is something the reader would still recognize as a benefit after saying yes. Anything '
    'else is bait.')

h1(doc, 'Deep dive: one message, four registers')
para(doc, 'The tone dial deserves a demonstration. One fact — a project deadline is moving from '
    'Friday to Wednesday — rendered at four settings:')
para(doc, 'Formal report register: “The delivery milestone has been rescheduled from May 16 to '
    'May 14 to accommodate the client’s revised audit window. All workstream leads have confirmed '
    'feasibility of the compressed timeline.” Complete sentences, no contractions, third-person '
    'distance, documentation-grade precision. For: records, external formality, anything legal '
    'might read.', bold_lead='Register 1.')
para(doc, 'Client letter register: “To align with your revised audit window, we’ve moved delivery '
    'up to Wednesday, May 14. Our leads have confirmed the earlier date is comfortable — you’ll '
    'have everything before your auditors arrive.” Warm, contractions permitted, you-view forward, '
    'still precise. For: external professional relationships.', bold_lead='Register 2.')
para(doc, 'Internal email register: “Heads up — delivery moves to Wednesday 5/14 (client’s audit '
    'window shifted). All leads have confirmed we’re good. Flag me by tomorrow if that breaks '
    'anything on your end.” Compressed, direct, action-oriented, but complete: dates, reason, ask. '
    'For: colleagues who share your context.', bold_lead='Register 3.')
para(doc, 'Team chat register: “FYI deadline now Wed 5/14 — client audit moved. Leads confirmed '
    'OK. Problems → tell me by tmrw.” Telegraphic but still carrying every load-bearing fact. For: '
    'rapid coordination with people who trust you.', bold_lead='Register 4.')
para(doc, 'Study what stays constant: the facts, the reason, and the ask survive every register — '
    'only ceremony scales. That is the whole discipline of tone: the dial adjusts formality, never '
    'completeness, and never accuracy. A writer who drops the reason in chat, or the ask in the '
    'formal version, has changed the message, not the register.', bold_lead='The invariants.')

h1(doc, 'Deep dive: why pressure backfires — reactance')
para(doc, 'One more piece of psychology completes the skeptical-reader toolkit. When people feel '
    'their freedom to choose being squeezed, they push back to reassert it — a reflex psychologists '
    'call reactance (Brehm, 1966). It is why hard-sell messages generate not just refusal but '
    'resentment, why “you must” produces less compliance than “you can,” and why the deadline that '
    'reads as a threat gets tested while the deadline that reads as information gets met. The '
    'planning consequences: preserve visible choice wherever choice truly exists (“two options that '
    'both work — your call”); frame constraints as facts of the world rather than exertions of your '
    'will (“registration closes Friday” beats “you need to register by Friday”); and never '
    'manufacture pressure you cannot back, because reactance plus discovery equals a reader who now '
    'opposes you on principle. The skeptical reader is not just weighing your evidence; they are '
    'monitoring their own autonomy. Messages that respect it get read with the guard down.')

h1(doc, 'Research corner: what readers actually do with your message')
para(doc, 'Plan for the reading you will actually get, not the reading you deserve. Eye-tracking '
    'research on screen reading famously found that users scan in rough F-shaped patterns — reading '
    'the first lines fully, then less of each following line, then skimming down the left edge '
    '(Nielsen, 2006). Translation for planners: your first sentence gets read; your first words of '
    'each paragraph get sampled; the middle of paragraph four effectively does not exist. This is why '
    'journalists have written in the inverted pyramid — most important first, detail descending — '
    'for over a century, and why this course keeps repeating “frontload.”')
para(doc, 'The planning consequences are concrete: put the ask and the benefit in the zone that gets '
    'read (subject line, sentence one); start paragraphs with their point, because first words are the '
    'skim path; use white space, bolded deadlines, and lists to give scanners handholds; and treat '
    'anything below the first screen as optional reading — never hide required action there. None of '
    'this dumbs writing down. It is designing for the real behavior of busy readers, which is the '
    'entire ethic of this chapter.')

h1(doc, 'Planning under time pressure: the 60-second plan')
para(doc, 'Real inboxes do not allow a canvas for every message. Compress the discipline into one '
    'minute, three questions: What do I want? (the purpose template, spoken silently) — Why would '
    'they care? (one reader benefit, moved into sentence one) — What exactly happens next? (act plus '
    'date at the end). Sixty seconds, three answers, and your routine messages inherit most of the '
    'value of full planning. Reserve the six-box canvas for stakes: money, strangers, resistance, '
    'permanence, or anything a hidden reader might someday see.')

h1(doc, 'Planning for global and multicultural readers')
para(doc, 'Chapter 1’s context continuum (Hall, 1976) becomes a planning checklist the moment your '
    'audience rings include readers from other cultures — which, in modern organizations, is always.')
bullets(doc, [
    ('Strip idioms at the planning stage.', '“Circle back,” “low-hanging fruit,” and every sports metaphor force non-native readers to translate twice.'),
    ('Make dates unambiguous.', '“5 March 2026,” never “3/5/26” — half the world reads that backwards.'),
    ('Plan more context for high-context readers.', 'Relationship acknowledgment before business is not padding; it is the message working.'),
    ('Expect indirect yes/no.', 'Plan follow-up questions that let a reluctant “no” surface safely (“what obstacles should we plan around?”).'),
    ('Confirm agreements in writing, gently.', 'A short summary respects both styles: explicit for low-context readers, face-saving for high-context ones.'),
])

h1(doc, 'Format signals: email, memo, or letter?')
para(doc, 'The container is part of the plan, because format signals weight before a word is read. '
    'Email is the default for nearly everything internal and much external — fast, filed, '
    'forwardable. A memo (or memo-formatted PDF) signals institutional weight: policies, formal '
    'announcements, anything that will be referenced later; its To/From/Date/Subject block is a '
    'promise of documentation. A letter on letterhead is the heavyweight: external, formal, '
    'personal — offers, recommendations, official notices, apologies that must feel signed. Choosing '
    'a heavier container than the content warrants reads as pompous; choosing a lighter one than the '
    'occasion demands reads as careless. When in doubt, ask what the reader will need to DO with the '
    'document — file it, forward it, frame it — and pick the container built for that verb.')

h1(doc, 'AI as a planning partner')
para(doc, 'Planning is the writing phase where AI helps most safely, because you are generating '
    'hypotheses rather than facts. Useful prompts: “List the objections a hospital CFO might raise to '
    'this proposal” (widens your resistance list); “What does a first-year employee likely NOT know '
    'in this announcement?” (audience knowledge check); “Rewrite this opening so the reader benefit '
    'comes first” (you-view drill). The boundaries from Chapter 15 still hold — the AI does not know '
    'your actual reader, so treat its output as a brainstormed list to verify against the human you '
    'know, and never paste confidential context into public tools. Used this way, AI makes the '
    'planning phase faster without touching the part that must stay yours: the judgment about which '
    'hypothesis is true.')

h1(doc, 'Three readers you will meet everywhere')
para(doc, 'Audience analysis gets faster with pattern recognition. Three archetypes cover a remarkable '
    'share of business readers — learn to spot them and plan accordingly.')
h2(doc, 'The executive skimmer')
para(doc, 'Reads the subject line, the first two sentences, and any bolded deadline — on a phone, '
    'between meetings. Wants the decision surfaced immediately and the reasoning available but not '
    'mandatory. Plan for them by frontloading the ask, keeping one screen of text, and structuring the '
    'support so it can be skipped without missing the point. If your main point is in paragraph three, '
    'the executive skimmer never met it.')
h2(doc, 'The expert scrutinizer')
para(doc, 'Reads everything, checks your numbers, and notices what you left out. Wants completeness, '
    'sources, and honest limitations. Plan for them with precise claims (“reduces run time about 30% '
    'in our pilot” beats “dramatically faster”), cited evidence, and the objection section — because '
    'they will raise the objections whether you address them or not, and addressing them first is '
    'ethos. Skimping on rigor to “keep it simple” insults this reader; layering (summary up front, '
    'detail behind) serves both them and the skimmer.')
h2(doc, 'The anxious stakeholder')
para(doc, 'Reads your message asking one question: what does this mean for me? Change announcements, '
    'policy updates, and reorganizations all land on this reader. Plan for them by answering the '
    'personal impact question explicitly and early (“your role, pay, and location are unchanged”), '
    'never leaving the most personal implication to be inferred — inference under anxiety always '
    'selects the worst reading. This is the reader the wellness-memo case (below) forgot.')

h1(doc, 'Features vs. benefits: the “which means” ladder')
para(doc, 'The most common planning failure in persuasive messages is listing features — attributes of '
    'the thing — where the reader needs benefits: outcomes in their life. The repair tool is a '
    'two-word ladder: after every feature, force the phrase “which means…” and climb until you reach '
    'the reader.')
bullets(doc, [
    ('“The new LIMS auto-logs samples”', '→ which means no manual entry → which means your techs save about an hour a day and transcription errors disappear from audits.'),
    ('“I am a certified quality auditor”', '→ which means your findings close in-house → which means no more $1,800 external reviews.'),
    ('“The course is asynchronous”', '→ which means you complete modules on your schedule → which means the certificate fits around a full-time job.'),
])
para(doc, 'Two rungs is usually enough; stop when the sentence contains something the reader would '
    'put in their own status report. If you cannot complete the ladder for a feature, the feature may '
    'not belong in the message at all — planning is also deciding what to leave out.')

h1(doc, 'The opening-line playbook')
para(doc, 'Openings are where planning pays first. Match the first sentence to the message type:')
bullets(doc, [
    ('Routine request.', 'The ask, immediately: “Could you send the Q2 vendor list by Thursday noon?”'),
    ('Good news.', 'The news itself: “Your proposal is approved — funding starts May 1.”'),
    ('Information / update.', 'The one-line takeaway: “The migration finished last night; all systems are normal.”'),
    ('Meeting follow-up.', 'The decisions: “Three decisions from today’s call:”'),
    ('Request to a stranger.', 'The connection plus the reason for THIS person: “Dr. Rios suggested I contact you about the co-op program.”'),
    ('Gentle reminder.', 'Assume good faith: “Resending in case this got buried — the form is due Friday.”'),
    ('Complex proposal.', 'The recommendation, then the roadmap: “I recommend renewing with TechServe; the comparison below covers cost, support, and risk.”'),
    ('Bad news (preview of Chapter 7).', 'A buffer of honest context — the one opening on this list that does NOT lead with the point.'),
    ('Thanks / recognition.', 'The specific act: “Your triage of Saturday’s outage saved the launch.”'),
    ('Apology.', 'Ownership without hedging: “I missed the deadline I committed to, and it delayed your review.”'),
])

h1(doc, 'Planning self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'Before important messages, I can state in one sentence what the reader should do.',
    'I identify the primary reader by name or role — not “everyone.”',
    'I consider who might see the message beyond the addressee.',
    'My first two sentences contain the point, not the preamble.',
    'I name reader benefits, not just my request or my features.',
    'I anticipate the top objection and answer it in the message.',
    'I choose the channel deliberately for sensitivity and record.',
    'My requests carry a specific action and a date.',
    'I adjust formality to the occasion rather than writing one way always.',
    'I reread important drafts once as the least-informed likely reader.',
])
para(doc, 'Scoring: 16–20, your planning habit is a professional asset — refine, don’t overhaul. '
    '10–15, choose the two lowest items and drill them for two weeks; the purpose template and the '
    'call-to-action rule pay fastest. Below 10, adopt exactly one habit this week: complete the '
    'purpose template before every message that matters. Retake at midterm.')

h1(doc, 'Case study 1: the wellness memo that backfired')
para(doc, 'An HR director launches a wellness initiative with an all-staff memo: two paragraphs '
    'celebrating the company’s investment, a bulleted list of program features (biometric screenings, '
    'an app, lunchtime seminars), and a closing line — “We are excited about this journey!” '
    'Participation after one month: eleven percent. The grapevine version: “they’re making us do health '
    'screenings so insurance can raise our rates.”')
numbered(doc, [
    'Diagnose the planning failures: what did the memo know about its audience’s fears, and whose benefits did it list?',
    'Which ring of Figure 3 did the writer forget, and how did that ring end up writing the message’s real meaning?',
    'Re-plan the message with the six-box canvas: what changes in the opening, the benefit, and the call to action?',
])
h2(doc, 'Case analysis')
para(doc, 'The memo was planned for the sender: its benefits list was the company’s feature list, its '
    'tone celebrated the company’s generosity, and it never addressed the one thing a skeptical '
    'employee audience actually asks — what happens to my data? Silence on the top objection handed '
    'the interpretation to the grapevine (Chapter 1’s rule: informal channels fill every silence). A '
    'planned version opens with the employee’s benefit (“a $40 monthly premium credit and free '
    'screenings, on work time”), addresses the privacy objection by name (“results go to you alone; '
    'the company sees only anonymous participation counts — here is the policy”), and makes the first '
    'yes small (“fifteen-minute screening, four slots Thursday”). Same program; opposite message; the '
    'difference is entirely in the planning.')

h1(doc, 'Case study 2: two versions of the same request')
para(doc, 'A lab supervisor wants the department to fund her Certified Quality Auditor exam ($545). '
    'Version A, to her manager: “I have been developing my skills in quality systems and feel this '
    'certification would be a great next step in my professional growth. The exam costs $545. I hope '
    'the department can support my development.” Version B: “Funding my CQA exam ($545) would let our '
    'lab close audit findings in-house instead of hiring the external reviewer we used twice last year '
    'at $1,800 per visit. The exam is in March; passing it makes us self-sufficient by Q2. Could you '
    'approve by the 15th so I can register at the early rate?”')
numbered(doc, [
    'Both versions are polite and truthful. Map each against the purpose-statement template and the six-box canvas: what is missing from Version A?',
    'Whose benefits appear in each version? Count them.',
    'Version B names money going out and money saved. Which of Aristotle’s appeals is that, and why does it need to be paired with the deadline in the call to action?',
])
h2(doc, 'Case analysis')
para(doc, 'Version A is a writer-view message: its subject is the writer’s growth, its benefit list is '
    'empty from the manager’s side, and its call to action (“I hope…”) asks for nothing checkable by '
    'any date. It plans to be appreciated, not approved. Version B passes the template — who (manager) '
    'does what (approve by the 15th) because (saves $1,800 visits, self-sufficiency by Q2) — and its '
    'logos is concrete: a cost paired against a larger recurring cost. The deadline converts goodwill '
    'into action by giving the yes a place to land. The deeper lesson: the writer’s real reasons '
    '(growth, ambition) are legitimate — but the message’s reasons must be the reader’s. Plan the '
    'overlap, and both people get what they want.')

h1(doc, 'Planning documents with multiple masters')
para(doc, 'Some documents cannot pick one primary reader: the project charter read by sponsors, '
    'engineers, and finance; the policy read by employees, managers, and someday a lawyer. '
    'Multi-audience planning has its own craft. Layer the document so each audience has a designed '
    'path: an executive summary for deciders, labeled sections for implementers, appendices for '
    'verifiers — the layering IS the audience analysis, expressed as structure. Segregate '
    'vocabulary: body text at the least-expert reader’s altitude, technical precision quarantined in '
    'clearly-marked sections where experts will look and others may skip. Resolve benefit conflicts '
    'explicitly: when what delights one audience alarms another (automation thrills finance and '
    'threatens the team), address both in their own sections rather than hoping neither notices the '
    'other’s. And when audiences genuinely conflict — the document cannot serve both — split it: '
    'two short documents beat one document at war with itself. The instinct to “just send everyone '
    'the same thing” is a planning decision too; it is simply usually the wrong one.')
para(doc, 'Professionals who write frequently keep a planning file: the audience protocol answers '
    'for their recurring readers (the CFO wants tables, hates adjectives, reads at 6 a.m.), the '
    'purpose templates for their recurring genres, and their own best openings and calls to action '
    'for reuse. Chapter 1 suggested notes after conversations; this is the writing twin. Ten minutes '
    'of curation a month turns planning from a per-message tax into a compounding asset — and it is '
    'exactly the kind of personal knowledge base that makes AI assistance sharper, since your '
    'planning file is the context no model has (Chapter 15).', bold_lead='The planning file.')

h1(doc, 'Teardown: the finished email, annotated')
para(doc, 'Here is the faculty-judges message from the worked example, drafted from its plan — with '
    'the planning visible in brackets.')
para(doc, 'Subject: Judge our case competition? 3 hours, Sat. May 14 [ask + size of ask visible '
    'before the email is even opened]')
para(doc, '“Dr. Alvarez — Could you serve as a judge for our undergraduate case competition on '
    'Saturday, May 14, 9:00–noon? [the full ask, sentence one: act, date, duration] Eighty students '
    'will present strategy recommendations, and your supply-chain expertise is exactly what the final '
    'round needs. [benefit + why THIS reader — ethos returned to the reader] Judging is structured '
    'and simple: a one-page rubric, four presentations, coffee and lunch on us. [objection handling: '
    'effort, ambiguity, and Saturday-morning logistics answered before asked] Faculty judges are '
    'listed in the program and event photos go to the college’s newsletter. [second benefit: visible '
    'mentorship] Could you reply by Friday the 6th so we can confirm the panel? [call to action: '
    'specific act, specific date, reason for the date] Happy to answer anything — and thank you for '
    'considering it. [warm close, door open]”')
para(doc, 'Count what the plan bought: the ask is in the subject line and first sentence (executive '
    'skimmer served), the effort objection is answered inside (expert scrutinizer served), every '
    'benefit belongs to the reader, and the yes has a date to land on. One hundred twenty words, '
    'nothing wasted — because the deciding happened before the drafting.', bold_lead='The point.')

h1(doc, 'Deep dive: where tailoring ends and pandering begins')
para(doc, 'Everything in this chapter teaches adaptation — and adaptation has an ethical edge worth '
    'mapping precisely, because your credibility lives on it. Three tests separate legitimate '
    'audience adaptation from its corrupt twin.')
para(doc, 'The facts test: adaptation changes emphasis, order, vocabulary, and framing; it never '
    'changes the facts. Telling the CFO about cost savings and the team about workload relief is '
    'tailoring — both are true. Telling the CFO the system is proven while telling the team it is '
    'experimental is lying twice. If two of your audiences compared notes, would they find different '
    'perspectives on one truth, or two truths? Only the first survives the comparison — and '
    'audiences do compare notes.', bold_lead='Test one.')
para(doc, 'The commitment test: adapted messages make different arguments; they never make '
    'incompatible promises. The classic career wound is the writer who, adapting enthusiastically to '
    'each room, commits to finance that the project needs no new headcount and to the team that help '
    'is coming. Each message was locally persuasive; jointly they are a time bomb. Before sending '
    'any adapted message, ask what its promises look like laid beside the promises of its siblings.',
    bold_lead='Test two.')
para(doc, 'The respect test: tailoring serves the audience’s interests; pandering serves their '
    'prejudices. Framing automation as job-enriching because it genuinely removes drudge work is '
    'tailoring. Framing it that way while planning the layoffs is contempt with good manners. The '
    'difference is invisible in the text and obvious in the outcome — which is why this test, '
    'unlike the others, is applied to your intentions rather than your prose. Chapter 16’s '
    'visibility question is the portable version: if the audience could watch you plan this '
    'message, would they thank you for the care or resent you for the management?', bold_lead='Test three.')
para(doc, 'Held together: adapt the presentation, never the substance; vary the arguments, never '
    'the commitments; serve their interests, never merely their comfort. Writers who hold that line '
    'discover a compounding advantage — audiences who have compared notes and found one consistent '
    'truth begin extending trust in advance, which is the cheapest persuasion there is.')

h1(doc, 'Watch list: three short talks worth your time')
para(doc, 'All free, public TED talks — search the titles. Watch for how each speaker plans around an '
    'audience, not a topic.')
bullets(doc, [
    ('Simon Sinek, “How Great Leaders Inspire Action.”', 'His “start with why” is this chapter’s purpose statement scaled up to organizations — notice that the why is always the audience’s reason to care.'),
    ('Nancy Duarte, “The Secret Structure of Great Talks.”', 'A presentation designer maps famous speeches as journeys designed around what the audience believes now versus what they could believe — audience analysis made visible.'),
    ('Chimamanda Ngozi Adichie, “The Danger of a Single Story.”', 'The deepest version of frame-of-reference: what happens when a writer or a reader knows only one story about the other.'),
])

h1(doc, 'Message planner worksheet')
para(doc, 'Photocopy this mentally onto every message that matters. For a message you actually need to '
    'send this week:')
numbered(doc, [
    'Purpose (template): so that __________ does __________ because __________.',
    'Primary reader’s current knowledge of the topic (one line): __________.',
    'Their likely feeling about it (receptive / neutral / resistant): __________.',
    'Their top objection, stated honestly: __________. Where in the message will you answer it?',
    'Secondary or hidden readers who could see this: __________. Anything to adjust?',
    'Reader benefit, in their words, appearing in the first two sentences: __________.',
    'Channel and why: __________.',
    'Call to action — specific act + deadline: __________.',
])

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find a message you received recently that was clearly planned for the sender, not for you. What did it feel like to read — and what one planning question would have fixed it?',
    'Recall a time you wrote something long because you had not decided what you wanted. What was the real purpose, and when did you discover it?',
    'Aristotle says credibility (ethos) is an appeal you carry into the message. What is your current ethos with your manager, professor, or team — and what messages built it?',
    'Write the purpose statement for the next important message of your real life — a job application, a difficult family email, a pitch. Notice what deciding it changes.',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'The course standard — could a supervisor send this as-is? — is applied at planning level '
    'before sentence level. A beautifully worded message with no discernible purpose, no reader '
    'benefit, and no call to action is not sendable; a plain message that knows its job usually is. '
    'Before submitting any assignment, verify: the purpose statement is completable, the opening faces '
    'the reader, the top objection is answered, and the ask has a date.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('Drafting first, deciding later.', 'Fix: complete the purpose template before typing; if you cannot, gather what you are missing — that is the actual task.'),
    ('Writing to “everyone.”', 'Fix: name the primary reader; write to them; let the rings read over their shoulder.'),
    ('Listing your features instead of their benefits.', 'Fix: after every feature, force the phrase “which means you…” and finish the sentence.'),
    ('Purpose overload.', 'Fix: one message, one job. The second ask gets its own message — or a clearly separated section.'),
    ('Vague calls to action.', 'Fix: a specific act plus a date. “Thoughts?” is not a call to action; it is a donation request for attention.'),
    ('Tone by mood.', 'Fix: set the dial deliberately for the occasion and the reader’s stakes, then hold it for the whole message.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“Planning feels slow. I write fine on the fly.”', 'For routine messages you probably do — habit is compiled planning. The discipline is for messages with stakes: new audiences, money, resistance, or permanence. Those are exactly the ones instinct gets wrong.'),
    ('“What if I don’t know what the audience thinks?”', 'That is a finding, not a dead end: ask someone who knows, or write the message to earn the answer (“what would need to be true for this to work for your team?”). Guessing is the only wrong option.'),
    ('“Isn’t the you-view manipulative?”', 'Framing real benefits in the reader’s terms is respect; inventing benefits is manipulation. The test from Chapter 16 applies: if the reader could see your technique, would they still feel respected?'),
    ('“Can AI do my audience analysis?”', 'It can generate hypotheses — “what objections might a CFO have?” is a great prompt. It cannot know your actual CFO. Use it to widen your list, then verify against the human you know. See Chapter 15.'),
    ('“How long should planning take?”', 'For a routine email: the ten seconds it takes to complete the purpose template in your head. For a proposal: as long as the drafting. Scale it to stakes, not to guilt.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 2).', 'The question bank drills purpose, audience rings, you-view transformations, and channel choice.'),
    ('Writing prompts (course site).', 'The purpose-statement and dual-audience prompts rehearse Figures 2 and 3 directly.'),
    ('Your major assignments.', 'Every graded document this term — market research, letters, the executive summary — will be graded first on the planning layer this chapter teaches.'),
    ('Next chapter.', 'Chapter 3 takes the plan and organizes the draft: direct versus indirect strategy, paragraphs, and sentences that carry weight.'),
    ('The lecture deck.', 'The Chapter 2 slides follow this guide section-for-section — use them as your review pass.'),
])

keyterms(doc, [
    ('Purpose statement', 'one sentence naming who must do what, and why they would want to — the test of readiness to draft.'),
    ('Primary / secondary audience', 'the reader who acts, and the readers who receive it later by forward, file, or record.'),
    ('Gatekeeper', 'a reader who decides whether the message reaches the primary audience at all.'),
    ('Hidden audience', 'readers you did not address but must assume: legal, HR, the public record.'),
    ('Rhetorical situation', 'Bitzer’s trio of exigence, audience, and constraints that every message answers to.'),
    ('Ethos / pathos / logos', 'Aristotle’s appeals: credibility, audience values and emotion, and logical argument.'),
    ('You-view', 'organizing content around reader benefit and dignity rather than writer activity.'),
    ('Tone', 'the reader’s impression of your attitude — planned via the formality dial, not left to mood.'),
    ('Forwardability test', '“Could this be forwarded unedited without embarrassing me?” — audience analysis in one question.'),
    ('Call to action', 'the specific act plus deadline that converts agreement into behavior.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Planning is half the work: experts decide before they draft (Flower & Hayes, 1981).',
    'One message, one job: complete “so that [reader] does [act] because [their reason]” before typing.',
    'Audiences come in rings — primary, secondary, gatekeeper, hidden. Write to the first; write knowing the rest exist.',
    'Every message sits in a rhetorical situation: an exigence, an audience, constraints (Bitzer, 1968) — and persuades through ethos, pathos, and logos (Aristotle).',
    'The you-view organizes content around reader benefit and protects reader dignity; it is planning made visible in grammar.',
    'Tone is one professional voice on a formality dial — positive framing, no fossils, bias-free, matched to the reader’s stakes.',
    'For skeptical readers: name the objections, answer the big two inside the message, show evidence, make yes small and dated.',
    'Plain language is codified law for U.S. agencies (Plain Writing Act, 2010) and plain economics for everyone else.',
])

quiz(doc, [
    ('The first question to answer before drafting any business message is:', ['How long should it be?','What is my purpose — what should the reader know or do?','Which font looks professional?','Should I copy my manager?']),
    ('A complete purpose statement names:', ['The topic and the deadline','Who must act, what they should do, and why they would want to','The sender’s credentials','The channel and the tone']),
    ('The reader who will act on your message is the primary audience. A gatekeeper is:', ['Anyone who dislikes the message','A reader who decides whether the message reaches the primary audience','The IT department','The most senior reader']),
    ('The forwardability test asks:', ['Whether the message is short enough to forward','Whether the message could be forwarded unedited without embarrassing you','Whether reply-all is enabled','Whether attachments are included']),
    ('In Bitzer’s rhetorical situation, the exigence is:', ['The audience’s mood','The problem that calls the message into being','The formatting rules','The deadline']),
    ('“You can now shop weeknights until 9 p.m.” demonstrates:', ['Writer-view','You-view — the fact framed as the reader’s benefit','Purpose overload','A gatekeeper strategy']),
    ('When delivering criticism, skilled writers often avoid “you” because:', ['The you-view is always wrong','“You” in accusatory contexts becomes blame language that triggers defense','Readers prefer passive voice','It shortens the message']),
    ('Which revision uses positive language most effectively?', ['“We cannot ship your order until Friday.”','“Your order will ship on Friday.”','“Unfortunately, shipment is impossible before Friday.”','“Do not expect your order before Friday.”']),
    ('Aristotle’s three appeals are:', ['Purpose, audience, channel','Ethos, pathos, logos','Plan, draft, revise','Exigence, audience, constraints']),
    ('For a skeptical audience, naming the biggest objection yourself:', ['Weakens your case','Builds credibility — readers trust writers who have considered the other side','Is legally required','Should wait for the follow-up email']),
    ('An effective call to action includes:', ['A warm closing','A specific act plus a deadline','At least three options','An apology for asking']),
    ('“Please be advised that enclosed please find…” is an example of:', ['Required legal phrasing','Fossil phrases — inherited formality that adds noise, not respect','You-view writing','Plain language']),
    ('The Plain Writing Act of 2010:', ['Applies to all U.S. businesses','Requires federal agencies to write clearly for the public','Banned passive voice','Regulates email length']),
    ('Expert writers differ from novices chiefly in:', ['Vocabulary size','Typing speed','How much they plan — setting goals and representing the audience (Flower & Hayes, 1981)','Avoiding revision']),
], ['b','b','b','b','b','b','b','b','b','b','b','b','b','c'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Write the purpose statement for a message you sent recently that did not get the response you wanted. Did the sent version actually serve that purpose?',
    'Describe a real gatekeeper or hidden audience in your work or campus life. How does knowing they exist change one message you might send this month?',
    'Take a marketing email you received today and rewrite its opening in genuine you-view. What did the company’s version reveal about who it was planned for?',
    'Which of Aristotle’s appeals do you lean on by habit — and which audience in your life requires the one you use least?',
    'Find a public-facing document (university policy, utility notice, terms of service) that fails the plain-language standard. Re-plan its first paragraph with the six-box canvas.',
])

references(doc, [
    'Aristotle. (2007). On rhetoric: A theory of civic discourse (G. A. Kennedy, Trans., 2nd ed.). Oxford University Press. (Original work ca. 350 BCE)',
    'Bitzer, L. F. (1968). The rhetorical situation. Philosophy & Rhetoric, 1(1), 1–14.',
    'Brehm, J. W. (1966). A theory of psychological reactance. Academic Press.',
    'Flower, L., & Hayes, J. R. (1981). A cognitive process theory of writing. College Composition and Communication, 32(4), 365–387.',
    'Hall, E. T. (1976). Beyond culture. Anchor Press/Doubleday.',
    'Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.',
    'Nielsen, J. (2006). F-shaped pattern for reading web content. Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/',
    'National Association of Colleges and Employers. (2025). Job Outlook 2025. NACE. https://www.naceweb.org/',
    'Plain Writing Act of 2010, Pub. L. No. 111-274, 124 Stat. 2861. https://www.plainlanguage.gov/',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch02-study-guide.docx')
finish(doc, os.path.abspath(out))
