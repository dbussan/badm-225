# Chapter 4 Study Guide — Revising Business Messages
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(4, 'Revising Business Messages',
    'Conciseness, clarity, and proofreading — the judging phase, where good drafts become sendable documents.')

h1(doc, 'How to use this guide')
para(doc, 'Chapters 2 and 3 planned and drafted; this chapter judges. Revision is where professionals '
    'are made, because it is the phase amateurs skip — the draft feels done, the deadline looms, send '
    'gets clicked. Read this guide with something you have written open beside it, apply each pass to '
    'your own prose, and finish with the workshop drills. Then hit the Chapter 4 practice bank on the '
    'course site.')

h1(doc, 'Revision is a system, not a mood')
para(doc, 'The reason “I read it over” fails as a revision method is altitude: structure problems, '
    'sentence problems, and typos live at three different heights, and the eye cannot patrol all three '
    'at once. Hunting typos while questioning your organization guarantees you do both badly. '
    'Professionals separate the altitudes into passes.')
figure(doc, os.path.join(FIG, 'ch4_passes.png'),
    'Figure 1. The three-pass system: structure, then sentences, then proof — never all at once.',
    'Three-pass revision system: pass one checks structure (right strategy, main point findable, sections earning their place); pass two checks sentences (concise, clear, active, parallel, old-to-new flow); pass three proofreads spelling, names, numbers, and dates that spellcheck cannot catch.')
para(doc, 'Pass one rereads the message against Chapters 2 and 3: is the strategy right for this '
    'reader’s reaction? Is the main point where a skimmer will meet it? Does every section serve the '
    'purpose — and does anything serve nothing? Fix structure first, because there is no point '
    'polishing a paragraph that pass one will delete. Pass two is sentence work: conciseness, clarity, '
    'voice, parallelism, flow — the bulk of this chapter. Pass three is proofreading proper: the '
    'mechanical hunt for what spellcheck cannot see. Three passes sound slow; they are faster than one '
    'muddled read repeated four times.')

h1(doc, 'The cooling-off period')
figure(doc, os.path.join(FIG, 'ch4_cooling.png'),
    'Figure 2. The cooling curve: time converts the writer back into a reader.',
    'Curve showing objectivity rising with time since drafting: immediately after finishing, you read what you meant to write; hours later, errors begin to surface; by the next morning you read with a stranger’s eyes.')
para(doc, 'Fresh from drafting, you cannot proofread your own work — not from carelessness, but '
    'because your brain already knows what the text is supposed to say and helpfully shows you that '
    'instead of what is on the page. Researchers who study typos describe exactly this: writers work '
    'from the meaning they intended, so the brain fills gaps and glides over transpositions that leap '
    'out at any stranger (Stafford, quoted in Stockton, 2014). Distance is the antidote. Overnight is '
    'ideal for anything substantial; even twenty minutes and a coffee resets the eyes meaningfully. '
    'Plan the cooling period into deadlines: a document due Friday is drafted Wednesday for exactly '
    'this reason.')

h1(doc, 'Conciseness: respect measured in words')
para(doc, 'Concise writing is not short writing — it is writing with nothing extra. A 40-page report '
    'can be concise; a three-line email can be bloated. The test is whether every word is doing work, '
    'and business prose fails that test in predictable places.')
figure(doc, os.path.join(FIG, 'ch4_targets.png'),
    'Figure 3. The six conciseness targets — where flab reliably hides in business prose.',
    'Six conciseness targets with repairs: long lead-ins to delete; there-is and it-is openers to invert; redundant pairs like each and every to trim; flabby phrases such as due to the fact that becoming because; hedges and intensifiers like very and really to cut; and noun stacks to untangle with verbs.')
bullets(doc, [
    ('Long lead-ins.', '“I am writing this email to let you know that the meeting moved” — the first ten words announce that words are coming. Start where the news starts: “The meeting moved to 3:00.”'),
    ('There is / it is openers.', '“There are three issues that remain” hides the subject. “Three issues remain” promotes it.'),
    ('Redundant pairs and modifiers.', '“Each and every,” “final outcome,” “past history,” “completely finished,” “basic fundamentals” — one word was already doing the job.'),
    ('Flabby phrases.', '“Due to the fact that” = because. “In the event that” = if. “At this point in time” = now. “In order to” = to.'),
    ('Hedges and intensifiers.', '“Very,” “really,” “quite,” “rather” add heat, not light. And nothing is “very unique.”'),
    ('Noun stacks.', '“Employee parking permit application process revision” — five nouns deep, zero verbs. Untangle: “revising how employees apply for parking permits.”'),
])
figure(doc, os.path.join(FIG, 'ch4_shrink.png'),
    'Figure 4. The shrink in action: 43 words of ceremony, six words of meaning.',
    'Before and after example: a 43-word ceremonial closing paragraph — please be advised that in the event you should have any questions do not hesitate to reach out to the undersigned — shrinks to six words: Questions? Call me any time.')
para(doc, 'William Zinsser’s verdict on this entire section has never been improved on: clutter is '
    'the disease of American writing, and the secret of good writing is “to strip every sentence to '
    'its cleanest components” (Zinsser, 2006). Strunk and White compressed it further — “omit '
    'needless words” — and made the crucial point that this requires not that the writer make all '
    'sentences short, but that every word tell (Strunk & White, 2000).')

h1(doc, 'Clarity: concrete beats abstract')
figure(doc, os.path.join(FIG, 'ch4_ladder.png'),
    'Figure 5. The abstraction ladder: climb down until the claim is checkable.',
    'Abstraction ladder with three rungs: “improved performance” is abstract (believe me); “faster support responses” is directional (trust me); “cut response time from nine hours to 2.1 hours in the 90-day pilot” is concrete (check me).')
para(doc, 'Vague prose asks the reader to trust; concrete prose lets the reader verify. “Improved '
    'performance” could mean anything and therefore means nothing; “cut response time from nine '
    'hours to 2.1 in the 90-day pilot” can be believed, challenged, and remembered — and it survives '
    'forwarding to the expert scrutinizer from Chapter 2. In revision, hunt your abstractions: every '
    '“significant,” “substantial,” “improved,” and “streamlined” is a ladder-rung begging for the '
    'number or example beneath it. If no number or example exists, the abstraction was hiding that, '
    'too — which is something you want to discover before your reader does.')
