# Chapter 5 — Short Workplace Messages and Digital Media (24 slides, delivery-neutral)
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
