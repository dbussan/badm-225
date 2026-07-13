# Chapter 5 — Short Workplace Messages and Digital Media (41 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 5"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Short Workplace Messages and Digital Media",
    "Email that works · chat that coordinates · the digital professionalism that follows your name", D)
notes(s, "Unit 3 opens: the foundation chapters meet the inbox.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Build", "emails with six working parts — subject as the job, point in sentence one, dated ask at the end."),
    ("Choose", "among email, chat, and text by record, speed, and stakes — and know each channel's ceiling."),
    ("Practice", "thread hygiene: reply-all discipline, To/CC clarity, new-topic-new-thread."),
    ("Write", "as if legal reads it — because on workplace systems, it can."),
    ("Curate", "the digital layer that interviews before you do."),
], D, nxt())
notes(s, "Objectives map to the Chapter 5 bank and the email-signature assignment.")

s = stat_slide(prs, "Everyone you write to is drowning", "28%",
    "of the interaction worker's week was already spent reading and answering email a decade ago (McKinsey Global Institute, 2012) — volume has only grown since.",
    [("Hundreds of billions of emails move daily", "(Radicati Group, 2024)."),
     ("The professional consequence is arithmetic:", "the writer who costs the reader the least time wins the reputation."),
     ("Short messages aren't a new skill —", "they are Chapters 1–4, compressed."),
    ], D, nxt())
notes(s, "The economics of the inbox.")

s = section_slide(prs, "01", "Email",
    "Still the workplace's official language — and the channel of record.", D, nxt())
notes(s, "Section 1.")

s = icon_rows_slide(prs, "Anatomy of a working email", [
    ("①", "Subject = the message's job", "“Approve Q3 budget rev by Fri 7/10” — opens it today, finds it next quarter."),
    ("②", "Sentence one = the point", "The ask, the news, the takeaway. Here. (Chapter 3's frontloading.)"),
    ("③", "Body = one screen", "Lists and short paragraphs; scrolling means it's competing with reports."),
    ("④", "Call to action = act + date", "Standing alone at the end, where scanning terminates."),
    ("⑤", "Signature = your letterhead", "Name, title, organization, phone — this unit's signature assignment."),
], D, nxt())
notes(s, "Every part executes a foundation chapter.")

s = two_col_slide(prs, "Subject lines: four formulas",
    "The formulas", [
        ("ACTION:", "verb + object + date — “Approve vendor list by Thu”"),
        ("INFO:", "topic + takeaway — “Migration done; all normal”"),
        ("QUESTION:", "the actual question — “OK to move standup to 9:30?”"),
        ("RESCUE:", "new topic = new subject line"),
    ],
    "Why they matter", [
        "A subject line has three careers: opened today, found next quarter, telling skimmers what's owed",
        "“Quick question” has no careers at all",
        ("Habit:", "write the subject LAST — after the message tells you what it's about"),
    ], D, nxt())
notes(s, "Five front-loaded words decide everything.")

s = icon_rows_slide(prs, "Thread hygiene", [
    ("↩", "Reply vs. reply-all", "Reply-all only when every name needs every word. The reply-all “thanks!” taxes forty attention budgets."),
    ("🧵", "New topic = new thread", "Don't bury the hiring decision in “RE: RE: FW: lunch” — search will never find it."),
    ("➤", "To = act · CC = know", "Blurring them is why nobody is sure who owns the task."),
    ("🚪", "BCC = the exit ramp", "“Moving Dana to BCC with thanks” — freed, politely and visibly."),
], D, nxt())
notes(s, "Pollution control for a shared ecosystem.")

s = section_slide(prs, "02", "Chat, text, and boundaries",
    "The hallway, digitized — and its ceiling.", D, nxt())
notes(s, "Section 2.")

s = bullets_slide(prs, "Chat's rules of engagement", [
    ("Front-load even here.", "“Quick one: OK to move the demo to 2:00? Need to know by 11” beats the naked “hey” that takes a hostage."),
    ("@mention like a hand on a shoulder,", "not an air horn."),
    ("Know the ceiling:", "the moment chat produces a decision with consequences, it graduates to email — “confirming what we agreed.”"),
    ("Texts are invitation-only:", "time-critical logistics with people who shared their number; nothing confidential, complex, or contractual."),
], D, nxt())
notes(s, "Chat coordinates; email records.")

