# Chapter 4 — Revising Business Messages (31 slides, original, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 4"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Revising Business Messages",
    "Conciseness · clarity · proofreading — the judging phase, where drafts become sendable", D)
notes(s, "Chapter 4: the phase amateurs skip. Companion study guide includes the ten-repair workshop and the Oakhurst comma case.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Revise", "in three separated passes — structure, sentences, proof — instead of one anxious reread."),
    ("Cut", "the six kinds of flab: lead-ins, there-is openers, redundancies, flabby phrases, hedges, noun stacks."),
    ("Replace", "abstractions with checkable claims — numbers and examples that survive forwarding."),
    ("Catch", "what spellcheck cannot: real-word errors, homophones, wrong names, wrong numbers."),
    ("Run", "the pre-send ritual: read aloud, verify, last-thing check."),
], D, nxt())
notes(s, "Objectives map to the Chapter 4 practice bank.")

s = section_slide(prs, "01", "Revision is a system",
    "Three problems live at three altitudes. The eye can't patrol all three at once.", D, nxt())
notes(s, "Section 1.")

s = flow_slide(prs, "The three-pass system", [
    ("PASS 1 · STRUCTURE", "Right strategy? Main point findable? Every section earning its place?"),
    ("PASS 2 · SENTENCES", "Concise, clear, active, parallel, old→new flow."),
    ("PASS 3 · PROOF", "Spelling, names, numbers, dates — what software cannot see."),
], D, nxt(), note_text="Structure first — there is no point polishing a paragraph pass one will delete. Three passes are faster than one muddled read repeated four times.")
notes(s, "The core discipline of the chapter.")

s = bullets_slide(prs, "The cooling-off period", [
    ("Fresh from drafting, you cannot proofread your own work.", "Your brain already knows what the text should say — and shows you that instead."),
    ("The science:", "writers read from intended meaning; the brain fills gaps and glides over transpositions a stranger would catch instantly."),
    ("The antidote is distance.", "Overnight for anything substantial; even twenty minutes resets the eyes meaningfully."),
    ("Plan it into deadlines:", "the document due Friday is drafted Wednesday. On purpose."),
], D, nxt())
notes(s, "Typo blindness is expertise misfiring, not carelessness.")

s = section_slide(prs, "02", "Conciseness",
    "Respect, measured in words.", D, nxt())
notes(s, "Section 2.")

s = icon_rows_slide(prs, "The six flab targets", [
    ("✂", "Long lead-ins", "“I am writing this email to let you know that…” → start where the news starts."),
    ("✂", "There is / it is openers", "“There are three issues that remain” → “Three issues remain.”"),
    ("✂", "Redundant pairs", "“Each and every” · “final outcome” · “past history” — one word was already working."),
    ("✂", "Flabby phrases", "“Due to the fact that” = because · “at this point in time” = now · “in order to” = to."),
    ("✂", "Hedges & intensifiers", "“Very, really, quite, rather” add heat, not light. Nothing is “very unique.”"),
], D, nxt())
notes(s, "Sixth target on next slide with the shrink example.")

s = stat_slide(prs, "The shrink", "43→6",
    "“Please be advised that in the event that you should have any questions… do not hesitate to reach out to the undersigned at your earliest convenience.” → “Questions? Call me any time.”",
    [("Same meaning. 86% lighter.", "The reader keeps the difference."),
     ("Noun stacks get untangled too:", "“employee parking permit application process revision” → “revising how employees apply for parking permits.”"),
     ("The classic rule:", "“Omit needless words” — not all sentences short, but every word telling (Strunk & White)."),
    ], D, nxt())
notes(s, "Zinsser: clutter is the disease of American writing.")

s = section_slide(prs, "03", "Clarity",
    "Concrete beats abstract — let the reader verify, not trust.", D, nxt())
notes(s, "Section 3.")

s = flow_slide(prs, "The abstraction ladder — climb down", [
    ("“Improved performance”", "Abstract: believe me."),
    ("“Faster support responses”", "Directional: trust me."),
    ("“9 hrs → 2.1 hrs in the 90-day pilot”", "Concrete: CHECK me."),
], D, nxt(), note_text="Every “significant,” “substantial,” and “streamlined” is a rung begging for the number beneath it. No number exists? The abstraction was hiding that too.")
notes(s, "Concrete claims survive forwarding to the expert scrutinizer.")

