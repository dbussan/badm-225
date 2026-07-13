# Chapter 11 study guide — Professionalism, Teamwork, and Meetings (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(11, 'Professionalism, Teamwork, and Meetings',
    'Etiquette that compounds · teams that argue well · meetings people don’t dread')

h1(doc, 'Why this chapter exists')
para(doc, 'Everything you have built so far in this course — the planning discipline, the drafting craft, '
    'the revision system, the persuasive machinery, the report architecture — travels through a workplace '
    'made of people. Those people are keeping score, and the score they keep is not primarily about your '
    'prose. It is about whether you did what you said you would, whether working with you is easy or '
    'exhausting, whether your name on a meeting invite makes colleagues sigh or show up. This chapter is '
    'about that score: the behavioral layer that gives your documents their reputation before anyone reads a word.')
para(doc, 'A useful way to hold the whole chapter: your writing skills determine how good your messages CAN be; '
    'your professionalism determines how they are RECEIVED. A flawless status report from a colleague who has '
    'missed three quiet deadlines gets audited line by line. A two-sentence note from a colleague with a year '
    'of kept promises gets believed instantly. Same genre, same grammar — wildly different transaction costs. '
    'Professionalism is the discipline of driving those costs down, for everyone who has to deal with you.')
para(doc, 'The chapter runs in three movements. First, professionalism itself — defined behaviorally, as five '
    'daily practices rather than a dress code. Second, teamwork: ground rules, productive conflict, and the four '
    'failure modes that quietly kill groups. Third, meetings — the most expensive communication channel any '
    'organization runs, and the one most in need of the discipline this course has been building all term.')

h1(doc, 'Professionalism: predictability plus respect')
para(doc, 'Strip away the folklore — the firm handshakes, the suit advice, the corporate theater — and '
    'professionalism reduces to something almost mathematical: predictability plus respect, demonstrated in '
    'small repeated behaviors. Predictability means others can build plans on you the way engineers build on '
    'load ratings. Respect means the people around you never pay a hidden tax — in time, attention, or dignity — '
    'for your participation. Neither requires charisma. Both require repetition.', bold_lead='The definition.')
para(doc, 'Notice what this definition excludes. It excludes formality for its own sake: the stiffest writer in '
    'the building can be deeply unprofessional if deadlines slide and confidences leak. It excludes hours '
    'worked: the colleague who answers at midnight but forgets what she promised at noon is unpredictable with '
    'excellent lighting. And it excludes agreement: professionals disagree constantly — the second movement of '
    'this chapter is about disagreeing well. What the definition keeps is the pair of questions every colleague '
    'is silently asking about you: can I rely on it, and does it respect me?')

h2(doc, 'The five daily fundamentals')
figure(doc, os.path.join(FIG, 'ch11_fundamentals.png'),
    'Figure 1. The five daily fundamentals — each one checkable behavior, not personality.',
    'Five labeled rows: reliability (deadlines met, promises kept), responsiveness (acknowledge within a business day), '
    'polish (proofread everything), composure (never send angry), and discretion (confidences stay confidences).')
para(doc, 'Trust is built on boring consistency. The deadline met without drama, the meeting attended on time, '
    'the promise tracked in your own system so it cannot slip your memory — none of it is impressive on any given '
    'day, and all of it compounds. Reliability has a bookkeeping requirement most people miss: you cannot be '
    'reliable on memory alone. The professionals who never drop commitments are not better people; they write '
    'commitments down (Chapter 5’s task discipline) and review them. If you take one mechanical habit from this '
    'section, take that one.', bold_lead='Reliability.')
para(doc, 'Acknowledge within a business day, even when the real answer will take a week: “Got it — '
    'I’ll have the full numbers to you Friday.” That sentence costs fifteen seconds and buys enormous '
    'goodwill, because silence is not neutral. Silence reads as avoidance, overload, or disrespect, and the '
    'sender starts composing follow-ups and forming judgments. Responsiveness is not about speed of answers; '
    'it is about never leaving a counterparty in the dark about whether their message landed.', bold_lead='Responsiveness.')
para(doc, 'Everything you send is a work sample. The typo in your email is charged not against your typing but '
    'against your carefulness — the reader’s silent inference is “if this is how they treat a message, how do '
    'they treat the analysis?” Chapter 4 gave you the machinery: the proofread pass, the last-thing check, the '
    'verification of names and numbers. Professionalism is running that machinery even on the small stuff, '
    'because the small stuff is most of what people see.', bold_lead='Polish.')
para(doc, 'Never send angry. Draft it if you must — in a document, never in the reply window — then sleep, '
    'then edit, then usually delete (Chapter 7 built the full protocol). Composure extends past email: it is '
    'the level voice in the tense meeting, the refusal to match a hostile thread’s temperature, the two-second '
    'pause before responding to provocation. Under pressure, composure is the most visible professional behavior '
    'there is, because everyone else is failing at it simultaneously.', bold_lead='Composure.')
para(doc, 'What colleagues tell you in confidence stays in confidence — full stop. Gossip feels like currency '
    'and works like debt: every secret you pass buys momentary attention and permanently reprices you as a leak. '
    'The listener you gossip to runs the obvious inference — “what do they say about me?” — and adjusts. '
    'Discretion also covers the quieter leaks: the forwarded email that wasn’t yours to forward, the salary '
    'detail mentioned in passing, the org-chart speculation traded at lunch.', bold_lead='Discretion.')

h2(doc, 'Etiquette is bandwidth management')
para(doc, 'It is fashionable to treat workplace etiquette as decoration — inherited manners with no function. '
    'Treat it instead as engineering: every courtesy exists to keep a shared communication channel usable. '
    '“Please” and a correctly spelled name keep the receiver’s attention on your content instead of your '
    'carelessness. Waiting for a speaker to finish preserves the room’s single conversational thread. Arriving '
    'on time respects the arithmetic of a ten-person meeting, where five late minutes spend fifty person-minutes. '
    'The open laptop during a colleague’s presentation broadcasts, fluently and permanently, “this is my second '
    'screen.” Etiquette, in other words, is what Chapter 5 called attention economics — practiced at the level '
    'of behavior instead of subject lines.')
para(doc, 'Two implications follow. First, etiquette varies by room: the formality that reads as respect with a '
    'client reads as distance on a scrappy internal team. Reading and matching the local register (Chapter 2’s '
    'audience analysis, pointed at culture) is itself the professional skill, not any fixed set of rules. Second, '
    'when you do break a norm — interrupting because the building is on fire, escalating past a manager because '
    'the MUM effect has trapped bad news — break it visibly and explain it. Norms bent with stated reasons '
    'survive; norms broken silently become your reputation.')