s = icon_rows_slide(prs, "Response-time norms", [
    ("🌐", "External / client email", "Acknowledge the same business day — even if the full answer comes Friday."),
    ("👔", "Manager's direct question", "Hours, not days. Silence reads as avoidance."),
    ("💬", "Chat @mention", "Within the working session."),
    ("📋", "CC / FYI traffic", "No reply owed — that's what CC means."),
    ("🌙", "After-hours anything", "Next business day. Schedule-send protects the norm for everyone — including future you."),
], D, nxt())
notes(s, "Predictability beats raw speed: the reputation is 'always closes the loop.'")

s = section_slide(prs, "03", "Permanence",
    "Write like legal reads it — because legal can.", D, nxt())
notes(s, "Section 3.")

s = bullets_slide(prs, "The permanence gradient", [
    ("Email and documents:", "archived, searchable, discoverable in disputes."),
    ("Chat platforms:", "logged and exportable — employer property, not private space."),
    ("“Disappearing” messages:", "screenshots never do."),
    ("The operating rule:", "the publicity test isn't hypothetical on digital channels — it's the literal condition. Type accordingly."),
], D, nxt())
notes(s, "Internal is not private.")

s = bullets_slide(prs, "Case: the reply-all storm", [
    ("1,400 names in the To line.", "One “please remove me” → six more → eleven people sending “STOP REPLYING ALL” — reply-all."),
    ("900 messages in an hour;", "IT locks the list; the sales director's all-caps meltdown becomes the company screenshot."),
    ("The technical fix was one line:", "mass mail goes BCC or through a no-reply tool — prevention beats etiquette."),
    ("The behavioral lesson:", "every “stop replying” author diagnosed the problem correctly and became it."),
], D, nxt())
notes(s, "Composure is most visible when everyone else loses it.")

s = bullets_slide(prs, "Case: the screenshot", [
    ("A private-channel vent about a colleague", "gets misforwarded to a group containing her manager. Apologies. Silence."),
    ("Three months later she's promoted —", "to lead the venter's team — and the old screenshot recirculates."),
    ("Where the risk lived:", "at the moment of TYPING. On logged platforms, you never control the copies."),
    ("The recovery:", "unhedged voice apology in hour one; a brief, forward-facing note in week one of the new org chart. Face the debt before it faces you."),
], D, nxt())
notes(s, "Typed frustration is a screenshot on layaway. Safe venting: voice, off platform, outside the org chart.")

s = section_slide(prs, "04", "Attention & presence",
    "The ping is engineered. Your defenses should be too.", D, nxt())
notes(s, "Section 4.")

s = bullets_slide(prs, "Attention management is inbox management", [
    ("As a sender:", "every message spends someone's focus. Batch the small stuff; make messages answerable without a follow-up."),
    ("As a receiver:", "process in blocks, not per ping. Triage: act (<2 min) → schedule → file → delete."),
    ("Protect one unpinged stretch daily.", "Continuous partial attention degrades even the conversations you stay in (Turkle, 2015)."),
    ("Attention is career capital.", "Spend it like money, because everyone else is spending yours."),
], D, nxt())
notes(s, "The receiver's side of the chapter.")

s = bullets_slide(prs, "Your digital layer interviews first", [
    ("Public posts:", "assume permanent and employer-visible — both are true."),
    ("Professional profiles:", "a standing portfolio. Competent photo, headline that says what you do, activity showing judgment."),
    ("Private channels:", "one screenshot from public — the gradient never sleeps."),
    ("The goal isn't blandness:", "it's that the person visible online and the person in the interview are colleagues, not strangers."),
], D, nxt())
notes(s, "Chapter 1's standing portfolio, operationalized.")

s = two_col_slide(prs, "Three makeovers you'll use this week",
    "Before", [
        "Chat: “hey” … “you there?” … “quick question”",
        "Email: four paragraphs; the schedule slip hiding in paragraph three",
        "Reply-all: “Thanks everyone!!” × 1,400 inboxes",
    ],
    "After", [
        "“Quick one: OK to move the demo to 2:00 so Priya can join? Confirm by 11.”",
        "“Sprint update — on track except one item. Slipping: data migration (3 days; fix due Wed). Need from you: nothing yet.”",
        "Reply (sender only): “Thanks, Dana — the turnaround saved us.” Narrower = more personal.",
    ], D, nxt())
notes(s, "Complete, frontloaded, correctly addressed.")

s = section_slide(prs, "05", "Memos and internal documents",
    "Email's older sibling still has a job — knowing which job is the skill.", D, nxt())
notes(s, "Section 5: the memo. Not nostalgia — a distinct tool for policy, record, and anything that must outlive an inbox.")

