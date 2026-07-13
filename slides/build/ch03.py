# Chapter 3 — Organizing and Drafting Business Messages (34 slides, original, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 3"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Organizing and Drafting Business Messages",
    "Direct vs. indirect strategy · outlines that think · paragraphs that hold · sentences that carry weight", D)
notes(s, "Chapter 3: building the message the plan decided on. Companion study guide has the full treatment.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Choose", "direct or indirect strategy based on the reader's likely reaction — and defend the choice."),
    ("Outline", "any message in three steps: dump, group into named families, sequence."),
    ("Build", "paragraphs with one claim each, opened by a topic sentence, held together by echoes."),
    ("Control", "emphasis with the stress position, sentence rhythm, and active voice."),
    ("Repair", "nominalizations, broken parallelism, and walls of unchunked text."),
], D, nxt())
notes(s, "Objectives map to the site's Chapter 3 bank.")

s = section_slide(prs, "01", "The organizing decision",
    "Main point first — or reasons first? The reader's reaction decides.", D, nxt())
notes(s, "Section 1.")

s = two_col_slide(prs, "The two master patterns",
    "DIRECT — receptive/neutral readers", [
        "Main point in sentence one",
        "Details and reasons after",
        "Goodwill close",
        ("Why:", "respects scanning, survives forwarding, reads as confidence"),
    ],
    "INDIRECT — resistance or bad news", [
        "Buffer of honest context first",
        "Reasons BEFORE the conclusion",
        "Main point arrives pre-justified, then pivot forward",
        ("Why:", "a blunt opening slams minds shut before reasons get a hearing"),
    ], D, nxt())
notes(s, "One input decides: how will the reader feel? Chapters 7-8 develop the indirect arts.")

s = bullets_slide(prs, "Two abuses of the strategy choice", [
    ("Indirect as fog.", "Burying a routine request under three paragraphs of preamble isn't diplomacy — it's hiding."),
    ("Direct as bluntness.", "“Your project is cancelled, details below” is a wound with a bibliography."),
    ("The rule:", "strategy follows the reader's stakes — not the writer's nerves, not the writer's impatience."),
    ("Most business messages, most days:", "direct."),
], D, nxt())
notes(s, "Guard rails for the decision.")

s = section_slide(prs, "02", "Outlines",
    "The cheapest place to discover your message doesn't hold together.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "Outlining in three moves", [
    ("DUMP", "Scratch-list every point you might make. No order, no judging."),
    ("GROUP", "Three-ish families, each with a NAME — the names become your headings."),
    ("SEQUENCE", "Direct or indirect, per the strategy call. Cut what serves no family."),
], D, nxt(), note_text="Working memory holds about 7±2 chunks (Miller, 1956) — and tired readers on phones hold fewer. Three main points is a classic for a reason.")
notes(s, "The unity test applies to outlines too: every branch serves the box above it.")

s = section_slide(prs, "03", "Paragraphs",
    "One claim, stated first, held together.", D, nxt())
notes(s, "Section 3.")

s = icon_rows_slide(prs, "Paragraph anatomy", [
    ("◎", "Topic sentence", "The paragraph's one claim, stated first. Everything after works for it."),
    ("▤", "Unity", "One claim per paragraph — the wandering sentence supports some other claim and should live there."),
    ("⛓", "Coherence", "Transitions (however, therefore) plus echoed key words tie sentences together."),
    ("¶", "Brevity", "On screens, 4–6 lines is a paragraph; 8 is a wall. White space is the reader's handhold."),
], D, nxt())
notes(s, "Topic sentences come straight from the outline's family names.")

s = bullets_slide(prs, "Old before new: the flow readers expect", [
    ("Topic position (sentence opening):", "familiar information — the thing we're already discussing."),
    ("Stress position (sentence end):", "the news, the emphasis — what the reader carries away (Gopen & Swan, 1990)."),
    ("Use the dial:", "“The committee rejected the proposal” stresses the proposal; “…rejected by the FULL committee” stresses who."),
    ("Echo transitions:", "repeat the last stress in the next topic — “…raises the question of cost. That cost has three parts.”"),
], D, nxt())
notes(s, "Prose honoring old→new feels lucid without the reader knowing why.")

s = section_slide(prs, "04", "Sentences",
    "Voice, rhythm, parallelism, chunks.", D, nxt())
notes(s, "Section 4.")