h2(doc, 'The trust account')
figure(doc, os.path.join(FIG, 'ch11_trust.png'),
    'Figure 2. The trust account — deposits are small and constant; withdrawals are always larger.',
    'Two panels labeled deposits (kept promises, early warnings, credit passed down, specific thanks, honest yellows) and '
    'withdrawals (surprises, spin, hoarded credit, missed deadlines gone quiet), above a banner: high balance means cheap '
    'communication; an empty account means every message needs two pages of proof.')
para(doc, 'Every interaction with a colleague deposits into or withdraws from an account held in their memory. '
    'Kept promises, early warnings about slipping work, credit passed downward, the five-quality thank-you note '
    '(Chapter 6) — deposits. Surprises, spin, hoarded credit, the deadline that slid without a word — withdrawals. '
    'The account’s cruel arithmetic is asymmetry: deposits are small and must be constant; withdrawals are large '
    'and remembered. One “they knew and didn’t tell us” can spend a year of reliability in an afternoon.')
para(doc, 'Why frame it this way? Because the balance determines your communication costs for everything else '
    'in this course. High trust makes messages cheap: your two-line status update is believed, your one-paragraph '
    'proposal gets a fair reading, your “this needs to move to Thursday” is accepted without a defense brief. '
    'Low trust makes everything expensive: every claim needs evidence attached, every request needs context, '
    'every mistake needs a hearing. The professionals who seem to glide through organizations are not better '
    'writers than you are about to be — they are writing against a funded account.')
para(doc, 'One more property matters: you cannot make deposits during the withdrawal. The crisis that needs '
    'your credibility is the wrong time to start building it — which is why the five fundamentals have to run '
    'daily, in peacetime, on the boring messages, long before anything is at stake. Chapter 7’s slipping-launch '
    'case showed this from the message side; this chapter shows it from the account side.')

h1(doc, 'Teamwork: the structure of working together')
para(doc, 'Almost everything you produce after graduation will be produced with other people — co-authored, '
    'reviewed, merged, presented jointly, or delivered through a chain of colleagues who each add a piece. Team '
    'communication is therefore not a separate genre; it is the operating condition for all the genres. What '
    'changes in a team is that communication acquires structure: agreements about how decisions get made, how '
    'documents get shared, how disagreement gets processed, and how credit gets routed. Teams that make those '
    'agreements explicitly, in writing, before stakes rise, perform differently from teams that improvise them '
    'during their first crisis. This section is about making them explicitly.')

h2(doc, 'Ground rules: agree on process while nobody needs it')
para(doc, 'The single highest-leverage hour in any team’s life is the hour spent writing ground rules before '
    'the work starts. Not because the rules are profound — they rarely are — but because rules written during '
    'peace are cheap, and rules invented during war are impossible. When the contested decision arrives, a team '
    'with a written decision method argues about the decision; a team without one argues about how to argue, '
    'with the stakes already loaded.')
bullets(doc, [
    ('Decide how you’ll decide.', 'Consensus, majority vote, or owner-decides-after-input — any of the three '
     'works; not choosing is what fails. Name the method and the tiebreaker before the first contested call.'),
    ('Set the document rules.', 'One living copy in shared space, one named owner per document, drafts circulated '
     '24 hours before meetings, comments resolved by their authors — Chapter 5’s version discipline, adopted as law.'),
    ('Name the communication norms.', 'Which channel for what, expected response times, and the escalation ladder: '
     'when a chat thread has gone three rounds without converging, it becomes a call (Chapter 5’s graduation rule).'),
    ('Write the credit norm.', 'One line prevents the most common team wound: “every deliverable lists every '
     'contributor.” Adopted early, it makes credit disputes structurally impossible.'),
    ('Write it all down.', 'Unwritten norms are just the founders’ habits — invisible to whoever joins in week six, '
     'and unenforceable against whoever breaks them in week nine.'),
])
para(doc, 'A one-page team agreement covering those five items takes twenty minutes to draft and feels faintly '
    'ridiculous while you do it — five competent adults writing down that they will share documents properly. '
    'The case study later in this guide is about what happens without that ridiculous page, and what changed '
    'with it.')

h2(doc, 'Conflict about ideas, never about people')
figure(doc, os.path.join(FIG, 'ch11_conflict.png'),
    'Figure 3. Two kinds of conflict — specific and checkable versus general and unfalsifiable.',
    'Two panels contrast conflict about the idea (a specific, checkable claim about a timeline assumption, ending in a '
    'better decision) with conflict about the person (a general accusation that someone always lowballs timelines, ending '
    'in a winner, a loser, and a quieter team), with a repair line: restate as behavior plus impact.')
para(doc, 'Teams that never disagree are not harmonious — they are silent, and silence has a price equal to '
    'whatever the unvoiced objection knew. The pilot flaw someone noticed and didn’t raise, the budget '
    'assumption the quiet analyst doubted — organizations pay for these in exactly the currency they thought '
    'harmony was saving. The goal of team communication is therefore not less conflict; it is conflict of the '
    'productive kind, kept rigorously on the correct side of one line.')
para(doc, 'The line runs between the idea and the person. “The timeline assumes zero vendor delay — that’s '
    'the weak joint” attacks a claim: it is specific, checkable, and answerable with evidence. “You always '
    'lowball timelines” attacks a character: it is general, unfalsifiable, and answerable only with defense or '
    'counterattack. The first kind of conflict ends with a better decision and intact colleagues. The second '
    'ends with a winner, a loser, and a team that has learned to keep its objections private — which returns '
    'you to the silence you were trying to escape.')
para(doc, 'The repair, when conflict drifts personal, is Chapter 7’s SBI structure: restate the grievance as '
    'situation, behavior, impact. “You always lowball” becomes “In the March plan, the integration estimate '
    'was two weeks and it took six — that gap is what I’m worried about here.” Same concern, but now it is '
    'about evidence, and evidence can be discussed by adults.', bold_lead='The repair.')

h2(doc, 'Disagree, then commit — out loud')
para(doc, 'Productive conflict needs a second discipline to be safe: what happens after the decision. The '
    'pattern is disagree-and-commit. Before the decision, argue fully — that is what the meeting is for, and '
    'soft-pedaling your objection to be agreeable is a withdrawal from the team’s account disguised as a '
    'deposit. After the decision, the decision belongs to everyone, including the people who argued against it. '
    '“I voted against this, and here’s my full effort” is the most professional sentence in teamwork.')
para(doc, 'The defection to watch for — in others and in yourself — is hallway relitigation: accepting the '
    'decision in the room and then campaigning against it at lunch. It keeps the argument alive after the fair '
    'fight ended, and it teaches everyone that the meeting was theater. If genuinely new facts arrive, the '
    'professional move is to reopen formally: “the vendor slipped their date — does that change our call?” '
    'goes to the group, on the record, not to the grapevine.')

