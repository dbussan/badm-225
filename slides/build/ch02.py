# Chapter 2 — Planning Business Messages (35 slides, original, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 2"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Planning Business Messages",
    "Purpose · audience analysis · reader benefits · tone · the decisions before the first word", D)
notes(s, "Chapter 2: the invisible half of writing — planning. Companion study guide covers everything here in depth.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Write", "a one-sentence purpose statement naming who must do what, and why they would want to."),
    ("Profile", "an audience in rings — primary, secondary, gatekeeper, hidden — and write for all of them."),
    ("Convert", "writer-view sentences and feature lists into you-view benefits."),
    ("Set", "tone deliberately with the formality dial: positive, fossil-free, bias-free."),
    ("Plan", "for skeptical readers: name objections, answer the big two, make yes small and dated."),
], D, nxt())
notes(s, "Objectives map to guide sections and the site's Chapter 2 practice bank.")

s = stat_slide(prs, "The most expensive sentence in business", "×2",
    "…is the one that has to be sent twice. Unclear messages generate replies, corrections, meetings, and wrong action.",
    [("Planning buys the time back.", "Minutes spent deciding purpose, audience, and benefit are repaid every time version one does its job."),
     ("The research agrees:", "expert writers differ from novices mostly in how much they plan — goals and audience, before and during drafting (Flower & Hayes, 1981)."),
     ("Novices start typing.", "Experts start deciding."),
    ], D, nxt())
notes(s, "Anchor: rework is the hidden cost of unplanned writing.")

s = section_slide(prs, "01", "The writing process",
    "Plan, draft, revise — three different mental jobs, deliberately separated.", D, nxt())
notes(s, "Section 1.")

s = flow_slide(prs, "Three phases, three different jobs", [
    ("PLAN", "Decide: purpose, audience, benefit, channel. Half the work happens here."),
    ("DRAFT", "Generate: get it down, not perfect. Refuse to edit while writing."),
    ("REVISE", "Judge: reader's eyes, structure, polish, proof. Chapter 4's territory."),
], D, nxt(), note_text="Separating deciding, generating, and judging is why drafts come faster and revisions cut deeper. This chapter is phase one.")
notes(s, "Unbundling the three mental jobs explains most 'writer's block': it is usually undone planning.")

s = section_slide(prs, "02", "Purpose",
    "One message, one job.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "Anatomy of a working purpose statement", [
    ("WHO must act?", "The reader — named, not 'everyone.'"),
    ("WHAT exactly?", "A checkable act with a date, not a topic."),
    ("WHY would they?", "Their reason — the benefit in their terms."),
], D, nxt(), note_text="Template: “So that [reader] does [specific act] because [their reason].” If you can't complete it, you're not ready to draft.")
notes(s, "Drill the template aloud with two or three class examples.")

s = two_col_slide(prs, "Purpose statements: weak vs. working",
    "Weak", [
        "“Update everyone on the project.”",
        "“Tell the team about the new expense system.”",
        "No actor, no action, no test for success",
    ],
    "Working", [
        "“So that my manager approves two extra testing days, because shipping untested risks the client.”",
        "“So that every team member submits May expenses in the new system by May 31, because late entries wait until July.”",
        ("Test:", "someone else could verify whether the message worked"),
    ], D, nxt())
notes(s, "The working versions are falsifiable — you can check whether the purpose was achieved.")

s = bullets_slide(prs, "Purpose overload: the message that does everything and achieves nothing", [
    "Three asks, two announcements, and a question in one email — every purpose competes with the others.",
    ("Readers act on one thing.", "Ten asks produce either the easiest one or none."),
    ("The rule:", "one message, one job. The second ask gets its own message or a clearly separated section."),
    ("Corollary for subject lines:", "the subject names THE job: “Approve budget rev by Fri” beats “Some updates.”"),
], D, nxt())
notes(s, "Purpose overload is the most common planning failure in student and workplace email alike.")

