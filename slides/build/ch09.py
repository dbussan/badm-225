# Chapter 9 — Informal Reports (22 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 9"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Informal Reports",
    "Progress · incidents · minutes · recommendations — documents that carry facts to decisions", D)
notes(s, "Unit 4 opens: the long-form genres. The pyramid is the engine of everything here.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Classify", "reports by the reader's question — informational (what happened?) vs. analytical (what should we do?)."),
    ("Build", "the pyramid: answer on top, MECE reasons beneath, evidence beneath those."),
    ("Write", "status reports with honest yellows, minutes that record decisions, incidents that name causes."),
    ("Design", "displays that make one point each — takeaway in the title, axes honest."),
    ("Hold", "the analysis-versus-advocacy line: persuasive AND complete."),
], D, nxt())
notes(s, "Objectives map to the Chapter 9 bank and the market-research assignment.")

s = two_col_slide(prs, "The report family",
    "INFORMATIONAL — “what happened?”", [
        "Progress and status reports",
        "Trip and conference reports",
        "Meeting minutes",
        "Incident records",
        ("Virtues:", "accuracy, proportion, findability"),
    ],
    "ANALYTICAL — “what should we do?”", [
        "Justification / recommendation",
        "Comparison and evaluation",
        "Feasibility (your capstone)",
        ("Inherits everything, adds:", "Chapter 8's persuasive machinery"),
        ("The test:", "ends in a recommendation → analytical rules govern"),
    ], D, nxt())
notes(s, "'Informal' describes the container, not the care.")

s = flow_slide(prs, "The pipeline: conclude BEFORE structuring", [
    ("DEFINE", "The question this report answers"),
    ("GATHER", "Data, sources, evidence"),
    ("CONCLUDE", "The answer — one written sentence, FIRST"),
    ("PYRAMID", "Answer → reasons → evidence"),
    ("DRAFT + REVISE", "Chapters 3–4, applied"),
], D, nxt(), note_text="The deepest report error happens before writing: structuring the investigation's story instead of the conclusion's case.")
notes(s, "Writers who conclude first produce documents where every section knows its job.")

s = section_slide(prs, "01", "The pyramid",
    "Answer on top. Reasons beneath. Evidence beneath those. (Minto)", D, nxt())
notes(s, "Section 1: the structural engine.")

s = icon_rows_slide(prs, "Pyramid mechanics", [
    ("▲", "Summit discipline", "The top is an ANSWER (“Renew with TechServe”), never a topic (“Vendor Analysis”). A noun phrase is a filing label."),
    ("⇅", "Vertical logic", "Each layer answers the question the layer above provokes: why? → how do you know?"),
    ("⇔", "Horizontal logic (MECE)", "Reasons are the same KIND, no overlaps, no gaps. “Cost, price, budget” is one reason in three costumes."),
    ("📄", "It generates the document", "Summit = opening + subject line · reasons = headings in decision-weight order · evidence = body · orphans = cut or appendix."),
], D, nxt())
notes(s, "Build the pyramid, then transcribe it — the permanent answer to 'how do I organize this?'")

s = bullets_slide(prs, "Why answer-first works (even though it feels wrong)", [
    ("The resistance:", "you want the reader to experience the journey — the method, the earned conclusion."),
    ("The cognition:", "working memory is small (Miller, 1956); a reader holding your unresolved question retains fragments. Given the answer, everything after becomes active confirmation or challenge."),
    ("Better meetings too:", "attendees argue WITH the recommendation instead of asking what it is."),
    ("The journey has a home:", "the appendix — where the scrutinizer audits your method after the summit earned their attention."),
], D, nxt())
notes(s, "Answer-first is also cheaper to WRITE: selection replaces narration.")

s = section_slide(prs, "02", "The workhorses",
    "Status reports, minutes, incidents.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "The progress report skeleton", [
    ("STATUS LINE", "“On track for 8/16” — the verdict, sentence one, no suspense"),
    ("DONE", "Completed since last report, with dates"),
    ("IN PROGRESS", "Current work, expected completion"),
    ("BLOCKED / RISKS", "The honest yellow: threat + plan + what you need"),
    ("NEXT + ASK", "The coming period; any decision needed"),
], D, nxt(), note_text="Fixed cadence, fixed skeleton, deltas over restatements (Chapter 5). The BLOCKED section carries the report's integrity.")
notes(s, "The reader's first question is the report's first answer.")

s = bullets_slide(prs, "The honest yellow — and the dashboard that lied politely", [
    ("Five months of green;", "month six: integration goes green → red. The committee: “how does a project fail in thirty days?” It didn't — the PM's private tracker showed four months of known slippage."),
    ("No false sentence was ever written.", "“Green” drifted from “on track” to “I can still fix this quietly” — the MUM effect wearing a status color (Rosen & Tesser, 1970)."),
    ("The audit is retrospective:", "when projects fail, old status reports get reread. The week-3 yellow is diligence; the week-11 green is the career event."),
    ("The structural fix:", "define green with teeth — “all milestones met AND no known risk to the next” — and ask every report: “what's the yellowest thing in your green?”"),
], D, nxt())
notes(s, "Committees that interrogate yellows manufacture greens — incentive design matters (Chapter 16).")

s = two_col_slide(prs, "Minutes: decisions, not transcripts",
    "Transcript minutes", [
        "Who said what, in order",
        "Long, late, unread",
        "Occasionally dangerous — the stray remark as Exhibit A",
    ],
    "Decision minutes", [
        "Decisions (verbatim where wording matters)",
        "Owners + deadlines per action",
        "Open questions, explicitly parked",
        ("One page. Same day.", "Five private meetings become one shared one."),
    ], D, nxt())
notes(s, "Contested wording gets resolved IN the meeting: 'let me read back the decision as I'll record it.'")

