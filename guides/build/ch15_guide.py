# Chapter 15 study guide — AI, Agents & Professional Communication (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(15, 'AI, Agents & Professional Communication',
    'The tools that draft · the judgment that ships · verification, disclosure, and the skills that appreciate')

h1(doc, 'Why this chapter exists')
para(doc, 'Unit 6 opens with the tool that is quietly rewriting every genre this course has taught. AI '
    'drafting is now fast enough, cheap enough, and good enough that declining to use it is a competitive '
    'disadvantage — and using it without judgment is a professional liability. Both facts are true '
    'simultaneously, and this chapter exists to hold them together: what AI actually does mechanically, '
    'where that mechanism succeeds and fails, how to draft with it as a collaborator rather than a '
    'ghostwriter, what must never be delegated, and what happens when the tool stops drafting and starts '
    'acting on your behalf as an agent.')
para(doc, 'Hold one governing sentence through the whole chapter: your name ships on it. Whatever '
    'assistance produced a draft, the judgment, verification, and accountability for what goes out the '
    'door remain yours — exactly as they would if a brilliant, tireless junior colleague had written the '
    'first draft. That frame, introduced here, resolves nearly every specific question the chapter takes '
    'up: what to verify, what to disclose, what never to automate, and how much authority to hand an '
    'agent before a human has to look.')

h1(doc, 'The floor rose. The ceiling didn’t move.')
figure(doc, os.path.join(FIG, 'ch15_floorceiling.png'),
    'Figure 1. The floor and the ceiling — competent prose is now nearly free; judgment is exactly where it was.',
    'Two panels: the floor (competent prose, nearly free — routine drafting is no longer a differentiator) and the '
    'ceiling (knowing what’s true, what matters, what the moment requires — exactly where it always was), with the '
    'instruction to use the tools fully, verify ruthlessly, and invest in the ceiling.')
para(doc, 'The single organizing metaphor for this chapter, introduced in Chapter 1 and paid off here: '
    'AI raises the floor of writing quality — competent, well-structured prose is now nearly free to '
    'produce. The ceiling — knowing what is true, what matters, and what a given moment requires — has '
    'not moved an inch, because nothing about predicting plausible text touches judgment. The practical '
    'consequence is a redistribution of value. Competent-sounding prose, which used to separate careful '
    'writers from careless ones, is no longer scarce; anyone can generate it in seconds. What remains '
    'scarce — and therefore valuable — is exactly the ceiling: the person who knows which claims are '
    'true, which details matter to this reader, and what this situation actually calls for. This '
    'chapter’s thesis in one sentence: use the tools fully, verify ruthlessly, and invest in the ceiling, '
    'because the floor was never where your career lived anyway.')

h1(doc, 'What these tools are')
para(doc, 'A vendor-neutral, plain-language mental model does more work here than any feature list, '
    'because the model predicts both the tool’s brilliance and its failures from one mechanism.')
h2(doc, 'What a language model actually does')
para(doc, 'A large language model predicts plausible next words, trained on enormous quantities of '
    'text, and produces fluent, well-structured, statistically likely prose. That is the entire '
    'mechanism, and it explains everything else in this chapter. Fluency is the product; truth is '
    'incidental — the model is not lying when it states something false, because it has no concept of '
    'lying. It is doing exactly its job (plausible continuation) on a question where plausible does not '
    'imply true. It also has no access to your situation: your reader, your organizational history, this '
    'week’s facts, the politics of the room — none of it is available unless you supply it in the '
    'prompt, which is why the prompting section below reads like Chapter 2’s audience analysis, because '
    'it is.')
figure(doc, os.path.join(FIG, 'ch15_capability.png'),
    'Figure 2. What it’s great at and where it fails — both columns follow from one mechanism.',
    'Two panels: great at (first drafts of routine genres, rewriting and tone shifts, critique on demand, brainstorming, '
    'single-error sweeps) and fails at (facts, numbers, names, citations that don’t exist, anything after training data '
    'ends, your specific context, judgment calls), with the note that both columns follow from predicting plausible '
    'next words.')
para(doc, 'The two-column capability map is worth memorizing rather than looking up, because it '
    'determines what you delegate and what you verify. On the great-at side: first drafts of routine '
    'genres (email, summaries, outlines), rewriting for tone or brevity, critique on demand (“name the '
    'three weakest points”), brainstorming options and counterarguments, and single-error sweeps '
    '(Chapter 4’s targeted passes, now automatable). On the fails-at side: facts, numbers, and names '
    '(fluent fabrication is the signature failure mode); citations to sources that do not exist; '
    'anything past its training cutoff, delivered with the same confidence as everything else; your '
    'specific context, which it cannot know unless told; and judgment calls about what to say, whether '
    'to send, and who might be hurt. Every item in both columns traces back to the same prediction '
    'mechanism — nothing here is a temporary limitation awaiting the next model version. It is what the '
    'architecture does.')
para(doc, 'The mental model that calibrates both trust and verification correctly: treat AI like a '
    'gifted new hire who started this morning. Extraordinary at producing work; zero knowledge of your '
    'world; unaware when wrong, because unawareness is not something day-one hires or language models '
    'experience as a deficiency. You would never send a day-one hire’s draft out unreviewed — the same '
    'review standard, applied identically, is the entire AI policy this chapter recommends. You would '
    'also never decline the help out of pride; refusing a tireless drafting assistant is choosing to be '
    'slower at the same quality. Delegation without abdication is the discipline: the work can be handed '
    'off, the accountability cannot, which the agents section develops fully.', bold_lead='The junior-colleague model.')

h1(doc, 'Drafting with AI')
para(doc, 'Where the mechanical model earns its keep is in producing better drafts faster — if you '
    'bring the same discipline you would bring to briefing a human writer.')
h2(doc, 'The prompt is a brief')
para(doc, 'Write the prompt the way Chapter 2 taught you to plan any message: purpose, audience, key '
    'facts, constraints, tone. “Write something about the delay” produces generic output because it is '
    'a generic instruction; a real brief produces usable drafts. Supply the situation the tool cannot '
    'know — “the client has already complained twice; we need firm but warm” — and state the format '
    'you want (“three-line status update,” “one-page memo with headings”): structure requested is '
    'structure received. When output misses the mark, the fix is almost always a missing fact or '
    'constraint in the brief, not a flaw in the tool — the exercise of iterating the prompt frequently '
    'reveals a requirement you had not consciously named, which makes prompting a form of thinking, not '
    'just a form of asking.')