para(doc, 'Clarity revision also finishes Chapter 3’s work: unfreeze remaining nominalizations, '
    'replace jargon with the reader’s vocabulary (semantic noise, Chapter 1), and check that every '
    'pronoun has one unmistakable parent — “Bring the projector and the laptop; it is fragile” '
    'leaves the reader guarding the wrong equipment.', bold_lead='Loose ends.')

h1(doc, 'Proofreading: the hunt for what software cannot see')
figure(doc, os.path.join(FIG, 'ch4_spellcheck.png'),
    'Figure 6. Spellcheck passes all of these. Proofreading exists because software cannot read.',
    'Four categories of errors spellcheck misses: real words in the wrong place such as manger for manager; homophones such as their, there, its, it’s, affect, effect; names and numbers such as Katherine versus Kathryn or $45,000 versus $450,000; and grammar ghosts including subject-verb slips, dangling modifiers, and missing words the writer reads as present.')
para(doc, 'Spellcheck and grammar tools catch misspelled non-words and flag some grammar; they '
    'cheerfully pass “please review the attached from” and “the manger will meet you at 3.” Worse, '
    'the errors that survive to publication cluster exactly where tools are weakest and stakes are '
    'highest: names (misspelling a client’s name is a personal insult delivered in writing), numbers '
    '(a transposed digit in a price is a contractual event), and dates (March 12 versus March 21 is '
    'two missed flights and a cancelled meeting). Proofread these categories by verification, not by '
    'reading: check the name against the signature block of their last email; check every number '
    'against its source.')
figure(doc, os.path.join(FIG, 'ch4_routines.png'),
    'Figure 7. Four proofreading routines that actually work.',
    'Four proofreading routines: read aloud so ears catch missing words and clunky rhythm; sweep for one error type at a time such as a numbers-only pass; change the costume by printing or changing the font to reset familiarity blindness; and the last-thing check of subject line, recipient list, and attachment.')
bullets(doc, [
    ('Read it aloud.', 'Ears catch what eyes forgive: the missing word, the doubled the, the sentence that runs out of breath. Reading aloud is the single highest-yield proofreading technique available.'),
    ('One error type per sweep.', 'A numbers-only pass, then a names-only pass, then an its/it’s pass. Narrow focus catches what broad reading glides over.'),
    ('Change the costume.', 'Print it, or change the font and size. The text looks unfamiliar, and familiarity is exactly the blindness you are fighting.'),
    ('The last-thing check.', 'Before send: subject line says what the message does; the recipient list is who you think it is; the attachment is attached — and is the right file. The classic trio of avoidable disasters.'),
])

h1(doc, 'Deep dive: the structure pass, as a checklist')
para(doc, 'Pass one is the least mechanical and the most valuable, so give it teeth. Ten questions, '
    'asked of the cooled draft, in order:')
numbered(doc, [
    'Reaction check: how will THIS reader feel about the core message — and does the strategy (direct/indirect) match?',
    'Findability: can a skimmer locate the main point in ten seconds? (Test it: skim your own draft with a timer.)',
    'The headings-only test: read only subject line, headings, and bolded text. Does the argument survive?',
    'Purpose audit: does every section serve the purpose statement? Name each section’s job aloud; the section that has no job has no place.',
    'Order audit: is the sequence the reader’s decision-order, or the archaeology of your effort?',
    'Completeness: can the reader act without a follow-up question? (Chapter 6’s complete-ask test, applied to everything.)',
    'The rings: does anything here fail the forwardability test — or need a definition for the secondary reader?',
    'Proportion: does the space each topic gets match its importance to the reader? (A 60/40 page split implies a 60/40 importance split, whether you meant it or not.)',
    'The opening and the closing: does sentence one carry the point, and does the final sentence carry information rather than upholstery?',
    'The one-sentence summary: can you state what this document does in one sentence? If not, neither will anyone else — return to Chapter 2 before touching a comma.',
])
para(doc, 'Structural repairs are demolition, and demolition before decoration is the whole economy '
    'of the three-pass system: five minutes moving a section saves thirty minutes polishing '
    'sentences that were never going to survive.', bold_lead='Why first.')

h1(doc, 'Deep dive: the conciseness pass, performed live')
para(doc, 'Watch pass two run on a real paragraph. The patient, 96 words: “It should be noted that '
    'in the course of conducting our review of the vendor proposals that were submitted, it became '
    'apparent to the members of the team that there are three primary areas of concern that will '
    'need to be addressed prior to the making of a final decision. These areas of concern are in '
    'regard to the matter of pricing structure, the question of implementation timeline, and issues '
    'pertaining to the ongoing provision of technical support going forward into the future.”')
para(doc, 'The surgery, cut by cut: “It should be noted that” — throat-clearing, deleted. “In the '
    'course of conducting our review of” — one verb hiding in eight words: “reviewing.” “That were '
    'submitted” — which other proposals would we review? Deleted. “It became apparent to the '
    'members of the team that” — the team noticed; say so, or say nothing. “There are three primary '
    'areas of concern that will need to be addressed” — there-is opener plus passive plus '
    'nominalization: “three concerns must be resolved.” “Prior to the making of a final decision” '
    '— “before we decide.” The list: “in regard to the matter of,” “the question of,” “issues '
    'pertaining to” — three different flab wrappers on three parallel items; strip all three. '
    '“Going forward into the future” — as opposed to backward into it? Deleted.')
para(doc, 'The survivor, 22 words: “Our review of the vendor proposals surfaced three concerns to '
    'resolve before deciding: pricing structure, implementation timeline, and ongoing technical '
    'support.” Seventy-seven percent lighter, one hundred percent of the meaning, and — notice — '
    'MORE authoritative, not less: flab reads as evasion, and its removal reads as command. Run this '
    'surgery on one of your own paragraphs and keep the before/after; nothing teaches the '
    'conciseness pass faster than watching your own 96 become your own 22.', bold_lead='The result.')

h1(doc, 'Deep dive: precision — the confusables that survive every pass')
para(doc, 'Some errors are not flab or structure but wrong words wearing right-word costumes. '
    'Spellcheck passes them; casual proofreading passes them; only knowledge catches them. The '
    'business-critical set:')
