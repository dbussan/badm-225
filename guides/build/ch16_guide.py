# Chapter 16 study guide — Leadership Under Pressure & Influence (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(16, 'Leadership Under Pressure & Influence',
    'Crisis clarity · influence without authority · the people principles that have worked for a century')

h1(doc, 'Why this chapter exists')
para(doc, 'Every genre this course has taught gets tested at the moment stakes rise — and this chapter '
    'is about that moment. Part one covers communication under pressure: what stress does to a '
    'writer’s judgment, the four-beat protocol that survives it, and the specific discipline of leading '
    'a team or organization through a genuine crisis. Part two turns to influence — in the tradition of '
    'Dale Carnegie’s How to Win Friends and Influence People (1936), restated for the modern workplace '
    'and cross-referenced, deliberately, to nearly every earlier chapter, because Carnegie’s century-old '
    'observations turn out to be audience analysis, persuasion, and goodwill practiced as a way of '
    'treating people rather than as drafting technique alone.')
para(doc, 'Hold one frame through both halves: leadership, in the sense this chapter means it, is not a '
    'title. It is a set of communication choices available to anyone in a room — the decision to be the '
    'one who slows down on purpose under pressure, the decision to ask instead of accuse, the decision '
    'to admit an error before anyone finds it. None of what follows requires authority. All of it '
    'requires choosing it.')

h1(doc, 'What pressure does to communication')
para(doc, 'Stress does not build character; it reveals whatever was already there, and it does '
    'something specific and predictable to communication that is worth naming before any fix. It '
    'narrows: under stress people write faster, read less, and assume more — precisely when precision '
    'matters most. It leaks: tension transmits through word choice, punctuation, and pace, so a team '
    'reads a leader’s temperature before it reads the leader’s words (Chapter 1’s nonverbals, expressed '
    'in prose). And it shortcuts: the verification pass, the tone pass, the cooling-off period '
    '(Chapter 4) all get skipped exactly when their absence costs the most. The leader’s job, in any '
    'sense worth having, is to be the exception — someone in the room has to slow down on purpose, and '
    'deciding that it will be you is most of what leadership actually is.', bold_lead='It narrows, it leaks, it shortcuts.')

h2(doc, 'Clarity over reassurance')
para(doc, 'People can act on accurate hard news. They cannot act on comfortable fog. “We’ll be fine” '
    'plans nothing, staffs nothing, fixes nothing — and it spends trust rather than building it, '
    'because the leader who said “fine” before the layoff is never fully believed again, while the one '
    'who said “here’s what I know and don’t know” is (Chapter 7’s pattern, at leadership stakes). '
    'Clarity is not coldness: “this is serious, here’s the plan, here’s your part” respects people as '
    'adults with jobs to do, and the honest yellow — calibrated, neither alarmist nor falsely calm — is '
    'a leadership instrument as much as a reporting one (Chapter 9).')

h2(doc, 'The pressure protocol')
figure(doc, os.path.join(FIG, 'ch16_protocol.png'),
    'Figure 1. The pressure protocol — pause, facts, frame, forward — thirty seconds that hold at any scale.',
    'A four-step flow: pause (two breaths before any reply), facts (known versus assumed, written as two lists), '
    'frame (their stakes, not yours), and forward (the next concrete action, owned and timed), with the note that '
    'the protocol survives every crisis size from a hot email to a plant shutdown.')
para(doc, 'Four beats, small enough to run under real stress. Pause: two breaths before any reply, '
    'because the send button has no undo (Chapter 7). Facts: write the two lists — what is actually '
    'known versus what is assumed — because pressure blurs exactly that line first. Frame: what this '
    'means for the people being addressed, their stakes rather than the writer’s. Forward: the next '
    'concrete, owned, timed action — always end at the future, never at the recap of what went wrong. '
    'The protocol compresses Chapters 4, 7, and 9 into a field kit small enough to run in the thirty '
    'seconds before a hot reply, and it scales without modification from a heated email to an '
    'organizational crisis.')
para(doc, 'Composure is contagious in both directions. Teams synchronize to a leader’s affect — panic '
    'propagates faster than facts, and so does calm, which means a leader is broadcasting one or the '
    'other whether they intend to or not. Calm is performable and legitimate: slower speech, complete '
    'sentences, written follow-ups produce their effect even while the leader’s own pulse argues '
    'otherwise. Visible process beats visible confidence — “here’s how we’ll figure this out” steadies '
    'a room longer than “it’ll be okay,” because process is checkable and confidence is only a mood. '
    'And the composure budget is real: sleep, breaks, and the unpinged block from Chapter 5 are not '
    'wellness perks during a crisis. They are the supply chain for the only calm the team is going to get.',
    bold_lead='Composure is contagious.')

h1(doc, 'Crisis leadership')
figure(doc, os.path.join(FIG, 'ch16_firsthour.png'),
    'Figure 2. The first hour of a crisis — acknowledge, assign, promise the cadence, feed the grapevine facts.',
    'Four rows: acknowledge to your own people first, assign three hats (comms, the fix, the log), promise a cadence '
    'of updates whether or not anything changes, and feed the grapevine facts to outrun the informal network.')
para(doc, 'The first hour of any crisis needs no answers — it needs visible leadership process while '
    'the answers are still being found. Acknowledge to your own people first: silence from a leader is '
    'itself data, and it reads as either ignorance or concealment, neither of which is what most leaders '
    'intend. Assign three hats — who owns communication, who owns the fix, who owns the log — to three '
    'different heads where possible, because the classic failure mode is everyone fixing and nobody '
    'communicating. Promise the cadence: “updates at 10, 2, and 5, whether anything changes or not” — a '
    'promised rhythm, kept, does more to calm a room than any single update’s content. And feed the '
    'grapevine facts, because the informal network runs at crisis speed (Chapter 1) and will fill any '
    'silence with invention if it is not outrun by official truth.')
para(doc, 'Honest unknowns are a leadership technology in their own right, not a weakness to minimize. '
    '“Here’s what we don’t know yet,” said plainly, is the sentence that separates credible leaders '
    'from spokespeople reciting talking points (Chapter 7’s crisis rules, personalized). It also does '
    'something subtler: when a leader admits uncertainty aloud, the engineer holding bad news stops '
    'polishing it before reporting up — the MUM effect, disarmed at the top, because leader-admitted '
    'uncertainty is what makes honest upward reporting feel safe (Chapters 1, 7, and 9, converging). '
    'Every stated unknown needs an owner and a next step attached — “we don’t know the cause; the '
    'vendor call is at 2” is a plan, while an unknown alone is only dread. And never guess to fill '
    'silence: the retracted guess costs more credibility than a day of “still confirming,” because a '
    'leader’s speculation gets treated as fact and quoted back for years.')
