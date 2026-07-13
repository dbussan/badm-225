# Chapter 11 — Professionalism, Teamwork, and Meetings (30 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 11"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Professionalism, Teamwork, and Meetings",
    "Etiquette that compounds · teams that argue well · meetings people don't dread", D)
notes(s, "Chapter 11: the behavioral layer — how the writing skills of Units 1–4 get a reputation attached to them.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Practice", "the professionalism fundamentals: reliability, responsiveness, composure, discretion — on purpose, daily."),
    ("Contribute", "to teams that disagree productively: ground rules, roles, and conflict about ideas instead of people."),
    ("Run", "meetings with outcomes, owners, and time boxes — and be the most valuable attendee in the ones you don't run."),
    ("Handle", "the hard moments: credit disputes, freeloaders, hidden agendas, and the colleague who talks over everyone."),
    ("Build", "the trust account that makes every future message cheaper to send."),
], D, nxt())
notes(s, "Objectives map to the Chapter 11 practice bank.")

s = section_slide(prs, "01", "Professionalism",
    "Predictability plus respect — demonstrated in small repeated behaviors.", D, nxt())
notes(s, "Section 1: professionalism defined behaviorally, not sartorially.")

s = icon_rows_slide(prs, "The five daily fundamentals", [
    ("⏱", "Reliability", "Deadlines met, promises kept, meetings attended — trust is built on boring consistency (Chapter 1)."),
    ("↩", "Responsiveness", "Acknowledge within a business day, even when the full answer comes later — silence reads as avoidance."),
    ("✉", "Polish", "Proofread everything; the typo tax is charged against your competence, not your typing."),
    ("🧊", "Composure", "Never send angry; never match the temperature of a hostile thread (Chapter 7's de-escalation)."),
    ("🤐", "Discretion", "What colleagues tell you in confidence stays there. Gossip is a loan against your own trustworthiness."),
], D, nxt())
notes(s, "The five from Chapter 1, now as the operating system for teamwork. Each is checkable behavior, not personality.")

s = bullets_slide(prs, "Etiquette is bandwidth management", [
    ("Courtesy is not decoration — it's protocol.", "'Please,' names spelled right, and warm openings keep the channel clear for the actual content."),
    ("Interruptions are expensive twice:", "they cost the speaker's thought and the room's attention — the note-and-wait habit beats the blurt."),
    ("Punctuality is respect made visible.", "Arriving late to a ten-person meeting spends ten people's minutes without asking."),
    ("Devices signal priorities.", "The open laptop says 'this meeting is my second screen' — and everyone reads it fluently."),
], D, nxt())
notes(s, "Etiquette reframed as engineering: every courtesy exists to keep a shared channel usable. This framing lands better with skeptical students than 'manners matter.'")

s = bullets_slide(prs, "The trust account", [
    ("Every interaction deposits or withdraws.", "Kept promises, early warnings, and passed credit deposit; surprises, spin, and hoarded credit withdraw."),
    ("Deposits are small; withdrawals are large.", "One 'they knew and didn't tell us' can spend a year of reliability."),
    ("Trust makes communication cheap.", "High-trust colleagues can send two-line messages that low-trust colleagues would need two pages to defend."),
    ("You can't withdraw from an empty account —", "which is why professionalism has to run BEFORE the crisis that needs it (Chapter 7's slipping-launch case)."),
], D, nxt())
notes(s, "The account metaphor organizes the chapter: professionalism is deposit behavior, and the payoff is denominated in communication cost.")

s = section_slide(prs, "02", "Teamwork",
    "Teams that argue well beat teams that agree fast.", D, nxt())
notes(s, "Section 2: team communication — ground rules, conflict, and the failure modes.")

s = bullets_slide(prs, "Ground rules: agree on process before stakes rise", [
    ("Decide how you'll decide.", "Consensus, majority, or owner-decides-after-input — pick BEFORE the contested decision arrives."),
    ("Set the document rules:", "one living copy, drafts circulated 24 hours before meetings, comments resolved by owners (Chapter 5)."),
    ("Name the communication norms:", "which channel for what, response-time expectations, and when to escalate from chat to a call."),
    ("Write them down.", "Unwritten norms are just the founders' habits — invisible to the person who joins in week six."),
], D, nxt())
notes(s, "Ground rules feel bureaucratic until the first real disagreement, when they're the difference between conflict about the idea and conflict about the process.")