h2(doc, 'The critique loop beats the generate loop')
para(doc, 'Two workflows produce very different outcomes for identical tools. In the generate loop, '
    'the tool drafts and you lightly edit — fast, and it produces the house-style prose readers are '
    'learning to recognize and discount. In the critique loop, you draft first and ask the tool to '
    'attack it: “find the three weakest arguments in this proposal,” “where does this memo bury the '
    'ask?” This preserves your authorship while borrowing the tool’s tirelessness for the red-team '
    'function Chapter 10 taught you to seek from a cold human reader. A hybrid works too, provided the '
    'edit pass is real: let the tool draft, then reorder, cut, verify, and re-voice as an owner rather '
    'than a proofreader. Ask for options rather than verdicts — “give me three ways to open this '
    'refusal” — which preserves the choosing, and choosing is where the judgment layer actually lives. '
    'And run targeted, single-error passes exactly as Chapter 4 taught (“check subject-verb agreement '
    'only,” “flag every claim lacking a number”), because the tool is genuinely excellent at narrow, '
    'well-defined sweeps.')
h2(doc, 'Keeping your voice')
para(doc, 'Default AI prose has a recognizable house style — smooth, hedged, slightly padded, '
    'oddly agreeable — and readers are increasingly able to name it, which means it now reads as '
    '“nobody home” rather than as competent. Two defenses: feed the tool your own voice (“match the '
    'tone of this paragraph I wrote”) or re-voice the draft yourself in the edit pass. De-pad on sight: '
    '“I hope this finds you well,” triple restatements, and “it’s important to note” are Chapter 4’s '
    'flab targets wearing a new source. And apply the relationship test from the never-delegate list '
    'below: if the reader would feel differently on learning a machine produced it — the thank-you, the '
    'apology — a machine should not have.')

h1(doc, 'What not to delegate — ever')
figure(doc, os.path.join(FIG, 'ch15_neverdelegate.png'),
    'Figure 3. The never-delegate list — goodwill, apologies, performance feedback — and why.',
    'Three rows: goodwill messages (the pause IS the message), apologies (ownership ghostwritten is ownership '
    'faked), and performance feedback (SBI requires having seen the behavior), with the common thread that wherever '
    'the message IS the relationship, the drafting IS the sincerity.')
para(doc, 'Three genres fail no matter how good the model gets, because their entire content is a '
    'human fact that automation erases. Goodwill messages — thanks, congratulations, condolences '
    '(Chapter 6) — exist because a human paused to notice and write; automating the pause deletes the '
    'message even if the words survive. Apologies (Chapter 7) require ownership, and ghostwritten '
    'ownership is ownership faked — the flat cadence of AI-drafted contrition reads as exactly what it '
    'is. Performance feedback (Chapter 7’s SBI) requires having actually observed the behavior; '
    'delegated observation is fiction wearing a rubric. The unifying principle: wherever the message '
    'IS the relationship rather than a container for information, the drafting IS the sincerity, and '
    'efficiency is the wrong axis to optimize entirely.')

h1(doc, 'Verification and confidentiality: the two non-negotiables')
figure(doc, os.path.join(FIG, 'ch15_pipeline.png'),
    'Figure 4. The verification pipeline — flag, trace, fix, own — runs on every AI draft.',
    'A four-step flow: flag every load-bearing claim, trace each to a real source, fix by correcting, sourcing, or '
    'deleting, and own the result as yours — with the warning that the more precise an unverified claim, the more '
    'suspicious it should be.')
para(doc, 'Everything else in this chapter is style; these two are hard rules. The verification '
    'pipeline runs identically whether the draft is yours or the tool’s, because the tool simply moved '
    'WHERE errors cluster: your own fatigue-driven errors cluster in haste, while AI errors cluster in '
    'confident, precise-sounding specifics. Flag every load-bearing claim — facts, numbers, names, '
    'dates, citations. Trace each to a source you can actually open. Fix by correcting, sourcing, or '
    'deleting — there is no fourth option for a claim that cannot be verified. Then own it: from the '
    'moment it ships, it is yours regardless of provenance. The single most useful heuristic: the more '
    'precise an unverified AI claim sounds, the more suspicious it should be, because fabrication and '
    'genuine precision are stylistically indistinguishable and only one of them survives a source check.')
para(doc, 'The signature failure deserves its own emphasis: a fabricated citation — a real journal, '
    'plausible authors, a title that sounds exactly right — for a paper that does not exist. It survives '
    'every check except the one that matters, opening the source. Chapter 10’s credibility ladder '
    'already ranked AI output at rung five: a research assistant that can find and summarize real '
    'sources, never a source in its own right. “The AI said so” is not a citation in any register — in '
    'school it is an integrity violation, and at work it is your name attached to an untraceable claim. '
    'Same failure, different invoice.', bold_lead='The fabricated citation problem.')
para(doc, 'Confidentiality follows a simple test: pasting client names, salaries, unreleased figures, '
    'or student records into a public AI tool is disclosure to an external service, and should be '
    'weighed exactly like posting the same content publicly (Chapter 5’s permanence rule). Learn which '
    'tools your organization has actually licensed — many workplaces provide enterprise instances with '
    'real data agreements, and the rules genuinely differ between that instance and the free consumer '
    'tab. Anonymize when the task allows it (“a client in medical devices” usually preserves everything '
    'the drafting task needs). And when in doubt, apply the old test: would you email this content to an '
    'outside vendor without asking anyone first? If not, do not paste it either.', bold_lead='Confidentiality: the paste is a publication.')

h1(doc, 'Disclosure and integrity')
para(doc, 'Norms around disclosing AI assistance are still forming, which makes a durable decision '
    'procedure more useful than a fixed rule. Follow explicit policy first — your syllabus, your '
    'employer’s guidelines, your client’s contract. Where policy is silent, disclose by stakes: routine '
    'drafting help rarely needs a footnote, while analysis, research, or anything traded on your '
    'personal expertise usually does. The honest formulation costs one sentence: “drafted with AI '
    'assistance; all facts and recommendations verified and mine.” And the test that outlives every '
    'specific policy is Chapter 1’s publicity test, pointed at your tools: if disclosure would embarrass '
    'you, the use was wrong in the first place — the discomfort is the information.')
para(doc, 'For this course specifically, the boundary runs where most current academic and workplace '
    'norms converge: encouraged uses include critique loops on your own drafts, grammar and tone '
    'passes, brainstorming, outlining, and practice drills; out of bounds are submitting AI output as '
    'your own assessed writing, fabricated or unverifiable citations, pasting confidential or personal '
    'data, and AI-drafted goodwill, apologies, or feedback. Confirm the specifics against your actual '
    'syllabus, since instructor policies vary and evolve.')