para(doc, 'The debrief afterward is where the crisis pays for itself or doesn’t. Keep it blameless in '
    'structure and specific in facts — “what did the SYSTEM allow?” is Chapter 9’s incident-report '
    'discipline, applied to the team’s own performance rather than to an external event. The leader’s '
    'own errors go first: “I sat on the yellow flag for two days” unlocks more honesty in a room than '
    'anything else available, and it previews the influence section’s error-admission principle. '
    'Harvest the communication failures specifically — who didn’t know what, when — because most crisis '
    'damage turns out to be information routing rather than the triggering event itself. And write the '
    'one-pager (Chapter 5’s wiki habit): what happened, what changed — or the next crisis reruns this '
    'one with different names attached.')

h1(doc, 'Case study: two plant managers, one recall')
para(doc, 'The same product defect struck two facilities on the same day. Manager A held a floor '
    'meeting in hour two: what’s known, what isn’t, updates promised at shift change — then took '
    'questions until they stopped. Manager B “waited for corporate guidance.” By day two, B’s floor was '
    'running three separate rumor variants, including a layoff rumor nobody had authorized, and two of '
    'his best technicians had quietly begun job searches.')
para(doc, 'Six months later, the recall’s financial outcome was identical at both plants — same '
    'defect, same remedy, same cost. A’s plant retained its staff at the same rate as before the '
    'incident. B’s plant lost two technicians and, eventually, its manager, reassigned after a climate '
    'survey flagged the team’s trust collapse. The lesson generalizes past this single event: the '
    'recall itself was never the risk that mattered. The silence was — the defect cost money on a fixed '
    'schedule; the communication decided everything else about what the organization looked like '
    'afterward.')

h1(doc, 'Influence without authority')
para(doc, 'Most careers run substantially on influence rather than authority — peers, clients, other '
    'departments, and frequently one’s own manager all sit outside any formal chain of command (Chapter '
    '8’s timesheet case revisited). Carnegie’s central, century-old observation still holds: people are '
    'moved by those who demonstrably understand and serve their interests, not by those who win '
    'arguments at them. It is the you-view from Chapter 2, scaled from a single message to an entire '
    'style of treating people — which means every technique in this section is audience analysis '
    'practiced as relationship, not merely as drafting craft. One warning governs the whole section, '
    'and Carnegie’s own writing led with it: every technique here fails completely when faked. These '
    'are practices for becoming genuinely interested in people, not scripts for appearing interested, '
    'and Chapter 8’s truth test — would the reader, seeing the technique named, still feel respected? — '
    'applies throughout.')
figure(doc, os.path.join(FIG, 'ch16_carnegie.png'),
    'Figure 3. The Carnegie core — four foundations, attributed to How to Win Friends and Influence People (1936).',
    'Four rows: don’t criticize, condemn, or complain (diagnose systems, correct behavior); give honest sincere '
    'appreciation (the five-quality note IS this principle); arouse an eager want (frame every ask in their interests); and '
    'become genuinely interested in people (outperforms trying to be interesting).')
para(doc, 'Criticism triggers defense rather than change — the psychology Chapter 7 already covered '
    'in detail — so the practical move is diagnosing systems and correcting behavior rather than '
    'issuing character verdicts. The five-quality goodwill note from Chapter 6 IS honest appreciation, '
    'stamped and delivered; the principle was already in the course before this chapter named its '
    'source. Arousing an eager want is Chapter 8’s entire persuasion engine, stated eighty-plus years '
    'earlier: frame every ask in the other person’s interests, never in your own convenience. And '
    'becoming genuinely interested in people — Carnegie’s claim that two months of real interest in '
    'others wins more friends than two years spent trying to be interesting — shows up validated in networking '
    '(Chapter 13), sales, and team leadership alike.')
para(doc, 'Three daily practices carry the foundation into ordinary weeks. A person’s name remains, in '
    'Carnegie’s phrase, the sweetest sound they know: spell it right (Chapter 4’s verification '
    'discipline), say it in greeting, use it in the thank-you — the smallest deposit that reliably '
    'lands. Being the listener — Chapter 1’s skill, aimed deliberately at good ends — means the '
    'colleague who paraphrases, asks the follow-up question, and remembers the answer next week becomes '
    'the most trusted person on a team by doing very little else. And talking in terms of others’ '
    'interests — opening with their project, their deadline, their win — is the conversational you-view; '
    'watch any meeting tilt toward whoever does this consistently. In modern channels the effect '
    'doubles: a remembered detail resurfacing in a follow-up email is written, permanent, forwardable '
    'proof that someone was actually listening.', bold_lead='Names, listening, and their interests.')
para(doc, 'The deepest human want, in Carnegie’s account, is to feel important and appreciated, and '
    'most workplaces run a permanent deficit of exactly this. The honest version is observational — '
    '“your triage call saved the launch” (Chapter 6’s specificity) demonstrates importance with '
    'evidence rather than inflating it with adjectives. Distribute it downward and sideways especially: '
    'praising upward is easily read as suspect, while praising down and across is closer to leadership '
    'itself (Chapter 6’s credit-routing). Flattery fails on contact because people reliably detect the '
    'difference between being seen and being buttered — the technique here is attention, and attention '
    'cannot be faked at any length worth mentioning.', bold_lead='Make them feel important — because they are.')

h1(doc, 'Winning people to your thinking')
para(doc, 'Carnegie’s rule that the only way to win an argument is to avoid one sounds like surrender '
    'until its logic is followed through: “victory” in a workplace argument leaves the loser convinced '
    'against their will, and a convinced-against-their-will colleague votes against the winner at the '
    'next meeting. Being right in the thread while the relationship dies is a loss wearing a trophy '
    '(Chapter 7’s flame-war case). The replacement for the duel is the question — “walk me through how '
    'you got there?” — which half the time surfaces the other person’s own gap and half the time '
    'surfaces the asker’s. And the professional who argues rarely is devastating when they finally do: '
    'argument frequency functions as a currency, and the stress-position logic from Chapter 3 applies '
    'socially — spend it rarely, and it means something when spent.', bold_lead='You can’t win an argument.')
para(doc, 'Direct contradiction — “you’re wrong” — locks the defense reflex from Chapter 7 every time; '
    'no one in recorded history has replied “good point, I’ll abandon my position.” Carnegie’s '
    'alternative, paraphrased for the workplace, costs nothing and opens everything: “I may be wrong '
    '— I often am. Let’s look at the data together.” Correct with questions and evidence — “how does that square with the March '
    'numbers?” — and let facts do the confronting while the correcting party stays a colleague rather '
    'than a prosecutor. When a correction genuinely must land on the record, contradict the claim, cite '
    'the source, and skip the victory lap: “the export shows 4%, not 14%” needs no editorial '
    'commentary (Chapter 9).', bold_lead='“You’re wrong” never works.')
