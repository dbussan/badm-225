# Chapter 3 — Organizing and Drafting Business Messages (33 slides, original, delivery-neutral)
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

s = takeaways_slide(prs, [
    "One decision first: direct for receptive readers, indirect for resistance and bad news.",
    "Outline in three moves — dump, group into named families, sequence — and cut the orphans.",
    "Paragraphs: one claim, topic sentence first, echoes carrying old-to-new flow.",
    "The stress position at the sentence's end is your emphasis dial (Gopen & Swan, 1990).",
    "Active by default; passive on purpose; never as camouflage. Keep series parallel; chunk for 7±2.",
    "Draft fast, judge later — generating and judging are different jobs.",
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