h1(doc, 'Agents: when the tool stops drafting and starts doing')
para(doc, 'An agent is a model with hands — it does not just draft the email, it sends it; does not '
    'just plan the research, it runs it, files the results, and schedules the follow-up. The shift is '
    'from suggestion to action, and it changes the accountability question completely. Drafting tools '
    'propose; agents execute — across calendars, inboxes, purchases, postings, even code. Whatever an '
    'agent does under your name is legally and professionally yours: the agent that emails the wrong '
    'client or posts an unverified figure acted with your authority, and “the AI did it” defends about '
    'as well as “the intern did it” always has. Agentic assistance is also genuinely useful today — '
    'research sweeps, report drafts, data pulls, scheduling — and this course’s own materials were built '
    'with supervised agentic help, which is offered here as an honest example rather than a hidden '
    'admission.')
figure(doc, os.path.join(FIG, 'ch15_agentmandate.png'),
    'Figure 5. Delegating to agents without abdicating — scope, gate, start narrow, audit.',
    'Four rows: scope the mandate in writing, gate the irreversible actions for human review, start narrow and widen '
    'with evidence, and audit on a cadence — spot-checking what it did, not just what it reported.')
para(doc, 'Four supervision habits map directly onto management fundamentals, because agent '
    'supervision IS management, minus the interpersonal considerations. Scope the mandate in writing: '
    'what it may do, what it must ask about, what it must never touch — Chapter 6’s complete-ask '
    'discipline, aimed at software instead of a colleague. Gate anything irreversible — sending, '
    'deleting, purchasing, publishing — behind human review; draft-for-approval beats act-then-apologize '
    'wherever the action cannot be undone. Start narrow and widen scope only with evidence, exactly as '
    'a new hire earns trust on Chapter 8’s ladder. And audit on a cadence: spot-check what the agent '
    'actually did, not merely what it reported doing, because Chapter 9’s honest-yellow logic applies '
    'to tools exactly as it applies to people.')

h1(doc, 'Case study: the agent that emailed the draft')
para(doc, 'An analyst’s agent managed her routine follow-ups under a mandate with one loose line: '
    '“send routine confirmations without review.” A renegotiation email — still carrying candid '
    'internal notes in the same thread — matched “routine confirmation” by the agent’s literal reading. '
    'It sent. The client read the notes.')
para(doc, 'The recovery ran Chapter 7’s protocol exactly: same-hour ownership call, no blame assigned '
    'to the tool in public (“my process failed,” not “the AI sent something it shouldn’t have”), and an '
    'immediate mandate rewrite adding a review gate for anything touching a live negotiation thread. The '
    'takeaway generalizes past this incident: agents execute the mandate you WROTE, not the one you '
    'meant, which converts precision in delegation into a writing skill with a genuine blast radius. '
    'Every ambiguous word in a mandate is a decision you handed to a system that cannot ask '
    'clarifying questions the way a cautious junior colleague would.')

h1(doc, 'Talking about AI with your team')
para(doc, 'AI use is now a team-communication topic in its own right, not just an individual choice. '
    'Agree on norms out loud, per Chapter 11’s ground-rules discipline: which tools, for which tasks, '
    'what gets disclosed, what never gets pasted — unwritten AI norms are incidents on layaway. Never '
    'weaponize the accusation: “this feels AI-written” is becoming the new “did you even write this?”, '
    'and it critiques a suspected genealogy instead of an actual failure; critique the work’s real '
    'weaknesses instead (Chapter 4). Share prompts the way you would share a template — the brief that '
    'produced a genuinely excellent status report is team infrastructure, worth documenting in the wiki '
    '(Chapter 5). And name the access gap plainly if it exists: when half a team has enterprise tools '
    'and half does not, the resulting output gap is not a talent gap, and saying so before a performance '
    'review has to is a leadership act.')

h1(doc, 'The career layer: invest in the ceiling')
figure(doc, os.path.join(FIG, 'ch15_appreciation.png'),
    'Figure 6. Skills that appreciate as drafting gets free — judgment, verification, the brief, relationships, editing.',
    'Five cells: judgment (what’s true, what matters), verification (source discipline), the brief (specifying work '
    'precisely), relationships (trust, presence, the room), and editing (turning a B-minus draft into your A).')
para(doc, 'As drafting gets cheap, a specific portfolio of skills appreciates in value, and every item '
    'in it is a chapter of this course — which is not a coincidence, since the curriculum was built as '
    'a hedge against exactly this shift. Judgment: knowing what is true, what matters, what the moment '
    'requires — the whole ceiling. Verification and source discipline (Chapter 10): when fluent text is '
    'free, the person who can reliably separate true from merely plausible becomes the scarce input. '
    'The brief: specifying work precisely, for humans or agents, is simultaneously the management skill '
    'and the prompting skill, now visibly the same competency. Relationships and presence (Chapters 11, '
    '12, 16): the trust account, the room, the hard conversation — none of it is touched by the '
    'toolchain. And editing: the floor’s output still needs an owner with taste, and rebuilding a '
    'competent draft into your best work is now a core professional competency rather than a chore.')
para(doc, 'Stay current without hype-chasing by treating your own capability map as a dated document '
    '(Chapter 9’s “as of” discipline): what the tools could not do in January sometimes ships by June, '
    'so re-test assumptions on a quarterly cadence rather than trusting last year’s read. Learn '
    'primarily by automating one real workflow rather than reading takes about automation — a single '
    'genuinely completed task teaches more than fifty threads of commentary. And distrust both cults '
    'equally: “it changes nothing” and “it changes everything” are both lazy positions, and the '
    'professional stance is a running, personally tested inventory of what it actually changes for '
    'your specific work.')

h1(doc, 'Case study: two analysts, one tool')
para(doc, 'Same team, same enterprise AI license, radically different trajectories. Analyst A pastes '
    'the assignment into the tool, submits whatever comes back, and calls it efficiency — the generate '
    'loop, unmodified. Analyst B briefs the tool like a junior colleague, runs the critique loop on her '
    'own drafts, verifies every number against the source system, and re-voices the close so it reads '
    'as hers, because it is.')
para(doc, 'In month three, A’s client deliverable contains a confidently stated benchmark that turns '
    'out to be fabricated — precise-sounding, properly formatted, and entirely invented. The discovery '
    'triggers a review of everything he has shipped since. B, whose habits made verification routine '
    'rather than exceptional, absorbs his accounts instead. Same tool, same access, same starting '
    'competence. The variable was never the technology. It was who stayed the author — which is the '
    'chapter’s thesis, and very nearly the course’s.')