para(doc, 'Admitting an error fast and emphatically beats every alternative, including silence. Beat '
    'the accusation to the punch — “before anyone checks, the Q2 figure was mine and it was wrong” — '
    'converts a prosecution into a footnote (Chapter 7’s apology anatomy, at leadership stakes). '
    'Self-criticism disarms completely because there is nothing left to argue once the speaker has said '
    'it harder than anyone else would have, and it buys the leader’s praise its value: the person who '
    'owns errors visibly is the only one whose “well done” actually means something (this chapter’s own '
    'debrief principle, personalized). The career math ties back to Chapter 7’s MUM-effect research: '
    'trust gets staked on how a person handles being wrong, precisely because everyone already knows '
    'they sometimes are.', bold_lead='Admit your errors fast.')
para(doc, 'Three tactical moves round out the set. Begin friendly: a drop of honey before business, in '
    'the Lincoln line Carnegie loved to quote, is Chapter 7’s buffer applied to every hard conversation, not only bad-news '
    'ones. Engineer the early yes: opening on genuine agreement — “we both need this shipped by Q4” — '
    'starts the psychology of consistency (Chapter 8) working in the conversation’s favor rather than '
    'against it. And let the other person talk first and fully: uninterrupted airing is frequently the '
    'concession people actually wanted, and it hands the listener, for free, the real objection to '
    'address — Chapter 8’s objection inventory, discovered rather than guessed.', bold_lead='Begin friendly; find the early yes; let them talk.')
para(doc, 'People fight for what they authored and against what they are handed, which makes ownership '
    'the strongest adoption force available — Chapter 8’s pilot case, where the once-skeptical '
    'colleague ends up presenting the winning results herself, is this principle in action. Plant '
    'ideas with questions: “what would fix the Friday bottleneck?” frequently lands in the same place '
    'as “here’s my fix,” with completely different adoption odds. Share credit structurally — “per '
    'Dana’s point…” (Chapter 8’s pre-wiring) turns visible fingerprints into co-ownership. The honest '
    'accounting: this is not selflessness so much as a conscious trade of credit for outcomes, made '
    'deliberately because the outcome mattering more than the authorship is usually true.',
    bold_lead='Let the idea be theirs.')
para(doc, 'Two final principles close the persuasion set. Try honestly to see the other person’s view '
    'first — not as a tactic but as an actual diagnosis, because resistance almost always makes sense '
    'from where the resister is standing (Chapter 8’s status-quo analysis). And appeal to the nobler '
    'motive: “you’ve always been the one who catches these” invokes a professional self-image people '
    'will strain to live up to, and it previews the reputation-effect section below — because the '
    'nobler motive being invoked is usually genuinely real, which makes the appeal accurate targeting '
    'rather than flattery.')

h1(doc, 'Leading people through change')
figure(doc, os.path.join(FIG, 'ch16_correcting.png'),
    'Figure 4. Correcting without crushing — praise first, the behavior indirectly, questions not orders, save face.',
    'A four-step sequence: honest praise first as the foundation, the behavior addressed indirectly, questions '
    'instead of orders, and saving face always — with the note that the goal is changed behavior AND an intact '
    'contributor, either alone being failure.')
para(doc, 'Carnegie’s leadership set governs correction specifically, and it runs as a sequence rather '
    'than a single move. Honest praise first — real and specific, never a softener disguising bad news '
    '(the fake-sandwich problem Chapter 7 already flagged). The behavior addressed indirectly where it '
    'works: “I’ve made this exact mistake” outperforms the pointed finger by removing the defensive '
    'trigger entirely. Questions rather than orders — “what would keep this from recurring?” — hands '
    'authorship back to the person being corrected, exactly per the section above. And face saved, '
    'always: correction stays private, dignity stays public, because the corrected person has to '
    'survive the correction and keep contributing (Chapter 7’s SBI structure, completed). The standard '
    'for the whole sequence: changed behavior AND an intact contributor. Either alone is a failed '
    'correction.')
figure(doc, os.path.join(FIG, 'ch16_reputation.png'),
    'Figure 5. The reputation to live up to — named identity, defended by behavior, self-enforcing over time.',
    'Two panels: a named reputation that must be true at least in trajectory, and the effect — the person defends '
    'that reputation with behavior, and spoken standards become identity that self-enforces — above the note that '
    'this corrects harder than any reprimand and hurts better.')
para(doc, 'Naming an identity someone can grow into is, by most accounts, Carnegie’s single most '
    'powerful and least-taught principle. “You’re the most careful reviewer on this team” gives the '
    'listener a reputation to defend with subsequent behavior — provided it is true at least in '
    'trajectory; granted reputations that are pure fiction read as sarcasm within a week, and the '
    'technique only works honestly. Used as correction for a generally strong performer, “this slipped, '
    'which surprised me — your work is usually the standard” corrects harder than any reprimand and '
    'hurts considerably less. And the same mechanism scales to teams: “this group doesn’t ship '
    'unverified numbers,” said aloud and repeatedly, becomes true partly because it was said — spoken '
    'standards become group identity, and identity, once established, self-enforces without further '
    'management (Chapter 11’s ground rules, internalized rather than merely written down).')

h1(doc, 'Case study: the turnaround supervisor')
para(doc, 'A new supervisor inherited a plant’s worst-performing line — quality misses, two pending '
    'grievances, a crew described to her in advance as “unmanageable.” Her first month ran almost '
    'entirely on listening: she asked every operator individually “what would you fix first?”, then '
    'implemented two of their answers visibly, crediting them by name on the shop floor board.')
para(doc, 'Corrections stayed private and question-shaped throughout; wins stayed public and '
    'name-attached. She told the crew, before it was fully true, that they were “the line that catches '
    'what the system misses” — a reputation to grow into, planted early. By month seven the line held '
    'the plant’s best quality record, with the same crew that had arrived labeled unmanageable. Her own '
    'summary of the turnaround: “I didn’t change the people. I changed what got noticed.” That sentence '
    'is this chapter, compressed to twelve words.')

h1(doc, 'A final case: the intern who led without a title')
para(doc, 'A summer intern on a product team noticed, in her third week, that two senior engineers '
    'were quietly duplicating effort on the same integration problem — each unaware the other had '
    'started, both too deep into their own work to notice the overlap in daily standups. She held no '
    'authority to redirect either of them and had been employed for eighteen days.')
para(doc, 'What she did draws on nearly every principle in this chapter despite her having read none '
    'of it formally. She did not announce the overlap publicly, which would have mildly embarrassed '
    'both engineers in front of the team (the private-correction principle, applied laterally rather '
    'than downward). She approached each separately with a genuine question rather than a correction: '
    '"I might be misunderstanding the architecture — are you both handling the payment-retry logic, '
    'or am I missing a division of work?" (the "I may be wrong" opener, deployed by someone with no '
    'standing to be right or wrong about it, which made it disarming rather than presumptuous). Both '
    'engineers, independently, realized the overlap themselves from her question rather than being '
    'told about it — letting the discovery be theirs rather than delivering it as a finding.')