s = flow_slide(prs, "Incident anatomy: grammar as a safety system", [
    ("WHAT HAPPENED", "Time order, actors NAMED — active voice is functional here"),
    ("IMPACT", "Downtime, product, exposure — quantified"),
    ("ROOT CAUSE", "Past the convenient stop: “technician error” is one why short"),
    ("ACTIONS", "Owner + date each. “Identified” ≠ “assigned”"),
    ("PREVENTION", "The system change that makes recurrence hard"),
], D, nxt(), note_text="Reports written to assign blame get gamed; reports written to fix systems get fed. Safe reporting is complete reporting.")
notes(s, "Chapter 3's incident case, now as the full genre.")

s = section_slide(prs, "03", "Data displays",
    "One display, one point — announced in the title.", D, nxt())
notes(s, "Section 3.")

s = two_col_slide(prs, "Table or chart?",
    "TABLE — exact values", [
        "Lookup and line-item comparison",
        "Audit trails",
        "When the reader will USE the numbers",
    ],
    "CHART — the shape", [
        "Trend, proportion, outlier",
        "Comparison at a glance",
        ("Either way:", "takeaway in the title · units labeled · sources named · axes honest (zero, or loudly marked)"),
    ], D, nxt())
notes(s, "Tufte's canon: maximize data-ink, kill the chartjunk. The truncated bar axis is the most common honest-numbers-dishonest-picture trick.")

s = bullets_slide(prs, "Titles carry takeaways", [
    ("Topic title:", "“Figure 2: Response Time Data” — informs no one."),
    ("Takeaway title:", "“Figure 2: Response times fell 41% after barcode intake” — works even for readers who never parse the bars."),
    ("Integration rule:", "every exhibit is referenced in the text BY ITS POINT; the unreferenced exhibit is cargo the reader unloads alone — cut it or appendix it."),
    ("Uncertainty is carried in the verbs:", "shows / suggests / we estimate / we believe — ranges beat false-precision points."),
], D, nxt())
notes(s, "Chapter 3's informative headings, wearing axes. Calibration vocabulary from the guide.")

s = bullets_slide(prs, "Case: the trip report nobody could use", [
    ("Engineer A:", "four chronological pages, filed a week later — flights, booth, sessions, “valuable overall.”"),
    ("Engineer B, next morning, one page:", "“Three findings that matter: competitor ships barcode intake Q4 (roadmap assumption dead) · Meridian wants a joint study (decision by the 15th) · FDA draft hits our amendment logs (summary attached).”"),
    ("Six months later:", "B's page shaped the roadmap; B briefs the executives before the next show."),
    ("The lesson:", "chronology is what writers reach for when they haven't decided what matters. Every report samples your judgment — selection IS the content."),
], D, nxt())
notes(s, "B's report was also FASTER to write: one hard thought replaced a week of easy ones.")

s = bullets_slide(prs, "Analysis vs. advocacy: the line", [
    ("The standard:", "present the evidence that lets a competent skeptic reach YOUR conclusion — including what gave you pause."),
    ("The failure modes:", "selection bias · strawman alternatives · precision theater · buried assumptions."),
    ("Cost the strongest alternative — and “do nothing.”", "Pricing the status quo is usually your best paragraph."),
    ("The test:", "the most skeptical reader, with full data access — every gap between what exists and what you presented is a withdrawal against your name."),
], D, nxt())
notes(s, "You are allowed to be persuasive. You are required to be complete.")

s = bullets_slide(prs, "Getting your report actually read", [
    ("The transmittal note IS the executive summary:", "“Bottom line: refurbishing three units saves $23K/yr; decision needed by 7/25” — never “please find attached.”"),
    ("Time it to the live decision;", "pre-brief the key decider before wide release (Chapter 8's pre-wiring)."),
    ("Schedule the next touch:", "“I'll bring this to Thursday's ops meeting” — a report without follow-up is a message in a bottle."),
    ("Length signals:", "the one-pager with a rigorous appendix beats the thick report — judgment plus depth, both visible."),
], D, nxt())
notes(s, "Internal marketing is legitimate craft.")

s = takeaways_slide(prs, [
    "Classify by the reader's question; a recommendation ending invokes analytical rules.",
    "Conclude before structuring — then build the pyramid: answer, MECE reasons, evidence.",
    "Status lines carry verdicts; honest yellows beat green-to-red surprises — the audit is retrospective.",
    "Minutes: decisions, owners, deadlines — one page, same day. Incidents: actors, causes, owners, prevention.",
    "Displays make one point, announced in the title, on honest axes.",
    "Persuasive AND complete: the skeptic test governs the analytical line.",
], D, nxt(), site_note="Practice now: course site → Chapter 9 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Every report is an audition you didn't know was scheduled — judged by readers you may never meet, on the one skill organizations can't fake caring about: knowing what matters.",
    "this chapter, compressed", D, nxt())
notes(s, "Reports travel above your manager's head with your name attached.")

s = discussion_slide(prs, "Discussion questions", [
    "Bring a real report and build its pyramid on one page: summit, reasons, orphans.",
    "Why do organizations reward the reporting behaviors they claim to hate? Locate the incentive.",
    "Defend or attack: the one-page report is harder and more senior than the twelve-page report.",
    "Design a definition of “green” that a judgment call cannot stretch.",
    "Find a misleading-but-true chart in the wild; name the mechanism and rebuild it honestly.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 9 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 9 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Apply:", "Your market-research assignment's sections are a pyramid scaffold — this chapter is its manual."),
    ("Read:", "The Chapter 9 Study Guide — the full workshop, templates, and both cases."),
    ("Coming next:", "Chapter 10 — proposals and formal reports: the upgrade kit for the same engine."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch09-informal-reports.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