s = section_slide(prs, "04", "Proofreading",
    "The hunt for what software cannot see.", D, nxt())
notes(s, "Section 4.")

s = icon_rows_slide(prs, "What spellcheck reliably misses", [
    ("👻", "Real words, wrong place", "manger/manager · form/from · pubic/public — correctly spelled, catastrophically placed."),
    ("🔊", "Homophones", "their/there · its/it's · affect/effect — grammatically invisible to most tools."),
    ("🎯", "Names & numbers", "Katherine vs. Kathryn · $45,000 vs. $450,000 · March 12 vs. 21 — highest stakes, weakest tooling."),
    ("⚠", "Grammar ghosts", "Subject–verb slips, dangling modifiers, and the missing word you read as present."),
], D, nxt())
notes(s, "Proofreading exists because software cannot read.")

s = icon_rows_slide(prs, "Four routines that actually work", [
    ("🗣", "Read it ALOUD", "Ears catch what eyes forgive — the single highest-yield technique available."),
    ("1", "One error type per sweep", "A numbers-only pass, a names-only pass, an its/it's pass. Searching beats reading."),
    ("👕", "Change the costume", "Print it, or change the font — unfamiliarity resets the blindness."),
    ("☑", "The last-thing check", "Subject line · recipient list · attachment. Three seconds against the classic disasters."),
], D, nxt())
notes(s, "Each routine attacks the brain's prediction habit a different way.")

s = bullets_slide(prs, "Verify — don't read — the high-stakes categories", [
    ("Names:", "check against the person's own signature block, never against memory. A misspelled name is a personal insult in writing."),
    ("Numbers:", "check every figure against its source. A transposed digit in a price is a contractual event."),
    ("Dates:", "“4 March 2026” — a format no country misreads. 3/4/26 is two different meetings on two continents."),
    ("Files:", "name attachments for the recipient: “Okafor-CoverLetter-May2026.docx” cannot be confused with a competitor's."),
], D, nxt())
notes(s, "Reading is how the error survived. Verification replaces it.")

s = bullets_slide(prs, "Case: the $5 million missing comma", [
    ("Maine's overtime law exempted", "“…storing, packing for shipment or distribution of” perishable foods — no comma after “shipment.”"),
    ("Delivery drivers argued", "“packing for shipment or distribution” was ONE activity — packing — which they didn't do."),
    ("The court agreed the sentence was ambiguous.", "Oakhurst Dairy settled for $5 million (O'Connor v. Oakhurst Dairy, 2017)."),
    ("The lessons:", "the serial comma is free insurance · ambiguity transfers money · a numbered vertical list would have made the ambiguity impossible."),
], D, nxt())
notes(s, "Real case, real money. Punctuation is load-bearing syntax.")

s = bullets_slide(prs, "Case: the reply-all résumé", [
    ("The cover letter was perfect —", "three drafts, two reviewers, flawless prose."),
    ("What went out:", "“Dear Ms. Hartman” to a recruiter named Okafor · subject line “appliaction materials” · attachment missing · follow-up attached the WRONG FIRM'S letter."),
    ("What was never proofread:", "everything typed last and everything outside the prose — exactly where the last-thing check lives."),
    ("The meta-lesson:", "quality is judged at the weakest point of the transmission, not the average of the paragraphs."),
], D, nxt())
notes(s, "Perfect paragraphs cannot rescue a wrong name.")

s = two_col_slide(prs, "Ten-second repairs you'll use forever",
    "Before", [
        "“I am writing to inform you that there has been a change in the schedule…”",
        "“The committee reached a final conclusion that the systems should be merged together.”",
        "“Sales showed significant improvement.”",
        "“Its important the team knows there going to get they're bonuses.”",
    ],
    "After", [
        "“The meeting moved to 3:00.”",
        "“The committee decided to merge the systems.”",
        "“Sales rose 12% in Q2.”",
        "“It's important the team knows they're going to get their bonuses.” — spellcheck passed the original",
    ], D, nxt())