bullets(doc, [
    ('Affect / effect.', 'Affect is (almost always) the verb — the delay affects delivery; effect the noun — the effect on delivery. (The rare inversions — “to effect change,” “flat affect” — are why memorizing the common case beats guessing.)'),
    ('Ensure / insure / assure.', 'You ensure outcomes (make certain), insure property (buy a policy), and assure people (give confidence). “We assure quality” promises a feeling; “we ensure quality” promises a process.'),
    ('Fewer / less.', 'Fewer counts (fewer errors, fewer meetings); less measures (less time, less risk). “Less errors” costs credibility with exactly the readers who matter.'),
    ('i.e. / e.g.', 'i.e. = “that is” (restates); e.g. = “for example” (samples). Mixing them changes meaning: “senior staff, i.e., directors” means ONLY directors; “e.g., directors” means directors among others.'),
    ('Principal / principle.', 'Principal is the main thing (the principal risk, the loan principal); principle is the rule (a matter of principle). “Our principle concern” is a spelling error dressed as ethics.'),
    ('Discreet / discrete.', 'Discreet keeps secrets; discrete keeps separateness (discrete steps, discrete variables). Lab and data writing lean on the second; HR writing on the first.'),
    ('Compliment / complement.', 'Compliments flatter; complements complete. “The software compliments our workflow” means it says nice things about it.'),
    ('That / which.', 'That restricts (the report that Legal reviewed — that one, not others); which adds, after a comma (the report, which Legal reviewed, ships Friday). Choosing wrong quietly changes which report you mean — the Oakhurst lesson at word scale.'),
])
para(doc, 'Build your personal confusables list from your own history: whatever pair YOU have '
    'confused is worth a dedicated sweep on high-stakes documents. Two minutes of Ctrl+F on “affect” '
    'and “effect” costs less than one wrong one in a client deliverable.', bold_lead='Personalize it.')

h1(doc, 'Deep dive: the numbers audit')
para(doc, 'Business and technical prose runs on numbers, and numbers have their own error physics — '
    'they are high-stakes, spellcheck-invisible, and psychologically trusted (a wrong number reads '
    'as MORE authoritative than a vague word). The audit disciplines: verify every figure against '
    'its source document, never against memory or an earlier draft — transcription is where digits '
    'transpose. Check units ride with their numbers: “the tolerance is 0.5” invites catastrophe; '
    '0.5 what? Check consistency across the document: the $45,200 in your summary must match the '
    '$45,200 in your table (readers who find one mismatch stop trusting every number, a bankruptcy '
    'from one bounced check). Match precision to knowledge: “approximately $45,000” and “$45,187” '
    'are both honest; “$45,187.23” projected three years out is false precision that invites '
    'ridicule — significant digits are a claim about certainty, in business exactly as in the lab. '
    'And re-run every calculation someone else will check, because someone else will: the '
    'percentage that doesn’t match its own numerator and denominator is the most-caught error in '
    'business documents. For any document where numbers carry the decision, give them their own '
    'dedicated sweep — numbers-only, source documents open.')

h1(doc, 'Deep dive: revising with AI — the pass-zero protocol')
para(doc, 'Modern editing tools (Word’s Editor, Grammarly, AI assistants) have earned a place in the '
    'system — as pass zero, run before your three passes, never instead of them. The protocol: '
    'accept their mechanical catches gratefully (doubled words, agreement slips, missing commas '
    'cost nothing to fix); treat their style suggestions as questions, not commands — “consider '
    'shortening” is sometimes right and sometimes flattening your deliberate emphasis (the tool '
    'cannot know your stress-position choice from Chapter 3 was a choice); and give an AI assistant '
    'a real revision brief rather than “make this better”: “tighten this to 150 words for an '
    'executive skimmer, keep the Friday deadline prominent, don’t change any figures” produces '
    'editing; “improve this” produces homogenization.')
para(doc, 'Know the boundary layer precisely. Tools cannot run pass one (they cannot know your '
    'reader, your strategy, or whether the document does its job); they cannot run the verification '
    'parts of pass three (names, numbers, dates, attachments, recipients — the highest-stakes '
    'categories are exactly the ones no tool can check against reality); and they will confidently '
    '“correct” domain language into wrongness (a chemistry term, a legal term of art, your '
    'client’s preferred spelling of their own product). The division of labor, stated once: tools '
    'patrol the mechanics, you patrol the meaning, and your name patrols the consequences '
    '(Chapter 15’s ownership rule, at revision scale).', bold_lead='The boundary.')

h1(doc, 'Deep dive: revising other people’s writing')
para(doc, 'You will spend as much career time reviewing others’ drafts as revising your own, and '
    'review is a communication genre with its own failure modes. The craft:')
bullets(doc, [
    ('Declare your altitude.', 'Tell the writer which pass you ran: “structural comments only — I haven’t proofed” sets expectations and permits usefully incomplete reviews. The reviewer who mixes a comma catch into a structure question buries the structure question.'),
    ('Diagnose, don’t just prescribe.', '“This paragraph has two claims” teaches; silently splitting it merely fixes. On teams, teaching compounds — you are revising the writer, not only the draft.'),
    ('Question-form for judgment calls, direct-form for errors.', '“Would the CFO version lead with the number?” respects ownership where taste governs; “this figure doesn’t match the table” is not a question. (Chapter 16’s ask-versus-order, applied to margins.)'),
    ('Praise specifically, and first.', '“The risk section’s ordering is exactly right” is information, not decoration — it tells the writer what to protect through the next revision. Reviews that are only defect lists teach writers to hide drafts.'),
    ('Respect the writer’s voice.', 'Rewrite sentences only when broken, not when merely unlike yours. The review goal is THEIR strongest document, not your document with their name on it.'),
])
para(doc, 'And when you are the one reviewed: hunt the pattern, not the instances. Twelve comma '
    'comments are one lesson about commas; ask your reviewer for the pattern (“what’s the theme?”) '
    'and bank it in your personal error list — the compounding asset that makes each future '
    'document cheaper than the last.', bold_lead='Receiving it.')

h1(doc, 'Research corner: why you can’t see your own typos')
para(doc, 'The blindness is not sloppiness — it is expertise misfiring. Writing is a high-level task: '
    'you compose meaning, and your brain delegates the mechanical rendering. When you reread your own '
    'fresh prose, the meaning arrives from memory faster than the letters arrive from the page, so '
    'the brain — an aggressive prediction machine — displays the intended sentence rather than the '
    'typed one. Psychologist Tom Stafford, who has studied the phenomenon, notes that this is the same '
    'generalization that makes skilled reading fast: we extract meaning from surface features and skip '
    'the details, which is wonderful until the details are wrong (Stockton, 2014). Every effective '
    'proofreading routine in Figure 7 is an attack on that prediction: aloud slows the eye to speech '
    'speed; unfamiliar fonts break the memory match; single-error sweeps replace reading with '
    'searching. You are not trying to read more carefully. You are trying to stop reading and start '
    'inspecting.')

