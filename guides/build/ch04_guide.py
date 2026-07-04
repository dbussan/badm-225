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
    'out at any stranger (Stafford, quoted in Dean, 2014). Distance is the antidote. Overnight is '
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

h1(doc, 'Research corner: why you can’t see your own typos')
para(doc, 'The blindness is not sloppiness — it is expertise misfiring. Writing is a high-level task: '
    'you compose meaning, and your brain delegates the mechanical rendering. When you reread your own '
    'fresh prose, the meaning arrives from memory faster than the letters arrive from the page, so '
    'the brain — an aggressive prediction machine — displays the intended sentence rather than the '
    'typed one. Psychologist Tom Stafford, who has studied the phenomenon, notes that this is the same '
    'generalization that makes skilled reading fast: we extract meaning from surface features and skip '
    'the details, which is wonderful until the details are wrong (Dean, 2014). Every effective '
    'proofreading routine in Figure 7 is an attack on that prediction: aloud slows the eye to speech '
    'speed; unfamiliar fonts break the memory match; single-error sweeps replace reading with '
    'searching. You are not trying to read more carefully. You are trying to stop reading and start '
    'inspecting.')

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
])

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
])

h1(doc, 'How your writing will be graded (and read at work)')
para(doc, 'This chapter is where the course rubric’s top band lives: “your supervisor would gladly '
    'send this with no edits” is a statement about revision. The A-grade document has survived all '
    'three passes: structure a skimmer can navigate, sentences with nothing extra and nothing vague, '
    'and mechanics that verification — not luck — made clean. One transposed digit or misspelled '
    'name drops a document out of the top band faster than any stylistic weakness, in this course '
    'and in every job after it, because errors are the one writing flaw every reader can see.')

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
])

h1(doc, 'Chapter summary')
numbered(doc, [
    'Revision is a system of three passes at three altitudes — structure, sentences, proof — never one anxious reread.',
    'Cool the draft: your brain shows you what you meant to write until distance resets it (Dean, 2014).',
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
    'Dean, J. (2014, August 12). What’s up with that: Why it’s so hard to catch your own typos. Wired. https://www.wired.com/2014/08/wuwt-typos/',
    'Flesch, R. (1949). The art of readable writing. Harper & Brothers.',
    'O’Connor v. Oakhurst Dairy, 851 F.3d 69 (1st Cir. 2017).',
    'Strunk, W., Jr., & White, E. B. (2000). The elements of style (4th ed.). Longman.',
    'Williams, J. M., & Bizup, J. (2017). Style: Lessons in clarity and grace (12th ed.). Pearson.',
    'Zinsser, W. (2006). On writing well: The classic guide to writing nonfiction (30th anniversary ed.). HarperCollins.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch04-study-guide.docx')
finish(doc, os.path.abspath(out))