s = two_col_slide(prs, "Productive conflict vs. personal conflict",
    "About the IDEA (grow this)", [
        "'The timeline assumes zero vendor delay — that's the weak joint'",
        "Specific, checkable, aimed at the work",
        "Ends with a better decision and intact colleagues",
        ("Norm:", "hard on the problem, soft on the person"),
    ],
    "About the PERSON (stop this)", [
        "'You always lowball timelines'",
        "General, unfalsifiable, aimed at character",
        "Ends with a winner, a loser, and a quieter team",
        ("Repair:", "restate as behavior + impact (Chapter 7's SBI)"),
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "Teams that never conflict aren't harmonious — they're silent, and silence costs whatever the unspoken objection knew. The skill is keeping conflict in the left column.")

s = bullets_slide(prs, "Disagree, then commit — out loud", [
    ("Argue fully before the decision:", "the meeting's job is to stress-test the options while changing course is still cheap."),
    ("Once decided, the decision is everyone's.", "'I voted against this but here's my full effort' is the most professional sentence in teamwork."),
    ("Relitigating in the hallway is the defection:", "it keeps the argument alive after the fair fight ended — and everyone learns the meeting wasn't the real venue."),
    ("If new facts arrive, reopen formally:", "'the vendor slipped — does that change our call?' goes to the group, not the grapevine."),
], D, nxt())
notes(s, "Disagree-and-commit is the mechanism that lets teams argue hard without fracturing: full voice before, full support after, formal reopening on new evidence.")

s = icon_rows_slide(prs, "The four team failure modes (and their fixes)", [
    ("🛋", "The freeloader", "Uneven effort, visible to all. Fix: tasks with names and dates in writing — vagueness is the freeloader's habitat."),
    ("🏆", "The credit taker", "'My analysis' for the team's work. Fix: pass credit publicly and immediately; the pattern exposes itself (Chapter 6)."),
    ("🕶", "The hidden agenda", "Decisions maneuvered outside the agenda. Fix: name the topic and put it ON the agenda — sunlight is the protocol."),
    ("📢", "The dominator", "Talks over everyone; the quiet expertise never surfaces. Fix: structured turns — 'let's hear from everyone on this one' — run by whoever holds the floor."),
], D, nxt())
notes(s, "Each failure mode survives on ambiguity; each fix is a form of writing things down or making things public. That's the chapter's quiet thesis: documentation is team hygiene.")

s = bullets_slide(prs, "Delivering your part: the teammate contract", [
    ("Your deadline is someone's input.", "A slip you announce Tuesday is a plan; a slip discovered Friday is a betrayal (Chapter 7's early-and-upward)."),
    ("Report status without being asked.", "The three-line update (on track / slipping / need) is a gift to whoever depends on you."),
    ("Ask early, not heroically.", "Struggling silently for a week to 'not bother anyone' bothers everyone, later and worse."),
    ("Review others' work like you want yours reviewed:", "triaged, specific, kind — Chapter 4's rules are team rules."),
], D, nxt())
notes(s, "Individual reliability, expressed as its effect on teammates. The 'ask early' point pushes against the student instinct that asking for help is weakness.")

s = section_slide(prs, "03", "Meetings",
    "The most expensive communication channel — spend it like money.", D, nxt())
notes(s, "Section 3: meetings, extending Chapter 5's calendar-communication rules into running the room.")

s = stat_slide(prs, "The meeting math nobody runs", "8×1",
    "Eight people for one hour is a working day of organizational time — priced accordingly, most status meetings would never be scheduled.",
    [("The test from Chapter 5:", "one-way information flow with no decision = a message wearing a meeting costume."),
     ("Meetings earn their cost on exactly three jobs:", "decisions, conflict, and connection — things that need live humans."),
     ("Everything else", "is a written update that arrived with a room attached."),
    ], D, nxt())
notes(s, "The cost frame from Chapter 5's case, now as the organizing principle. Decisions, conflict, connection — if the meeting does none of these, it's mail.")

s = flow_slide(prs, "Anatomy of a meeting that works", [
    ("PURPOSE", "The outcome, named in the invite: 'decide Q3 vendor'"),
    ("AGENDA", "Items as outcomes, each with owner + time box"),
    ("THE ROOM", "Only the needed; notes to the curious"),
    ("THE RECORD", "Decisions + owners + dates, sent within the hour"),
    ("FOLLOW-THROUGH", "Actions tracked to done — or the meeting was theater"),
], D, nxt(), note_text="Chapter 5 built the invite, agenda, and record. This chapter adds the live skill: running the room in between.")
notes(s, "The five-part anatomy; the middle part (facilitation) is the new material and gets the next slides.")

s = bullets_slide(prs, "Running the room", [
    ("Start on time, with the purpose.", "'We're here to pick the vendor — by 2:25' resets everyone's clock and dignity."),
    ("Hold the agenda visibly.", "'Good point — parking-lotting it so we finish item two' protects the meeting from its most interesting tangent."),
    ("Draw out the quiet expertise:", "'Dana, you ran the pilot — what did we miss?' The best data in the room often needs an invitation."),
    ("Read back every decision before moving on:", "'recording: we renew, Maya drafts by the 12th' — contested wording surfaces NOW, not in the minutes war later."),
    ("End early when you're done.", "Nothing builds meeting credibility like giving back eleven minutes."),
], D, nxt())
notes(s, "Facilitation as five teachable behaviors. The read-back habit is the highest-value: it converts soft agreement into an actual decision while everyone's still present.")

s = bullets_slide(prs, "Being the best attendee in someone else's meeting", [
    ("Arrive prepared:", "pre-reads read, your data ready, your position thought through — preparation is visible within ninety seconds."),
    ("Speak to move the item forward:", "add the missing fact, name the decision, or concede — repetition and speeches move nothing."),
    ("Disagree in the room, not after it", "(the disagree-and-commit rule, live)."),
    ("Volunteer for actions you'll actually do —", "and then do them. The follow-through list is where meeting reputations are made."),
], D, nxt())
notes(s, "Most students will attend fifty meetings for every one they run — attendee craft matters more than facilitation for their first years.")

s = two_col_slide(prs, "Remote and hybrid meetings: the added rules",
    "Remote basics", [
        "Camera on for discussion; async for broadcast",
        "Mute discipline; one conversation at a time",
        "Chat is the parallel channel — someone must watch it",
        "Being visibly present is the new eye contact (Chapter 1)",
    ],
    "Hybrid hazards", [
        "The room forgets the screen — assign a remote advocate",
        "Decisions made after the call 'ended' disenfranchise the remote half",
        "Whiteboards need a camera or a shared doc equivalent",
        ("Rule:", "if one person is remote, run it as a remote meeting"),
    ], D, nxt())
notes(s, "The one-remote-all-remote rule is the industry consensus fix for hybrid's two-tier problem. The remote-advocate role is assignable and works.")

s = bullets_slide(prs, "Case: the team that wrote its rules after the blowup", [
    ("The project had no ground rules —", "just five competent people, two of whom stopped speaking after a credit dispute in month two."),
    ("The repair meeting made one deliverable:", "a one-page team agreement — decision method, document rules, credit norms ('the doc lists every contributor'), and a conflict protocol."),
    ("The skeptics called it kindergarten.", "Then the next dispute — same people, same stakes — resolved in one meeting, by the protocol, without a casualty."),
    ("The lesson:", "rules written during peace are cheap; rules invented during war are impossible. Write them while nobody needs them."),
], D, nxt())
notes(s, "The case argues for ground rules empirically. 'The doc lists every contributor' is a one-line credit norm that prevents the most common team wound.")

s = bullets_slide(prs, "Case: the meeting audit", [
    ("A new director inherited eleven standing meetings.", "She ran the three-job test on each: decision, conflict, or connection?"),
    ("Four became written updates.", "Two merged. One shrank from 60 minutes to 25. The weekly all-hands kept its hour — connection is a real job."),
    ("Freed: roughly 40 person-hours a week.", "Complaints: zero. The information all still flowed — in Chapter 5's channels, at reading speed."),
    ("The lesson:", "nobody defends a dead meeting once someone prices it. Be the person who runs the audit, politely."),
], D, nxt())
notes(s, "Note the all-hands survives — the point isn't 'meetings bad,' it's the three-job test applied honestly. Connection meetings are legitimate and should be run AS connection.")

s = section_slide(prs, "04", "The professional, in person",
    "Phones, meals, introductions, shared space — the analog skills that still decide impressions.", D, nxt())
notes(s, "Section 4: in-person professionalism. Digital natives often have the least practice exactly here.")

s = bullets_slide(prs, "The phone call: still a professional instrument", [
    ("Answer with your name:", "'Quality lab, this is Derek' — the caller instantly knows they've landed, and with whom."),
    ("Calls beat threads at richness (Chapter 1):", "two hot replies or three rounds of confusion means pick up the phone — and then confirm in writing."),
    ("Voicemail in fifteen seconds:", "name, number SLOWLY, one-line reason, best callback window. Repeat the number at the end."),
    ("Schedule calls like meetings:", "'Can I call at 2:00 for ten minutes about the audit?' respects the other calendar — cold calls interrupt by design."),
], D, nxt())
notes(s, "Phone anxiety is real and generational; framing the skills as checklists lowers the barrier. The fifteen-second voicemail spec is immediately usable.")

s = bullets_slide(prs, "Introductions: the ninety-second skill", [
    ("Say names clearly, in both directions:", "'Dana, this is Marcus from facilities — Marcus, Dana runs the audit team.' Context attached to each name."),
    ("Honor the order convention lightly:", "introduce others TO the senior or client party first — but a warm, clear introduction beats a perfectly ordered mumble."),
    ("Forgot the name? Say so once, fast:", "'I'm blanking on your name and I'm embarrassed about it' costs two seconds; a whole conversation of avoidance costs the relationship."),
    ("Introduce yourself when nobody does:", "hand, name, role, one hook — 'I'm the one who sends the Friday status emails' — and you've rescued the whole circle."),
], D, nxt())
notes(s, "Introductions are the most rehearsable social skill in the chapter — students can literally practice the two-way pattern aloud.")

s = bullets_slide(prs, "The business meal and the work social event", [
    ("The meal IS the meeting:", "order mid-menu, mirror the host's pace, and let the other party's food arrive before your agenda does."),
    ("Alcohol: the ceiling is one, the floor is zero,", "and nobody was ever penalized for the floor."),
    ("The social event is still work:", "the colleague you vent to at the party is the coworker who heard you vent — Chapter 5's permanence, without the screenshots."),
    ("Work the room like a professional:", "arrive, greet the host, meet two new people properly (see: introductions), and leave on time — presence recorded, dignity intact."),
], D, nxt())
notes(s, "The vent warning ties to the screenshot case from Chapter 5 — same principle, analog channel. The one-drink ceiling framing gets remembered.")

s = bullets_slide(prs, "Shared space etiquette: open plans and common rooms", [
    ("Sound travels; grievances travel further.", "The open-plan phone voice and the hallway complaint both have audiences you didn't invite."),
    ("Headphones are a door.", "Respect them as one — and take yours off enough to remain reachable (availability signaling, Chapter 5)."),
    ("Book the room you need, release the room you don't,", "and end on time — the next meeting's start is your hard stop."),
    ("The kitchen and the printer are reputation venues:", "the person who leaves the jam, the mess, or the empty pot is more famous than they think."),
], D, nxt())
notes(s, "Light in tone, real in consequence — shared-space behavior is the most visible professionalism there is, because everyone sees it daily.")

s = bullets_slide(prs, "The first ninety days: reputation onboarding", [
    ("Default to over-professionalism early:", "punctual, prepared, camera on, names learned — you can relax a formality later; you can't easily un-relax one."),
    ("Learn the norms before bending them:", "every team has channel habits, meeting culture, and unwritten rules — watch for two weeks before optimizing anything."),
    ("Deliver something small, fast, and clean:", "the first finished task — polished and on time — sets the prior every later judgment updates from."),
    ("Find the person who knows how things work", "and buy the coffee. Every org has a Dana; the map she carries isn't written anywhere."),
], D, nxt())
notes(s, "Closes the section with the situation every student faces next: arriving new. The 'watch before optimizing' rule prevents the classic new-hire wound.")

s = takeaways_slide(prs, [
    "Professionalism is five daily behaviors: reliable, responsive, polished, composed, discreet.",
    "Trust is an account: deposit small and constantly; withdrawals are always larger.",
    "Write ground rules during peace: how you'll decide, document, communicate, and fight.",
    "Keep conflict about ideas — specific and checkable — then disagree and commit, out loud.",
    "Meetings earn their cost on decisions, conflict, and connection; everything else is mail.",
    "Read decisions back in the room; send the two-line record within the hour; track actions to done.",
], D, nxt(), site_note="Practice now: course site → Chapter 11 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Your teammates will forget most of what you wrote. They will remember, with perfect accuracy, whether you did what you said you would.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Which of the five fundamentals is your weakest — and what's the smallest visible behavior that would move it this week?",
    "Describe a team conflict you've seen: was it about the idea or the person? What would have kept it in the left column?",
    "Run the three-job test on a standing meeting you attend. What's your redesign — and how would you pitch it (Chapter 8)?",
    "Which team failure mode have you actually been? What ambiguity made it possible?",
    "Draft the five-line team agreement you'd want for your next group project.",
], D, nxt())
notes(s, "Async-ready. Question four requires honesty and gets the best discussions.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 11 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 11 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Do:", "Write the team agreement for your current group work — decision method, document rules, credit norm, conflict protocol."),
    ("Audit:", "Price one recurring meeting you attend (people × hours). Which of the three jobs does it do?"),
    ("Coming next:", "Chapter 12 — business presentations: the room, the slides, and the nerves."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch11-professionalism-teamwork-meetings.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