h2(doc, 'The four failure modes')
figure(doc, os.path.join(FIG, 'ch11_failuremodes.png'),
    'Figure 4. The four team failure modes and their fixes — each fix is a form of writing things down or making things public.',
    'Four cells: the freeloader (fix: tasks with names and dates in writing), the credit taker (fix: pass credit publicly '
    'and immediately), the hidden agenda (fix: name the topic and put it on the agenda), and the dominator (fix: structured turns).')
para(doc, 'Most team dysfunction is one of four recognizable patterns, and each survives on a specific '
    'ambiguity. The freeloader survives on vague assignments: when tasks have no names and no dates, uneven '
    'effort has no paper trail, and resentment grows privately until it detonates. The fix is boring and total: '
    'every task gets a name and a date, in writing, where everyone can see it. Freeloading cannot survive a '
    'visible task list; it doesn’t have to be confronted so much as documented out of existence.')
para(doc, 'The credit taker survives on routing ambiguity — in most organizations, credit flows to whoever '
    'reports the work rather than whoever did it. The structural fix is the credit norm from your ground rules; '
    'the behavioral fix is Chapter 6’s habit of passing credit publicly and immediately (“the analysis is '
    'Maya’s”). Do both, and the occasional credit taker exposes themselves against a background of visible '
    'attribution.')
para(doc, 'The hidden agenda survives on off-the-record decision-making: the real choice happens in a side '
    'conversation, and the meeting ratifies it without knowing it. The fix is sunlight — “that sounds like a '
    'real proposal; let’s put it on Thursday’s agenda” — said pleasantly and relentlessly. And the dominator '
    'survives on unstructured airtime: in a free-for-all, the loudest voice wins by volume, and the quiet '
    'expertise never surfaces. The fix is structure, applied by whoever holds the floor: “let’s hear from '
    'everyone on this one,” round-robin, written pre-reads (which let ideas compete before personalities do).')

h2(doc, 'The teammate contract')
para(doc, 'Underneath the group mechanics runs an individual obligation set — the teammate contract. Your '
    'deadline is someone else’s input: a slip you announce Tuesday is a plan, and the same slip discovered '
    'Friday is a betrayal (Chapter 7’s early-and-upward rule, applied laterally). Status gets reported without '
    'being asked: the three-line update — on track, slipping, need — is a gift to everyone downstream of you. '
    'Help gets requested early, not heroically: struggling silently for a week to avoid “bothering” anyone '
    'bothers everyone, later and worse. And reviews of teammates’ work run by Chapter 4’s rules: triaged, '
    'specific, kind, and about the work.')

h1(doc, 'Meetings: the most expensive channel')
figure(doc, os.path.join(FIG, 'ch11_meetingtest.png'),
    'Figure 5. The three-job test — decisions, conflict, and connection are the only jobs that need a live meeting.',
    'Three boxes labeled decisions, conflict, and connection, above a warning banner: a meeting doing none of the three '
    'is a message wearing a meeting costume; eight people for one hour, fifty weeks a year, is four hundred hours.')
para(doc, 'Price any meeting honestly and the number is startling: eight people for one hour is a full working '
    'day of organizational time. Priced that way, most standing meetings would never survive the expense report. '
    'The test that sorts the justified from the wasteful is the three-job test: live meetings earn their cost on '
    'exactly three jobs — decisions (choices that need live argument), conflict (disagreement that needs a room '
    'and a richer channel than text), and connection (the humans behind the usernames, which is a real job and '
    'not a soft one). A gathering doing none of the three is a message wearing a meeting costume, and Chapter 5 '
    'already taught you how to write the message.')

h2(doc, 'The anatomy of a meeting that works')
figure(doc, os.path.join(FIG, 'ch11_meeting.png'),
    'Figure 6. Meeting anatomy — written artifacts before and after; the live skill in the middle.',
    'A five-step flow: purpose named in the invite, agenda items as outcomes with owners and time boxes, the room limited '
    'to the needed, the record of decisions and owners sent within the hour, and follow-through tracking actions to done.')
para(doc, 'Chapter 5 built the written artifacts: the invite whose title names the outcome, the agenda whose '
    'items are outcomes with owners and time boxes, the two-line record — decisions, owners, dates — sent within '
    'the hour. This chapter adds the live skill in the middle: running the room. Five behaviors carry it.')
numbered(doc, [
    'Start on time, with the purpose: “we’re here to pick the vendor — by 2:25.” Starting late teaches '
    'punctual people to stop being punctual; restating the purpose resets everyone’s attention on the outcome.',
    'Hold the agenda visibly. The most interesting tangent is the meeting’s greatest threat: “good point — '
    'parking-lotting it so we finish item two” protects the room’s promise to itself. Parked items go in the '
    'record, so parking is deferral, not dismissal.',
    'Draw out the quiet expertise: “Dana, you ran the pilot — what did we miss?” The best information in the '
    'room frequently belongs to whoever is least likely to interrupt, and inviting it is the facilitator’s '
    'highest-value act.',
    'Read every decision back before moving on: “recording: we renew with TechServe; Maya drafts terms by the '
    '12th.” Contested wording surfaces immediately, while everyone is present — instead of in a minutes war '
    'three days later.',
    'End early when the work is done. Nothing builds meeting credibility faster than returning eleven minutes '
    'to ten calendars.',
])
para(doc, 'Most of your meeting life, especially early, happens in rooms you don’t run — and attendee craft '
    'is its own skill. Arrive prepared: pre-reads read, your data ready, your position thought through — '
    'preparation is visible within ninety seconds and permanently shapes how your contributions are weighed. '
    'Speak to move the item forward: add the missing fact, name the decision, or concede; speeches and '
    'repetition move nothing. Disagree in the room, not after it. And volunteer for actions you will actually '
    'complete — the follow-through list is where meeting reputations are made, one kept commitment at a time.',
    bold_lead='Being the best attendee.')

h2(doc, 'Remote and hybrid: the added rules')
para(doc, 'Remote meetings inherit every rule above plus Chapter 1’s virtual nonverbals: camera presence for '
    'discussion, mute discipline, one conversation at a time, and someone assigned to watch the chat — the '
    'parallel channel where remote participants raise hands in text. Hybrid meetings add the hardest problem: '
    'the room forgets the screen. Side conversations the microphone can’t catch, whiteboards the camera '
    'can’t see, decisions finished in the hallway after the call “ended” — all of it disenfranchises the '
    'remote half. Two fixes carry most of the weight: assign a remote advocate in the room whose job is '
    'noticing exclusion, and adopt the one-remote-all-remote rule — if one participant is on the screen, '
    'everyone runs the meeting as if they were.')