s = bullets_slide(prs, "When a memo still beats an email", [
    ("The content must outlive the inbox.", "Policies, procedures, and decisions of record get attached as memos — a document is filed; an email is buried."),
    ("The audience is 'everyone, indefinitely.'", "A memo posted to the intranet reaches the person hired next year; an email never will."),
    ("The formality is the message.", "A signed memo announcing a reorganization says 'this is official' in a way a chat ping cannot."),
    ("The practical pattern:", "a two-line email carries a one-page memo attachment: 'Attached is the updated travel policy, effective August 1. Summary below.'"),
], D, nxt())
notes(s, "The memo survived because email is a delivery channel, not an archive. Anything with a shelf life belongs in a document.")

s = icon_rows_slide(prs, "Memo anatomy — four lines, then business", [
    ("➤", "TO / FROM / DATE / SUBJECT", "The four-line header replaces salutation and signature — no 'Dear,' no 'Sincerely.'"),
    ("◎", "Opening = the point", "First sentence states the news or decision, exactly like a direct email (Chapter 3)."),
    ("▤", "Headings for anything past half a page", "Memos get skimmed on bulletin boards and intranets — design for the F-pattern."),
    ("✍", "Initials, not signatures", "Convention: the sender initials next to their name in the FROM line — the whole document is the signature."),
], D, nxt())
notes(s, "Format walk-through. The subject line rules from Section 1 apply verbatim — 'Parking Permit Renewal Due June 15,' not 'Parking.'")

s = bullets_slide(prs, "The status update that manages up", [
    ("The three-line skeleton:", "On track: [what's fine]. Slipping: [what's not + the fix + new date]. Need from you: [ask or 'nothing yet']."),
    ("Lead with the exception.", "If something is slipping, that's the news — never make a manager excavate for it (Chapter 1's upward filter)."),
    ("Same format every time.", "Predictable structure means your manager reads it in ten seconds — and notices instantly when something changes."),
    ("Silence is a report too.", "A skipped update is read as 'something is wrong and they're not saying' — usually correctly."),
], D, nxt())
notes(s, "The single highest-frequency 'manage up' document. The honest 'Slipping:' line builds more trust than a month of 'all good.'")

s = section_slide(prs, "06", "Meetings start in writing",
    "The invite, the agenda, and the two-line record afterward.", D, nxt())
notes(s, "Section 6: calendar communication. A meeting is three written artifacts wrapped around a conversation.")

s = bullets_slide(prs, "The meeting invite is a message — write it like one", [
    ("The title states the outcome.", "'Decide Q3 vendor' beats 'Sync' — attendees should know why they're there before they accept."),
    ("The body carries the agenda,", "the pre-read links, and what each person should bring. An empty invite is a blank check drawn on everyone's calendar."),
    ("Invite the necessary, inform the rest.", "Every optional attendee who comes anyway doubles the cost; send the notes to the curious instead."),
    ("Honest duration.", "Book the 25 minutes it needs, not the 60 the calendar defaults to — meetings expand to fill the container."),
], D, nxt())
notes(s, "The invite is a persuasive message: it asks people to spend their scarcest resource. The cost math slide later makes this concrete.")

s = icon_rows_slide(prs, "Agenda anatomy: items that can actually be run", [
    ("◎", "Each item is an outcome", "'Choose between vendors A and B' — not the topic-shaped fog of 'Vendors.'"),
    ("👤", "Each item has an owner", "The person who presents, frames the decision, and captures the result."),
    ("⏱", "Each item has a time box", "Ten minutes on item one is a promise to items two and three."),
    ("📎", "Pre-reads attached, expectations stated", "'Read the one-pager before we meet; we will not walk through it live.'"),
], D, nxt())
notes(s, "Agendas fail when items are nouns instead of outcomes. 'Budget' can absorb an hour; 'approve the two changed budget lines' takes eight minutes.")

s = bullets_slide(prs, "After the meeting: the two-line record", [
    ("Decisions + owners + dates.", "'Decided: renew TechServe. Maya drafts terms by 7/12; Sam reviews by 7/15.' That's the whole document."),
    ("Send it within the hour,", "to attendees AND the informed-but-absent — memory of a meeting has a half-life measured in minutes."),
    ("Post it where the team decides things,", "not just in one inbox: the channel, the wiki, the project page."),
    ("Unrecorded decisions get re-decided.", "The three-minute summary is cheaper than the second meeting to settle what the first one settled."),
], D, nxt())
notes(s, "This is the chat-graduation rule applied to meetings: spoken decisions become written records or they evaporate. Chapter 9 develops formal minutes.")

