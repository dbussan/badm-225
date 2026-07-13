# Chapter 16 — Leadership Under Pressure & Influence (37 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 16"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Leadership Under Pressure & Influence",
    "Crisis clarity · influence without authority · the people principles that have worked for a century", D)
notes(s, "Chapter 16: leadership communication. Part one: pressure and crisis. Part two: influence principles in the tradition of Dale Carnegie's How to Win Friends and Influence People — attributed, and translated to the modern workplace.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Communicate", "under pressure with the protocol: pause, facts, frame, forward — clarity over reassurance."),
    ("Lead", "through a crisis: the first hour, the honest unknowns, the cadence that replaces rumor."),
    ("Influence", "without authority: genuine interest, real appreciation, and arguments won by not having them."),
    ("Correct", "people so the behavior changes AND the person keeps contributing — face saved, standard kept."),
    ("Build", "the reputation-to-live-up-to effect in teams — the influence tool that works while you sleep."),
], D, nxt())
notes(s, "Objectives map to the Chapter 16 practice bank. The influence sections draw on Carnegie (1936) with modern translation — always attributed.")

s = section_slide(prs, "01", "Pressure reveals",
    "Stress doesn't build communication character. It exposes it.", D, nxt())
notes(s, "Section 1: what pressure does, and the protocol that holds.")

s = bullets_slide(prs, "What pressure does to communication", [
    ("It narrows:", "under stress, people write faster, read less, assume more — precisely when precision matters most."),
    ("It leaks:", "your tension transmits in word choice, punctuation, and pace — the team reads your temperature before your text (Chapter 1's nonverbals, in prose)."),
    ("It shortcuts:", "the verification pass, the tone pass, the cooling-off period (Chapter 4) — the disciplines drop exactly when their absence costs most."),
    ("The leader's job is to be the exception:", "someone in the room has to slow down on purpose. Deciding it's you is most of leadership."),
], D, nxt())
notes(s, "The diagnosis slide. 'Deciding it's you' frames leadership as a communication choice available to anyone — no title required, which is the chapter's through-line.")

s = bullets_slide(prs, "Clarity over reassurance", [
    ("People can act on accurate hard news;", "they cannot act on comfortable fog — 'we'll be fine' plans nothing, staffs nothing, fixes nothing."),
    ("Reassurance spends trust; clarity builds it:", "the leader who said 'fine' before the layoff is never believed again — the one who said 'here's what I know and don't' is (Chapter 7)."),
    ("Clarity is kind AND warm when done right:", "'this is serious, here's the plan, here's your part' respects people as adults with jobs to do."),
    ("The line to walk:", "honest without alarmist — calibrated language (Chapter 9's honest yellow) is a leadership instrument, not just a reporting one."),
], D, nxt())
notes(s, "The chapter's most quotable principle. The kindness reframe matters: students conflate clarity with coldness until shown the structure.")

s = flow_slide(prs, "The pressure protocol", [
    ("PAUSE", "Two breaths before any reply — the send button has no undo under stress (Chapter 7)"),
    ("FACTS", "What's actually known vs. assumed — write the two lists"),
    ("FRAME", "What does this mean for the people you're addressing — their stakes, not yours"),
    ("FORWARD", "The next concrete action, owned and timed — always end at the future"),
], D, nxt(), note_text="Four beats, thirty seconds, and it survives every crisis size — from a hot email to a plant shutdown.")
notes(s, "The protocol is deliberately small enough to run under real stress. It compresses Chapters 4, 7, and 9 into a field kit.")

s = bullets_slide(prs, "Composure is contagious (both directions)", [
    ("Teams synchronize to the leader's affect:", "panic propagates faster than facts; so does calm — you are broadcasting either way (Chapter 1)."),
    ("Calm is performable and legitimate:", "slower speech, complete sentences, written follow-ups — the FORM of composure produces its effect even while your pulse argues."),
    ("Visible process beats visible confidence:", "'here's how we'll figure this out' steadies people longer than 'it'll be okay' — process is checkable; confidence is a mood."),
    ("The composure budget is real:", "sleep, breaks, and the unpinged block (Chapter 5) aren't wellness perks in a crisis — they're the supply chain for the only calm the team gets."),
], D, nxt())
notes(s, "Performable calm is the actionable insight: students think composure is a trait; it's substantially a set of behaviors that can be executed under stress.")

s = section_slide(prs, "02", "Crisis leadership",
    "The first hour, the honest unknowns, and the cadence that starves rumor.", D, nxt())