h1(doc, 'Deep dive: the tone pass — reading as your least charitable reader')
para(doc, 'Between sentence mechanics and proofreading lives a pass most writers never run: tone '
    'revision. Its method is a deliberate change of persona — reread the draft as the busiest, '
    'most skeptical, least charitable person who could plausibly receive it, because on a bad day '
    'that is exactly who will. Sentences that read as efficient to the writer read as curt to the '
    'tired reader; the “just checking in” that felt friendly at noon reads as pressure at 7 a.m.; '
    'the “as I mentioned” that felt like helpful context reads as a filed grievance.')
para(doc, 'What the tone pass hunts: accidental commands (“send me the file” lands differently '
    'than “could you send the file?” — Chapter 16’s ask-versus-order, at revision time); '
    'blame-adjacent phrasing (“you failed to include” → “the attachment didn’t come through”); '
    'passive-aggression fossils (“per my last email,” “as previously stated,” “friendly '
    'reminder”); sarcasm, which survives transmission at roughly zero percent fidelity; and '
    'hedging asymmetry — check whether you hedge your strong claims (“it might be worth possibly '
    'considering”) while stating weak ones baldly, a pattern that inverts your intended emphasis. '
    'The repair is not universal softening: firmness is professional; friction is not. “The '
    'deadline is Friday, and I need the numbers to hit it” is firm and clean. The tone pass keeps '
    'the firmness and removes the shrapnel.', bold_lead='The hunt list.')
para(doc, 'One clinical trick: read the draft aloud in a flat, unfriendly voice — deliberately '
    'stripped of the warmth your inner narrator adds for free. Whatever survives that reading '
    'coldly is what the text actually says; your smile is not attached to the email.',
    bold_lead='The cold read.')

h1(doc, 'Deep dive: the ten-minute emergency protocol')
para(doc, 'Deadlines sometimes eat the system. When ten minutes is all there is, spend them in this '
    'order — it front-loads catastrophe prevention: (1) two minutes on structure triage: is the '
    'main point in sentence one, and does the ask have a date? Move them if not; nothing else '
    'matters more. (2) One minute on the last-thing check: recipients, subject line, attachment — '
    'the career-limiting trio. (3) Three minutes reading aloud at speaking pace — the single '
    'highest-yield pass per minute spent. (4) Two minutes verifying every name and number against '
    'sources. (5) Two minutes on the tone cold-read of the opening and closing only — the '
    'positions readers actually remember. What gets sacrificed: sentence-level polish, conciseness '
    'sweeps, elegance. Flabby-but-correct embarrasses no one; wrong-name-fast does. And log the '
    'debt: a document that shipped on the emergency protocol gets flagged for a real pass before it '
    'is ever reused as a template — today’s forgivable haste is tomorrow’s inherited error.')

h1(doc, 'Deep dive: design consistency — the visual proofread')
para(doc, 'Documents carry a visual layer that needs its own sweep, because inconsistency reads as '
    'carelessness even when every word is right. The checklist: one body font and size throughout '
    '(the paste from another document that arrives wearing Calibri-11 into your Cambria-12 is the '
    'most common offender — paste as text, always); heading levels styled identically at each '
    'level (two different bold sizes for the same level implies a hierarchy you didn’t intend); '
    'list punctuation consistent (all items ending with periods, or none — mixed endings are the '
    'visual equivalent of broken parallelism); spacing rhythm uniform (one blank line between '
    'paragraphs, not sometimes-one-sometimes-two); emphasis inventory audited — if bold means '
    '“deadline” somewhere, it should mean nothing less everywhere, because readers learn your '
    'signals faster than you assign them; and numbers formatted one way ($45,000 or $45K, pick '
    'once). In Word, styles do this work structurally — which is why the accessible heading styles '
    'this course requires are also, quietly, a design-consistency machine: one definition, applied '
    'everywhere, impossible to drift.')

h1(doc, 'Case study 1: the $5 million missing comma')
para(doc, 'In 2017, a U.S. federal appeals court decided a wage dispute between the Oakhurst Dairy '
    'and its delivery drivers — and the entire case turned on a missing comma. Maine’s overtime law '
    'exempted workers involved in “the canning, processing, preserving, freezing, drying, marketing, '
    'storing, packing for shipment or distribution of” perishable foods. Without a comma after '
    '“shipment,” the drivers argued, “packing for shipment or distribution” was one activity — '
    'packing — which they did not do; they merely distributed. The court agreed the sentence was '
    'ambiguous, ruled for the drivers, and the dairy ultimately settled for $5 million '
    '(O’Connor v. Oakhurst Dairy, 2017).')
numbered(doc, [
    'Rewrite the statute’s list so that no reader — or judge — could find two meanings in it. What did you change beyond the comma?',
    'The drafters followed a style manual that discouraged the serial (Oxford) comma. What does this case teach about style rules versus clarity outcomes?',
    'Where in your own writing do lists carry money, obligations, or deadlines? What is your equivalent of the Oakhurst comma?',
    'Which pass of the three-pass system should have caught this — and why might it survive even careful review?',
])
h2(doc, 'Case analysis')
para(doc, 'The deepest lesson is not “always use the Oxford comma” — though in business writing you '
    'should, precisely because it costs nothing and forecloses ambiguity. The lesson is that '
    'punctuation is not decoration; it is load-bearing syntax, and in contracts, policies, and '
    'specifications, ambiguity is a transfer of money to whichever party the second reading favors. '
    'The repair is structural as much as mechanical: a vertical, numbered list of exempt activities '
    'would have made the ambiguity impossible for any comma to create — Chapter 3’s chunking as '
    'legal armor. And note which pass owns this: pass two (sentence clarity), not pass three — the '
    'sentence contained no error a proofreader hunts, only a structure two readers could parse two '
    'ways. That is why revision is a system: each pass catches what the others cannot.')

h1(doc, 'Case study 2: the reply-all résumé')
para(doc, 'A graduating senior spends a weekend perfecting a cover letter for her top-choice firm: '
    'three drafts, two friends’ feedback, flawless prose. Monday morning she sends it — with the '
    'salutation “Dear Ms. Hartman” intact from her previous application, to a recruiter named '
    'Ms. Okafor, with the subject line “appliaction materials,” and the attachment missing. A '
    'follow-up “sorry! attached now!” arrives four minutes later with the wrong file: a draft cover '
    'letter for a competing firm. The prose in every document was immaculate.')