h1(doc, 'What stays true when the tools change')
para(doc, 'Every specific example in this chapter — today’s model behaviors, today’s common failure '
    'modes, today’s regulatory state — will be at least partly outdated within a few years, possibly '
    'sooner. That is not a flaw in the chapter; it is the nature of writing about a fast-moving '
    'technology honestly rather than pretending to permanence it does not have. What will not date is '
    'the structure underneath the examples: a tool that predicts plausible text will always need a '
    'human who checks for true text: the genres where the drafting IS the sincerity will not stop '
    'requiring a human pause just because the drafting got better; the accountability for what ships '
    'under your name will not transfer to the tool that helped produce it, no matter how sophisticated '
    'that tool becomes; and the disclosure question — would this survive being said aloud to the '
    'person it affects — will outlive every specific policy written to answer it in the meantime. '
    'Read the specifics in this chapter as a snapshot. Read the structure as the actual lesson.')

h1(doc, 'A note on speed versus haste')
para(doc, 'The most common way this chapter’s principles get skipped in practice is not deliberate '
    'recklessness — it is ordinary deadline pressure meeting a tool that makes skipping verification '
    'feel almost free. A draft that took an hour to write invited a careful read; a draft that took '
    'ninety seconds to generate can feel, wrongly, like it deserves only a ninety-second review. It '
    'does not. The verification pipeline’s cost is roughly fixed regardless of how fast the draft '
    'arrived, because the thing being checked — is this true, is this the right call, is this '
    'defensible — has nothing to do with drafting speed. Building in the pause deliberately, the way '
    'Chapter 4 built in the cooling-off period for ordinary revision, is the single most protective '
    'habit this chapter can leave you with: treat every AI-assisted draft as though it took as long to '
    'produce as it will take to verify, and schedule accordingly.')

h1(doc, 'Frequently asked questions, continued')
para(doc, 'Rarely a full rewrite — usually the small tells this chapter has already named: the house '
    'style’s hedge-and-pad rhythm, an oddly even tone across topics that should carry different '
    'emotional weight, and transitions that connect ideas a little too smoothly. None of these prove '
    'AI origin on their own (careful human writers can produce all three), which is precisely why '
    'accusing someone based on "vibes" is unreliable and unfair (the myths section above). Treat the '
    'tells as a prompt to look harder at substance, never as a verdict in themselves.',
    bold_lead='How can I tell if something I’m reading was AI-written?')
para(doc, 'Ask for the reasoning, not just the answer: "walk me through why you’d recommend that" — an '
    'AI-only submission with no real engagement typically cannot defend its own claims under a '
    'follow-up question, because the "writer" never actually reasoned through the problem. This is '
    'also simply good management practice independent of AI, and it is why Chapter 14’s working-session '
    'protocol scores the reasoning process rather than the final answer alone.',
    bold_lead='My team member submitted work I suspect is entirely AI-generated with no review. What do I do?')
para(doc, 'Genuinely useful for the mechanical parts — vocabulary drilling, grammar explanation, '
    'practice conversation — provided you verify idiomatic or cultural claims the way you would verify '
    'any other AI output, since fluency in tone can mask errors in register just as easily in a '
    'second language as a first. The judgment layer (what to say, to whom, and why) still has to be '
    'yours; the tool can help you say it correctly without deciding it for you.',
    bold_lead='I’m not a native English speaker — can AI help me write more professionally?')

h1(doc, 'A closing frame: three questions before you send anything AI-assisted')
para(doc, 'Every principle in this chapter compresses into three questions, fast enough to run before '
    'any AI-assisted message ships, whatever the genre or the stakes.')
numbered(doc, [
    'Have I verified every fact, number, name, and citation against a real source I actually opened? '
    '(The verification pipeline, run in full — not "it looked right.")',
    'Does this message belong on the never-delegate list — is the drafting itself the sincerity? '
    '(If yes, the AI-assisted version, however polished, is the wrong artifact regardless of quality.)',
    'If the reader knew exactly how this was produced, would they feel misled, or simply informed? '
    '(The publicity test, one last time — the question that outlives every specific policy this '
    'chapter or any future one could write.)',
])
para(doc, 'A yes to the third question, a clean pass on the first, and a no on the second together '
    'describe the entire chapter in the time it takes to read three sentences. That is the point: the '
    'technology will keep changing, sometimes faster than any guide can track. The three questions '
    'will not.')

h1(doc, 'The apprenticeship problem')
para(doc, 'A concern raised seriously by experienced professionals across many fields deserves its own '
    'treatment rather than a dismissive footnote: if AI drafts the routine work that used to train '
    'juniors — the first-pass memos, the rough analyses, the early-career repetitions that built '
    'judgment through volume — where does the NEXT generation’s judgment come from? This is not a '
    'reason to avoid AI. It is a reason to be deliberate about what replaces the apprenticeship '
    'function the routine work used to serve.')
para(doc, 'Two responses matter for you specifically, whichever side of that transition you are on. '
    'If you are early-career: do not let AI assistance substitute for the REPS that build judgment. '
    'Draft difficult passages yourself before consulting the tool, specifically so you feel where the '
    'hard decisions are — Chapter 12’s rehearsal principle, applied to writing itself. The critique '
    'loop (draft first, then ask AI to attack it) preserves exactly this rep in a way the generate '
    'loop does not, which is the strongest practical argument for preferring it beyond the '
    'voice-preservation reasons already given. If you supervise or will supervise early-career staff: '
    'the judgment-building assignments — the ones where getting it wrong and fixing it teaches more '
    'than getting it right — deserve explicit protection from full automation, even though automating '
    'them would look efficient on a quarterly report. Chapter 11’s ground rules apply at the '
    'organizational level: decide deliberately which work stays a training ground, rather than letting '
    'efficiency pressure make that decision by default.')

h1(doc, 'If you have to write your team’s AI policy')
para(doc, 'Sooner than expected, someone in your career will be asked to draft the AI usage guidelines '
    'for a team, and the temptation is to either ban everything (unenforceable and self-defeating) or '
    'say nothing (the disclosure vacuum that produced the consulting-analyst case above). A workable '
    'policy fits on one page and answers five questions plainly, in Chapter 11’s ground-rules style.')
numbered(doc, [
    'Which tools are approved, and for what data? Name the enterprise-licensed tool and state '
    'explicitly what may and may not be pasted into it or any consumer-grade alternative.',
    'What must always be verified before it ships? Name the categories — facts, figures, names, '
    'citations, anything client-facing — rather than leaving "check your work" to interpretation.',
    'What must never be delegated? Adopt this chapter’s never-delegate list explicitly, and add any '
    'genre specific to your team’s work where the drafting IS the content.',
    'When must AI assistance be disclosed, and to whom? State the stakes threshold plainly rather '
    'than leaving it to individual judgment call by call — consistency here IS the fairness.',
    'Who owns an AI-related error, and what happens next? Answer this BEFORE an incident, using '
     'Chapter 7’s ownership language — "the team member who shipped it owns the fix," never "the AI '
     'made a mistake."',
])
para(doc, 'Circulate the draft for input exactly as Chapter 11 recommends for any ground rules — '
    'agreement is cheap before an incident and expensive after one. And revisit the page on a fixed '
    'cadence (quarterly is reasonable), because this chapter’s own content will be outdated faster '
    'than most of this course’s — treat your team’s policy the same way.')