para(doc, 'The two engineers resolved the division of labor between themselves within the hour, and '
    'one later mentioned the exchange to the team lead — not as a complaint, but as an example of '
    'exactly the kind of cross-team attentiveness the lead wanted to see more of. The intern received '
    'credit for the save despite never having claimed to have found a problem or fixed one; she had '
    'simply asked a well-framed question. The case closes this chapter appropriately: nothing in it '
    'required a title, years of experience, or formal authority. It required noticing something worth '
    'raising, and raising it in a way that let the people involved solve it themselves. That is '
    'leadership, in the sense this chapter has meant the word throughout.')

h1(doc, 'Building your own leadership communication practice')
para(doc, 'This chapter’s techniques compound the way every skill in this course compounds — through '
    'deliberate, low-stakes repetition long before a genuine crisis or a high-stakes influence '
    'situation demands them. A brief closing practice regimen, sized for a busy term.')
numbered(doc, [
    'Pick one Carnegie principle per week and apply it deliberately, even artificially at first — '
    'genuinely using someone’s name in every interaction, or asking one real follow-up question in '
    'every conversation. The artificiality fades with repetition; the habit does not form without it.',
    'Run a personal pre-mortem on one upcoming deadline or presentation: what would failure look '
    'like, and what is the cheapest insurance against the most likely version of it?',
    'The next time you receive criticism, practice the correction sequence in reverse — notice '
    'whether it was delivered with praise first, indirectly, as a question — and notice how the '
    'delivery affected your own receptiveness, data for your own future corrections of others.',
    'Draft, even without sending, the first-hour communication plan for a plausible crisis in your '
    'own field. Having written it once makes the real version faster to produce under actual pressure.',
])
para(doc, 'None of this requires a title or an assigned team. It requires treating leadership '
    'communication as a practiced skill rather than a trait some people have and others don’t — '
    'which has been this chapter’s claim from its first paragraph to its last.')

h1(doc, 'When the principles seem to fail')
para(doc, 'Students who try these techniques honestly sometimes report they "didn’t work" — the '
    'colleague still resisted, the manager still said no, the team member still repeated the mistake. '
    'Three diagnoses cover most of these reported failures, and distinguishing them matters more than '
    'abandoning the principle.')
bullets(doc, [
    ('The technique was performed, not practiced.', 'A scripted-sounding "I may be wrong" delivered '
     'without any genuine openness to being wrong reads as exactly what it is — Carnegie’s own '
     'sincerity warning, failing to land because it was skipped rather than because the principle '
     'itself is unsound.'),
    ('The underlying interest genuinely conflicted.', 'Not every disagreement has a shared interest '
     'waiting to be discovered underneath it (unlike the mediation case later in this chapter, where one existed). '
     'Sometimes the interests are actually opposed, and no amount of eager-want framing manufactures '
     'alignment that is not there — in those cases, the honest move is naming the real conflict '
     'rather than continuing to search for false harmony.'),
    ('One conversation was expected to undo a pattern.', 'A single well-run correction rarely reverses '
     'months of an established dynamic — Chapter 11’s trust account applies here too: these are '
     'deposit behaviors, not a single transaction, and judging a relationship-building principle by '
     'its first use mistakes the timescale it actually operates on.'),
])
para(doc, 'The diagnostic value of naming these three failure modes: it keeps a leader from either '
    'abandoning sound principles after one disappointing result, or from mechanically repeating a '
    'technique that was never going to work because the underlying condition (genuine interest, real '
    'shared ground, sufficient repetition) was never actually met.')

h1(doc, 'What Carnegie couldn’t have known')
para(doc, 'How to Win Friends and Influence People was written for a world of face-to-face sales calls, '
    'handwritten letters, and telephone party lines — no email, no video calls, no algorithmic '
    'feed deciding which of a leader’s words a team actually sees. The remarkable fact is how little '
    'updating the core principles need, and it is worth being explicit about why: Carnegie was never '
    'really writing about the tools of his era. He was writing about what people want — to be heard, '
    'to feel important, to author their own choices, to be corrected without humiliation — and those '
    'wants have proven far more stable than any communication channel built to serve them. The email '
    'and the video call are new; the eager want underneath every persuasive message is not.')
para(doc, 'What DOES need updating, and what this chapter has tried to supply throughout, is the '
    'application layer: how "become genuinely interested in people" operates across a Slack channel '
    'instead of a dinner conversation, how "give honest appreciation" survives translation into a '
    'five-quality email instead of a handwritten note, how "let the idea be theirs" functions when the idea '
    'is co-developed across a shared document rather than a single meeting. The principles are '
    'Carnegie’s. The channels are this course’s. Both halves matter, and neither substitutes for the '
    'other — a leader fluent in Slack norms but indifferent to genuine interest in people will '
    'communicate efficiently and influence no one; a leader with perfect Carnegie instincts who cannot '
    'operate the tools their team actually uses will have excellent intentions nobody encounters.')

h1(doc, 'A closing frame: the three questions of this chapter')
para(doc, 'Every technique across both halves of this chapter compresses into three questions worth '
    'running before any high-stakes communication, whatever the specific situation.')
numbered(doc, [
    'Am I responding to what is actually known, or to what I am assuming under pressure? (The '
    'pause-and-facts beats of the pressure protocol, run as a single check.)',
    'Am I framing this in terms of the other person’s stakes and interests, or my own convenience? '
    '(The eager-want principle, as a universal filter before speaking or writing.)',
    'If this technique were named aloud to the person it’s aimed at, would they still feel respected? '
    '(Chapter 8’s visibility test, which governs the entire influence half of this chapter and '
    'distinguishes leadership from manipulation in every case this chapter has examined.)',
])
para(doc, 'A genuine yes to all three describes most of what this chapter has to teach, compressed to '
    'three sentences a leader can run silently in the two seconds before responding to anything — '
    'which is, not coincidentally, exactly enough time for the pause this whole chapter opened with.')

h1(doc, 'Emotional intelligence as a communication infrastructure')
para(doc, 'Everything in this chapter rests on a capacity psychologists call emotional intelligence — '
    'reading one’s own emotional state and others’ accurately enough to communicate well despite it — '
    'and it is worth naming the underlying skill directly rather than leaving it implicit across a '
    'dozen techniques.')
bullets(doc, [
    ('Self-awareness under pressure', 'is what makes the pressure protocol’s first beat — pause — '
     'possible at all. A leader who cannot notice their own rising defensiveness in the moment cannot '
     'insert a pause before it drives the reply; this is a practiced skill, not an innate trait, '
     'built the same way any habit is built: repetition in lower-stakes moments before it is needed '
     'in high-stakes ones.'),
    ('Reading others accurately', 'underlies both the crisis section (sensing when a team needs more '
     'reassurance versus more information) and the influence section (sensing what someone’s real '
     'interest is, per the mediation case later in this chapter). Chapter 1’s listening skills are the practical '
     'entry point — most emotional-intelligence failures are actually attention failures first.'),
    ('Regulating one’s own response', 'is the skill behind composure’s performability: the finding '
     'that calm can be produced deliberately even under genuine internal stress depends on a learnable '
     'capacity to separate the felt emotion from the chosen behavior, not on suppressing the emotion '
     'itself.'),
])
para(doc, 'None of this requires clinical training. It requires treating "read the room, then choose '
    'your response deliberately" as a skill worth deliberately practicing — in low-stakes meetings, '
    'in ordinary disagreements — so that it is available under the higher-stakes conditions this '
    'chapter has spent most of its pages describing.')

