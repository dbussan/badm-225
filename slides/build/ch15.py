# Chapter 15 — AI, Agents & Professional Communication (34 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 15"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "AI, Agents & Professional Communication",
    "The tools that draft · the judgment that ships · verification, disclosure, and the skills that appreciate", D)
notes(s, "Chapter 15: Unit 6 opens. AI as a professional communication tool — capabilities, failure modes, ethics, and career implications. Original material; no vendor content.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Explain", "what large language models actually do — and predict their failure modes from it."),
    ("Draft", "with AI as a junior collaborator: real briefs, critique loops, your voice preserved."),
    ("Verify", "everything load-bearing: facts, numbers, names, citations — before your name ships on it."),
    ("Protect", "confidential information, and disclose AI use per the rules of your school and employer."),
    ("Supervise", "AI agents that act — with limits, review gates, and accountability that stays yours."),
], D, nxt())
notes(s, "Objectives map to the Chapter 15 practice bank.")

s = stat_slide(prs, "The floor rose. The ceiling didn't move.", "floor",
    "AI raises the FLOOR of writing quality — competent prose is now nearly free. The ceiling — knowing what's true, what matters, and what the moment requires — is exactly where it was.",
    [("The floor rising is real:", "routine drafting that took an hour takes minutes; there is no going back, and pretending otherwise is career malpractice."),
     ("The consequence:", "competent-sounding is no longer a differentiator. Judgment is — because it's the part that didn't get cheaper."),
     ("This chapter's thesis:", "use the tools fully, verify ruthlessly, and invest in the ceiling."),
    ], D, nxt())
notes(s, "Floor-vs-ceiling is the chapter's organizing metaphor, introduced in Chapter 1 and developed fully here.")

s = section_slide(prs, "01", "What these tools are",
    "Prediction engines with excellent manners — the model that explains everything else.", D, nxt())
notes(s, "Section 1: a working mental model, plain-language and vendor-neutral.")

s = bullets_slide(prs, "What a language model actually does", [
    ("It predicts plausible next words,", "trained on enormous text — producing fluent, well-structured, statistically-likely prose."),
    ("Fluency is the product, truth is incidental:", "the model isn't lying when it errs; it's doing exactly its job — plausible continuation — on a question where plausible ≠ true."),
    ("It has no access to your situation:", "your reader, your history, your org's politics, this week's facts — unless you supply them (the prompt-as-brief slide)."),
    ("From this one model, every rule follows:", "why it drafts brilliantly, why it fabricates confidently, and why verification is non-negotiable."),
], D, nxt())
notes(s, "The plain mechanical model inoculates against both hype and dismissal. Everything later in the deck derives from this slide.")