h1(doc, 'Case study: the team that wrote its rules after the blowup')
para(doc, 'A five-person product team — capable, experienced, well-staffed — launched a six-month project with '
    'no ground rules. Why would they need any? They were professionals. For two months the omission cost '
    'nothing. Then a client presentation went well, and the account manager who delivered it accepted the '
    'praise without mentioning that the analysis was almost entirely the work of two teammates. No rule had '
    'been broken, because there was no rule. The two analysts said nothing official; they simply stopped '
    'volunteering. Meeting contributions thinned. Drafts started arriving exactly on deadline and never a day '
    'early. One analyst began quietly copying her own manager on work products — insurance, of a kind.')
para(doc, 'The project limped for six weeks before the team lead named the problem in a one-on-one, heard the '
    'grievance, and did something unusual: instead of adjudicating the past, she called a meeting to write down '
    'the future. One page. How decisions get made (owner decides after input, and every input gets a written '
    'response). How documents move (one living copy, drafts 24 hours before meetings). How credit routes '
    '(“every deliverable lists every contributor” — one sentence). And how conflict gets processed (raise it '
    'about the work, within a week, in the room).')
para(doc, 'The skeptics called it kindergarten, and they were half right — nothing on the page was beyond a '
    'sixth-grade classroom. Then, in month five, the same fault line loaded again: a director praised the lead '
    'for a deliverable the whole team had built. This time the lead answered by protocol, in the meeting, '
    'without heroics: “the model is Priya’s and Tomas’s work; the framing is mine.” It took four seconds. '
    'The dispute that had cost six weeks in month two was structurally impossible in month five, because credit '
    'routing was no longer a virtue — it was a rule.')
bullets(doc, [
    ('The lesson about timing:', 'rules written during peace are cheap; rules invented during war are impossible. '
     'The one-page agreement took twenty minutes; its absence took six weeks.'),
    ('The lesson about form:', 'norms must be written to be enforceable. Everyone privately agreed credit should '
     'be shared — but until the sentence existed, sharing it was optional generosity, not accountable practice.'),
    ('The lesson about repair:', 'the lead fixed the future rather than prosecuting the past. Teams rarely need '
     'a verdict about the old wound; they need a structure that prevents the next one.'),
])

h1(doc, 'Case study: the meeting audit')
para(doc, 'A newly promoted director inherited a department with eleven standing meetings — a weekly all-hands, '
    'two staff meetings, three project syncs, four status reviews, and a Friday “alignment session” whose '
    'purpose nobody could state. Her predecessor had created none of them and cancelled none of them; standing '
    'meetings, like weeds, mostly arrive without a founder and outlive every reason. Her first month, she '
    'audited: for each meeting, she attended once, priced it (people × hours × frequency), and ran the '
    'three-job test — decisions, conflict, or connection?')
para(doc, 'The results were unglamorous and decisive. Four status reviews failed the test completely: '
    'information flowed one way, no decisions were made, and attendance had become performative. They became '
    'written updates — Chapter 5’s three-line format, posted Wednesdays, readable in thirty seconds. Two '
    'project syncs covered overlapping teams and merged. The Friday alignment session, priced at 300 '
    'person-hours a year, was retired without a single objection — its purpose had evaporated two '
    'reorganizations ago. One staff meeting shrank from sixty minutes to twenty-five by moving its status '
    'segment to writing and keeping only the two items that needed argument.')
para(doc, 'And the weekly all-hands survived untouched — because it passed the test on the third job. It made '
    'no decisions and processed no conflict, but it was where the department remained a group of humans rather '
    'than a distribution list: new faces introduced, wins celebrated, the quarter’s direction narrated by a '
    'person instead of a memo. Connection is a real job. The audit’s point was never that meetings are bad; '
    'it was that each one must know which job it does.')
para(doc, 'The arithmetic: roughly forty person-hours a week returned to the department, zero complaints, and '
    'no information lost — everything still flowed, in channels that cost reading speed instead of meeting '
    'speed. The direct quote from her retrospective is worth keeping: “nobody defends a dead meeting once '
    'someone prices it. But someone has to be willing to price it.” Be that someone, politely.')

h1(doc, 'The professional, in person')
para(doc, 'A generation fluent in every digital channel often has the least practice in the analog ones — and '
    'the analog moments still decide impressions out of proportion to their frequency. Four short field guides.')
h2(doc, 'The phone, still a professional instrument')
para(doc, 'Answer with your name — “Quality lab, this is Derek” — so the caller knows instantly that they’ve '
    'landed, and with whom. Reach for the phone deliberately when threads run hot or confused: two heated '
    'replies or three rounds of written confusion is the signal to switch channels (Chapter 1’s richness '
    'ladder), and then confirm the outcome in writing (Chapter 6). Leave voicemail in fifteen seconds: name, '
    'number spoken slowly, one-line reason, best callback window — and repeat the number at the end, because '
    'the listener is hunting for a pen. Schedule calls like meetings: “can I call at 2:00 for ten minutes '
    'about the audit?” respects a calendar the way cold calls, by design, do not.')
h2(doc, 'Introductions: the ninety-second skill')
para(doc, 'Introduce people to each other with names said clearly and context attached in both directions: '
    '“Dana, this is Marcus from facilities — Marcus, Dana runs the audit team.” Convention says introduce '
    'others to the senior or client party first, but a warm, clear introduction beats a perfectly ordered '
    'mumble every time. When you forget a name, say so once, fast — “I’m blanking on your name and I’m '
    'embarrassed about it” costs two seconds; a conversation engineered around avoidance costs the '
    'relationship. And when nobody introduces you, rescue the circle yourself: hand, name, role, one hook.')
h2(doc, 'Meals and work social events')
para(doc, 'The business meal is still the meeting: order mid-menu, mirror the host’s pace, and let the other '
    'party’s food arrive before your agenda does. On alcohol, the ceiling is one and the floor is zero — and '
    'no career was ever damaged by the floor. The work social event is work wearing a lanyard: the colleague '
    'you vent to at the holiday party is a coworker who heard you vent, which is Chapter 5’s permanence '
    'principle running on human memory instead of screenshots. Work the room like a professional: greet the '
    'host, meet two new people properly, leave on time.')
h2(doc, 'The first ninety days')
para(doc, 'Every reader of this guide will soon be new somewhere, and the onboarding window sets priors that '
    'take years to move. Default to over-professionalism early — punctual, prepared, camera on, names learned — '
    'because you can relax a formality later far more easily than you can un-relax one. Learn the norms before '
    'bending them: every team has channel habits, meeting culture, and unwritten rules; watch for two weeks '
    'before optimizing anything. Deliver something small, fast, and clean — the first finished task is the '
    'prior every later judgment updates from. And find the person who knows how things actually work, and buy '
    'the coffee. Every organization has a Dana. The map she carries is not written anywhere.')