notes(s, "Section 2: crisis communication from the leader's chair — extending Chapter 7's crisis section from statements to leadership.")

s = flow_slide(prs, "The first hour", [
    ("ACKNOWLEDGE", "To your own people first — silence from the leader is data, and it reads as either ignorance or concealment"),
    ("ASSIGN", "Who owns comms, who owns the fix, who owns the log — three hats, three heads where possible"),
    ("PROMISE THE CADENCE", "'Updates at 10, 2, and 5 whether anything changes or not'"),
    ("FEED THE GRAPEVINE FACTS", "The informal network runs at crisis speed (Chapter 1) — outrun it with official truth or it runs on invention"),
], D, nxt(), note_text="Nothing in the first hour requires knowing what happened. It requires knowing what LEADERSHIP happens while you find out.")
notes(s, "The insight students need: first-hour leadership is process communication, not answers. The three-hats assignment prevents the classic everyone-fixes-nobody-communicates failure.")

s = bullets_slide(prs, "Honest unknowns are a leadership technology", [
    ("'Here's what we don't know yet' — said plainly —", "is the sentence that separates credible leaders from spokespeople (Chapter 7's crisis rules, personalized)."),
    ("Unknowns stated create permission to report:", "when the leader admits uncertainty, the engineer with bad news stops polishing it (the MUM effect, disarmed at the top)."),
    ("Attach every unknown to a hunt:", "'we don't know the cause; the vendor call is at 2' — an unknown with an owner is a plan; an unknown alone is dread."),
    ("Never guess to fill the silence:", "the retracted guess costs more than a day of 'still confirming' — leaders' speculation gets treated as fact and quoted forever."),
], D, nxt())
notes(s, "The permission-to-report effect is the deep mechanism: leader-admitted uncertainty is what makes honest upward reporting safe. This links Chapters 1, 7, and 9 into the leadership frame.")

s = bullets_slide(prs, "After: the debrief that pays for the crisis", [
    ("Blameless in structure, specific in facts:", "'what did the SYSTEM allow?' — the incident-report discipline (Chapter 9) applied to the team's own performance."),
    ("The leader's errors go first:", "'I sat on the yellow flag for two days' — nothing else in the room unlocks honesty faster (and see: Carnegie, this deck)."),
    ("Harvest the communication failures too:", "who didn't know what, when? Most crisis damage is information routing, not the event itself."),
    ("Write the one-pager (Chapter 5's wiki rule):", "what happened, what we changed — or the next crisis reruns this one with new actors."),
], D, nxt())
notes(s, "The debrief closes the crisis loop and pivots the deck: the leader-goes-first move is the bridge into the influence sections — modeling costs as the price of candor.")

s = bullets_slide(prs, "Case: two plant managers, one recall", [
    ("Same defect, two facilities.", "Manager A held the floor meeting in hour two: what's known, what isn't, updates at shift change — then took questions until they stopped."),
    ("Manager B 'waited for corporate guidance.'", "By day two, B's floor had three rumor variants including layoffs; two good technicians quietly started job searches."),
    ("Six months later: identical recall outcomes,", "financially. A's plant: turnover flat. B's: down two techs and one manager — B, reassigned after the climate survey."),
    ("The lesson:", "the recall was never the risk. The silence was — the event cost money; the communication decided everything else."),
], D, nxt())
notes(s, "The controlled comparison makes the invisible cost visible. Note A's move is entirely Chapter 7 + this deck's first hour — nothing requires genius, only protocol.")

s = section_slide(prs, "03", "Influence without authority",
    "The Carnegie foundation: interest, appreciation, and their eager want.", D, nxt())
notes(s, "Section 3: the influence core, in the tradition of Dale Carnegie (1936) — attributed throughout, translated to modern channels.")

s = bullets_slide(prs, "The premise: you can't order anyone to care", [
    ("Most careers run on influence, not authority:", "peers, clients, other departments, your own boss — nobody in that list takes orders from you (Chapter 8's timesheet case)."),
    ("Carnegie's century-old observation holds:", "people are moved by those who demonstrably understand and serve their interests — not by those who win arguments at them."),
    ("It's the you-view (Chapter 2), scaled to relationships:", "every principle in this section is audience analysis practiced as a way of treating people, not just drafting messages."),
    ("The sincerity load is real:", "every technique here fails when faked — these are practices for becoming interested, not scripts for seeming it (Chapter 8's truth test)."),
], D, nxt())
notes(s, "Framing Carnegie as pre-discovered audience analysis unifies the course. The sincerity warning is Carnegie's own and must lead — this section reads as manipulation without it.")