numbered(doc, [
    'List every failure in send order. Which appear in Figure 6’s categories, and which belong to the last-thing check?',
    'The applicant proofread the letter repeatedly. What did she never proofread, and why does the three-pass system still miss it without the last-thing check?',
    'Draft the recovery email. What does Chapter 7’s coming lesson on bad news suggest about owning errors quickly?',
    'Build a personal pre-send checklist of five items for high-stakes messages. Which item would have saved her twice?',
])
h2(doc, 'Case analysis')
para(doc, 'Every failure lived outside the prose: the wrong name (a verification item — check '
    'against the posting or their email, never against memory), the misspelled subject line (typed '
    'last, after proofreading energy was spent — which is exactly why the last-thing check exists), '
    'the missing attachment, and the wrong file (name your files for the recipient: '
    '“Okafor-CoverLetter-May2026.docx” cannot be confused with a competitor’s). The recovery is one '
    'short, unhedged, typo-free message — “My apologies: the correct letter is attached. I '
    'appreciate your patience” — sent once, not four times. The meta-lesson closes the chapter: '
    'revision quality is judged at the weakest point of the whole transmission, not the average '
    'quality of the prose. Perfect paragraphs cannot rescue a wrong name.')

h1(doc, 'The full system, performed: one memo through all three passes')
para(doc, 'Here is the complete pipeline on one artifact. The draft, as first written (146 words):')
para(doc, '“Subject: Update. Hi all, I wanted to reach out to touch base regarding the status of '
    'the equipment procurement process. As you may recall, we have been working on evaluating '
    'options for replacing the aging centrifuge in Lab 2. After extensive research and discussions '
    'with several vendors, it has been determined that the Beckman unit represents the best value. '
    'There are however some considerations around the fact that the current pricing is only being '
    'held until the 15th of this month, after which point there may be an increase. It would '
    'therefore be advisable for a decision to be made in the relatively near future. The total '
    'cost would be approximately $28,750 including installation. Please let me know your thoughts '
    'at your earliest convenience. Thanks so much, Jamie.”')
para(doc, 'Pass one — structure. The reaction check: reader is the lab director, neutral-to-'
    'receptive; direct pattern required, not delivered — the recommendation hides in sentence four '
    'and the deadline in sentence five. The subject line (“Update”) has no careers. The ask '
    '(“let me know your thoughts”) is unfalsifiable, and the one date that matters is buried '
    'mid-paragraph. Findability fails; purpose audit shows one paragraph doing four jobs. '
    'Structural verdict: rebuild around the decision — recommendation first, money and deadline '
    'visible, one dated ask.', bold_lead='Pass 1.')
para(doc, 'Pass two — sentences. The flab census: “I wanted to reach out to touch base regarding” '
    '(lead-in), “as you may recall” (filler), “after extensive research and discussions” '
    '(self-praise as throat-clearing), “it has been determined that” (passive camouflage — WHO '
    'determined?), “there are however some considerations around the fact that” (there-is plus '
    'noun-wrap), “after which point there may be an increase” (hedge stack), “it would therefore '
    'be advisable for a decision to be made” (passive + nominalization — by WHOM?), “relatively '
    'near future” (vague where a date exists), “at your earliest convenience” (fossil). '
    'Abstraction check: “best value” is rung one of the ladder — the numbers exist; climb down.',
    bold_lead='Pass 2.')
para(doc, 'Pass three — proof. Verification catches: the vendor’s own quote says “Beckman '
    'Coulter,” not “Beckman” (names get checked); the quote total is $28,570, not $28,750 — a '
    'transposition that survived two rereadings and would have survived ten (numbers get verified, '
    'not read); and “the 15th of this month” is ambiguous in a memo that might be read on the 3rd '
    'or forwarded next month — absolute dates only. The subject line, typed first and never '
    'revisited, gets its careers.', bold_lead='Pass 3.')
para(doc, 'The document that ships (58 words): “Subject: Approve centrifuge purchase by July 11 — '
    'price hold expires. Recommendation: replace the Lab 2 centrifuge with the Beckman Coulter '
    'Allegra X-30R at $28,570 installed. It scored highest of three bids on capacity, service '
    'coverage, and five-year cost (comparison attached). The quoted price holds through July 11. '
    'Could you approve by the 10th so we order inside the hold?”', bold_lead='The result.')
para(doc, 'Sixty percent shorter, every fact verified, the decision impossible to miss — and '
    'notice the compounding: pass one’s rebuild made pass two faster (less to polish), and both '
    'made pass three’s targets visible. The system is not three times the work of “reading it '
    'over.” Done in order, it is usually less.', bold_lead='The compounding.')