h1(doc, 'The regulatory landscape, in brief')
para(doc, 'AI governance is moving from voluntary guideline to enforceable law faster than most '
    'professionals have registered, and the direction of travel matters even if specific statutes '
    'differ by jurisdiction. Several patterns are stable enough to plan around.')
bullets(doc, [
    ('Disclosure requirements are expanding.', 'A growing number of jurisdictions require disclosure '
     'when AI is used in hiring decisions, credit decisions, or content that could be mistaken for '
     'human-created work in specific regulated contexts. "No one will know" is an increasingly poor '
     'bet, and the publicity test (Chapter 1) was already telling you not to make it.'),
    ('Copyright and ownership remain unsettled.', 'Whether AI-generated content can be copyrighted, '
     'and who owns output trained partly on others’ copyrighted work, is actively litigated in '
     'multiple jurisdictions as this is written. Practical implication: do not treat AI-generated '
     'creative or technical work as automatically safe to use commercially without checking your '
     'organization’s current legal guidance, which may have changed since you last asked.'),
    ('Sector-specific rules are stricter than general ones.', 'Healthcare, finance, legal services, '
     'and hiring all carry additional AI-specific regulatory obligations beyond general business '
     'practice — if you work in or communicate for a regulated industry, the general rules in this '
     'chapter are a floor, not a ceiling, and your compliance function has the current specifics.'),
])
para(doc, 'None of this requires you to become a lawyer. It requires the same habit Chapter 9 taught '
    'for any fast-moving fact: date your understanding, and re-verify before it becomes load-bearing '
    'in a decision that matters. "AI policy" is not a thing you learn once in this course and carry '
    'unchanged into a twenty-year career; it is a live document you re-read.')

h1(doc, 'Writing assistants versus general chat tools')
para(doc, 'This chapter has mostly discussed general-purpose AI chat tools, but purpose-built writing '
    'assistants integrated into word processors, email clients, and messaging apps are a distinct '
    'category worth distinguishing, because the right level of trust differs between them.')
bullets(doc, [
    ('Integrated grammar and style tools', '(the descendants of spell-check) catch mechanical errors '
     'reliably and rarely fabricate — their scope is narrow enough that the failure modes this chapter '
     'emphasizes mostly do not apply. Use them liberally as a first pass, the way Chapter 4 already '
     'recommended treating any automated check: a smart detector, not a judge.'),
    ('Email and chat "smart compose" suggestions', 'predict short, routine continuations and are '
     'usually safe for genuinely routine content — but watch for the house-style flattening this '
     'chapter warned about: accepted suggestions accumulate into a voice that is nobody’s, including '
     'yours.'),
    ('General-purpose chat tools', '(the main subject of this chapter) carry the full range of '
     'capabilities and failure modes discussed throughout — the most powerful category and the one '
     'requiring the most active verification discipline.'),
    ('Specialized professional tools', '(legal research assistants, medical documentation tools, '
     'financial analysis copilots) sit in between: narrower scope than general chat tools, often with '
     'built-in citation or sourcing features, but still capable of confident errors within their '
     'domain and still requiring the verification pipeline for anything load-bearing.'),
])
para(doc, 'The practical rule: match your verification effort to the tool’s actual scope and track '
    'record, not to its marketing. A tool that only reorders your own sentences needs less scrutiny '
    'than one that generates new factual claims from a prompt — and knowing which one you are using, '
    'at any given moment, is itself part of the professional judgment this chapter is teaching.')

h1(doc, 'AI fluency as a hiring and career signal')
para(doc, 'Employers increasingly evaluate AI fluency directly — not "can you use ChatGPT," which is '
    'nearly universal now, but "do you use it with judgment." This shows up in interviews (Chapter 14) '
    'in specific, learnable ways worth preparing for explicitly.')
bullets(doc, [
    ('The direct question.', '"How do you use AI in your work?" rewards a specific, honest answer over '
     'a vague one: naming a real workflow (the critique loop on your own drafts, a research-sweep '
     'pattern you use routinely) beats either "I don’t really use it" (reads as behind) or "I use it '
     'for everything" (reads as undiscriminating).'),
    ('The verification probe.', 'Strong interviewers follow up with "how do you know the output was '
     'right?" — this is asking directly whether you run the verification pipeline this chapter '
     'teaches, or whether you trust fluency as a proxy for truth. Have a real example ready, per '
     'Chapter 14’s story-bank logic: a time AI output was wrong and you caught it.'),
    ('The disclosure question.', 'Some employers now ask directly about your personal disclosure '
     'practice — treat it exactly as you would the ethics questions in Chapter 8: a considered '
     'position, not a rehearsed slogan, demonstrates the judgment they are actually screening for.'),
])
para(doc, 'The broader point for a job search built on Chapter 13’s campaign logic: AI fluency is '
    'becoming a résumé-worthy skill in its own right, but only when it can be evidenced the way any '
    'achievement bullet must be evidenced — a real workflow, a real verification habit, a real '
    'outcome — not a claimed familiarity with a tool everyone already has access to.')

h1(doc, 'Case study: the cover letter that was too good')
para(doc, 'A hiring manager received a cover letter that was, by every visible measure, excellent — '
    'flawless prose, perfectly matched to the posting’s language, warm but professional in tone. It '
    'was also, she suspected within two paragraphs, entirely AI-generated from the job posting with '
    'no evidence the candidate had done any of the research Chapter 13 recommends: no specific '
    'company detail that couldn’t have been scraped from the posting itself, no evidence of the '
    'informational interviews or warm paths the campaign approach produces, and a strange, '
    'unplaceable uniformity of tone that echoed, faintly, every other AI-polished letter in the pile '
    'that week.')
para(doc, 'She could not prove it, and the letter violated no stated policy — but it also convinced '
    'her of nothing, because it demonstrated no evidence of fit beyond keyword matching a machine '
    'could perform on any candidate. The candidate was not interviewed, not because using AI was '
    'against the rules, but because the letter failed the job it was supposed to do: proving THIS '
    'candidate researched THIS company and connected THEIR evidence to THIS need (Chapter 13’s '
    'connection pattern). A second candidate’s letter, visibly less polished in places, named the '
    'specific product launch, referenced a real conversation with a current employee, and connected '
    'one clearly true achievement to one clearly named company problem. She got the interview.')