s = bullets_slide(prs, "Case: the meeting that should have been a message", [
    ("The standing Thursday review:", "eight people, one hour, status read aloud from slides nobody saw in advance."),
    ("The math:", "8 people × 1 hour × 50 weeks = 400 hours a year — reading aloud what a three-line status email carries in 30 seconds."),
    ("The repair:", "written status by Wednesday noon; Thursday shrinks to 20 minutes for the two items that need discussion."),
    ("The test that generalizes:", "if information flows one way and no decision is made, it's a message wearing a meeting costume."),
], D, nxt())
notes(s, "Not anti-meeting — anti-broadcast-meeting. Real-time belongs to conflict, complexity, and connection (Chapter 1's rich-channel rule).")

s = section_slide(prs, "07", "Working in shared documents",
    "The document is the meeting room now — behave accordingly.", D, nxt())
notes(s, "Section 7: collaboration platforms — comments, suggestions, versions.")

s = bullets_slide(prs, "Comment etiquette in shared documents", [
    ("Comment on the text, not the author.", "'This claim needs a source' — not 'you never cite anything.' (Chapter 4's review rules apply verbatim.)"),
    ("Make comments resolvable.", "A comment is a task: state what would satisfy it, so the writer can do the thing and close it."),
    ("Use suggestion mode for wording,", "comments for substance. Direct edits to someone else's live draft are drive-by rewrites."),
    ("Resolve your own threads.", "When your question is answered, close it — a document with 60 open comments is unnavigable."),
    ("Big disagreements leave the margins.", "Three comment-thread volleys mean the discussion needs a richer channel; settle it, then record the outcome."),
], D, nxt())
notes(s, "Comment threads are permanent, visible-to-all writing. The margin of a shared doc is a public room, not a private note.")

s = two_col_slide(prs, "Version discipline: chaos vs. system",
    "You have version chaos if…", [
        "Report_FINAL_v2_REALLY_final.docx",
        "Three people edited three copies — someone's Saturday merges them",
        "The deck presented wasn't the deck approved",
        "'Which file is current?' gets asked weekly",
    ],
    "The system (four rules)", [
        "ONE living copy, in shared space — never emailed as an attachment for editing",
        "The filename says what it is; the platform tracks versions",
        "One named owner per document — merge authority lives somewhere",
        "Frozen snapshots (sent, approved, submitted) get dated copies: 'Proposal—as-submitted-2026-07-15'",
    ], D, nxt())
notes(s, "Cloud platforms made copies unnecessary — version chaos today is a habit problem, not a tooling problem. The 'as-submitted' snapshot ties to Chapter 10's versioning discipline.")

s = bullets_slide(prs, "Out-of-office replies and availability signals", [
    ("The OOO has three jobs:", "dates you're gone, who covers what while you are, and when the sender can expect you — three lines, done."),
    ("Name a human per category:", "'Contracts: Dana Ruiz. Everything else: I'll reply after July 21.' A bare 'I'm away' just defers the sender's problem."),
    ("No apology spiral.", "'I apologize for any inconvenience my vacation may cause' — rest is not a billing discrepancy (Chapter 4's tone pass)."),
    ("Status indicators are micro-OOOs.", "'Focus time — back at 2:00' does for an afternoon what the autoreply does for a vacation. Set them honestly, honor others'."),
], D, nxt())
notes(s, "Availability signaling is boundary-keeping made polite and searchable. Ties to response-time norms from Section 2.")

s = section_slide(prs, "08", "The wider digital workplace",
    "Beyond inbox and chat: the channels that hold institutional memory.", D, nxt())
notes(s, "Section 8: wikis, internal posts, video messages — where knowledge lives after the thread scrolls away.")

s = icon_rows_slide(prs, "Channels beyond the inbox", [
    ("📚", "Wiki / intranet pages", "Institutional memory: how-tos, policies, decisions of record. Written once, found for years."),
    ("📰", "Internal posts & newsletters", "Broadcast without reply-pressure — announcements, wins, context-setting from leadership."),
    ("🎥", "Recorded video / audio messages", "Tone-rich broadcast for change and morale; pair with a written summary for searchability."),
    ("💬", "Forums & open channels", "Questions asked in public teach everyone — yesterday's answered thread is tomorrow's documentation."),
], D, nxt(), kicker="Match the channel to the content's SHELF LIFE, not just its urgency.")
notes(s, "New axis introduced: shelf life. Chat is minutes, email is weeks, the wiki is years. Writers who put long-shelf-life content in short-shelf-life channels doom the team to re-asking.")