s = two_col_slide(prs, "Active by default, passive on purpose",
    "ACTIVE — the default", [
        "“Maria approved the budget.”",
        "Actor visible, shorter, faster to decode",
        "Honest about who did what",
    ],
    "PASSIVE — the tool", [
        "Actor unknown: “damaged in transit”",
        "Actor obvious/irrelevant: “stored at −80 °C”",
        "Diplomatic focus on the act, not the person",
        ("NEVER:", "“Mistakes were made” — accountability camouflage"),
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "When the reader needs the actor, name the actor.")

s = bullets_slide(prs, "Rhythm, parallelism, and chunks", [
    ("Vary sentence length.", "Fifteen 20-word sentences read like a metronome. After long ones, a short sentence lands like a verdict. It works."),
    ("Parallelism:", "same job, same form. “Safety procedures, report filing, client communication” — one clean series."),
    ("Chunk for working memory:", "fourteen items in a paragraph is a memory test; three labeled lists of 4–5 is a document (Miller, 1956)."),
    ("Unfreeze nominalizations:", "“make a decision about the implementation of” = “decide to implement” wearing three coats."),
], D, nxt())
notes(s, "The four highest-frequency sentence repairs in business prose.")

s = icon_rows_slide(prs, "The emphasis toolbox (in order of power)", [
    ("1", "Position", "First sentence of the message; end of the sentence; first line after a heading."),
    ("2", "Isolation", "A one-sentence paragraph. Once = spotlight; often = confetti."),
    ("3", "The short sentence", "After long ones — the verdict effect."),
    ("4", "Labeled structure", "Headings and bolded lead-ins (“Deadline:”) that scanning can't miss."),
    ("✗", "What doesn't work", "Exclamation points, “very/really,” bold paragraphs, ALL CAPS — inflation that devalues the currency."),
], D, nxt())
notes(s, "Everything can't be important, or nothing is.")

s = section_slide(prs, "05", "Drafting",
    "Permission to write badly — briefly, and on purpose.", D, nxt())
notes(s, "Section 5.")

s = bullets_slide(prs, "Drafting habits that actually help", [
    ("Write the easy section first.", "Momentum transfers; openings are easier once the middle exists."),
    ("Topic sentences come from the outline.", "The family names you wrote ARE the paragraph openers."),
    ("When wording fights back:", "type the clumsy version, mark [FIX], keep moving. Revision is a separate appointment."),
    ("Park mid-thought.", "Never stop at a section's end — tomorrow's re-entry will thank you."),
    ("Draft without editing; edit without drafting.", "Two jobs, two sittings. Doing both at once stalls both."),
], D, nxt())
notes(s, "The judging phase is Chapter 4.")

s = bullets_slide(prs, "Headings: the skeleton that skims", [
    ("Informative beats categorical.", "“Cost: TechServe saves $22K/year” outworks “Cost Analysis.”"),
    ("The headings-only test:", "read just your headings. Do they tell the story? A skimmer will read exactly that."),
    ("Two levels serve almost everything.", "Four levels is a filing system, not a message."),
    ("Headings discipline the writer too:", "a section you can't summarize honestly in its heading is two sections — or none."),
], D, nxt())
notes(s, "The outline, left visible for the reader.")

s = bullets_slide(prs, "Case: the buried recommendation", [
    ("Two weeks of analysis,", "organized as the chronology of the work: history → criteria → four alternatives → and in the last paragraph, the recommendation."),
    ("The VP read paragraph one,", "filed it 'for later,' and asked a colleague whether the evaluation ever reached a conclusion."),
    ("The repair:", "“I recommend renewing with TechServe on renegotiated terms — saving $22,000/year. Comparison below.”"),
    ("The lesson:", "organize by the reader's decision, never by the archaeology of your effort. Show the work in a skippable, labeled body."),
], D, nxt())
notes(s, "Excellent analysis, invisible conclusion — the most common structural heartbreak in business.")

s = bullets_slide(prs, "Case: the incident report that named no one", [
    ("“The containment was found to have been compromised.", "The transfer was performed without the checklist having been completed. Corrective measures have been identified.”"),
    ("Grammatical. Useless.", "Who transferred? Who found it? Who owns the fix, by when?"),
    ("Active rewrite:", "“The on-duty technician skipped the pre-transfer checklist… The lab manager will retrain all transfer-qualified staff by March 14.”"),
    ("The stakes:", "organizations learn from incidents only when reports carry actors, causes, and owners. Grammar is a safety system."),
], D, nxt())
notes(s, "Passive-as-camouflage in its natural habitat. Ties to Chapter 1's upward-communication filter.")

s = flow_slide(prs, "From outline to draft: the 20-minute pipeline", [
    ("Plan (2 min)", "Purpose template + reader profile — Chapter 2's work"),
    ("Dump (4 min)", "Fifteen scratch points, no judging"),
    ("Group (3 min)", "Three named families; orphans die"),
    ("Sequence (1 min)", "Direct for the neutral reader"),
    ("Sprint (10 min)", "Topic sentences from family names; [FIX] marks; done"),
], D, nxt(), note_text="The hard intellectual work — deciding, grouping, sequencing — finishes before the prose pressure starts.")
notes(s, "Walkthrough matches the study guide's worked memo.")

s = bullets_slide(prs, "Measuring readability (and its limits)", [
    ("Word will score your prose:", "File → Options → Proofing → “Show readability statistics.”"),
    ("Flesch Reading Ease ~50–70", "and grade level ~9–12 fit most business prose (Flesch, 1949)."),
    ("The formulas see only", "sentence length and syllables — they can't detect a buried lead or a broken parallel."),
    ("Use them as a smoke detector, not a judge.", "Grade 16 on a customer email is an alarm; grade 9 certifies nothing."),
], D, nxt())
notes(s, "Automated metrics as sanity check; human structure judgment remains the skill.")

s = section_slide(prs, "06", "Structure the eye can see",
    "Lists, tables, transitions — and the way screens are actually read.", D, nxt())
notes(s, "Section 6: visible structure. The outline made the logic; this section makes the logic visible at scanning speed.")

s = stat_slide(prs, "How screens are actually read", "F",
    "Eye-tracking research shows readers scan web pages and email in an F-shape: across the top, a shorter sweep lower down, then straight down the left edge (Nielsen Norman Group).",
    [("The top line gets read.", "Your first sentence is the only sentence you can count on — which is why the direct pattern wins on screens."),
     ("The left edge gets scanned.", "Paragraph openers, bolded lead-ins, and list items live on the scan path; mid-sentence content does not."),
     ("Design for the F:", "front-load sentences, front-load paragraphs, and put keywords where the eye actually travels."),
    ], D, nxt())
notes(s, "The F-pattern is why the topic-sentence rule and bolded lead-ins are not decoration — they sit exactly where attention goes. Everything off the F-path is optional reading.")

s = two_col_slide(prs, "Bullets or numbers? Each has a job",
    "BULLETED list — unordered", [
        "Items are parallel and interchangeable in order",
        "Options, features, criteria, examples",
        "Signals: 'these belong together; sequence doesn't matter'",
        ("Limit:", "4–8 items; past that, group into labeled sub-lists"),
    ],
    "NUMBERED list — ordered", [
        "Sequence, ranking, or priority is the point",
        "Steps, instructions, ranked recommendations",
        "Numbers let readers reference: 'see item 3'",
        ("Rule:", "never number a list whose order is arbitrary — numbers promise meaning"),
    ], D, nxt())
notes(s, "The choice broadcasts a claim about the content. A numbered list of unranked options invites the question 'why is this one first?'")

s = bullets_slide(prs, "List discipline: what separates a list from a fragment pile", [
    ("Lead-in sentence.", "Every list needs a sentence that tells the reader what the items are: 'The proposal has three risks:'"),
    ("Parallel form.", "All items start the same part of speech — all verbs, all nouns. One broken item breaks the rhythm of all of them."),
    ("Comparable weight.", "A six-word item next to a sixty-word item signals the list wasn't designed — split or trim."),
    ("One level, maybe two.", "Nested bullet forests three levels deep are outlines that never got written into prose. Flatten or restructure."),
    ("Punctuate consistently.", "Fragments: no periods. Full sentences: periods. Never a mix within one list."),
], D, nxt())
notes(s, "Lists get skimmed precisely because readers trust their structure — sloppy lists spend that trust. Parallelism review from Section 4 applies item-by-item.")

s = two_col_slide(prs, "When a table beats prose",
    "Use a TABLE when readers need to…", [
        "Compare options across the same dimensions",
        "Look up exact values (prices, dates, specs)",
        "Check completeness — every cell visibly filled or empty",
        ("Test:", "if you're writing 'X is $40, while Y is $55, whereas Z…' — that sentence wants to be a table"),
    ],
    "Keep PROSE when readers need to…", [
        "Follow causation — why something happened",
        "Weigh an argument with qualifications and exceptions",
        "Hear tone: goodwill, apology, persuasion",
        ("Test:", "if every cell would hold a paragraph, the table is a cage, not a tool"),
    ], D, nxt())
notes(s, "Tables are for comparison and lookup; prose is for reasoning and relationship. Chapter 9 develops data displays fully — this is the drafting-level decision.")

s = icon_rows_slide(prs, "Transitions: the traffic signals of prose", [
    ("＋", "Addition", "also · moreover · in addition — 'more of the same direction ahead.'"),
    ("↔", "Contrast", "however · yet · on the other hand — 'turn coming; slow down.'"),
    ("∴", "Cause & consequence", "therefore · as a result · consequently — 'this follows from that.'"),
    ("№", "Sequence", "first · next · finally — 'you are here' markers in a process."),
    ("◉", "Example & proof", "for instance · specifically · in particular — 'the claim is about to get concrete.'"),
], D, nxt(), kicker="Readers decode transitions before they decode the sentence — a wrong signal misroutes the whole paragraph.")
notes(s, "Transitions are promises. 'However' followed by agreement is a broken promise, and readers feel it even when they can't name it. Echoed key words (old-to-new) do the same work invisibly.")

s = bullets_slide(prs, "Openings that earn the reader's next ten seconds", [
    ("The subject line is sentence zero.", "'Budget approval needed by Friday' outworks 'Question' — the decision to open, defer, or delete is made right there."),
    ("Direct messages: main point, sentence one.", "Request, recommendation, or news — before any background."),
    ("One sentence of context is a courtesy;", "three paragraphs of context is a hostage situation."),
    ("Never open with the archaeology:", "'I was reviewing the files from last quarter and noticed…' — start with what you found, not the story of finding it."),
], D, nxt())
notes(s, "Openings are where the buried-recommendation failure begins. The reader's first question is always 'what is this and what do you need from me?' — answer it immediately.")

s = bullets_slide(prs, "Closings that move the work forward", [
    ("Action, owner, date.", "'Please send the revised figures to me by Thursday, March 12' — every request needs all three or it isn't a request, it's a wish."),
    ("Make the next step frictionless.", "Attach the form, link the calendar, include the number — every step you remove doubles the odds of action."),
    ("End with goodwill that is specific.", "'Thanks for turning this around during inventory week' beats the upholstery of 'Thanks in advance!'"),
    ("Don't reopen the case in the closing.", "New arguments in the last paragraph un-decide everything above them."),
], D, nxt())
notes(s, "Closings are the stress position of the whole message — what sits there is what gets remembered and acted on. Deadlines without dates are decorations.")

s = bullets_slide(prs, "Case: the email that became a table", [
    ("Before:", "Nine sentences comparing three vendors' prices, support hours, and contract terms — every fact true, no fact findable twice."),
    ("The reply:", "'Can you summarize the differences?' — the writer had summarized them. In prose. That was the problem."),
    ("After:", "A three-column table (vendor × price, support, term) plus TWO sentences of prose: the recommendation and the reason."),
    ("The lesson:", "prose carries the argument; the table carries the facts. When you make readers hold six numbers in working memory, they hold none (Miller, 1956)."),
], D, nxt())
notes(s, "Common real-world repair: the writer did the analysis and hid it in paragraph form. The rewrite splits the jobs — table for lookup, sentences for judgment.")

s = takeaways_slide(prs, [
    "One decision first: direct for receptive readers, indirect for resistance and bad news.",
    "Outline in three moves — dump, group into named families, sequence — and cut the orphans.",
    "Paragraphs: one claim, topic sentence first, echoes carrying old-to-new flow.",
    "The stress position at the sentence's end is your emphasis dial (Gopen & Swan, 1990).",
    "Active by default; passive on purpose; never as camouflage. Keep series parallel; chunk for 7±2.",
    "Draft fast, judge later — generating and judging are different jobs.",
    "Design for the F-pattern: front-load sentences and paragraphs; lists and tables where comparison lives.",
], D, nxt(), site_note="Practice now: course site → Chapter 3 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Readers do not remember what you wrote. They remember what they read — and they read the first sentence, the headings, and the ends of things.",
    "this chapter, compressed", D, nxt())
notes(s, "Position is emphasis.")

s = discussion_slide(prs, "Discussion questions", [
    "Find a real message organized by the writer's process instead of the reader's decision. What earns sentence one?",
    "Collect three passives from documents around you: tool or camouflage? Rewrite the camouflage.",
    "Audition every sentence of your last substantial paragraph against its topic sentence. What moves out?",
    "Where is the line between direct and merely abrupt? Give a case from your own inbox.",
    "Run Word's readability statistics on something you wrote. What does the score see — and what does it miss?",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 3 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 3 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Read:", "The Chapter 3 Study Guide — includes the sentence workshop with ten repairs and answers."),
    ("Do:", "Outline your next substantial message with dump-group-sequence before drafting a word."),
    ("Coming next:", "Chapter 4 — revising and proofreading: conciseness, clarity, and catching what spellcheck can't."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch03-organizing-and-drafting.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