s = icon_rows_slide(prs, "The Carnegie core, translated", [
    ("🚫", "Don't criticize, condemn, or complain", "Criticism triggers defense, not change (Chapter 7's psychology) — diagnose systems, correct behavior, skip the character verdicts."),
    ("💎", "Give honest, sincere appreciation", "The five-S goodwill note (Chapter 6) IS this principle with a stamp — specific, true, and wanted more than almost anything."),
    ("🎯", "Arouse an eager want", "Frame every ask in THEIR interests — Chapter 8's entire persuasion engine, stated in 1936."),
    ("😊", "Become genuinely interested in people", "Six weeks of real interest in others outperforms two years of trying to be interesting — in networking (Chapter 13), sales, and teams."),
], D, nxt(), kicker="Attributed to Dale Carnegie, How to Win Friends and Influence People (1936) — restated for the inbox era.")
notes(s, "The four foundations, each cross-referenced to where the course already taught it. The pattern students should see: Carnegie keeps being rediscovered by every chapter.")

s = bullets_slide(prs, "Names, listening, and their interests — the daily trio", [
    ("A person's name is still the sweetest sound:", "spell it right (Chapter 4's verification!), say it in greeting, use it in the thank-you — the smallest deposit that always lands."),
    ("Be the listener (Chapter 1, weaponized for good):", "the colleague who paraphrases, asks the second question, and remembers the answer next week becomes the most trusted person on the team by doing almost nothing else."),
    ("Talk in terms of their interests:", "open with THEIR project, THEIR deadline, THEIR win — the conversational you-view. Watch meetings tilt toward whoever does this."),
    ("The modern channels count double:", "remembered details in a follow-up email prove listening in writing — permanent, forwardable evidence that you were present."),
], D, nxt())
notes(s, "The three daily practices, sized for immediate use. The written-evidence point modernizes Carnegie: digital channels make genuine interest visible and durable.")

s = bullets_slide(prs, "Make them feel important — because they are", [
    ("The deepest human want, per Carnegie:", "to feel important and appreciated — and the workplace runs a permanent deficit of it."),
    ("The honest version is observational:", "'your triage call saved the launch' (Chapter 6's specificity) — importance demonstrated with evidence, not flattery inflated past it."),
    ("Distribute it downward and sideways especially:", "praising up is suspect; praising down and across is leadership (Chapter 6's credit-routing)."),
    ("Flattery fails on contact:", "people detect the difference between being SEEN and being buttered — the technique is attention, and attention can't be faked at length."),
], D, nxt())
notes(s, "Closes the foundation section. The seen-vs-buttered distinction is the whole ethics of the principle in one line.")

s = section_slide(prs, "04", "Winning people to your thinking",
    "Arguments, errors, yeses, and whose idea it gets to be.", D, nxt())
notes(s, "Section 4: Carnegie's persuasion set, mapped onto the course's influence chapters.")

s = bullets_slide(prs, "You can't win an argument", [
    ("Carnegie's rule: the only way to win one is to avoid it —", "'victory' leaves the loser convinced against their will and voting against you at the next meeting."),
    ("The workplace version:", "being right in the thread while the relationship dies is a loss wearing a trophy (Chapter 7's flame-war case)."),
    ("Replace the duel with the question:", "'walk me through how you got there?' — half the time they find their own gap; the other half, YOU find yours."),
    ("Save the stand for what matters:", "the professional who argues rarely is devastating when they finally do — argument frequency is a currency; spend it like one (Chapter 3's emphasis rule, socially)."),
], D, nxt())
notes(s, "The scarcity-of-stands point converts 'avoid arguments' from doormat advice into influence strategy.")

s = bullets_slide(prs, "'You're wrong' — the sentence that never works", [
    ("Direct contradiction locks the defense (Chapter 7):", "no one has ever replied 'good point, I'll abandon my position' to 'you're wrong' — the sentence produces doubling-down as a reflex."),
    ("The Carnegie alternative:", "'I may be wrong — I often am. Let's look at the data together.' Humility costs nothing and opens everything."),
    ("Correct with questions and evidence:", "'how does that square with the March numbers?' lets the facts do the confronting while you stay the colleague."),
    ("When you must contradict on the record:", "contradict the CLAIM, cite the source, skip the victory lap — 'the export shows 4%, not 14%' needs no editorial (Chapter 9)."),
], D, nxt())
notes(s, "The 'I may be wrong' opener is Carnegie verbatim and still the best de-escalating preface in professional life. The on-the-record exception keeps this honest — some corrections must land publicly.")