h1(doc, 'Deep dive: the escalation ladder')
para(doc, 'Every professional eventually faces the situation the ground rules did not cover: a teammate’s '
    'missed commitments are sinking the project, a conflict has gone personal despite your repairs, a decision '
    'is being steered around the stated process. Escalation — taking the problem above the team — is the right '
    'tool for some of these moments and a trust-account catastrophe for others. The difference is almost never '
    'WHETHER you escalate; it is the order of steps you took first. Escalation is a ladder, and skipping rungs '
    'is what converts a legitimate concern into a reputation for going over people’s heads.')
numbered(doc, [
    'Rung one: the direct conversation. Private, about the behavior, in SBI form, with a genuine question '
    'attached: “the last three handoffs came after the deadline — what’s happening on your end?” The majority '
    'of problems die here, because most people are not villains; they are overloaded, blocked, or unaware. '
    'Skipping this rung is the cardinal sin of escalation: the manager’s first question will be “what did they '
    'say when you raised it?” — and “I didn’t” ends the meeting.',
    'Rung two: the direct conversation, in writing. If the spoken version changed nothing, restate it in a '
    'message — kind, factual, dated: “following up on our conversation: the Thursday handoff matters because '
    'my analysis depends on it. Can you commit to it, or should we re-plan?” This creates the record that makes '
    'rung three fair, and it often succeeds where speech failed, because written commitments bind differently.',
    'Rung three: the team. Some problems belong to the group, not to a boss: “I want to raise a process issue — '
    'handoffs are slipping and it’s compounding downstream. Can we fix the schedule or the ownership?” Framed '
    'as process rather than prosecution, this rung repairs most of what rungs one and two could not, without '
    'anyone above the team ever hearing a name.',
    'Rung four: the manager — with the ladder visible. “I’ve raised this directly twice, once in writing, and '
    'we took it to the team on the 10th; the pattern is unchanged and it now threatens the deliverable. I need '
    'help.” Every element of that sentence is doing work: the history proves fairness, the written trail proves '
    'accuracy, and the ask is for help rather than punishment. Escalation done this way DEPOSITS trust with '
    'everyone watching, including, remarkably often, the person escalated about.',
])
para(doc, 'Two boundary cases override the ladder. Genuine ethics violations — falsified data, harassment, '
    'safety — go up immediately; the ladder is for performance and process, never for integrity, and “I was '
    'following the escalation ladder” is no defense for sitting on a safety report. And anything you would '
    'want to know instantly if the roles were reversed (the reversal test from Chapter 1) probably should not '
    'wait for rung three.', bold_lead='The exceptions.')

h1(doc, 'Worked example: a team charter you can copy')
para(doc, 'Here is a complete one-page charter of the kind the blowup case ended with — drafted for a '
    'five-person student project team, but the structure survives contact with any workplace. Adapt the '
    'specifics; keep the categories.')
h2(doc, 'Team charter — Market Research Project (five members)')
bullets(doc, [
    ('Decisions.', 'Each deliverable has one owner. Owners decide after hearing input; every written objection '
     'gets a written response before the decision closes. Deadlocks on shared questions go to majority vote; '
     'the owner breaks ties.'),
    ('Documents.', 'One living copy of everything, in the shared drive — never emailed as attachments for '
     'editing. Drafts circulate 24 hours before any meeting that discusses them. Comments are resolved by '
     'whoever opened them. Frozen versions get dated names (“as-submitted-2026-04-12”).'),
    ('Communication.', 'Chat for coordination, email for record, meetings only for the three jobs (decide, '
     'resolve, connect). Response expectation: same day on weekdays. Three chat rounds without convergence '
     'means a call. Bad news travels fastest: a slipping task is announced the day it slips, with a plan.'),
    ('Credit.', 'Every deliverable lists every contributor. In presentations, each member presents their own '
     'work where format allows.'),
    ('Conflict.', 'Concerns are raised about the work, within a week, in the room — SBI form. Nothing about a '
     'teammate travels to anyone outside the team before it has been said to the teammate.'),
    ('Meetings.', 'Standing meeting Tuesdays, 25 minutes, agenda posted Monday noon or the meeting is '
     'cancelled by default. Decisions read back in the room; the two-line record posts within the hour.'),
])
para(doc, 'Twenty minutes of drafting, one page of text, and notice what it quietly encodes: Chapter 5’s '
    'version discipline, Chapter 7’s early-bad-news rule, Chapter 9’s decision minutes, this chapter’s credit '
    'norm and three-job test. A charter is the course’s toolkit, ratified as law by the people it governs. '
    'The cancellation-by-default clause deserves special notice — it makes the agenda load-bearing, which '
    'keeps the meeting honest forever.')

h1(doc, 'Worked example: one meeting, end to end')
para(doc, 'Because the meeting section’s advice is easier to copy than to invent, here is a complete, '
    'realistic artifact trail for one 25-minute meeting — invite, agenda, live facilitation moments, and the '
    'record. The team is choosing a survey platform for the market-research project.')
h2(doc, 'The invite (sent Monday, for Tuesday 2:00)')
para(doc, 'Subject: “Decide: survey platform (25 min, Tue 2:00).” Body: “Outcome: pick QForm or SurveyLite '
    'and unblock the questionnaire build. Pre-read: one-page comparison (link) — costs, limits, export '
    'formats. Come with a preference and your strongest objection to it. Optional for anyone not building '
    'the questionnaire; notes will post to the channel by 3:00.”')
para(doc, 'Every element is doing chapter work: the title is an outcome with a duration; the pre-read '
    'travels with expectations attached (“come with a preference”); attendance is honestly tiered; and the '
    'notes promise means nobody attends purely from fear of missing out.')
h2(doc, 'The agenda (in the invite body)')
numbered(doc, [
    '2:00 — Decision frame (2 min, Maya): what we’re choosing, what we’re NOT choosing today (analysis '
    'tooling is next week).',
    '2:02 — Comparison walkthrough questions only (8 min, Tomas owns the doc): clarifications, corrections, '
    'anything the one-pager got wrong.',
    '2:10 — The objection round (8 min, all): each person states their preference and their strongest '
    'objection TO IT — the two-sided discipline from Chapter 8, run as a meeting format.',
    '2:18 — Decide (5 min, Maya owns): read back the decision and the first two actions.',
    '2:23 — Parking lot review (2 min): anything captured mid-meeting gets an owner or gets dropped.',
])
para(doc, 'The objection round is worth stealing: requiring each person to argue against their own preference '
    'surfaces the real risks in eight minutes, prevents advocacy theater, and makes the eventual decision '
    'everyone’s (the ownership principle from Chapter 16, run in miniature).')