s = section_slide(prs, "03", "Audience",
    "Write to the person who is actually there — and everyone behind them.", D, nxt())
notes(s, "Section 3.")

s = icon_rows_slide(prs, "Your audience comes in rings", [
    ("●", "Primary", "The reader who acts. Profile them: what do they know, feel, need?"),
    ("◍", "Secondary", "The forward, the file, next year's reader. Define terms they won't know."),
    ("◈", "Gatekeeper", "Decides whether your message reaches the primary reader at all — the assistant, the moderator, the algorithm."),
    ("○", "Hidden", "Legal, HR, competitors, the public record. Never write what this ring shouldn't see."),
], D, nxt())
notes(s, "Business messages travel. The rings are why.")

s = stat_slide(prs, "The forwardability test", "FWD",
    "Could this message be forwarded, unedited, without embarrassing me?",
    [("It compresses audience analysis into one question", "— and it is the question your message will eventually face anyway."),
     ("Passing it changes drafting:", "defined terms, professional tone everywhere, nothing said about people you wouldn't say to them."),
     ("Failing it has a name in court records:", "'Exhibit A.'"),
    ], D, nxt())
notes(s, "Memorable compression of the rings concept.")

s = icon_rows_slide(prs, "Three readers you will meet everywhere", [
    ("⚡", "The executive skimmer", "Subject line, two sentences, bolded deadline — on a phone. Frontload or vanish."),
    ("🔍", "The expert scrutinizer", "Checks your numbers, notices omissions. Precise claims, cited evidence, objections addressed."),
    ("💭", "The anxious stakeholder", "Asks only 'what does this mean for ME?' Answer it explicitly and early — inference under anxiety picks the worst reading."),
], D, nxt())
notes(s, "Archetypes accelerate audience analysis. Most change announcements fail the third reader.")

s = bullets_slide(prs, "Design for how people actually read", [
    ("Screen readers scan in an F-pattern:", "first lines fully, then less of each line, then down the left edge (Nielsen, 2006)."),
    ("Consequences:", "the ask lives in sentence one; paragraphs open with their point; deadlines get bold; lists give scanners handholds."),
    ("The inverted pyramid", "— most important first — has served journalism for a century for the same reason."),
    ("Below the first screen is optional reading.", "Never hide required action there."),
], D, nxt())
notes(s, "Frontloading is not style preference; it is designing for measured reading behavior.")

s = section_slide(prs, "04", "The you-view",
    "The reader is the main character.", D, nxt())
notes(s, "Section 4.")

s = two_col_slide(prs, "Writer-view → you-view",
    "Writer-view (I/we)", [
        "“We are pleased to announce our new evening hours.”",
        "“I have approved your request.”",
        "“Our policy requires this form.”",
    ],
    "You-view", [
        "“You can now shop weeknights until 9 p.m.”",
        "“Your request is approved — your new hours begin Monday.”",
        "“To protect your refund, submit this form by Friday.”",
    ], D, nxt())
notes(s, "Same facts, re-anchored on the reader. Grammar follows the planning.")

s = bullets_slide(prs, "Two cautions that keep the you-view honest", [
    ("It's not the word “you.”", "It's organizing content around reader benefit — “you will be terminated” is you-view grammar and a diplomatic disaster."),
    ("In criticism, pivot AWAY from you.", "“The report needs sources” beats “you forgot the sources” — protect dignity, target the work."),
    ("The principle under both:", "face the reader's interests, protect the reader's face."),
    ("Ethics check:", "framing real benefits is respect; inventing benefits is manipulation."),
], D, nxt())
notes(s, "Connects to Chapter 16's face-saving principle.")

s = flow_slide(prs, "The “which means” ladder: features → benefits", [
    ("Feature", "“The new LIMS auto-logs samples”"),
    ("…which means", "no manual entry for your techs"),
    ("…which means", "an hour a day saved, and transcription errors gone from audits"),
], D, nxt(), note_text="Climb until the sentence contains something the reader would put in their own status report. Can't finish the ladder? The feature may not belong in the message.")
notes(s, "Two rungs usually suffice. Great drill for resumes too — preview of Chapter 13.")