s = bullets_slide(prs, "Writing for the wiki: findability is the whole game", [
    ("Title for the searcher, not the writer.", "'How to submit a travel reimbursement' — the words a desperate colleague will actually type."),
    ("Answer first, context after.", "Wiki readers arrive mid-task; give the steps, then the background (the inverted pyramid, again)."),
    ("Date it and own it.", "Every page shows when it was last verified and who maintains it — undated pages read as unreliable and usually are."),
    ("Delete or redirect the obsolete.", "A wrong wiki page is worse than none; it answers confidently and incorrectly forever."),
], D, nxt())
notes(s, "The wiki is where Chapter 3's structure rules meet an audience of future strangers. Findability beats elegance.")

s = two_col_slide(prs, "Video message or written message?",
    "Record VIDEO when…", [
        "Tone carries the content: change, thanks, morale",
        "You're demonstrating something visual",
        "The audience is broad and the message is once",
        ("Always:", "keep it short and attach the decisions in text"),
    ],
    "Write TEXT when…", [
        "Anyone will need to find it later — video is unsearchable",
        "Readers need to skim, quote, or forward pieces",
        "Precision matters: numbers, dates, commitments",
        ("Test:", "if someone will ask 'what exactly did they say?' — text"),
    ], D, nxt())
notes(s, "Video is rich but opaque to search; text is lean but permanent and quotable. The pairing pattern — video for tone, text summary for record — gets both.")

s = bullets_slide(prs, "Signature block anatomy (this unit's assignment)", [
    ("The load-bearing four:", "name · title · organization · one phone number. Everything else is optional."),
    ("Optional and fine:", "pronouns, LinkedIn URL, office hours or time zone — anything that helps a stranger reach you correctly."),
    ("Leave out:", "inspirational quote forests, six social icons, legal disclaimers you weren't told to add, and images that arrive as attachment paperclips."),
    ("Test it where it will live:", "on a phone screen, in a reply chain, in plain-text mode — the signature that only works in one client doesn't work."),
], D, nxt())
notes(s, "Direct setup for the email-signature assignment. The signature is letterhead: identification, not decoration.")

s = stat_slide(prs, "The real cost of 'quick' interruptions", "~23 min",
    "is roughly how long it takes to fully re-engage with demanding work after an interruption, in University of California, Irvine research on task switching (Mark et al.).",
    [("The ping is never just the ping.", "Ten 'quick questions' can dissolve a workday without any of them being unreasonable alone."),
     ("Sender-side implication:", "batch non-urgent asks; one message with three questions costs one recovery, not three."),
     ("Receiver-side implication:", "the unpinged block from Section 4 isn't a luxury — it's where the demanding work actually happens."),
    ], D, nxt())
notes(s, "Gloria Mark's UC Irvine work on interruption recovery — cite as approximate, the point is the order of magnitude. This arms students with the 'why' behind batching and focus blocks.")

s = takeaways_slide(prs, [
    "The subject line is the message's job; sentence one delivers it; the dated ask ends it.",
    "One screen for routine mail — longer content becomes an attachment with a cover note.",
    "Reply-all only when every name needs every word; To acts, CC knows; new topic, new thread.",
    "Chat coordinates, email records; decisions graduate. Texts are invitation-only logistics.",
    "Everything on workplace systems is logged and discoverable — type like it.",
    "Curate the public layer; it interviews before you do. And guard your attention like capital.",
], D, nxt(), site_note="Practice now: course site → Chapter 5 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "On digital channels, the publicity test is not a thought experiment. It is the terms of service.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Pull your three most recent subject lines. Which formula do they follow — and what are their repairs?",
    "Where does your team actually decide things, and what gets lost in that channel?",
    "Schedule-send: considerate boundary-keeping, or normalized after-hours work in disguise? Argue both, then commit.",
    "State your personal permanence-gradient policy: what will you never type on a logged platform?",
    "Design the company mass-email policy that makes reply-all storms impossible.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 5 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 5 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Build:", "Your email signature (this unit's assignment) to Figure 1's spec — and audit your last twenty sent messages against the playbook."),
    ("Read:", "The Chapter 5 Study Guide — the full channel matrix, both cases, and the triage system."),
    ("Coming next:", "Chapter 6 — positive and neutral messages: the everyday mail that quietly builds your reputation."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch05-short-workplace-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