h1(doc, 'Case study: the pre-mortem that paid off')
para(doc, 'A software team preparing to launch a payment-processing feature ran a pre-mortem two weeks '
    'before release, per their department’s standing practice. Among a dozen surfaced failure stories, '
    'one engineer — new to the team, generally quiet in meetings — offered a scenario the room '
    'initially waved off as unlikely: "what if the payment provider’s API silently changes its error '
    'format during a high-traffic period, and our retry logic interprets the new format as a different '
    'kind of failure than it actually is?" Two senior engineers noted it as "worth a ticket, low '
    'priority" and moved on.')
para(doc, 'The pre-mortem’s facilitator — running the discipline correctly — insisted every surfaced '
    'risk get an owner and a decision, not just a note. The junior engineer was assigned to investigate '
    'her own scenario, found that the retry logic genuinely had this gap, and fixed it before launch. '
    'Eleven weeks later, the payment provider DID change its error format during a traffic spike — the '
    'exact scenario, nearly verbatim. Because the fix already existed, the incident was a non-event: a '
    'log entry instead of an outage.')
para(doc, 'The case illustrates two principles at once. First, the pre-mortem’s value depends entirely '
    'on taking quiet voices seriously — the same "draw out the quiet expertise" principle from Chapter '
    '11’s meeting craft, here preventing a genuine outage rather than merely improving a discussion. '
    'Second, assigning ownership to every surfaced risk — not just the ones that feel urgent in the '
    'room — is what converts a pre-mortem from a venting exercise into an actual safeguard. The '
    'facilitator’s insistence on that discipline, more than any individual engineer’s foresight, is '
    'why the scenario got investigated instead of shelved.')

h1(doc, 'The pre-mortem: leading before the crisis exists')
para(doc, 'The most reliable form of crisis leadership happens before any crisis, in the deliberate '
    'practice of imagining failure while it is still cheap to prevent. A pre-mortem — gathering a team '
    'to ask "imagine this project failed spectacularly; what happened?" — surfaces risks that optimism '
    'bias hides during normal planning, and it does so by giving pessimism explicit permission and a '
    'time limit, exactly as Chapter 11’s chronic-pessimist protocol channels a difficult personality '
    'into a genuine contribution.')
bullets(doc, [
    ('Run it before launch, not after trouble starts.', 'The pre-mortem’s value is entirely in its '
     'timing — the same "what could go wrong" conversation held after a visible problem reads as '
     'blame-hunting; held before anything has gone wrong, it reads as diligence.'),
    ('Ask for specific failure stories, not general risks.', '"The vendor misses the deadline" is a '
     'category; "the vendor misses the deadline because their subcontractor’s subcontractor has a '
     'labor dispute nobody flagged" is a story specific enough to actually check.'),
    ('Assign an owner to investigate each surfaced risk,', 'exactly as Chapter 10’s risk section '
     'requires a named mitigation for every identified risk — a pre-mortem that produces a list '
     'nobody owns is a meeting, not a safeguard.'),
    ('Revisit the list at the actual crisis moment.', 'A well-run pre-mortem becomes the first '
     'artifact pulled out when trouble does arrive — "we flagged this exact scenario in March; here’s '
     'the plan we wrote then" converts foresight into immediate first-hour clarity.'),
])
para(doc, 'The pre-mortem is this chapter’s crisis-leadership discipline practiced in peacetime, and '
    'it is available to anyone on a team regardless of formal authority — running one requires only '
    'the willingness to ask the question and take the answers seriously, which returns to this '
    'chapter’s opening claim: leadership is a set of communication choices, not a title.')

h1(doc, 'Leading remote and distributed teams under pressure')
para(doc, 'Everything in this chapter’s crisis and influence sections gets harder when the team is not '
    'in one room, and the compounding effect of remote work on pressure situations deserves direct '
    'treatment, extending Chapter 1’s remote-work principles to leadership specifically.')
bullets(doc, [
    ('Composure is harder to read and harder to broadcast remotely.', 'A leader’s steady voice on a '
     'call carries less nonverbal reassurance than the same steadiness in a room — deliberately '
     'narrate calm rather than relying on it to transmit passively: "I want to be clear that we have a '
     'plan here, even though there’s real uncertainty" does explicitly what body language would do '
     'implicitly in person.'),
    ('The grapevine moves through different channels remotely', '— side Slack channels and private '
     'DMs replace the hallway, but the dynamic Chapter 1 describes is identical: silence from '
     'leadership gets filled by speculation somewhere, and the speed only changes format, not '
     'fundamentals. Feed the same official facts into whatever channel your team actually uses '
     'informally.'),
    ('The first-hour cadence needs an explicit channel commitment.', '"Updates will post in the '
     '#incident channel at 10, 2, and 5" replaces "I’ll let you know" — remote teams cannot read a '
     'leader visibly working the problem the way an in-person team can, so the cadence promise has '
     'to substitute for that visibility entirely.'),
    ('One-on-one check-ins carry more weight, not less, during distributed crises.', 'A leader who '
     'makes time for individual video calls during a stressful stretch signals investment that a '
     'group email cannot — the physical-presence principle from the nonverbal-leadership section later in this chapter, '
     'translated to the tools remote leadership actually has available.'),
])

h1(doc, 'Influence upward: managing your own manager')
para(doc, 'Every principle in this chapter applies with a specific twist when the person you are '
    'trying to influence outranks you, because the power asymmetry changes what is politically safe '
    'to say and how it must be framed.')
bullets(doc, [
    ('Frame requests in the manager’s stakes, not yours.', '"I need more resources" competes poorly '
     'against "the project you’re accountable for at the board meeting needs this input by Friday" — '
     'the eager-want principle, aimed upward, requires knowing what your manager is actually '
     'accountable for (often a level up from what they tell you directly).'),
    ('Deliver bad news to your manager the way Chapter 7 taught delivering it to anyone:', 'early, '
     'with a plan attached, never buried. A manager blindsided by a problem you knew about for a week '
     'loses more than information — they lose confidence in your reporting, which is far more '
     'expensive to rebuild (Chapter 11’s trust account, spent upward).'),
    ('Disagree with a manager’s decision using the same "I may be wrong" opener', 'this chapter '
     'recommends for peers — rank does not change the psychology of defensiveness, and a direct '
     '"you’re wrong" lands worse, not better, when the target outranks the speaker.'),
    ('Make your manager’s job easier as a standing practice,', 'not just during requests — the '
     'give-first principle (Chapter 13’s network-maintenance rule) applies to the relationship with '
     'your own boss as much as to any external contact, and it is the single most reliable way to '
     'earn the benefit of the doubt when you eventually need it.'),
])
para(doc, 'None of this is sycophancy — it is audience analysis (Chapter 2) applied to the single '
    'audience most early-career professionals think about least strategically: the person who writes '
    'their performance review.')