s = bullets_slide(prs, "Admit your errors fast and emphatically", [
    ("Beat the accusation to the punch:", "'before anyone checks — the Q2 figure was mine and it was wrong' converts a prosecution into a footnote (Chapter 7's apology anatomy)."),
    ("Self-criticism disarms completely:", "there's nothing left to argue when you've said it harder than they would have — and said the fix in the same breath."),
    ("It buys your praise its value:", "the leader who owns errors is the only one whose 'well done' means anything (this deck's debrief slide, personal edition)."),
    ("The career math (Chapter 7's MUM research):", "trust is staked on how you handle being wrong, because everyone already knows you sometimes are."),
], D, nxt())
notes(s, "Fast-emphatic error admission is where Carnegie, the MUM effect, and apology anatomy all converge — three chapters, one behavior.")

s = bullets_slide(prs, "Begin friendly, get to yes early, let them talk", [
    ("The friendly opening is load-bearing:", "a drop of honey before the business (Carnegie's phrase) is the buffer (Chapter 7) applied to every hard conversation, not just bad news."),
    ("Engineer the early yes:", "open on what you agree about — 'we both need this shipped by Q4' — and the psychology of consistency (Chapter 8) starts working FOR the conversation."),
    ("Let them talk themselves out:", "uninterrupted airing IS the concession most people actually want — and their full case tells you exactly which objection is real (Chapter 8's inventory, for free)."),
    ("Then respond to what was said,", "not what you rehearsed — the listening chapter (1), cashed in at its highest-value moment."),
], D, nxt())
notes(s, "Three tactical principles bundled: friendly start, yes-momentum, full airing. Each maps to machinery the course already built.")

s = bullets_slide(prs, "Let the idea be theirs", [
    ("People fight FOR what they authored", "and AGAINST what they're handed — ownership is the strongest adoption force there is (Chapter 8's pilot case: the skeptic presenting the results)."),
    ("Plant with questions:", "'what would fix the Friday bottleneck?' beats 'here's my fix for your bottleneck' even when they land the same place."),
    ("Share credit structurally:", "'per Dana's point…' (Chapter 8's pre-wiring) — visible fingerprints convert objectors into co-owners."),
    ("Check the ego math:", "if the idea shipping matters more than the idea being yours — and it does — then authorship is a currency you can spend to buy adoption."),
], D, nxt())
notes(s, "The ego-math close is the honest version of the principle: it's not selflessness, it's exchanging credit for outcomes — a trade professionals should make consciously.")

s = bullets_slide(prs, "See it their way; appeal to the nobler motive", [
    ("Try honestly to see their view first (Carnegie):", "not as a tactic — as the diagnosis. Resistance almost always makes sense from where the resister stands (Chapter 8's status-quo slide)."),
    ("Sympathize with the position out loud:", "'in your seat, I'd worry about exactly this' — costs nothing, and it's usually true."),
    ("Appeal to who they want to be:", "'you've always been the one who catches these' invokes the professional identity — people strain to live up to their own reputation (next section's engine)."),
    ("The nobler motive is usually REAL:", "most people genuinely want to be fair, thorough, good at their work — addressing that self-image isn't flattery; it's accurate targeting."),
], D, nxt())
notes(s, "The nobler-motive principle previews the reputation effect that anchors Section 5. The 'resistance makes sense' framing is the empathy-as-diagnosis move from Chapter 8.")

s = section_slide(prs, "05", "Leading people through change",
    "Correction, face, and the reputation to live up to.", D, nxt())
notes(s, "Section 5: Carnegie's leadership set — correction without crushing.")

s = flow_slide(prs, "Correcting without crushing", [
    ("HONEST PRAISE FIRST", "Real and specific — the foundation, not the softener (fake bread is the sandwich problem, Chapter 7)"),
    ("THE BEHAVIOR, INDIRECTLY WHERE IT WORKS", "'I've made this exact mistake' beats the pointed finger"),
    ("QUESTIONS, NOT ORDERS", "'What would keep this from recurring?' — authorship again"),
    ("SAVE FACE, ALWAYS", "Private correction, public dignity — the person must survive the fix (Chapter 7's SBI)"),
    ("PRAISE THE PROGRESS", "Every improvement noticed aloud — behavior grows toward the light"),
], D, nxt(), note_text="Carnegie's leadership principles, run as a sequence. The goal is a changed behavior AND an intact contributor — either alone is failure.")
notes(s, "The correction sequence integrates Carnegie with SBI and the feedback rules. 'Either alone is failure' is the standard.")