h2(doc, 'Three live moments, handled')
bullets(doc, [
    ('The tangent.', 'Mid-walkthrough, someone raises incentive budgets for survey respondents — real issue, '
     'wrong meeting. Facilitator: “Good catch — parking lot; it needs the budget sheet anyway. Back to export '
     'formats.” Eleven seconds, no one wounded, item captured.'),
    ('The quiet expert.', 'Priya, who ran surveys at her internship, has said nothing. “Priya, you’ve done '
     'this at scale — what breaks first?” Her answer (export format chaos with the cheaper tool) turns out to '
     'be the deciding fact. It was in the room the whole time; it just needed an invitation.'),
    ('The read-back.', '“Recording: we choose QForm. Tomas sets up the workspace by Thursday; Priya drafts '
     'the export template by Friday. Objections to the wording?” Silence that follows a read-back is consent; '
     'silence that follows a vague drift into the next topic is nothing at all.'),
])
h2(doc, 'The record (posted 2:41)')
para(doc, '“Survey platform — DECIDED: QForm ($0 tier, exports to CSV/SPSS). Actions: Tomas — workspace by '
    'Thu 4/16; Priya — export template by Fri 4/17. Parked: respondent incentives → Maya adds to budget-sheet '
    'agenda next week. Full comparison doc: (link).” Four lines. Same day. Findable in the channel forever. '
    'That artifact — not the meeting’s conversational brilliance — is what the project runs on.')

h1(doc, 'Office politics for honest people')
para(doc, '“Politics” is the word professionals use for influence routing they were not part of — and the '
    'reflexive contempt for it is a career mistake, because most of what gets called politics is legitimate '
    'coordination: pre-wiring proposals (Chapter 8), building coalitions of the genuinely affected, knowing '
    'who cares about what and telling them early. The honest version of politics is simply this chapter plus '
    'Chapter 16, practiced deliberately: deposits made before they are needed, credit routed generously, '
    'objections heard privately before decisions land publicly.')
bullets(doc, [
    ('Legitimate:', 'briefing a stakeholder before the meeting so the proposal isn’t an ambush; asking “who '
     'else should hear this first?”; building the coalition by incorporating objections visibly.'),
    ('Legitimate:', 'knowing the org chart’s REAL edition — who trusts whom, whose no is final — and routing '
     'work accordingly. That is not manipulation; it is a map.'),
    ('Corrosive:', 'information hoarded as leverage; alliances that require an enemy; praise up and contempt '
     'down; the hidden agenda in any of its costumes. The test is Chapter 8’s: would this move survive being '
     'described, out loud, to everyone it touches?'),
])
para(doc, 'The professionals who claim to be “above politics” usually mean they have opted out of influence — '
    'and their ideas, however good, inherit the consequences. You do not have to like the game. You do have to '
    'know that pre-wired, coalition-backed, generously credited proposals beat identical proposals without '
    'those things, everywhere, forever. Choosing not to do the honest version does not make you pure; it '
    'makes you outvoted.')

h1(doc, 'Async-first teams: professionalism without a shared clock')
para(doc, 'Distributed and flexible teams increasingly run async-first: the default channel is written, '
    'meetings are the exception requiring justification, and colleagues may not share four working hours. '
    'Async-first does not relax this chapter’s standards — it concentrates them. Reliability becomes the '
    'whole game when nobody can see effort (Chapter 1’s remote-work rule: visible written updates replace '
    'the hallway). The three-line status update stops being a courtesy and becomes the team’s only '
    'heartbeat. Decision minutes stop being good practice and become the only institutional memory there is.')
bullets(doc, [
    ('Write decisions where the absent can find them.', 'A decision that lives in a meeting recording nobody '
     'will scrub is async-hostile; the two-line record in the channel is the async-native form.'),
    ('Make messages complete (Chapter 5).', 'A question that takes three round-trips costs three DAYS across '
     'time zones. The complete-ask standard is not politeness in async teams; it is velocity.'),
    ('Respect the overlap window.', 'The two or three shared hours are for the three jobs — decisions, '
     'conflict, connection — and nothing else. Status never spends overlap time.'),
    ('Default documents to public.', 'In async teams, the DM is where information goes to die. Work happens '
     'in channels and shared docs; private messages carry only what is genuinely private.'),
])

h1(doc, 'Repairing your own withdrawal')
para(doc, 'Sooner or later the trust-account withdrawal will be yours: the deadline you let slip silently, '
    'the credit you absorbed without thinking, the vent that traveled. The repair protocol is Chapter 7’s '
    'apology anatomy, applied at teammate range — and speed matters more than eloquence. Own the act '
    'specifically (“I presented the model as ours and let the room think the framing was the work — the '
    'model is yours”). Name the impact without being told it. State the prevention, not just the regret '
    '(“in Thursday’s review I’ll open with the attribution”). Then stop: one clean repair outperforms a '
    'week of hallway penance, and the follow-through — the prevention actually happening — is the part '
    'that refills the account. Teams do not expect flawless colleagues. They expect colleagues whose '
    'failures are announced by the colleague, not discovered by the team.')

h1(doc, 'The extended field guide: three more difficult colleagues')
para(doc, 'The four failure modes covered the structural offenders — the ones ambiguity creates. Three more '
    'characters recur in every organization, and each has a communication protocol that works better than the '
    'instinctive response.')
para(doc, 'Every proposal is met with the complete catalog of what could go wrong — delivered with visible '
    'satisfaction. The instinctive response is to stop inviting them, which is exactly wrong: chronic '
    'pessimists are frequently your best risk-detection instrument running without an output filter. The '
    'protocol is to give the pessimism a job: “you’re better at failure modes than anyone here — take the '
    'plan and give me the top three risks WITH mitigations by Thursday.” Half the time you get the best risk '
    'section of your career. The other half, the pessimist discovers that cataloguing problems now comes with '
    'homework, and the recreational version stops. Either outcome improves the team.',
    bold_lead='The chronic pessimist.')
para(doc, 'Everything is urgent, always: the Friday 4:50 request that “has to go out tonight,” the third '
    '“drop everything” this month. The protocol is the calm clarifying question, asked every time: “I can do '
    'this by tomorrow noon, or I can drop the audit prep and do it tonight — which do you want?” Manufactured '
    'urgency runs on the assumption that nobody will price the trade-off out loud. Pricing it — pleasantly, '
    'reliably, in writing where possible — converts the emergency manufacturer into someone who plans, at '
    'least when dealing with you. (Genuine emergencies survive the question comfortably; that is how you '
    'tell them apart.)', bold_lead='The emergency manufacturer.')