s = section_slide(prs, "05", "Tone",
    "One professional voice, dialed to the occasion.", D, nxt())
notes(s, "Section 5.")

s = icon_rows_slide(prs, "Setting the dial deliberately", [
    ("☀", "Prefer positive framing", "“Your order ships Friday” beats “We cannot ship before Friday.” Same fact, opposite experience."),
    ("🦴", "Retire the fossils", "“Per my last email,” “please be advised,” “enclosed please find” — inherited noise, not respect."),
    ("⚖", "Bias-free by default", "Neutral titles, person-first language, the names and pronouns people use. Precision IS respect."),
    ("🎚", "Match the reader's stakes", "Cheerful tone on their billing error reads as indifference. Measured tone earns trust."),
], D, nxt())
notes(s, "Tone is planned, not left to mood.")

s = bullets_slide(prs, "Planning for global and multicultural readers", [
    ("Strip idioms at the planning stage.", "“Low-hanging fruit” and every sports metaphor force double translation."),
    ("Unambiguous dates.", "“5 March 2026,” never “3/5/26.”"),
    ("More context for high-context readers.", "Relationship before business isn't padding — it's the message working (Hall, 1976)."),
    ("Let a reluctant no surface safely.", "“What obstacles should we plan around?” beats demanding a yes/no."),
    ("Confirm gently in writing.", "Explicit for low-context readers, face-saving for high-context ones."),
], D, nxt())
notes(s, "Chapter 1's context continuum, applied at planning time.")

s = section_slide(prs, "06", "The skeptical reader",
    "Receptive audiences forgive shortcuts. Skeptical ones bill for them.", D, nxt())
notes(s, "Section 6.")

s = flow_slide(prs, "Planning for resistance", [
    ("List their objections", "Before writing. Honestly."),
    ("Answer the big two", "Inside the message, not after it."),
    ("Show, don't claim", "Evidence beats adjectives."),
    ("Make yes easy", "Small ask, clear step, real date."),
], D, nxt(), note_text="Name the price yourself: “This costs $2,400, and here's why it pays back in six weeks” beats hoping nobody notices.")
notes(s, "Naming the objection first is manufactured ethos — honestly manufactured.")

s = icon_rows_slide(prs, "No time to plan? The 60-second version", [
    ("1", "What do I want?", "Complete the purpose template silently: so that [reader] does [act] because [reason]."),
    ("2", "Why would they care?", "One reader benefit — moved into sentence one."),
    ("3", "What happens next?", "A specific act plus a date, at the end."),
], D, nxt(), kicker="Three questions cover routine messages. Save the full canvas for money, strangers, resistance, or permanence.")
notes(s, "Compressed discipline for real inboxes.")

s = icon_rows_slide(prs, "Opening lines by message type (part 1)", [
    ("→", "Routine request", "The ask immediately: “Could you send the Q2 vendor list by Thursday noon?”"),
    ("★", "Good news", "The news itself: “Your proposal is approved — funding starts May 1.”"),
    ("ℹ", "Update", "The one-line takeaway: “Migration finished; all systems normal.”"),
    ("✎", "Meeting follow-up", "The decisions: “Three decisions from today's call:”"),
    ("🤝", "Request to a stranger", "The connection: “Dr. Rios suggested I contact you about the co-op program.”"),
], D, nxt())
notes(s, "First sentences, matched to message type.")

s = icon_rows_slide(prs, "Opening lines by message type (part 2)", [
    ("⏰", "Gentle reminder", "Assume good faith: “Resending in case this got buried — form due Friday.”"),
    ("▤", "Complex proposal", "Recommendation first, roadmap second: “I recommend renewing with TechServe; comparison below.”"),
    ("☁", "Bad news", "The one exception: a buffer of honest context first. (Chapter 7 covers this.)"),
    ("♥", "Thanks", "The specific act: “Your triage of Saturday's outage saved the launch.”"),
    ("⚑", "Apology", "Ownership without hedging: “I missed the deadline I committed to.”"),
], D, nxt())
notes(s, "Note the single exception — indirect openings for bad news — and its own chapter.")