para(doc, 'The lesson is not "don’t use AI on cover letters" — this chapter has already endorsed '
    'AI-assisted drafting throughout. It is that polish was never the scarce resource the letter '
    'needed to supply. Evidence of genuine research and fit was, and that evidence has to come from '
    'the candidate’s actual work, not the tool’s ability to sound plausible. The chapter’s central '
    'metaphor, once more: the floor of prose quality rose to meet every candidate in that pile '
    'equally. The hiring manager was reading for the ceiling.')

h1(doc, 'AI in meetings, transcription, and institutional memory')
para(doc, 'AI meeting assistants — joining calls, transcribing, and drafting summaries — are now '
    'common enough to deserve their own etiquette, extending Chapter 11’s meeting craft into a new '
    'tool layer.')
bullets(doc, [
    ('Announce the bot.', 'A silent AI note-taker in a meeting is the recording-without-consent '
     'problem in a new costume; announce it at the start, exactly as you would announce that a call '
     'is being recorded, and let anyone object before it runs.'),
    ('Verify the summary before distributing.', 'AI meeting summaries confidently misattribute '
     'decisions and drop caveats — the same fabrication risk as any other AI output, now applied to '
     'what the ROOM agreed to. Chapter 11’s decision-minutes standard (decisions, owners, dates, read '
     'back in the room) still requires a human check before the summary becomes the official record.'),
    ('Keep the human read-back.', 'The AI transcript does not replace the facilitator’s spoken '
     '"recording: we renew, Maya drafts by the 12th" — it supplements it. The read-back catches '
     'contested wording live; the transcript catches it after the fact, when correction is expensive.'),
    ('Treat the raw transcript as a draft, not a record.', 'Full transcripts are searchable but '
     'unedited — casual remarks, half-finished thoughts, and speculation all get preserved with the '
     'same permanence as decisions (Chapter 5). Know your organization’s retention policy before '
     'relying on one.'),
])
para(doc, 'The upside is real: fewer meetings need a dedicated note-taker, freeing that person to '
    'participate, and searchable transcripts help absent teammates catch up (Chapter 5’s async-first '
    'principles). The discipline is the same one this whole chapter teaches — use it fully, verify '
    'before it becomes the record, and keep a human accountable for what the room actually decided.')

h1(doc, 'Case study: the AI customer-service rollout')
para(doc, 'A mid-size retailer deployed an AI chatbot to handle first-line customer inquiries, '
    'trained on the company’s policy documents and past support tickets. The rollout succeeded on '
    'volume metrics immediately — average response time dropped from hours to seconds — and failed '
    'on trust within three weeks, for reasons traceable directly to this chapter’s principles.')
para(doc, 'The bot, asked about a return outside the stated policy window, generated a plausible-sounding '
    'exception ("in cases of documented shipping delay, we extend the window by 14 days") that did '
    'not exist in any actual policy — it was a fluent, reasonable-sounding fabrication, indistinguishable '
    'in tone from the real policy text around it. Customers who received the fabricated answer and '
    'later had it denied by a human representative escalated as though they had been deliberately '
    'misled, because from their perspective they had been. The company had deployed a drafting tool '
    'as if it were a source of truth, skipping the verification layer this chapter insists on for any '
    'AI output — the difference being that here, no human was in the loop to catch it before it reached '
    'a customer.')
para(doc, 'The fix mirrors the agent-mandate case above: the bot’s scope was rewritten to separate '
    '"answer from verified policy text, quoting it directly" from "reason about edge cases," with the '
    'second category routed to a human every time. Response times rose slightly for edge cases and '
    'stayed low for the genuine majority of routine questions. The lesson for any business '
    'communicator evaluating an AI deployment: the question is never just "is it fast?" It is "where '
    'exactly does its mandate end, and what happens at that edge?" — the same question the agent '
    'section asks of a single analyst’s workflow, now asked of a system serving thousands of '
    'customers at once.')

h1(doc, 'Bias, fairness, and the training-data problem')
para(doc, 'Language models learn statistical patterns from enormous text corpora, and those corpora '
    'carry the biases of whoever produced and selected the text — historical, cultural, and '
    'demographic. This is not a hypothetical risk; it is a documented, measured property of these '
    'systems, and it has direct professional consequences wherever AI assists with hiring, '
    'performance evaluation, or any decision about people.')
bullets(doc, [
    ('Résumé and hiring screens.', 'AI tools used to screen or rank candidates can encode and amplify '
     'historical hiring patterns — including patterns an organization would explicitly disavow if '
     'stated outright. Any AI involvement in hiring decisions needs human review specifically for '
     'disparate impact, not just for accuracy (Chapter 13’s integrity standard, extended to the '
     'employer’s side of the table).'),
    ('Language and register bias.', 'Models trained predominantly on certain English registers can '
     'penalize or "correct" other legitimate professional registers and dialects, treating '
     'difference as error. When a tool flags phrasing as unprofessional, verify that judgment against '
     'Chapter 1’s actual audience-fit standard rather than accepting it as neutral truth.'),
    ('Representation in generated content.', 'AI-generated examples, images, and scenarios can default '
     'to narrow demographic assumptions unless prompted otherwise. In materials meant for a broad '
     'audience, review generated content for this the way you would review your own drafts for '
     'unreflective assumptions (Chapter 4’s bias-free language section).'),
])
para(doc, 'None of this argues against using the tools. It argues for treating AI output about or '
    'affecting people with the same scrutiny you would apply to a human decision-maker’s judgment — '
    'because the model’s "opinion" is, in a real sense, the aggregated and unexamined opinion of '
    'its training data, and unexamined aggregated opinion is exactly what professional judgment '
    'exists to check.')

h1(doc, 'Environmental and resource dimensions')
para(doc, 'Training and running large language models consumes significant computational resources — '
    'electricity and water for data-center cooling at a scale that has become a genuine point of '
    'public and corporate concern. This does not mean every individual query carries a meaningful '
    'footprint; a single email draft is not the same order of magnitude as training a new frontier '
    'model. It does mean that organizations adopting AI at scale increasingly face the same '
    'stakeholder questions this course’s value-based strategy chapter would predict: customers, '
    'employees, and regulators are beginning to ask about the resource cost of AI-heavy workflows '
    'the way they ask about any other operational choice with an environmental footprint. Professionals '
    'entering fields where AI adoption is heavy — and that is most fields, increasingly — should '
    'expect this to become a legitimate line item in vendor selection and public communication, not '
    'a fringe concern. Chapter 17’s value-stick framework applies here too: resource cost is simply '
    'another input to the willingness-to-sell calculation for the employees and communities a company '
    'depends on.')

h1(doc, 'A prompting pattern library')
para(doc, 'Rather than memorize rules, build a small library of prompt patterns for the tasks you '
    'actually repeat — the same instinct that built your Chapter 13 master résumé and Chapter 14 story '
    'bank. Five patterns cover most business drafting.')