para(doc, 'Messages vanish into them; commitments dissolve; the thread goes quiet exactly when their input '
    'is due. The protocol is structure, not pursuit: dated asks with named consequences of silence — “if I '
    'don’t hear by Wednesday noon, I’ll proceed with option A” (Chapter 6’s deadline-with-reason, weaponized '
    'gently). This converts their silence from a blocker into an answer, keeps your work moving, and creates '
    'the written trail the escalation ladder needs if the pattern persists. Never let a ghost make their '
    'unresponsiveness your missed deadline.', bold_lead='The ghost.')

h1(doc, 'Case study: the new hire who watched first')
para(doc, 'Two analysts joined the same operations team in the same month. Both were technically strong; both '
    'noticed within a week that the team’s Thursday review meeting was a broadcast wearing a meeting costume, '
    'and that the shared-drive folder structure was archaeology in progress. What they did with identical '
    'observations is the case.')
para(doc, 'Analyst one announced his findings in week two — in the Thursday meeting itself: the meeting was '
    'inefficient, the folder structure needed rebuilding, and he had already drafted a new taxonomy. He was '
    'right on every count. It did not matter. The team heard a fourteen-day veteran declaring their habits '
    'broken, the meeting’s owner heard her creation called waste in front of her manager, and the folder '
    'taxonomy — genuinely better — was adopted by nobody. His technical work was strong all year; his '
    'influence never recovered from week two. He had spent trust he had not yet deposited.')
para(doc, 'Analyst two ran the ninety-day protocol. She watched for a month, learned the norms before bending '
    'any (why DID the Thursday meeting exist? — it turned out to predate the status dashboard that had made '
    'it redundant), and delivered something small, fast, and clean: a cleanup of one project folder, done '
    'inside the existing taxonomy, unannounced. People noticed. In week seven she asked the meeting’s owner '
    'a question in private: “would it help if status moved to a written update and Thursday kept just the '
    'two discussion items?” — framed as her problem (“I’m still learning; the written version would help me '
    'keep up”). The owner piloted it in week nine as her own idea, which by then it half was. By month four, '
    'the meeting was 25 minutes, the folders were migrating to a structure the team believed it had designed, '
    'and analyst two was running onboarding for the next hire.')
bullets(doc, [
    ('The lesson about sequence:', 'deposits before proposals. Identical observations, identical solutions — '
     'the only variable was whether the account could fund the ask.'),
    ('The lesson about authorship:', 'analyst two gave both ideas away (Chapter 16’s let-the-idea-be-theirs) '
     'and collected the outcome instead of the credit. The outcome compounds; the credit would have expired.'),
    ('The lesson about norms:', 'the Thursday meeting had a reason once. Learning the history before proposing '
     'the change is what made the change adoptable — and is the difference between improvement and insult.'),
])

h1(doc, 'The composure toolkit: scripts for five hot moments')
para(doc, 'Composure fails not because people lack the trait but because the hot moment arrives faster than '
    'judgment. The fix is the same one Chapter 12 used for presentation nerves: script the load-bearing '
    'moments in advance, so autopilot carries you through the adrenaline. Five scripts cover most of a '
    'career’s worth of provocation.')
bullets(doc, [
    ('Blamed unfairly in a meeting.', '“Let me make sure I have the facts before we assign causes — I’ll '
     'pull the timeline and post it in the channel by 3:00.” No defense, no counterattack, no concession: '
     'a promised artifact. The timeline defends you better than any speech, and the room remembers who '
     'stayed procedural.'),
    ('Interrupted repeatedly.', '“I’ll finish this point, then I want to hear your take.” Said levelly, '
     'once — it names the interruption without prosecuting it. If the pattern persists, the structured-turns '
     'fix from the dominator protocol applies, requested of whoever holds the floor.'),
    ('Handed someone else’s anger.', 'The de-escalation sequence from Chapter 7, compressed: acknowledge '
     '(“this cost you a weekend — I get why you’re hot”), align (“we both need this fixed before Monday”), '
     'then move to facts and the next concrete step. Never match the temperature; one of you has to be the '
     'professional, and it is you.'),
    ('Asked to bend something in public.', '“I can’t do that — but here’s what I can do” (Chapter 7’s '
     'adjacent yes, under pressure). The refusal is quiet and total; the pivot is immediate. Refusing '
     'without theatrics is what makes refusing repeatable.'),
    ('Caught in your own visible mistake.', '“That’s my error. Here’s the correction, and here’s what '
     'prevents the repeat.” Twelve words of ownership outperform any explanation — and the room’s respect '
     'for the fast, clean admission is the most reliably underestimated force in professional life '
     '(Chapter 16’s error-admission principle, live).'),
])
para(doc, 'Notice what all five scripts share: each converts an emotional exchange into a procedural one — '
    'a timeline to post, a turn to finish, a step to take, an alternative to offer, a correction to ship. '
    'That conversion is what composure actually IS, mechanically: the practiced habit of answering heat '
    'with process. People who seem unflappable are rarely feeling less; they are running better scripts.')

h1(doc, 'Deep dive: writing the peer evaluation')
para(doc, 'Student teams end in peer evaluations; workplace teams end in 360 reviews — same genre, same '
    'traps. The document asks you to convert months of collaboration into an assessment someone else will '
    'act on, and most writers fail toward one of two poles: the everything-was-great evaluation (which '
    'defrauds the strong contributors by pricing everyone identically) or the grievance file (which reads '
    'as score-settling and discredits its own evidence). The professional version runs on this chapter’s '
    'machinery.')