s = two_col_slide(prs, "What it's great at / where it fails",
    "Great at (use freely)", [
        "First drafts of routine genres — email, summaries, outlines",
        "Rewriting: tone shifts, tightening, plain-language passes",
        "Critique: 'name the three weakest points in this memo'",
        "Brainstorming options and counterarguments",
        "Single-error sweeps (Chapter 4's targeted passes)",
    ],
    "Fails at (verify or avoid)", [
        "Facts, numbers, names — fluent fabrication is the signature failure",
        "Citations: plausible references to papers that don't exist",
        "Anything after its training data ends — staleness wears confidence too",
        "Your specific context: the reader's history, the politics, the stakes",
        "Judgment calls: what to say, whether to send, who gets hurt",
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "The two-column capability map students should carry. Both columns follow from the prediction-engine model.")

s = bullets_slide(prs, "The mental model: brilliant junior colleague, day one", [
    ("Treat AI like a gifted new hire who started this morning:", "extraordinary at producing work, zero knowledge of your world, and unaware when it's wrong."),
    ("You'd never send a day-one hire's draft unreviewed —", "the same review standard, applied identically, is the whole AI policy in one habit."),
    ("You'd also never refuse the help:", "declining a tireless drafting assistant out of pride or fear is choosing to be slower at the same quality."),
    ("Delegation without abdication:", "the work can be delegated; the accountability can't (this is the agents section's whole song, previewed)."),
], D, nxt())
notes(s, "The junior-colleague frame gives students a familiar social script for a new tool relationship — and it calibrates both trust and verification correctly.")

s = section_slide(prs, "02", "Drafting with AI",
    "The brief, the loop, and the voice that stays yours.", D, nxt())
notes(s, "Section 2: hands-on drafting craft.")

s = bullets_slide(prs, "The prompt is a brief — write it like Chapter 2", [
    ("Give it what you'd give a human writer:", "purpose, audience, key facts, constraints, tone — 'write something about the delay' gets you generic; a brief gets you usable."),
    ("Supply the situation it can't know:", "'the client has already complained twice; we need firm but warm' — context in, quality out."),
    ("State the format:", "'three-line status update' or 'one-page memo with headings' — structure requested is structure received."),
    ("Iterate the brief, not just the draft:", "when output misses, the fix is usually a fact or constraint you didn't supply — the tool made you discover your own requirements."),
], D, nxt())
notes(s, "Prompting is audience analysis pointed backward — students who plan messages well (Chapter 2) prompt well automatically. That's not a coincidence; it's the same skill.")

s = bullets_slide(prs, "The critique loop beats the generate loop", [
    ("Draft yourself, then ask for attack:", "'find the three weakest arguments in this proposal' keeps you the author and the tool the red team (Chapter 10's cold reader, on tap)."),
    ("Or reverse it — but edit like an owner:", "AI drafts, you rebuild: reorder, cut, verify, re-voice. The draft is raw material, never product."),
    ("Ask for options, not answers:", "'give me three ways to open this refusal' preserves the choosing — and choosing is the judgment layer."),
    ("Targeted passes, one at a time:", "'check subject-verb agreement only' · 'flag every claim lacking a number' — the tool excels at the single-error sweep (Chapter 4)."),
], D, nxt())
notes(s, "The critique loop is the professional pattern: it extracts the tool's strengths while keeping authorship — and it's how strong writers actually use these tools.")

s = bullets_slide(prs, "Keeping your voice", [
    ("Default AI prose has a house style:", "smooth, hedged, slightly padded, weirdly agreeable — readers are learning to recognize it, and it reads as 'nobody home.'"),
    ("Feed it your voice:", "'match the tone of this example' with a real paragraph of yours — or re-voice the draft yourself in the edit pass."),
    ("De-pad on sight:", "'I hope this finds you well' openers, triple restatements, and 'it's important to note' are the tell — cut them like Chapter 4 flab, because they are."),
    ("The relationship test:", "if the reader would feel differently knowing a machine wrote it — the goodwill note, the apology — a machine shouldn't (next slide)."),
], D, nxt())
notes(s, "Voice preservation is a craft skill AND a trust signal. The house-style tells are teachable and students spot them immediately once named.")

s = bullets_slide(prs, "What not to delegate — ever", [
    ("Goodwill messages (Chapter 6):", "thanks, congratulations, condolences — the entire content is that a human paused. Automating the pause deletes the message."),
    ("Apologies (Chapter 7):", "ownership ghostwritten is ownership faked — and the flat AI cadence reads exactly like what it is."),
    ("Performance feedback (Chapter 7):", "SBI requires having SEEN the behavior; delegated observation is fiction with a rubric."),
    ("The common thread:", "wherever the message IS the relationship, the drafting IS the sincerity. Efficiency is the wrong axis for these genres entirely."),
], D, nxt())
notes(s, "The never-delegate list, with the unifying principle. This slide closes the loop with Chapters 6 and 7 explicitly.")

s = section_slide(prs, "03", "Verification and confidentiality",
    "The two non-negotiables — everything else is style.", D, nxt())
notes(s, "Section 3: the hard rules.")

s = flow_slide(prs, "The verification pipeline", [
    ("FLAG", "Mark every load-bearing claim in the draft: facts, numbers, names, dates, citations"),
    ("TRACE", "Each one to a real source you can open (Chapter 10's ladder)"),
    ("FIX", "Correct, source, or delete — no third option for the unverifiable"),
    ("OWN", "Ship it as yours — because from this moment, it is"),
], D, nxt(), note_text="The pipeline runs on AI drafts exactly as it runs on your own — the tool just changed WHERE errors hide: yours cluster in haste, its cluster in confident specifics.")
notes(s, "Verification as a four-step mechanical process, not a vibe. The 'confident specifics' warning is the practical heuristic: the more precise an unverified AI claim, the more suspicious.")

s = bullets_slide(prs, "The fabricated citation problem", [
    ("The signature failure:", "a properly formatted reference — real journal, plausible authors, real-sounding title — for a paper that does not exist."),
    ("It survives every check except the real one:", "opening the source. Format-checking a fabricated citation is grooming a ghost."),
    ("The rule (Chapter 10):", "AI is rung five on the credibility ladder — a research ASSISTANT that finds and summarizes real sources, never a source itself."),
    ("'The AI said so' is not a citation.", "In school it's an integrity case; at work it's your name on a claim nobody can trace. Same failure, different invoice."),
], D, nxt())
notes(s, "The fabricated citation deserves its own slide because it's the failure most likely to end an academic career this semester.")

s = bullets_slide(prs, "Confidentiality: the paste is a publication", [
    ("Public AI tools are external services:", "pasting client names, salaries, unreleased numbers, or student records into one is disclosure — treat it like posting (Chapter 5)."),
    ("Know your organization's tooling:", "many provide enterprise AI with data agreements — the rules differ between the company instance and the free tab. Learn which is which."),
    ("Anonymize when the task allows:", "'a client in medical devices' preserves the task without the leak — most drafting help needs the shape, not the names."),
    ("When in doubt, the old test:", "would you email this content to an outside vendor without asking anyone? Then don't paste it either."),
], D, nxt())
notes(s, "The paste-as-publication frame makes the rule intuitive. The enterprise-vs-free distinction is the practical workplace knowledge.")

s = section_slide(prs, "04", "Disclosure and integrity",
    "The norms are forming now — here's the durable core.", D, nxt())
notes(s, "Section 4: ethics and disclosure, school and work.")

s = bullets_slide(prs, "Disclosure: the emerging professional norm", [
    ("Follow the explicit rules first:", "your syllabus, your employer's policy, your client's contract — where rules exist, the question is answered."),
    ("Where rules are silent, disclose by stakes:", "routine drafting help rarely needs a badge; analysis, research, or anything traded on your personal expertise usually does."),
    ("The honest formulation is cheap:", "'drafted with AI assistance; all facts and recommendations verified and mine' — one line, and it's true."),
    ("The test that outlives every policy:", "if disclosure would embarrass you, the use was wrong — the publicity test (Chapter 1), pointed at your tools."),
], D, nxt())
notes(s, "The stakes-based default plus the publicity test covers the policy vacuum students will actually face. The one-line disclosure formula is immediately usable.")

s = two_col_slide(prs, "In THIS course (and most workplaces)",
    "Encouraged", [
        "Critique loops on your own drafts",
        "Grammar, clarity, and tone passes",
        "Brainstorming, outlining, study help",
        "Practice: interview questions, quiz drills",
    ],
    "Out of bounds", [
        "Submitting AI work as your assessed writing",
        "Fabricated or unverifiable citations",
        "Pasting confidential or personal data",
        "AI-drafted goodwill, apologies, or feedback (see: never-delegate)",
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "Instructor: adjust the left column to your actual syllabus policy. As written it matches the common center of current academic norms.")

s = section_slide(prs, "05", "Agents",
    "When the tool stops drafting and starts DOING.", D, nxt())
notes(s, "Section 5: AI agents — the delegation frontier.")

s = bullets_slide(prs, "What an agent is", [
    ("A model with hands:", "an AI that doesn't just draft the email but sends it; doesn't just plan the search but runs it, files the results, and schedules the follow-up."),
    ("The shift is from suggestion to ACTION:", "drafting tools propose; agents execute — calendars, inboxes, purchases, postings, code."),
    ("Your actions, legally and professionally:", "the agent that mails the wrong client or posts the wrong figure acted under your name — 'the AI did it' is the new 'the intern did it,' and it defends exactly as well."),
    ("Useful and real today:", "research sweeps, report drafts, data pulls, scheduling — this course's own materials were built with agentic help, supervised precisely this way."),
], D, nxt())
notes(s, "The instructor's own agent use is a legitimate, honest example — the course site itself demonstrates supervised agentic work.")

s = bullets_slide(prs, "Delegating to agents without abdicating", [
    ("Scope the mandate in writing:", "what it may do, what it must ask about, what it must never touch — a job description, not a wish (Chapter 6's complete-ask, pointed at software)."),
    ("Gate the irreversible:", "sending, deleting, purchasing, publishing get human review — draft-for-approval beats act-then-apologize wherever the action can't be undone."),
    ("Start narrow, widen with evidence:", "the trust ladder (Chapter 8) applies to tools — the agent earns scope the way a new hire does."),
    ("Audit the output on cadence:", "spot-check what it did, not just what it reported — Chapter 9's honest-yellow logic applies to your tools too."),
], D, nxt())
notes(s, "Four supervision rules that map to management fundamentals — because agent supervision IS management, minus the feelings.")

s = bullets_slide(prs, "Case: the agent that emailed the draft", [
    ("An analyst's agent managed her follow-ups.", "One mandate line was loose: 'send routine confirmations without review.'"),
    ("A renegotiation email — with candid internal notes still in the thread —", "matched 'routine confirmation' by the agent's lights. It sent. The client read the notes."),
    ("The recovery ran Chapter 7:", "same-hour ownership call, no blame laid on the tool in public — 'my process failed' — and a mandate rewrite with a review gate."),
    ("The lesson:", "agents execute the mandate you WROTE, not the one you meant — precision in delegation is now a writing skill with a blast radius."),
], D, nxt())
notes(s, "The case is a composite of a failure pattern now common. 'The mandate you wrote, not the one you meant' — Chapter 3's precision stakes, updated.")

s = bullets_slide(prs, "Talking about AI with your team", [
    ("Agree on team norms out loud (Chapter 11):", "which tools, which tasks, what gets disclosed, what never gets pasted — unwritten AI norms are incidents on layaway."),
    ("Never weaponize the accusation:", "'this feels AI-written' is the new 'did you even write this?' — critique the work's actual failures, not its suspected genealogy (Chapter 4)."),
    ("Share prompts like you share templates:", "the brief that produced the great status report is team infrastructure — document it (Chapter 5's wiki rules)."),
    ("Level the access:", "if half the team has enterprise tools and half doesn't, the output gap isn't a talent gap — say so before performance reviews do."),
], D, nxt())
notes(s, "AI as a team-communication topic, not just an individual tool — closing the loop with Chapter 11's ground rules.")

s = section_slide(prs, "06", "The career layer",
    "Invest in the ceiling.", D, nxt())
notes(s, "Section 6: what appreciates, what depreciates, and how to stay current.")

s = bullets_slide(prs, "Skills that appreciate as drafting gets free", [
    ("Judgment:", "what's true, what matters, what the moment requires — the whole ceiling, and the whole course."),
    ("Verification and source discipline (Chapter 10):", "when fluent text is free, the person who can tell TRUE from plausible becomes the scarce input."),
    ("The brief:", "specifying work precisely — for humans or agents — is the management skill and the prompt skill, converged."),
    ("Relationships and presence (Chapters 11, 12, 16):", "the trust account, the room, the hard conversation — nothing in the toolchain touches these."),
    ("Editing:", "the floor's output still needs an owner with taste — rebuilding a B-minus draft into your A is the new core competency."),
], D, nxt())
notes(s, "The appreciation portfolio. Note that every item is a chapter of this course — the curriculum IS the hedge, and that's by design.")

s = bullets_slide(prs, "Staying current without hype-chasing", [
    ("The capabilities will keep moving;", "the principles in this deck — verify, protect, disclose, supervise — are built to survive the versions."),
    ("Re-test your assumptions quarterly:", "the thing AI 'couldn't do' in January is sometimes shipping by June — keep your capability map dated (Chapter 9's 'as of' rule)."),
    ("Learn by doing real tasks,", "not by reading takes: one workflow genuinely automated teaches more than fifty threads about automation."),
    ("Beware both cults:", "'it changes nothing' and 'it changes everything' are equally lazy — the professional position is a running, tested inventory of what it changes for YOU."),
], D, nxt())
notes(s, "Meta-skill: maintaining a personal, dated capability map. The quarterly re-test habit is concrete enough to actually happen.")

s = bullets_slide(prs, "Case: two analysts, one tool", [
    ("Same team, same enterprise AI license.", "Analyst A pastes the assignment in, submits what comes out, and calls it efficiency."),
    ("Analyst B briefs it like a junior,", "runs the critique loop on her own draft, verifies every number against the source system, and re-voices the close."),
    ("Month three: A's error in a client deliverable", "— a confident, fabricated benchmark — triggers a review of everything he'd shipped. B gets his accounts."),
    ("Same tool. The difference was never the tool.", "It was who stayed the author. That's the chapter — and mostly, the course."),
], D, nxt())
notes(s, "The closing case operationalizes floor-vs-ceiling as two career trajectories with identical tooling.")

s = takeaways_slide(prs, [
    "It predicts plausible text: brilliant drafting, confident fabrication — both from the same mechanism.",
    "Treat it as a gifted day-one junior: use it fully, review everything, stay the author.",
    "Verify the load-bearing: facts, numbers, names, citations — traced to sources you opened.",
    "The paste is a publication: confidential data never enters tools without an agreement.",
    "Agents act under your name: written mandates, gates on the irreversible, scope earned like trust.",
    "Invest in the ceiling: judgment, verification, the brief, relationships, editing.",
], D, nxt(), site_note="Practice now: course site → Chapter 15 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The tools will write better every year. The question they will never answer is whether the thing they wrote is true, kind, and yours to send. That question is the job.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Run the critique loop on something you've written this term. What did it catch — and what did it wrongly flag?",
    "Draft your personal never-delegate list beyond the chapter's three. What's the principle behind your additions?",
    "Write the one-paragraph agent mandate for managing YOUR inbox. Trade with a partner and hunt each other's loose lines.",
    "Where should your field's disclosure norm land? Draft the policy sentence you'd want your employer to adopt.",
    "Argue it: 'AI-written' criticism in peer review — legitimate quality signal or lazy ad hominem? Build the test.",
], D, nxt())
notes(s, "Async-ready. Question three (the mandate exchange) is the strongest live exercise.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 15 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 15 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Do:", "Automate one real workflow this week with the verification pipeline attached — and note what it got wrong."),
    ("Write:", "Your personal AI operating rules: one page — uses, never-uses, verification, disclosure."),
    ("Coming next:", "Chapter 16 — leadership under pressure and influence: the human skills the tools made MORE valuable."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch15-ai-agents-professional-communication.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