notes(s, "From the study guide's ten-repair workshop — full set with answers there.")

s = bullets_slide(prs, "Tools are pass zero — not the walkthrough", [
    ("Run them — they're free quality.", "Grammarly, Word's editor, and AI review catch more than ever."),
    ("They still miss verification errors entirely:", "wrong names, wrong numbers, wrong files, wrong recipients."),
    ("They cannot judge structure or emphasis", "— whether the main point is findable is invisible to a grammar engine."),
    ("The standard stays yours:", "your name is on it (Chapter 15's rule). Automated passes are smoke detectors, not judges."),
], D, nxt())
notes(s, "Division of labor between writer and tools.")

s = section_slide(prs, "05", "The tone pass",
    "Correct isn't the same as right. Read once more for how it sounds.", D, nxt())
notes(s, "Section 5: tone as a revision altitude. A message can be structurally sound, concise, and error-free — and still land wrong.")

s = bullets_slide(prs, "Tone: the pass most writers never run", [
    ("Read it as the recipient.", "Not 'is this what I meant?' but 'how does this feel arriving in MY inbox on a bad day?'"),
    ("Hunt the accidental accusations.", "'You failed to include the form' → 'The form wasn't attached — could you resend it?' Same fact, no finger."),
    ("Check the temperature of imperatives.", "'Send me the report' reads colder in text than it sounded in your head. Please is free."),
    ("Confidence without arrogance.", "'I believe this might possibly work' undersells; 'obviously this is the answer' overplays. State it plainly and stand behind it."),
    ("The forward test.", "Would this sentence embarrass you if forwarded to the person it's about? Then it's not done."),
], D, nxt())
notes(s, "Tone errors are invisible to every tool and most writers — they require deliberately switching seats. The forward test catches the sentences people regret most.")

s = two_col_slide(prs, "Bias-free language: precision, not politics",
    "The patterns to catch", [
        "Gendered job titles: chairman, salesman, manpower",
        "Unnecessary demographic tags: 'the female engineer'",
        "Age assumptions: 'young and energetic team'",
        "Disability phrasing that leads with the condition",
    ],
    "The repairs", [
        "Chair, sales rep, staffing — the neutral term is usually shorter",
        "Mention demographics only when relevant to the point",
        "Describe the behavior, not the birth year",
        "Person-first or identity-first per the person's own preference; when unknown, person-first",
    ], D, nxt())
notes(s, "Frame: bias-free language is a precision skill — the biased version usually states something the writer didn't mean to claim. Shorter and more accurate, not censored.")

s = bullets_slide(prs, "Reviewing someone else's draft", [
    ("Comment on the work, never the writer.", "'This paragraph buries the request' — not 'you always bury your requests.'"),
    ("Triage your comments.", "One structural issue outweighs nine comma notes. Lead with what matters; don't drown the writer in trivia."),
    ("Suggest, don't seize.", "Rewriting their document in your voice teaches nothing and breeds resentment. Mark the problem; let them solve it."),
    ("Say what works.", "'Keep this opening — it's exactly right' is information too. All-negative reviews get ignored as noise."),
], D, nxt())
notes(s, "Peer review etiquette. The reviewer's job is to make the document better AND keep the writer improving — both, not either.")

s = bullets_slide(prs, "Receiving edits without bleeding", [
    ("The document is not you.", "Detach on purpose: every mark is a reader telling you where they stumbled — free intelligence, painfully delivered."),
    ("Stumbles are data, wording is negotiable.", "If a reviewer misread the sentence, the sentence is guilty. You don't have to accept their fix — you do have to fix the stumble."),
    ("Ask the clarifying question.", "'What did you expect this section to say?' turns a vague 'this is confusing' into an actionable repair."),
    ("Thank the harsh reviewer.", "The colleague who marks everything is doing what your future readers would have done silently."),
], D, nxt())
notes(s, "The professional skill is separating identity from output. Writers who can't be edited stop being given important documents to write.")

s = section_slide(prs, "06", "Revision under pressure",
    "No time for three passes? There's still a system for five minutes.", D, nxt())
notes(s, "Section 6: deadline triage. The full system when there's time; the ranked shortlist when there isn't.")