bullets(doc, [
    ('The brief pattern.', '“Draft a [genre] for [audience] about [topic]. Key facts: [list]. Tone: '
     '[register]. Constraints: [length, format]. The reader’s main question is [X].” This is Chapter 2 '
     'in prompt form, and it produces usable first drafts because it supplies exactly what the model '
     'cannot infer.'),
    ('The critique pattern.', '“Read this draft as a skeptical [role — client, auditor, executive]. '
     'List the three weakest claims and the one thing most likely to get pushback.” Keeps you the '
     'author while borrowing the tool as a cold reader (Chapter 4’s reviewer, on demand).'),
    ('The translation pattern.', '“Rewrite this for a reader with no background in [field] — replace '
     'jargon, keep every fact.” Useful for layering technical content (Chapter 2’s audience layers) '
     'without losing precision — verify afterward that no fact was lost in translation.'),
    ('The single-sweep pattern.', '“Check only for [one error type — subject-verb agreement, '
     'unsupported claims, passive voice used as camouflage] in this document.” Narrow asks produce '
     'reliable results; broad asks (“fix this”) produce plausible but unverified rewrites.'),
    ('The options pattern.', '“Give me three different openings for this message, ranging from most '
     'direct to most cautious.” Preserves your choice at the decision point that matters most '
     '(Chapter 3’s emphasis), rather than accepting the tool’s single default.'),
])
para(doc, 'Keep the patterns that work for your field in a personal document — exactly the wiki habit '
    'Chapter 5 recommended for team knowledge, run for yourself. The prompt that reliably produces a '
    'good first draft of your weekly status report is worth more, saved, than re-deriving it from '
    'scratch every Monday.')

h1(doc, 'AI across the genres this course has taught')
para(doc, 'Every genre chapter in this course has an AI-assisted version worth naming explicitly, '
    'because the right use varies by genre in ways the general rules above only partly capture.')
bullets(doc, [
    ('Routine email and status updates (Chapters 5–6):', 'excellent AI territory. Brief it with the '
     'facts, verify every number and name, and check that your voice — not the house style — survived '
     'the edit pass.'),
    ('Negative and persuasive messages (Chapters 7–8):', 'draft with AI, but the tone pass MUST be '
     'human — the apology anatomy and the buffer craft require judgment about exactly this reader, '
     'this history, this relationship. Use the critique loop to pressure-test your buffer and your '
     'pivot, not to generate them from nothing.'),
    ('Reports (Chapters 9–10):', 'AI drafts sections well once you supply the pyramid — the answer, '
     'the reasons, the evidence — but it cannot build the pyramid FOR you from raw data without '
     'supervision, because the conclusion is a judgment call. Verify every figure against its source; '
     'never let the tool invent the executive summary’s number.'),
    ('Presentations (Chapter 12):', 'useful for slide-text tightening and speaker-note drafts; the '
     'takeaway sentence and the story must be yours, because they require knowing what THIS room '
     'needs to hear.'),
    ('Résumés and cover letters (Chapters 13–14):', 'AI can suggest phrasing and catch flab, but every '
     'number and achievement must be true and verifiable — Chapter 13’s integrity standard applies '
     'with zero exceptions, because the interview audits every line regardless of who typed it first.'),
])

h1(doc, 'Case study: the disclosure that wasn’t')
para(doc, 'A consulting analyst submitted a market analysis to a client, fully AI-drafted from her '
    'research notes, lightly edited, undisclosed — not because she intended deception, but because no '
    'one had discussed the norm and she assumed silence meant permission. The client’s internal team, '
    'running the same analysis independently, found a fabricated statistic: a plausible-sounding market '
    'growth figure that traced to no real source. When asked how the number was sourced, she could not '
    'produce an answer, because she had never verified it — the pipeline this chapter teaches had been '
    'skipped entirely.')
para(doc, 'The damage was compounding: the fabricated number, the inability to trace it, and the '
    'undisclosed process together read as either carelessness or dishonesty, and the client could not '
    'easily tell which. Her firm’s repair required two changes, not one. First, the verification '
    'pipeline became mandatory for all client deliverables, AI-assisted or not — every load-bearing '
    'claim flagged, traced, fixed, or cut. Second, the firm adopted an explicit disclosure line for '
    'AI-assisted work, removing the ambiguity that had let a reasonable analyst make an unreasonable '
    'assumption. The lesson generalizes past this one incident: the failure was not using AI. It was '
    'skipping the two non-negotiables — verify, and disclose by stakes — that make using it safe.')

h1(doc, 'Five myths, retired')
para(doc, 'Retired by the mechanism itself: a model that predicts plausible text will occasionally '
    'produce implausible-but-true statements and plausible-but-false ones with identical confidence. '
    'Fluency is not a truth signal, ever, regardless of how the sentence is phrased.',
    bold_lead='Myth: if it sounds confident, it’s probably right.')
para(doc, 'Retired by every professional integrity policy converging on the same answer: submitting '
    'AI output as your own assessed work is the violation, not using the tool during preparation. The '
    'boundary is disclosure and verification, not the existence of assistance.',
    bold_lead='Myth: using AI at all is academically dishonest.')
para(doc, 'Retired by the never-delegate list: genres where the drafting IS the sincerity cannot be '
    'automated at any quality level, because the automation removes the fact the message exists to '
    'convey — that a human paused, owned, or observed.', bold_lead='Myth: better models will eventually handle even goodwill messages.')
para(doc, 'Retired by the two-analysts case: identical tool access produced opposite career '
    'trajectories, because the variable was verification discipline, not capability. The tool is not '
    'the differentiator; the operator is.', bold_lead='Myth: everyone with the same AI tools has the same advantage.')
para(doc, 'Retired by the appreciation portfolio: judgment, verification, briefing, relationships, '
    'and editing are precisely the skills this course teaches, and none of them are touched by better '
    'autocomplete. The tools changed the floor. They did not touch the ceiling, and the ceiling is '
    'what careers are actually built on.', bold_lead='Myth: AI makes communication courses obsolete.')

h1(doc, 'Frequently asked questions')
para(doc, 'When the stakes are yours to own regardless: use it freely for drafting, critique, and '
    'research assistance, provided you verify and can defend every claim. Skip it — or disclose '
    'explicitly — when the assignment is specifically assessing your unaided skill, per your '
    'instructor’s stated policy.', bold_lead='When exactly should I use AI on a graded assignment?')
para(doc, 'Neither reliably: current detection tools produce both false positives (flagging your own '
    'authentic writing) and false negatives (missing AI text that was lightly edited). The more '
    'durable standard is verification and disclosure practiced consistently, which survives regardless '
    'of what detection technology can or cannot currently catch.', bold_lead='Can AI detectors reliably catch AI-written work?')