h1(doc, 'The apology that rebuilt a team')
para(doc, 'A department director had, over several months, developed a habit of publicly correcting '
    'staff mistakes in team meetings — never cruel, always factually accurate, but consistently '
    'public. Morale surveys eventually surfaced the pattern anonymously: people had stopped raising '
    'problems early because doing so risked a public correction later. The director, confronted with '
    'the data, had two paths — defend the practice as "just being direct," or apply this chapter’s own '
    'error-admission principle to leadership itself.')
para(doc, 'She chose the second, and the specific execution is instructive. In the next team meeting, '
    'she named the pattern herself, without waiting to be asked: "I’ve been correcting mistakes in '
     'front of the group, and the survey tells me that’s made this a harder place to admit problems '
    'early. That’s on me, and it stops now — corrections happen one-on-one from here forward." Twelve '
    'seconds, no defensiveness, no explanation that softened into an excuse. She modeled, in one '
    'moment, both the error-admission principle from this chapter and the private-correction standard '
    'it prescribes for everyone else.')
para(doc, 'The result, tracked in the following quarter’s survey, was a measurable rise in early '
    'problem reporting — precisely the MUM-effect reversal Chapter 7’s research would predict, now '
    'demonstrated at the leadership level rather than merely described in theory. The case argues a '
    'point this chapter has made from several directions: a leader’s willingness to apply these '
    'principles to their OWN behavior, publicly, is frequently more persuasive than any amount of '
    'telling others to apply them.')

h1(doc, 'Leadership writing: the memo that sets the tone for everyone below you')
para(doc, 'A disproportionate share of a leader’s influence travels through a small number of written '
    'artifacts — the all-hands email, the quarterly update, the memo announcing a hard decision — and '
    'these deserve their own treatment because their audience and stakes differ from any single '
    'message this course has covered elsewhere.')
bullets(doc, [
    ('State the decision before the reasoning.', 'Leadership writing that buries the actual decision '
     'under three paragraphs of context reads as either nervous or evasive — Chapter 3’s direct '
     'pattern applies with extra force here, because the reader’s first question is always "what is '
     'being decided, and does it affect me?"'),
    ('Own the decision explicitly, especially the unpopular ones.', '"I decided" or "we decided" '
     'lands more credibly than the passive "it has been decided" — Chapter 3’s passive-as-camouflage '
     'warning applies with particular force to leadership communication, where the passive voice reads '
     'as a leader hiding behind a decision rather than making it.'),
    ('Write for the person most affected, not the average reader.', 'A reorganization memo written to '
     'reassure the unaffected majority often fails the smaller group actually losing something — '
     'Chapter 2’s audience analysis, applied to the reader who will reread every sentence for what it '
     'means for them specifically.'),
    ('Close with what happens next, in concrete terms.', 'Leadership writing that ends on philosophy '
     '("we’re confident this positions us well for the future") without a next concrete step leaves '
     'the reader with feelings and no plan — Chapter 6’s dated-ask discipline applies to leadership '
     'messages exactly as it applies to routine ones.'),
])
para(doc, 'The unifying thread: leadership writing gets read more carefully and quoted more often than '
    'any other genre in this course, precisely because of the authority behind it — which means every '
    'principle from Chapters 3, 4, and 6 applies with the volume turned up, not with new rules invented.')

h1(doc, 'The public-facing crisis: media and external statements')
para(doc, 'Everything in this chapter’s crisis section applies internally; when a crisis reaches '
    'customers, media, or the public, several additional disciplines layer on top, extending Chapter '
    '7’s crisis-communication section from statements to spoken, on-record leadership.')
bullets(doc, [
    ('One spokesperson, consistently.', 'Multiple voices answering the same questions produce '
     'inconsistencies that become their own story — designate a single named spokesperson per crisis '
     'and route every external inquiry through them, even when it feels bureaucratic in the moment.'),
    ('Prepare the holding statement before you need it.', 'The four true things from Chapter 7’s '
     'holding-statement section — we know something happened, we’re investigating, here’s who’s '
     'affected as far as we know, here’s when we’ll say more — should exist as a template before any '
     'crisis, the way a fire drill exists before any actual fire.'),
    ('Never let legal review delete every human sentence.', 'Legally accurate and emotionally dead is '
     'its own failure mode (Chapter 7); the leader’s job is fighting for the human sentences inside a '
     'legally sound statement, not surrendering the statement entirely to counsel.'),
    ('Match the channel to the audience.', 'Employees deserve to hear consequential news before the '
     'press does, in a richer channel than a press release (Chapter 1’s pairing rule) — a workforce '
     'that learns of a crisis from the news before hearing from leadership internally has learned '
     'something corrosive about where they stand.'),
])
para(doc, 'The through-line connecting the public-facing crisis to everything else in this chapter: '
    'the audiences change, but honest unknowns, a promised cadence, and one consistent voice remain '
    'the load-bearing structure regardless of whether the audience is a shift of factory workers or a '
    'room of reporters.')

h1(doc, 'Reading the room: nonverbal leadership under pressure')
para(doc, 'Chapter 1 taught that nonverbal signals carry disproportionate weight when they conflict '
    'with words, and nowhere does this matter more than a leader addressing a nervous room. Three '
    'specific applications deserve emphasis here.')
bullets(doc, [
    ('Posture and pace broadcast the real message', 'faster than any words can correct it. A leader '
     'who says "we’ve got this handled" while visibly rushed and clipped is understood, correctly, to '
     'not have it handled — the room believes the body over the claim (Chapter 1’s conflict rule).'),
    ('Silence has to be filled deliberately, not accidentally.', 'A pause before answering a hard '
     'question reads as thoughtfulness; the identical pause accompanied by visible fidgeting reads as '
     'evasion. The content of the silence is nonverbal, and it is worth rehearsing exactly like the '
     'words (Chapter 12’s delivery discipline, applied to leadership moments rather than formal talks).'),
    ('Physical presence during a crisis is a message in itself.', 'A leader who visits the affected '
     'floor, shift, or team in person — even briefly, even without new information to share — '
     'communicates something no email can: that the crisis was worth their physical time. This is '
     'Chapter 1’s richness principle at its highest stakes application.'),
])

h1(doc, 'Leading through change and resistance')
para(doc, 'Beyond single crises, leaders regularly have to move a team or organization through a '
    'change nobody asked for — a reorganization, a system migration, a strategy pivot. The '
    'communication discipline differs from crisis response in one key way: there is usually time to '
    'plan the sequence, and the plan matters as much as any individual message.')