s = bullets_slide(prs, "Case: the wellness memo that backfired", [
    ("The launch:", "an all-staff memo celebrating the company's investment, listing program features, closing with excitement. Participation: 11%."),
    ("The grapevine's version:", "“they're making us do screenings so insurance can raise our rates.”"),
    ("Planning failures —", "benefits were the company's feature list; the audience's #1 objection (my data?) went unanswered; the anxious stakeholder was forgotten."),
    ("The replanned opening:", "“A $40 monthly premium credit and free screenings on work time. Your results go to you alone — the company sees only anonymous counts.”"),
], D, nxt())
notes(s, "Silence on the top objection hands interpretation to the grapevine — Chapter 1's rule in action.")

s = two_col_slide(prs, "Case: the same $545 request, planned two ways",
    "Version A (declined politely)", [
        "“…this certification would be a great step in my professional growth…”",
        "Subject: the writer's growth",
        "Manager's benefits: zero",
        "Call to action: “I hope…” — nothing checkable",
    ],
    "Version B (approved)", [
        "“Funding my CQA exam ($545) lets us close audit findings in-house instead of $1,800 external reviews.”",
        "Subject: the department's math",
        ("Ask:", "“approve by the 15th for the early rate”"),
        ("The lesson:", "your real reasons are legitimate — the MESSAGE'S reasons must be the reader's"),
    ], D, nxt())
notes(s, "Plan the overlap between your goal and their benefit; both people win.")

s = bullets_slide(prs, "AI as a planning partner", [
    ("Safest AI phase of writing:", "you're generating hypotheses, not facts."),
    ("Useful prompts:", "“List objections a hospital CFO might raise” · “What does a first-year employee NOT know in this announcement?” · “Rewrite this opening so the reader benefit comes first.”"),
    ("The boundary:", "AI doesn't know YOUR reader. Treat output as a brainstormed list; verify against the human you know."),
    ("And never", "paste confidential context into public tools. (Chapter 15 has the full playbook.)"),
], D, nxt())
notes(s, "AI widens the hypothesis list; judgment stays human.")

s = takeaways_slide(prs, [
    "Experts decide before they draft — planning is half the work.",
    "One message, one job: “so that [reader] does [act] because [their reason].”",
    "Audiences come in rings; write to the primary, write knowing the rest exist.",
    "The you-view faces the reader's interests and protects the reader's dignity.",
    "Tone is one voice on a deliberate dial — positive, fossil-free, bias-free, stakes-matched.",
    "For skeptics: name objections, answer the big two, show evidence, make yes small and dated.",
], D, nxt(), site_note="Practice now: course site → Chapter 2 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The single question that rescues more messages than any other: why would the reader want to?",
    "this chapter, compressed to one line", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Write the purpose statement for a recent message that flopped. Did the sent version serve that purpose?",
    "Name a real gatekeeper or hidden audience in your world. How does their existence change one message this month?",
    "Rewrite a marketing email's opening in genuine you-view. Who was the original planned for?",
    "Which of Aristotle's appeals do you lean on by habit — and which audience needs the one you use least?",
    "Apply the six-box canvas to a public document that fails plain-language standards. What was never decided?",
], D, nxt())
notes(s, "Async discussion-board ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 2 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 2 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Read:", "The Chapter 2 Study Guide (course site download) — the full 20+ page treatment with figures, cases, and the planner worksheet."),
    ("Do:", "Run the 60-second plan on every real message you send this week."),
    ("Coming next:", "Chapter 3 — organizing and drafting: direct vs. indirect strategy, paragraphs, and sentences that carry weight."),
], D, nxt())
notes(s, "Delivery-neutral closing pattern.")

out = os.path.join(os.path.dirname(__file__), "..", "ch02-planning-business-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