h1(doc, 'Revision workshop: ten repairs (answers follow)')
numbered(doc, [
    '“I am writing to inform you that there has been a change in the schedule with the result that the meeting has been moved to 3:00.”',
    '“Due to the fact that we are currently experiencing a high volume of inquiries at this point in time, responses may be delayed.”',
    '“The committee reached a final conclusion that the two systems should be merged together into one single platform.”',
    '“Sales performance showed significant improvement in the recent period.”',
    '“Each and every employee should refer back to the attached policy in the event that questions arise.”',
    '“The customer satisfaction survey response rate improvement initiative was a success.”',
    '“Having reviewed your application, a decision will be made within two weeks.”',
    '“Please contact Kathryn Meyer, our new VP of Operations.” (Her signature reads “Katherine Meyers.”)',
    '“The contract renews automatically on 3/4/26 unless cancelled with 30 days notice.” (For a client in London.)',
    '“Its important that the team knows there going to get they’re bonuses this quarter.”',
    '“The new procedure will effect significant improvements and insure less errors in the reporting process.”',
    '“We are pleased to announce that the principle findings of the audit, which we conducted over a three month period of time, was positive.”',
    '“Per my last email, please advise as to the status of the aforementioned deliverables at your earliest convenience.”',
    '“The comparison showed the Beckman unit was better. It costs $28,570. The Thermo unit was $31,200. The Eppendorf was cheaper at $26,900 but service coverage was worse. We picked the Beckman.” (For the lab director who asked for one recommendation.)',
])
h2(doc, 'Workshop answers')
numbered(doc, [
    '“The meeting moved to 3:00.” Long lead-in, there-is construction, and nominalization, all deleted.',
    '“Because we are receiving many inquiries, responses may be delayed” — or better, the concrete version: “Expect a reply within three business days.”',
    '“The committee decided to merge the two systems.” Final conclusions, merged together, and one single are all redundancies.',
    'Climb the ladder down: “Sales rose 12% in Q2.” If you do not have the number, that is the real finding.',
    '“All employees: see the attached policy with questions.” Each-and-every, refer back, in-the-event-that — three targets in one sentence.',
    'A five-noun stack. “Our initiative to raise survey response rates worked: responses rose from 12% to 31%.”',
    'Dangling modifier — the decision did not review the application. “Having reviewed your application, we will decide within two weeks.”',
    'Verification beats proofreading: “Katherine Meyers,” from her own signature. Names are checked, not read.',
    'Two repairs: unambiguous date (“4 March 2026” — a Londoner reads 3/4 as April 3) and “30 days’ notice.”',
    '“It’s important that the team knows they’re going to get their bonuses this quarter.” All three homophone families in one sentence — spellcheck passes the original.',
    'Confusables, both barrels: “The new procedure will produce significant improvements and ensure fewer reporting errors.” (Effect→produce or “effect” used correctly as verb is defensible but risky; insure→ensure; less→fewer; and the nominalization unwound.)',
    'Three at once: principle→principal, “three month”→“three-month,” findings…was→findings…were — plus the lead-in and “period of time” flab: “The audit’s principal findings, from our three-month review, were positive.”',
    'Fossil parade: “Where do the deliverables stand? I need them by Thursday to keep the review on track.” Every fossil replaced by information.',
    'Right facts, wrong altitude: synthesize for the decision-maker. “Recommendation: the Beckman Coulter at $28,570 — mid-priced, best service coverage. (Thermo $31,200; Eppendorf $26,900 with weaker coverage — comparison attached.)” The reader asked for a recommendation, not a tour of your spreadsheet.',
])

h1(doc, 'Deep dive: proofreading tables and charts')
para(doc, 'Data displays get skipped in revision because they look finished — grids and axes carry '
    'an aura of precision that prose never gets. They deserve the opposite treatment: exhibits are '
    'where readers go to verify, so exhibit errors are found by exactly the audience you least want '
    'finding them. The sweep: totals actually total (sum the column yourself — the pasted total '
    'from a prior draft is a classic survivor); units and periods labeled on every column and axis '
    '(“Q2” of which year? Dollars or thousands?); table figures match every mention of them in the '
    'prose — one $28,570 in text against $28,750 in the table detonates trust in both; chart axes '
    'start where readers assume (a bar chart truncated at 40 rather than zero is, intentionally or '
    'not, a visual exaggeration — Chapter 9 takes this up properly); legends match the series they '
    'describe after every color change; and captions state the takeaway, not just the topic '
    '(“Figure 2. Response times fell 41% after barcode intake” works even for readers who never '
    'parse the bars). Finally, check the sort: a table ordered by nothing forces the reader to '
    'impose order themselves — sort by the column that matters to the decision, which is the '
    'reader’s-use rule from Chapter 3 wearing a grid.')

h1(doc, 'Deep dive: version control for humans')
para(doc, 'Revision in organizations is collaborative, and collaboration has its own failure '
    'physics: the wrong version ships, two people edit divergent copies, a tracked change from '
    'three reviewers ago surfaces in the client’s copy. The disciplines that prevent each:')
bullets(doc, [
    ('Name versions so the newest is unmistakable.', '“Proposal-v3-2026-07-03.docx” sorts itself; “Proposal-FINAL,” “Proposal-FINAL2,” and “Proposal-FINAL-USE-THIS” is how the wrong version ships. Date-stamped names or a shared drive’s native versioning — pick one system and never freelance.'),
    ('One master at a time.', 'Divergent copies edited in parallel cannot be merged by hope. Either work in a live shared document, or pass an explicit baton: “you have the master until Thursday.”'),
    ('Tracked changes are for negotiation, not archaeology.', 'Turn them on when the writer needs to see and judge each edit; resolve them — accept, reject, discuss — at each round’s end. A document carrying six reviewers’ accumulated markup is unreadable and, worse, one “accept all” away from shipping half-considered edits.'),
    ('Comments carry questions; changes carry corrections.', 'Rewriting a sentence you merely dislike belongs in a comment as a suggestion; fixing a wrong number belongs as a change. Reviewers who blur this leave writers unable to tell taste from error.'),
    ('Scrub before it leaves the building.', 'The final pre-send step on any collaborative document: accept or reject every change, delete every comment, and check the file’s properties — metadata, tracked deletions, and comment threads have embarrassed more organizations than typos ever will. (Word: Review → “No Markup” is a VIEW, not a removal — the markup ships unless resolved.)'),
])
para(doc, 'And the human layer: when your reviewer is senior, their tracked change is not '
    'automatically correct — verify edited numbers against sources exactly as you would your own, '
    'because reviewer-introduced errors carry the least suspicion and survive the longest. The '
    'document’s named owner owns pass three, no matter how many hands touched pass two.',
    bold_lead='The owner’s burden.')

h1(doc, 'Watch list: three short pieces worth your time')
bullets(doc, [
    ('Mary Norris, “The nit-picking glory of The New Yorker’s Comma Queen” (TED).', 'Three decades of professional copyediting distilled into charm — and proof that precision is an act of care, not pedantry.'),
    ('John McWhorter, “Txtng is killing language. JK!!!” (TED).', 'A linguist on why texting is its own register, not broken writing — useful perspective for dialing tone (Chapter 2) without panic.'),
    ('Larry McEnerney, “The Craft of Writing Effectively” (UChicago).', 'Re-watch it after this chapter: his argument that value, not polish, is what readers pay for is the deepest revision standard there is.'),
])

h1(doc, 'Revision self-assessment')
para(doc, 'Score yourself: 2 = usually, 1 = sometimes, 0 = rarely.')
numbered(doc, [
    'I revise in separate passes rather than one anxious reread.',
    'I let drafts cool — even briefly — before revising them.',
    'I cut lead-ins, flabby phrases, and redundant pairs on sight.',
    'I replace abstractions with numbers or examples when they exist.',
    'I read important messages aloud before sending.',
    'I verify names against a source instead of trusting my memory.',
    'I check every number and date against where it came from.',
    'I do the last-thing check: subject, recipients, attachment.',
    'I use the serial comma and unambiguous date formats by default.',
    'I proofread the parts written last (subject lines, captions) hardest.',
])
para(doc, 'Scoring: 16–20, you are the colleague people ask to read things — a real currency. 10–15, '
    'adopt the read-aloud habit and the last-thing check this week; they pay immediately. Below 10, '
    'start with one rule: nothing with stakes goes out the same hour it was written. Retake at '
    'midterm.')