bullets(doc, [
    ('Name the why before the what.', 'People tolerate difficult changes when they understand the '
     'reasoning; they resist identical changes announced without one. "We’re consolidating vendors to '
     'cut $400K in overhead we can reinvest in the team" survives scrutiny; "leadership has decided to '
     'consolidate vendors" invites it (Chapter 8’s status-quo-pricing logic, applied to change '
     'management).'),
    ('Over-communicate during the ambiguous middle.', 'The period between announcement and full '
     'implementation is where rumor fills every silence (Chapter 1’s grapevine) — a change '
     'communication plan needs MORE frequent updates during this window, not fewer, even when there is '
     'genuinely little new to report.'),
    ('Let resisters be heard, not just informed.', 'Chapter 8’s "let them talk fully" principle scales '
     'to organizational change: a town hall that only broadcasts breeds more resistance than one that '
     'takes real questions, even unanswerable ones, because being heard is often the actual ask '
     'beneath the objection.'),
    ('Protect the early adopters visibly.', 'The colleague who volunteers to pilot the new system '
     'needs public credit and protection from the skeptics’ criticism — Chapter 6’s credit-routing, '
     'deployed as change-management strategy rather than simple courtesy.'),
])

h1(doc, 'Influence across cultures')
para(doc, 'Carnegie’s principles were written for a particular time and cultural context, and applying '
    'them globally requires the same calibration Chapter 1 taught for cross-cultural communication '
    'generally. Direct praise, for instance, lands as generous in some cultures and as excessive or '
    'even suspicious in others; the practice of "become genuinely interested in people" survives '
    'the translation far better than any specific phrasing does, because genuine interest is legible '
    'across register differences in a way that a scripted compliment is not.')
bullets(doc, [
    ('Public praise and public correction', 'both carry different weight across high-context and '
     'low-context cultures (Chapter 1). In many high-context settings, correcting someone in front of '
     'peers — even gently, even with a question — causes loss of face regardless of the questioner’s '
     'intent; the private-correction principle in this chapter is closer to a universal requirement '
     'in those settings than an optional best practice.'),
    ('The "eager want" framing translates,', 'but what counts as a legitimate interest to appeal to '
     'varies: individual advancement motivates powerfully in some cultures and reads as slightly '
     'crass in others, where team standing or collective outcomes are the more persuasive frame. '
     'Know which register the room runs on before choosing the appeal.'),
    ('Directness in admitting error', 'is read as refreshing candor in some cultures and as '
     'destabilizing in others, where a leader’s visible fallibility can undermine the authority the '
     'role is expected to project. The principle — take responsibility fast — usually survives; the '
     'delivery may need to shift from public to private.'),
])
para(doc, 'The generalizable rule, consistent with Chapter 1’s treatment of intercultural '
    'communication: hold the underlying principle (genuine interest, honest ownership, private '
     'correction, non-manipulative appeal) and let the specific delivery adapt to the room. Carnegie’s '
    'century-old book is a starting library, not a universal script.')

h1(doc, 'Case study: the meeting that mediated itself')
para(doc, 'Two department heads had been in an unresolved conflict for months — overlapping '
    'responsibilities, a shared budget line, and a history of terse emails CC’d to their common '
    'manager. The manager, new to the role and reluctant to simply issue a ruling, tried a different '
    'approach: she asked each of them, separately, "what does the other person need from you that '
    'they’re not getting?" — not "what’s wrong with them," which would have produced the usual '
    'grievance list, but a question aimed squarely at the other’s actual interest (Carnegie’s eager '
    'want, applied to mediation).')
para(doc, 'Both answers, independently, named the same thing: predictability. Department head A '
    'wanted advance notice before B’s team made requests that affected A’s staffing. Department head '
    'B wanted the same thing in reverse. Neither had ever stated this plainly to the other — months of '
    'friction had calcified into character judgments ("she’s territorial," "he doesn’t respect our '
    'timeline") that obscured a completely solvable logistics problem underneath.')
para(doc, 'The manager brought them together not to relitigate the friction but to solve the shared '
    'problem: a two-week notice norm for cross-team requests, written down in one paragraph (Chapter '
    '11’s ground rules), with both heads as co-authors rather than recipients of a ruling (letting the '
    'idea be theirs, quite literally). The conflict did not fully vanish — some interpersonal friction '
    'was real — but its operational fuel did, and the CC’d-manager emails stopped within a month. The '
    'manager’s method, reconstructed: she never criticized either party, she found the genuine shared '
    'interest beneath the complaint, and she let the solution belong to the people who had to live '
    'with it. Three Carnegie principles, one twenty-minute conversation, no ruling issued.')

h1(doc, 'Five myths, retired')
para(doc, 'Retired by the composure-is-performable finding: leaders who never feel afraid are rare to '
    'nonexistent. What distinguishes effective crisis leaders is not the absence of fear but the '
    'presence of a rehearsed protocol that functions despite it — this chapter’s whole first half.',
    bold_lead='Myth: great crisis leaders are naturally fearless.')
para(doc, 'Retired by the honest-unknowns principle: leaders who project total certainty during '
    'genuine uncertainty are gambling their credibility on being right, and the retracted guess costs '
    'more than the admitted unknown ever would. Confidence about the PROCESS, not about facts not yet '
    'known, is what actually reassures.', bold_lead='Myth: a good leader always projects total confidence.')
para(doc, 'Retired by the Carnegie core’s own leading warning: every technique in this chapter fails '
    'when performed without genuine underlying interest. Manipulation and influence are distinguished '
    'by exactly the same test Chapter 8 applied to persuasion — would the other person, seeing the '
    'technique named, still feel respected?', bold_lead='Myth: Carnegie’s techniques are manipulation with better branding.')
para(doc, 'Retired by the mediation case and the reputation-effect research alike: both principles '
    'work precisely because they respect the other person’s agency rather than overriding it. '
    'Coercion and influence produce different outcomes even when the immediate compliance looks '
    'similar — influence produces durable change; coercion produces compliance that evaporates the '
    'moment supervision does.', bold_lead='Myth: influence is just a softer word for control.')
para(doc, 'Retired by the "you can’t win an argument" principle itself, which is not conflict '
    'avoidance but conflict redirection — toward the idea rather than the person, toward questions '
    'rather than verdicts (Chapter 11’s productive-conflict distinction, applied here at the '
    'leadership level). Avoiding necessary disagreement is a failure of exactly the leadership this '
    'chapter describes.', bold_lead='Myth: good leaders avoid conflict entirely.')

h1(doc, 'Frequently asked questions')
para(doc, 'Genuinely, sometimes — Carnegie’s own warning applies here directly. If underlying respect '
    'or interest is absent, the technique reads as hollow no matter how well executed, because people '
    'detect insincerity reliably over time even when they cannot articulate how. The fix is not '
    'better delivery; it is examining whether the interest is real.', bold_lead='Can these techniques become manipulative if I don’t genuinely mean them?')
para(doc, 'Follow the escalation ladder from Chapter 11: direct conversation first, in writing if '
    'unresolved, then the team or a neutral third party. The techniques in this chapter work on '
    'reasonable disagreements; a colleague acting in bad faith requires a different, more '
    'documentation-heavy response that this chapter’s persuasion tools are not designed to solve alone.',
    bold_lead='What if the other person isn’t operating in good faith?')