s = bullets_slide(prs, "Give them a reputation to live up to", [
    ("Name the identity you want to grow:", "'you're the most careful reviewer on this team' — and watch the person defend that reputation with their behavior."),
    ("It must be TRUE at least in trajectory:", "reputation-granting is watering a real seedling, not painting one — the fake version reads as sarcasm within a week."),
    ("It's the strongest correction tool for good performers:", "'this slipped, which surprised me — your work is usually the standard' corrects harder than any reprimand, and hurts better."),
    ("Teams work the same way:", "'this group doesn't ship unverified numbers' becomes true BECAUSE it's said — spoken standards become identity, and identity self-enforces (Chapter 11's ground rules, internalized)."),
], D, nxt())
notes(s, "The reputation effect is Carnegie's most powerful and least-known principle — and the team version is how communication culture actually gets built.")

s = bullets_slide(prs, "Case: the turnaround supervisor", [
    ("Inherited: the plant's worst line —", "quality misses, two grievances pending, a crew described to her as 'unmanageable.'"),
    ("Month one she mostly asked and listened:", "every operator, 'what would you fix first?' — then implemented two of their answers VISIBLY, with credit posted on the board."),
    ("Corrections went private and question-shaped;", "wins went public and name-attached. She told the crew they were 'the line that catches what the system misses' — before it was true."),
    ("Month seven: best quality record in the plant.", "Same crew. Her summary: 'I didn't change the people. I changed what got noticed.' That's this chapter, in one sentence."),
], D, nxt())
notes(s, "Composite turnaround built entirely from the deck's principles: listening, authorship, face, credit-routing, and reputation-granting. Nothing in it requires charisma.")

s = takeaways_slide(prs, [
    "Under pressure, run the protocol: pause, facts, frame, forward — clarity over reassurance, always.",
    "First hour of crisis: acknowledge, assign the three hats, promise the cadence, feed the grapevine facts.",
    "Honest unknowns, attached to hunts, are what make truth-telling safe for everyone below you.",
    "Influence runs on genuine interest, honest appreciation, and their eager want — Carnegie, 1936, still undefeated.",
    "Don't argue; question. Never 'you're wrong'; admit your own errors fast. Let the idea be theirs.",
    "Correct in private with questions, save face, praise progress — and grant reputations worth living up to.",
], D, nxt(), site_note="Practice now: course site → Chapter 16 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Deal with people knowing they are creatures of emotion more than logic — moved by pride, fed by appreciation, and loyal to whoever truly listens.",
    "after Dale Carnegie, How to Win Friends and Influence People (1936)", D, nxt())
notes(s, "Paraphrase attributed to Carnegie's central theme — flagged as 'after' rather than verbatim quotation.")

s = discussion_slide(prs, "Discussion questions", [
    "Recall a leader you'd follow anywhere. Which of this chapter's behaviors did they run — and which did they never need?",
    "Draft the first-hour communication for a crisis in your field: the acknowledge, the three hats, the cadence.",
    "Carnegie says you can't win an argument. Find the exception: when MUST a professional argue on the record, and how?",
    "Where's the line between granting a reputation and manipulating with one? Build the test (hint: Chapter 8's visibility test).",
    "Rewrite a criticism you've received — as the correction sequence would have delivered it. What changes in your own likely response?",
], D, nxt())
notes(s, "Async-ready. Question five is the empathy-generator: students design the feedback they wish they'd gotten.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 16 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 16 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Do:", "Run one Carnegie practice for a full week — names, or the second question, or credit-routing — and log what changes."),
    ("Read:", "How to Win Friends and Influence People (1936) — a weekend read that outperforms most management shelves."),
    ("Coming next:", "Chapter 17 — strategy for communicators: where the value comes from, and how to write proposals that speak it."),
], D, nxt())
notes(s, "Delivery-neutral closing. The book recommendation is genuine and the instructor's own.")

out = os.path.join(os.path.dirname(__file__), "..", "ch16-leadership-under-pressure-influence.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