bullets(doc, [
    ('Evaluate behavior, not character —', 'SBI at document length. “Missed three of five integration '
     'handoffs; the pattern cost us the April buffer” can be acted on; “unreliable and doesn’t care” '
     'cannot, and says as much about the writer.'),
    ('Report the distribution honestly.', 'If contributions were unequal, say so with evidence — the '
     'visible task list from the freeloader protocol is now your source document. This is what the list '
     'was FOR.'),
    ('Give the strong performers their specifics.', '“Priya’s export template saved every later phase” is '
     'a deposit that costs nothing and follows her — the five-quality rules apply to evaluations too.'),
    ('Write nothing you haven’t said.', 'The evaluation should surprise no one (the escalation ladder’s '
     'rung one guarantees this). A grievance appearing first in a peer evaluation convicts two people, '
     'and one of them is you.'),
    ('Sign it in your head.', 'Anonymous or not, write as if the subject will read it with your name '
     'attached — the reversal test, one last time. Evaluations written to that standard need no editing '
     'when the process turns out to be less anonymous than advertised. It usually does.'),
])

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Pick your weakest fundamental — most people know theirs instantly — and choose the smallest visible '
    'behavior that moves it: a commitment tracker for reliability, the fifteen-second acknowledgment for '
    'responsiveness, the read-aloud pass for polish.',
    'Draft the one-page team agreement for your current group project: decision method, document rules, '
    'communication norms, credit norm. Propose it at the next meeting and watch how fast adults adopt a '
    'kindergarten page.',
    'Price one standing meeting you attend (people × hours × frequency) and run the three-job test. If it '
    'fails, draft the written update that would replace it — then pitch the swap with Chapter 8’s machinery.',
    'Read every decision back at your next meeting, whoever is running it: “so we’re recording: X, owned by '
    'Y, by date Z?” Watch how often the room discovers it hadn’t actually decided.',
    'Route one piece of credit downward this week, publicly and by name — and notice what it costs you. '
    '(Nothing. It costs nothing.)',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Which of the five fundamentals is hardest to sustain in your actual week, and what is the mechanical '
    '(not motivational) fix — the system change that makes the behavior automatic?',
    'Describe a team conflict you have witnessed. Was it about the idea or the person — and precisely where '
    'did it cross the line? What single sentence, said by whom, would have kept it productive?',
    'Disagree-and-commit assumes the decision process was fair. What should a professional do when it wasn’t — '
    'when the hidden agenda won? Distinguish the professional responses from the corrosive ones.',
    'Run the three-job test on a meeting you attend regularly. If it fails, why does it survive? Name the '
    'incentive that keeps a dead meeting alive, and design the pitch that retires it without offending its owner.',
    'Which failure mode have you been — freeloader, credit taker, hidden agenda, or dominator? (Everyone has '
    'been at least one.) What ambiguity made it possible, and what written rule would have stopped you?',
])

keyterms(doc, [
    ('Professionalism', 'predictability plus respect, demonstrated in small repeated behaviors — reliability, '
     'responsiveness, polish, composure, and discretion practiced daily.'),
    ('Trust account', 'the running balance of deposits (kept promises, early warnings, shared credit) and '
     'withdrawals (surprises, spin, silence) each colleague holds about you; high balances make communication cheap.'),
    ('Ground rules', 'a team’s written agreements — decision method, document rules, communication norms, '
     'credit norm — made before stakes rise, when agreement is cheap.'),
    ('Productive conflict', 'disagreement about ideas: specific, checkable claims aimed at the work, ending in '
     'better decisions with intact colleagues.'),
    ('Disagree and commit', 'the discipline of arguing fully before a decision and supporting it fully after — '
     'with formal reopening (not hallway relitigation) if new facts arrive.'),
    ('Freeloading', 'uneven team effort that survives on vague assignments; documented out of existence by '
     'tasks with names and dates in writing.'),
    ('Hidden agenda', 'a decision maneuvered outside the stated process; fixed by sunlight — naming the topic '
     'and putting it on the agenda.'),
    ('Three-job test', 'the audit for any meeting: does it make decisions, process conflict, or build '
     'connection? None of the three means it should be a written message.'),
    ('Decision minutes', 'the two-line meeting record — decisions, owners, dates — sent within the hour '
     '(Chapter 9’s format, applied everywhere).'),
    ('One-remote-all-remote rule', 'if one participant joins a meeting by screen, the meeting runs by remote '
     'rules for everyone — the standard fix for hybrid’s two-tier problem.'),
    ('Remote advocate', 'the in-room participant assigned to notice and interrupt the exclusion of remote '
     'attendees in hybrid meetings.'),
    ('Parking lot', 'the visible list of worthy-but-off-agenda items captured during a meeting — deferral with '
     'a paper trail, not dismissal.'),
])

quiz(doc, [
    ('A colleague is consistently brilliant but misses roughly a third of his commitments without warning. '
     'In this chapter’s terms, his core failure is one of:',
     ['Polish', 'Reliability — predictability is the first half of professionalism', 'Discretion', 'Etiquette']),
    ('The trust account’s central asymmetry is that:',
     ['Deposits require seniority', 'Withdrawals are impossible to detect',
      'Deposits are small and constant while withdrawals are large and remembered', 'Balances reset each quarter']),
    ('A team should write its ground rules:',
     ['After the first conflict reveals what rules are needed', 'Before stakes rise, when agreement is cheap',
      'Only if required by management', 'During the project retrospective']),
    ('“You always lowball timelines” fails as team communication because it is:',
     ['Too specific about dates', 'General and unfalsifiable — aimed at character rather than checkable behavior',
      'Delivered in writing', 'Insufficiently formal']),
    ('Disagree-and-commit is violated most directly by:',
     ['Arguing forcefully before the decision', 'Voting against the winning option',
      'Hallway relitigation after the decision', 'Asking to reopen when new facts arrive']),
    ('The structural fix for freeloading is:',
     ['A confrontation about work ethic', 'Tasks with names and dates, in writing, visible to all',
      'Reassigning the freeloader’s work quietly', 'An anonymous complaint channel']),
    ('A weekly meeting where one person reads status to eight silent listeners fails the three-job test because:',
     ['Status is confidential', 'It makes no decisions, processes no conflict, and builds no connection — it’s a message in a room',
      'Eight is too few attendees', 'Status meetings require managers']),
    ('Reading a decision back in the room (“recording: we renew; Maya drafts by the 12th”) exists to:',
     ['Fill remaining agenda time', 'Surface contested wording while everyone is present, before the minutes war',
      'Demonstrate the facilitator’s authority', 'Replace written minutes entirely']),
    ('The one-remote-all-remote rule addresses:',
     ['Bandwidth costs of video', 'Hybrid meetings’ two-tier problem, where the room forgets the screen',
      'Time-zone scheduling', 'Camera fatigue']),
    ('In the meeting-audit case, the all-hands survived the audit because:',
     ['Leadership required it', 'It was the cheapest meeting',
      'It did the connection job — a legitimate third job of live meetings', 'Nobody attended it anyway']),
], ['b','c','b','b','c','b','b','b','b','c'])

references(doc, [
    'Carnegie, D. (1936). How to win friends and influence people. Simon & Schuster.',
    'Covey, S. R. (1989). The 7 habits of highly effective people. Free Press. (The emotional bank account '
    'metaphor this chapter’s trust account adapts.)',
    'Edmondson, A. C. (1999). Psychological safety and learning behavior in work teams. Administrative Science '
    'Quarterly, 44(2), 350–383.',
    'Grant, A. (2013). Give and take: A revolutionary approach to success. Viking.',
    'Lencioni, P. (2002). The five dysfunctions of a team. Jossey-Bass.',
    'Rogelberg, S. G. (2019). The surprising science of meetings. Oxford University Press.',
    'Rosen, S., & Tesser, A. (1970). On reluctance to communicate undesirable information: The MUM effect. '
    'Sociometry, 33(3), 253–263.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch11-study-guide.docx')
finish(doc, os.path.abspath(out))