para(doc, 'Address the situation, never the person’s character, exactly as the correction sequence '
    'prescribes — "the update didn’t go out and the client noticed" rather than "you’re unreliable." '
    'And do it in the moment or very soon after; delayed correction reads as an ambush regardless of '
    'how gently it is eventually delivered.', bold_lead='How do I correct a peer, not a direct report, without authority to back it up?')

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Run the pressure protocol — pause, facts, frame, forward — on the next email that makes your '
    'pulse rise before you reply. Time it; thirty seconds is the target.',
    'Draft the first-hour communication plan for a plausible crisis in your field: who acknowledges, '
    'who holds which of the three hats, what cadence gets promised.',
    'Spend one week running a single Carnegie practice deliberately — names, the second follow-up '
    'question, or downward credit-routing — and log what changes in how people respond to you.',
    'Rewrite a criticism you received recently as the four-step correction sequence would have '
    'delivered it. Notice what changes in your own likely reaction.',
    'Name one colleague a reputation to live up to this week — honestly, in trajectory — and observe '
    'what happens to their next piece of work.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Recall a leader you would follow anywhere. Which of this chapter’s specific behaviors did they '
    'run, and which did their situation never require?',
    'Carnegie claims you cannot win an argument. Find the genuine exception: when must a professional '
    'argue on the record, and how does the approach differ from an ordinary disagreement?',
    'Where is the line between granting someone a reputation to live up to and manipulating them with '
    'one? Build the test using Chapter 8’s visibility standard.',
    'The first-hour crisis protocol assumes a leader with some authority to assign roles. How does it '
     'adapt for someone influencing a crisis response without formal authority?',
    'Draft the first-hour communication plan for a crisis in a field or organization you know well. '
    'What would your "three hats" be, specifically?',
])

keyterms(doc, [
    ('Pressure protocol', 'pause, facts, frame, forward — the four-beat discipline for any '
     'high-stress reply, from a hot email to an organizational crisis.'),
    ('Clarity over reassurance', 'the principle that accurate hard news is actionable while comforting '
     'vagueness is not — and that clarity, done well, is also the kinder choice.'),
    ('Honest unknowns', 'stated uncertainty (“here’s what we don’t know yet”) that builds credibility '
     'and, by modeling honesty, makes upward reporting of bad news safer for everyone below the leader.'),
    ('The three hats', 'the first-hour crisis assignment of communication, the fix, and the log to '
     'separate owners, preventing the everyone-fixes-nobody-communicates failure.'),
    ('The Carnegie core', 'four foundational principles from How to Win Friends and Influence People '
     '(1936): don’t criticize; give honest appreciation; arouse an eager want; become genuinely interested in people.'),
    ('The eager want', 'framing any request in terms of the other person’s interests rather than the '
     'requester’s convenience — Chapter 8’s persuasion engine, Carnegie’s original formulation.'),
    ('Disagree-and-commit', '(cross-referenced from Chapter 11) — arguing fully before a decision, '
     'supporting it fully after — the discipline that keeps “winning arguments” from being necessary.'),
    ('The reputation effect', 'naming an honest, forward-looking identity for someone (“you’re the '
     'careful one”) that they then defend through subsequent behavior — self-enforcing once established.'),
    ('Correcting without crushing', 'the sequence of honest praise, indirect reference to the '
     'behavior, questions instead of orders, and saved face — aimed at changed behavior AND an intact contributor.'),
    ('Composure contagion', 'the finding that teams synchronize to a leader’s emotional state, making '
     'performed calm a functional leadership tool even under genuine internal stress.'),
])

quiz(doc, [
    ('The pressure protocol’s four beats, in order, are:',
     ['Facts, pause, forward, frame', 'Pause, facts, frame, forward', 'Frame, forward, facts, pause', 'Forward, facts, pause, frame']),
    ('"Clarity over reassurance" holds that:',
     ['Leaders should always sound optimistic', 'People can act on accurate hard news but not on comfortable vagueness',
      'Reassurance is never appropriate', 'Clarity requires blunt, cold delivery']),
    ('In the first hour of a crisis, the three "hats" that should go to separate people are:',
     ['Legal, HR, and finance', 'Communication, the fix, and the log', 'Sales, marketing, and operations', 'CEO, board, and press']),
    ('Honest unknowns build trust primarily because:',
     ['They lower expectations', 'Leader-admitted uncertainty makes it safer for others to report bad news honestly',
      'They satisfy legal disclosure requirements', 'They shorten crisis meetings']),
    ('Carnegie’s advice to "never say you’re wrong" directly is best replaced with:',
     ['Silence until proven right', 'A humble opener like "I may be wrong — let’s look at the data together"',
      'Immediate agreement to avoid conflict', 'Escalation to a manager']),
    ('Admitting your own error fast and emphatically works because:',
     ['It lowers performance expectations', 'It disarms the conversation and makes future praise credible',
      'It satisfies HR policy', 'It ends the discussion immediately']),
    ('"Let the idea be theirs" is effective because:',
     ['People forget who proposed what', 'People defend and adopt what they authored far more than what they are handed',
      'It avoids taking credit for failures', 'It is required in most workplaces']),
    ('Granting someone "a reputation to live up to" only works ethically when:',
     ['The person already knows it is flattery', 'It is true at least in trajectory, not pure fiction',
      'It is delivered publicly', 'It is paired with a material reward']),
    ('The correction sequence (praise, indirect reference, questions, saved face) aims for:',
     ['Compliance as fast as possible', 'Changed behavior AND an intact, still-contributing colleague',
      'Documentation for HR files', 'Public accountability']),
    ('The turnaround-supervisor case’s central lesson is that she:',
     ['Replaced most of the underperforming crew', 'Changed what got noticed and credited, not the people themselves',
      'Increased monitoring and reporting requirements', 'Focused exclusively on quality metrics']),
], ['b','b','b','b','b','b','b','b','b','b'])

references(doc, [
    'Carnegie, D. (1936). How to win friends and influence people. Simon & Schuster.',
    'Edmondson, A. C. (1999). Psychological safety and learning behavior in work teams. '
    'Administrative Science Quarterly, 44(2), 350–383.',
    'Goleman, D. (1995). Emotional intelligence. Bantam Books.',
    'Heifetz, R. A., & Linsky, M. (2002). Leadership on the line. Harvard Business School Press.',
    'Rosen, S., & Tesser, A. (1970). On reluctance to communicate undesirable information: The MUM '
    'effect. Sociometry, 33(3), 253–263.',
    'Rosenthal, R., & Jacobson, L. (1968). Pygmalion in the classroom. Holt, Rinehart & Winston. (The '
    'expectancy-effect research behind the reputation principle.)',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch16-study-guide.docx')
finish(doc, os.path.abspath(out))