h1(doc, 'Journal prompts')
numbered(doc, [
    'Find the most embarrassing error you ever sent (everyone has one). Which category from Figure 6 was it — and which routine from Figure 7 would have caught it?',
    'Take a page you wrote this term and run only the conciseness pass. Record the word counts before and after. What percentage was ceremony?',
    'Whose writing do you read as effortlessly clear? Steal one page and reverse-engineer it: measure sentence lengths, find the concrete details, count the abstractions. What is the recipe?',
    'Describe your current pre-send ritual honestly. Design the five-item checklist you will actually use, and put it where you will actually see it.',
    'Start your personal error log today with the last five mistakes you know reached readers. Categorize them against this chapter’s taxonomy. Which pass owns each — and what does the pattern say about where your ten minutes of revision should go?',
    'Run the tone cold-read on the last message you sent while irritated. Transcribe what the text actually says, stripped of the warmth you imagined into it. What shipped?',
    'Find a collaborative document from a recent group project. Audit its version hygiene: could a newcomer identify the master, the owner, and the state of the markup? What would the scrub step have caught?',
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'This chapter is where the course rubric’s top band lives: “your supervisor would gladly '
    'send this with no edits” is a statement about revision. The A-grade document has survived all '
    'three passes: structure a skimmer can navigate, sentences with nothing extra and nothing vague, '
    'and mechanics that verification — not luck — made clean. One transposed digit or misspelled '
    'name drops a document out of the top band faster than any stylistic weakness, in this course '
    'and in every job after it, because errors are the one writing flaw every reader can see.')

h1(doc, 'Revision budgets: how much is proportionate?')
para(doc, 'Scale the ritual to the stakes — a rule this guide keeps repeating because every skipped '
    'ritual and every gold-plated one is a proportionality error. Working budgets:')
bullets(doc, [
    ('Routine internal email:', 'one combined read plus the last-thing check — 60 to 90 seconds. More is procrastination wearing diligence.'),
    ('External email, new contact, or anything with money:', 'the full three passes at small scale plus verification of names and figures — five to ten minutes.'),
    ('One-page memo or letter with a decision riding on it:', 'cooling period (hours), full system, read-aloud, tone pass — 30 to 45 minutes across two sittings.'),
    ('Report, proposal, or anything with your name on the cover:', 'overnight cooling, three full passes on separate occasions, a numbers-only sweep, design consistency check, and one outside reader — budget 20 to 30 percent of total writing time for revision, and schedule it when you schedule the drafting.'),
    ('Anything going to more than a hundred people, to the public, or into a contract:', 'all of the above, plus a second qualified reader and the collaborative scrub. At this tier, revision is not a phase of writing; it is most of it.'),
])
para(doc, 'The budgets also settle the guilt question — “should I be revising this more?” has an '
    'answer now: meet the tier’s ritual, then send without ceremony. Discipline plus a definition '
    'of done is what separates careful writers from anxious ones.', bold_lead='Done is defined.')

h1(doc, 'Common mistakes and their fixes')
bullets(doc, [
    ('One anxious reread as “revision.”', 'Fix: three passes, three altitudes — structure, sentences, proof.'),
    ('Revising while still warm.', 'Fix: cool the draft; even twenty minutes converts you partway back into a reader.'),
    ('Polishing sentences pass one will delete.', 'Fix: structure first. Always.'),
    ('Trusting spellcheck.', 'Fix: it cannot see real-word errors, homophones, names, or numbers — the exact high-stakes categories.'),
    ('Reading names and numbers.', 'Fix: verify them against sources. Reading is how the error survived.'),
    ('Skipping the last-thing check.', 'Fix: subject, recipients, attachment — the three-second ritual that prevents the four-minute apology.'),
])

h1(doc, 'Frequently asked questions')
bullets(doc, [
    ('“How many passes for a routine email?”', 'One combined pass plus the last-thing check is proportionate. The full system is for stakes: money, strangers, permanence, or reputation. Scale the ritual to the risk.'),
    ('“Doesn’t Grammarly / Word / AI handle this now?”', 'Tools catch more than they used to and are worth running — as pass zero. They still miss verification errors (names, numbers, wrong-file) entirely, and they cannot judge structure or emphasis. Treat every automated pass as a smoke detector; the walkthrough is still yours (Chapter 15’s rule: your name is on it).'),
    ('“Is the serial comma actually required?”', 'No authority requires it everywhere — but in business writing, use it always: it never creates ambiguity and sometimes prevents a $5 million kind (see Case 1).'),
    ('“I revise forever and never feel done.”', 'Set exit criteria before you start: three passes, the checklist, done. Revision without a definition of done is anxiety wearing a productive costume.'),
    ('“British client, American office — whose conventions win?”', 'The reader’s, per Chapter 2. And where conventions collide (dates especially), choose formats no convention can misread: 4 March 2026.'),
    ('“How do I get better at revision, not just better drafts?”', 'Keep a personal error log: every mistake that survives to a reader goes in it, by category. Within a semester you will know your three signature failures — and a personal checklist of three beats a generic checklist of thirty, because it is aimed at YOUR misses. Review it before every high-stakes document; retire entries you haven’t hit in six months.'),
    ('“Should I revise on screen or paper?”', 'The evidence favors whichever is less familiar — the costume change is the active ingredient. Screen drafters catch more on paper; if printing is impractical, changing font, size, or column width buys most of the same freshness for free.'),
    ('“My reviewer rewrites everything into their voice. What now?”', 'Separate the signal from the style: bank every factual and structural catch gratefully, then raise the pattern once, directly, and in Chapter 16’s question form — “several of these read as voice preferences rather than errors; which ones do you consider must-change?” Most heavy rewriters have never been asked to sort their own edits, and the sorting question teaches both of you where the real defects were.'),
])

h1(doc, 'Crosswalk: this chapter → your course work')
bullets(doc, [
    ('Practice questions (course site, Chapter 4).', 'Conciseness repairs, error-spotting, and pass-assignment questions mirror this guide.'),
    ('Writing prompts (course site).', 'The five-error hunt drills Figure 6’s categories directly.'),
    ('Every graded document this term.', 'The rubric’s top band is a revision standard — budget cooling time before each deadline.'),
    ('Next unit.', 'Chapters 5–8 apply the finished toolkit to the real message types: short digital messages, good news, bad news, and persuasion.'),
    ('The lecture deck.', 'The Chapter 4 slides follow this guide section-for-section.'),
])

keyterms(doc, [
    ('Three-pass revision', 'structure, then sentences, then proof — separated because the eye cannot patrol three altitudes at once.'),
    ('Cooling-off period', 'planned distance between drafting and revising that converts the writer back into a reader.'),
    ('Conciseness', 'nothing extra — every word doing work; distinct from mere shortness.'),
    ('Lead-in / there-is opener', 'ceremonial throat-clearing that delays or demotes the subject.'),
    ('Noun stack', 'nouns piled into an unparseable tower; untangled by restoring verbs.'),
    ('Abstraction ladder', 'the climb from vague (“improved”) to checkable (“9 hrs → 2.1 hrs”).'),
    ('Real-word error', 'a correctly spelled wrong word (“manger”) — invisible to spellcheck.'),
    ('Verification proofreading', 'checking names, numbers, and dates against sources instead of reading them.'),
    ('Serial (Oxford) comma', 'the comma before the final list item; cheap insurance against expensive ambiguity.'),
    ('Last-thing check', 'subject line, recipient list, attachment — inspected in the final seconds before send.'),
    ('Tone pass', 'rereading as the least charitable plausible reader; firmness kept, shrapnel removed.'),
    ('Personal error log', 'your running record of mistakes that reached readers — the aimed checklist that beats generic ones.'),
    ('Scrub', 'the pre-send resolution of all tracked changes, comments, and metadata on collaborative documents.'),
    ('False precision', 'more significant digits than your knowledge supports — a claim about certainty you cannot back.'),
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Revision is a system of three passes at three altitudes — structure, sentences, proof — never one anxious reread.',
    'Cool the draft: your brain shows you what you meant to write until distance resets it (Stockton, 2014).',
    'Conciseness hunts six targets: lead-ins, there-is openers, redundant pairs, flabby phrases, hedges, and noun stacks — “omit needless words” (Strunk & White, 2000).',
    'Clarity climbs down the abstraction ladder until claims are checkable; concrete survives forwarding.',
    'Spellcheck cannot see real-word errors, homophones, names, or numbers — verify the high-stakes categories against sources.',
    'Punctuation is load-bearing: one missing comma cost $5 million (O’Connor v. Oakhurst Dairy, 2017).',
    'The last-thing check — subject, recipients, attachment — prevents the disasters that perfect prose cannot.',
])

quiz(doc, [
    ('The three revision passes, in order, are:', ['Proof, sentences, structure','Structure, sentences, proof','Spelling, grammar, tone','Draft, cool, send']),
    ('Structure comes first because:', ['It is easiest','There is no point polishing paragraphs that pass one will delete','Readers notice typos most','Spellcheck handles it']),
    ('You cannot proofread your own fresh draft mainly because:', ['You are careless','Your brain displays the intended text rather than the typed one','Fonts are too small','You lack training']),
    ('“There are three issues that remain” is best revised to:', ['“There remain three issues”','“Three issues remain”','“It is the case that three issues remain”','“Issues: three”']),
    ('“Due to the fact that” should almost always become:', ['“Owing to the circumstance that”','“Because”','“Since the situation is”','“As per”']),
    ('Which error will spellcheck reliably MISS?', ['“recieve”','“teh”','“The manger will meet you at 3”','“acommodate”']),
    ('Names in business messages should be:', ['Read carefully twice','Verified against a source such as the person’s own signature','Guessed from memory','Abbreviated']),
    ('The Oakhurst Dairy case turned on:', ['A misspelled name','A missing serial comma that made a statutory list ambiguous','A wrong attachment','An unsigned contract']),
    ('The deepest lesson of the Oakhurst case is:', ['Always use spellcheck','Punctuation is load-bearing syntax; ambiguity transfers money','Avoid lists','Courts dislike commas']),
    ('“Cut response time from 9 hours to 2.1 in the pilot” beats “improved performance” because it is:', ['Longer','Checkable — concrete claims can be verified and remembered','More formal','Passive']),
    ('The single highest-yield proofreading technique is:', ['Reading silently faster','Reading the text aloud','Trusting grammar software','Checking twice on screen']),
    ('The last-thing check covers:', ['Margins, font, spacing','Subject line, recipient list, attachment','Grammar, spelling, tone','Purpose, audience, channel']),
    ('“Having reviewed your application, a decision will be made” contains:', ['A noun stack','A dangling modifier — the decision did not review anything','A homophone error','A serial comma problem']),
    ('For a London client, “3/4/26” should become:', ['“3-4-26”','“4 March 2026” — a format no convention can misread','“March 3rd”','“Q1 2026”']),
], ['b','b','b','b','b','c','b','b','b','b','b','b','b','b'])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Which conciseness target from Figure 3 is your personal signature flab? Bring three examples from your own writing and their repairs.',
    'Time is the scarcest revision resource. Where in your actual workflow can a cooling period realistically live — and for which documents is it non-negotiable?',
    'Find a public document whose ambiguity could cost someone money. Rewrite the load-bearing sentence so no second reading exists.',
    'Automated tools flagged none of the ten workshop sentences as they stood. What does that imply about the division of labor between you and your tools?',
    'Defend or attack: “In business writing, the serial comma should be mandatory.” Use the Oakhurst case and one example of your own.',
])

references(doc, [
    'Stockton, N. (2014, August 12). What’s up with that: Why it’s so hard to catch your own typos. Wired. https://www.wired.com/2014/08/wuwt-typos/',
    'Flesch, R. (1949). The art of readable writing. Harper & Brothers.',
    'O’Connor v. Oakhurst Dairy, 851 F.3d 69 (1st Cir. 2017).',
    'Strunk, W., Jr., & White, E. B. (2000). The elements of style (4th ed.). Longman.',
    'Williams, J. M., & Bizup, J. (2017). Style: Lessons in clarity and grace (12th ed.). Pearson.',
    'Zinsser, W. (2006). On writing well: The classic guide to writing nonfiction (30th anniversary ed.). HarperCollins.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch04-study-guide.docx')
finish(doc, os.path.abspath(out))