para(doc, 'Verify it exactly like any other claim: check the paper exists, check it says what is '
    'claimed, and check the claim is representative rather than cherry-picked. Treat AI-suggested '
    'sources as leads to confirm, never as citations to use directly (Chapter 10’s ladder, rung five).',
    bold_lead='What do I do if I’m not sure whether a source AI gave me is real?')
para(doc, 'Follow your organization’s policy first; where none exists, disclose when the work trades '
    'on your personal expertise or when a reasonable reader would want to know. When genuinely '
    'unsure, ask directly — the conversation itself is usually short, and asking is itself a '
    'professional signal.', bold_lead='My employer has no AI policy. What should I do?')

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Run the critique loop on something you have already written this term: ask the tool to name its '
    'three weakest points, and evaluate which flags were real and which were noise.',
    'Draft your personal never-delegate list, starting from this chapter’s three and adding your own. '
    'State the principle behind each addition, not just the item.',
    'Write a one-paragraph agent mandate for something you would actually want automated (your inbox, '
    'your calendar, your reading queue). Trade with a classmate and hunt each other’s loose lines.',
    'Draft the disclosure sentence you would actually use in your field, and test it against the '
    'publicity test: would it survive being said aloud to the person it concerns?',
    'Pick one real task this week and automate it fully, verification pipeline attached. Note what the '
    'tool got wrong — that note is worth more than the task itself.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'The chapter argues AI raises the floor without moving the ceiling. Find a counterexample — a '
    'skill this metaphor mishandles — and explain where the floor/ceiling model breaks down.',
    'Where should your field’s disclosure norm land, given the stakes-based default this chapter '
    'proposes? Draft the actual policy sentence you would want your employer to adopt.',
    '“This feels AI-written” is becoming a common critique. Construct the test that separates a '
    'legitimate quality concern from an ad hominem about origin.',
    'The agent case blames a badly scoped mandate rather than the technology. Rewrite that mandate '
    'so the failure becomes structurally impossible — what exactly changes?',
    'Argue both extremes — “AI changes nothing important about this course’s skills” and “AI makes '
    'most of this course obsolete” — then state and defend your own position.',
])

keyterms(doc, [
    ('Floor and ceiling', 'the metaphor for AI’s effect on writing: competent prose gets cheap (the '
     'floor rises); judgment about truth and stakes does not (the ceiling is unmoved).'),
    ('Prediction mechanism', 'the plain-language model of how language models work — predicting '
     'plausible next words — that explains both their fluency and their confident errors.'),
    ('Critique loop', 'drafting yourself and asking AI to attack the draft, preserving authorship '
     'while borrowing the tool’s tirelessness as a red-team reviewer.'),
    ('House style', 'the recognizable default AI prose register — smooth, hedged, padded — that '
     'readers are increasingly able to name and discount.'),
    ('Verification pipeline', 'flag, trace, fix, own — the four-step process for auditing every '
     'load-bearing claim in an AI draft before it ships under your name.'),
    ('Fabricated citation', 'a properly formatted reference to a source that does not exist — AI’s '
     'signature failure mode, surviving every check except opening the source.'),
    ('Never-delegate list', 'goodwill messages, apologies, and performance feedback — genres where '
     'the drafting IS the sincerity, and automation erases the content regardless of the words produced.'),
    ('Agent', 'an AI system that acts (sends, schedules, purchases, publishes) rather than merely '
     'drafting — accountability for its actions remains with the human who authorized it.'),
    ('Mandate', 'the written scope of an agent’s authority: what it may do, must ask about, and must '
     'never touch — executed literally, including its ambiguities.'),
    ('Appreciation portfolio', 'the skills that grow more valuable as drafting gets cheap: judgment, '
     'verification, the brief, relationships, and editing.'),
])

quiz(doc, [
    ('The "floor and ceiling" metaphor claims that AI:',
     ['Eliminates the need for writing skill entirely', 'Raises the quality of routine drafting while leaving judgment untouched',
      'Only helps with grammar, not content', 'Makes verification unnecessary']),
    ('AI confidently fabricates facts and citations because:',
     ['It is deliberately deceptive', 'It predicts plausible text; fluency is the product, truth is incidental',
      'Its training data is too small', 'Users prompt it incorrectly']),
    ('The "junior colleague" mental model implies that AI drafts should be:',
     ['Sent without review to save time', 'Reviewed exactly as a new hire’s work would be — used fully, verified always',
      'Avoided entirely for important work', 'Used only for final, polished output']),
    ('The critique loop differs from the generate loop because the writer:',
     ['Never touches the AI tool', 'Drafts first and asks AI to find weaknesses, preserving authorship',
      'Only uses AI for citations', 'Publishes the AI’s first draft unedited']),
    ('The three items on the never-delegate list share which property?',
     ['They are too complex for AI', 'The drafting itself IS the sincerity — automation erases the content regardless of wording',
      'They require legal review', 'They are rarely written in the workplace']),
    ('Pasting client data into a public AI tool should be treated as:',
     ['Harmless since chatbots forget conversations', 'Disclosure to an external service, governed by the same confidentiality rules as any outside party',
      'Acceptable if no names are used', 'A problem only in regulated industries']),
    ('An AI agent differs from a drafting tool because it:',
     ['Cannot make errors', 'Takes actions (sending, purchasing, publishing) that are attributed to its human authorizer',
      'Requires no oversight', 'Only works with text, never other actions']),
    ('The agent-mandate case study’s central lesson is that agents:',
     ['Should never be used for email', 'Execute the mandate as written, not as intended — precision in scoping matters',
      'Are safe once enterprise-licensed', 'Require no human review of any kind']),
    ('A fabricated citation is dangerous specifically because it:',
     ['Is always obviously wrong', 'Passes every check except opening the actual source', 'Only appears in academic writing', 'Is illegal to generate']),
    ('The skills chapter identifies as "appreciating" in value all have one thing in common:',
     ['They are unrelated to this course', 'Each is untouched by AI’s drafting mechanism — judgment, verification, briefing, relationships, editing',
      'They require no practice', 'They are only relevant to executives']),
], ['b','b','b','b','b','b','b','b','b','b'])

references(doc, [
    'Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of '
    'stochastic parrots. Proceedings of FAccT 2021, 610–623.',
    'Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. Stanford '
    'CRFM/HAI technical report.',
    'Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative '
    'artificial intelligence. Science, 381(6654), 187–192.',
    'OpenAI, Anthropic, and Google DeepMind model documentation and usage policies (consult current '
    'published guidance — practices evolve quickly in this area).',
    'Susskind, R., & Susskind, D. (2015). The future of the professions. Oxford University Press.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch15-study-guide.docx')
finish(doc, os.path.abspath(out))