s = icon_rows_slide(prs, "The five-minute triage (in strict order)", [
    ("1", "The last-thing check", "Recipients · subject line · attachment. Twenty seconds against the classic catastrophes."),
    ("2", "Names and numbers", "Verify every one against its source — highest damage per error, fastest to check."),
    ("3", "The first sentence", "Is the main point there? A buried lead fails even with perfect grammar."),
    ("4", "Read the riskiest paragraph aloud", "The one with the bad news, the money, or the ask — ears on the highest-stakes prose only."),
    ("5", "One flab sweep of the opening", "Readers judge in the first three lines; trim those hardest."),
], D, nxt(), kicker="When time is short, spend it where errors cost most — not evenly.")
notes(s, "Triage logic: allocate scarce proofreading minutes by expected damage, not by document order. The last-thing check is first because those errors are both common and unrecoverable.")

s = bullets_slide(prs, "AI as a revision assistant — the right prompts", [
    ("Ask for critique, not rewrites.", "'List the three biggest clarity problems' keeps you the writer; 'rewrite this' makes you the typist of someone else's voice."),
    ("Ask targeted passes.", "'Check subject-verb agreement only' · 'flag every abstract claim that lacks a number' — the tool is excellent at single-error sweeps."),
    ("Verify its catches.", "AI flags phantom errors confidently; accept or reject each one deliberately, exactly as with a human reviewer."),
    ("Never paste what can't leak.", "Names, salaries, unreleased numbers — confidentiality rules apply to AI tools like any external service."),
    ("Your name ships on it.", "The judgment layer — tone, stakes, structure — stays yours (Chapter 15's rule)."),
], D, nxt())
notes(s, "AI is the best pass-zero tool yet built and still misses the verification errors entirely. Treat it as a tireless junior reviewer, not a sign-off authority.")

s = bullets_slide(prs, "Case: the apology that needed one more pass", [
    ("The draft was accurate:", "'We regret any inconvenience that may have been experienced as a result of the billing discrepancy.'"),
    ("Every word defensible. Every word wrong.", "Passive, conditional, abstract — 'may have been experienced' implies the customer might be imagining it."),
    ("The tone-pass rewrite:", "'We billed you twice, and that's our error. The refund is processing today, and here's what we changed so it can't recur.'"),
    ("The lesson:", "the six flab targets and the passive-as-camouflage habit aren't just style issues — under pressure, they read as evasion."),
], D, nxt())
notes(s, "Ties conciseness, active voice, and concreteness to tone. The rewrite is shorter, riskier-feeling to write, and completely disarming to receive — Chapter 7 develops this fully.")

s = takeaways_slide(prs, [
    "Three passes at three altitudes: structure, sentences, proof — never one anxious reread.",
    "Cool the draft; distance converts the writer back into a reader.",
    "Cut the six flab targets on sight; omit needless words.",
    "Climb down the abstraction ladder until claims are checkable.",
    "Verify names, numbers, and dates against sources — spellcheck cannot see the high-stakes errors.",
    "The last-thing check (subject · recipients · attachment) prevents what perfect prose cannot.",
], D, nxt(), site_note="Practice now: course site → Chapter 4 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Errors are the one writing flaw every reader can see. Revision is how professionals make sure the flaw they show the world is never that one.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Which flab target is your signature? Bring three examples from your own writing, repaired.",
    "Where can a cooling period realistically live in your workflow — and for which documents is it non-negotiable?",
    "Find a public sentence whose ambiguity could cost money. Rewrite it so no second reading exists.",
    "Automated tools pass all ten workshop sentences. What does that say about you versus your tools?",
    "Defend or attack: the serial comma should be mandatory in business writing.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 4 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 4 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Read:", "The Chapter 4 Study Guide — the ten-repair workshop and the full Oakhurst analysis."),
    ("Do:", "Build your five-item pre-send checklist and use it on everything with stakes this week."),
    ("Coming next:", "Unit 3 begins — Chapter 5: short workplace messages and digital media, where all four foundation chapters meet the inbox."),
], D, nxt())
notes(s, "Delivery-neutral closing. Unit 2 complete.")

out = os.path.join(os.path.dirname(__file__), "..", "ch04-revising-business-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
