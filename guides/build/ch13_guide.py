# Chapter 13 study guide — The Job Search and Résumés in the Digital Age (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(13, 'The Job Search and Résumés in the Digital Age',
    'The search as a campaign · bullets that sell · the ATS game · the digital layer that interviews first')

h1(doc, 'Why this chapter exists')
para(doc, 'This is the chapter where the course stops being about hypothetical messages and starts being '
    'about you. The job search is a full-stack communication project: research (Chapter 9), persuasion '
    '(Chapter 8), document craft under merciless scanning conditions (Chapters 3 and 4), relationship '
    'building (Chapters 6 and 11), and a digital footprint that gets read before you do (Chapter 5). '
    'Every skill in the course converges here, pointed at the highest-stakes audience you will ever '
    'write for: the stranger deciding whether you get a conversation.')
para(doc, 'Hold one reframe through the whole chapter: you are not asking for a job. You are proposing a '
    'transaction in which an employer exchanges salary for problems solved — which makes your application '
    'a proposal (Chapter 10), your résumé its evidence section, your cover letter its executive summary, '
    'and yourself the deliverable. Proposals get funded when they speak to the buyer’s needs in the '
    'buyer’s language with checkable evidence. So do candidates. The self-respect this reframe carries is '
    'not a pep talk; it is structurally accurate, and it will improve every document you produce.')
para(doc, 'One more orientation point: the modern search is mediated by software. An applicant tracking '
    'system (ATS) parses your résumé into a database record before any human sees it, and recruiters '
    'search those records the way you search anything. This changes formatting rules, keyword strategy, '
    'and file mechanics in specific, learnable ways — none of which excuse weak content, and all of '
    'which can bury strong content when ignored. The chapter covers both layers: the machine that '
    'surfaces you and the human who scans you.')

h1(doc, 'The search as a campaign')
figure(doc, os.path.join(FIG, 'ch13_campaign.png'),
    'Figure 1. The volume game versus the campaign — effort concentrated beats effort scattered.',
    'Two panels contrast the volume game (the same résumé to two hundred postings, no research, converting at '
    'lottery rates) with the campaign (fifteen to twenty-five researched targets, tailored applications, warm paths '
    'before portals), with the note that three tailored applications a week beats thirty in a panicked weekend.')
para(doc, 'The instinctive search strategy — one résumé, two hundred portals, hope — feels productive '
    'because it generates activity metrics. It converts terribly, because it competes at the widest point '
    'of every funnel with zero signal of fit: the untailored application announces, accurately, that its '
    'sender knows nothing particular about the employer and sent the same document everywhere. The '
    'campaign inverts the arithmetic: fifteen to twenty-five researched targets that genuinely fit, each '
    'application tailored to the posting’s own language, warm paths hunted before the portal is touched. '
    'Slower per application; wildly better per offer — and, not incidentally, far better for morale, '
    'because a campaign produces learnable feedback while a volume spray produces only silence.')
para(doc, 'Define the role family first — “quality roles in medical devices,” “financial analysis in '
    'healthcare” — because focus is what makes research possible. Then research each target with '
    'Chapter 8’s discipline: their products, their pain, their language. The job posting itself is a '
    'requirements document (Chapter 10’s RFP, at personal scale): read it with a highlighter, harvest '
    'the repeated nouns and must-haves, and treat those exact phrases as your keyword list, your cover '
    'letter’s vocabulary, and your interview prep. Tier the list — dream targets get the full campaign '
    'treatment; solid fits get strong tailoring; everything else is not on the list, which is the point '
    'of having one.', bold_lead='Build the target list like an analyst.')
para(doc, 'One sheet, one row per application: company, role, date sent, résumé version, contact, '
    'status, next action. The search is a project; Chapter 9 taught you to run projects on visible '
    'status. Every application gets a follow-up date assigned at submission (two silent weeks earns a '
    'polite nudge). Version tracking earns its keep fast: when the analyst-flavored résumé draws '
    'callbacks and the coordinator-flavored one draws silence, the spreadsheet just told you something '
    'the individual rejections never would. And the tracker enforces sustainable cadence — three '
    'tailored applications a week, every week, beats thirty in a panicked weekend, for conversion and '
    'for sanity alike.', bold_lead='Track the pipeline.')
para(doc, 'Referred candidates convert to interviews at several times the portal rate at most employers, '
    'for a rational reason: a referral is borrowed trust — someone the employer already believes has '
    'staked a sliver of credibility on you. “Warm” does not require being wired: alumni of your program, '
    'former colleagues and supervisors, the guest speaker whose session you asked a question in, your '
    'roommate’s manager — second-degree paths are everywhere once you map them deliberately. The ask is '
    'small and specific (Chapter 8’s calibrated rung): “would you be willing to submit my résumé for '
    'requisition 4471?” — never the unanswerable “can you get me a job?” And sequence matters: work the '
    'path BEFORE applying when you can, because a referral attached to a fresh application beats one '
    'chasing a two-week-old rejection through the system.', bold_lead='Warm paths move résumés.')

h1(doc, 'Networking without the ick')
para(doc, 'Students hate the word “networking” because they picture its transactional caricature: working '
    'a room, collecting contacts, extracting favors. The professional reality is closer to structured '
    'curiosity — small honest asks of people positioned to answer them — and it runs on machinery you '
    'already own: Chapter 6’s request craft, Chapter 1’s listening, Chapter 8’s laddering. The reframe '
    'that dissolves the ick: you are not asking for a job; you are asking for twenty minutes of '
    'perspective from someone who has the view you need. People genuinely like giving advice. The '
    'informational ask flatters honestly — “you have done what I am attempting” — and costs its giver '
    'almost nothing.')
para(doc, 'The ask: “Could I take twenty minutes to ask how you got from QA tech to quality '
    'manager?” Specific, small, dated, and true. Come with five real questions and ask three, spending '
    'the savings on listening: their path, what the work is actually like at 2 p.m. on a Tuesday, what '
    'separates the good hires from the great ones. Never ambush with a job request — the meeting’s '
    'integrity is the meeting’s value, and the informational that stays informational produces more '
    'referrals than the one that pivots, precisely because the giver leaves feeling consulted rather '
    'than used. If they offer to pass your résumé along, that is their move to make, and they make it '
    'more often than you would guess. Close the loop twice: thanks within a day, and the “your advice '
    'worked — here’s what I did with it” note weeks later. The second note is the one nobody sends and '
    'everybody remembers.', bold_lead='The informational interview.')
para(doc, 'The cold or lukewarm outreach message is Chapter 8’s cold email at personal scale, and it is '
    'five sentences long. The connection element goes first — “Dr. Reyes suggested I reach out,” '
    '“fellow alum working in med devices” — because warmth is the subject line’s job. Then one '
    'sentence of who you are, one of why THEM specifically (“your path from bench to management is the '
    'one I’m trying to understand”), the small dated ask, and the friction remover: “any twenty minutes '
    'in the next two weeks — I’ll work around your calendar.” The life story stays home. This is a '
    'knock, not a memoir.', bold_lead='The outreach message.')
para(doc, 'Networks run on Chapter 11’s trust-account arithmetic, which means the maintenance is '
    'give-first: send the article that fits their project, make the introduction they would want, '
    'congratulate the promotion (five-quality rules, Chapter 6) — all with no ask attached. Keep loose ties '
    'warm cheaply: a two-line check-in twice a year keeps a contact live, while five years of silence '
    'followed by a favor request reads as exactly what it is. The research backs the practice twice '
    'over: weak ties carry a disproportionate share of job information (Granovetter’s classic finding), '
    'and habitual givers end up overrepresented at the top of success distributions (Grant, Chapter 6). '
    'Build the network during employment; it is the one you will need between jobs.',
    bold_lead='Give first, always.')

h1(doc, 'Résumé strategy: one document, one job')
figure(doc, os.path.join(FIG, 'ch13_scan.png'),
    'Figure 2. The seven-second scan — design for where the eyes actually go.',
    'Four rows: the top third (name, summary, current title), the left edge (titles, employers, dates, bolded lead-ins), '
    'numbers (digits catch scanning eyes), and everything else (read only if the scan earns a second pass).')
para(doc, 'Recruiter eye-tracking research consistently finds the first résumé pass lasts seconds — a scan '
    'of names, titles, dates, and keywords, traveling the same F-pattern Chapter 3 taught you to design '
    'for. Three consequences cascade. Design: your best material lives in the top third and along the '
    'left edge, because that is where the scan goes. Writing: every bullet competes for a seconds-long '
    'audition, so flab does not lose slowly — it loses instantly. Strategy: the résumé’s job is not to '
    'get you the job; it is to survive the scan and get you the conversation. Everything else about the '
    'document follows from that one-sentence job description.')
para(doc, 'Four properties define the genre. It is an advertisement for an interview, not an '
    'autobiography — completeness is not a virtue; relevance is the only virtue, and the childhood '
    'paper route goes. It is a claims document that will be audited: every line is fair game in the '
    'interview (Chapter 14 is that audit), so write nothing you cannot discuss for five minutes. It is '
    'tailored per target family from a master document — the master holds every bullet you have ever '
    'earned; each sent version selects and reorders for THIS posting, which converts tailoring from a '
    'three-hour rewrite into a twenty-minute selection. And it is judged as a writing sample first: '
    'before anyone weighs your experience, they have weighed your formatting, your precision, and your '
    'typos. Chapter 4’s verification pass, at maximum personal stakes.', bold_lead='What a résumé is.')
para(doc, 'Reverse-chronological — experience newest-first with dates — is the default: recruiters '
    'expect it, and ATS parsers handle it best. The hybrid adds a skills-forward summary block above the '
    'chronology and earns its keep for career changers and thin-experience starters, leading with what '
    'transfers before the dates tell their story. The pure-functional format — skills only, no dated '
    'history — should be avoided entirely: recruiters read it as concealment, because that is '
    'overwhelmingly what it is used for, and the format choice itself becomes a red flag. Handle gaps '
    'with honest brevity instead (the integrity section below), not with formats designed to hide them.',
    bold_lead='Format: chronological or hybrid.')
para(doc, 'Top to bottom: the header (name large; city, phone, professional email, LinkedIn URL — no '
    'street address, no photo under U.S. norms, and never the word “Résumé” as a title). The optional '
    'summary line — one tailored sentence of what you are, your strongest credential, and what you are '
    'aimed at: “Finance graduate with two audit internships and advanced Excel, targeting analyst roles '
    'in healthcare.” It is your pyramid summit (Chapter 9); earn it or cut it, because “motivated '
    'professional seeking opportunities” spends the scan’s best seconds on nothing. (The objective '
    'statement — a paragraph about YOUR hopes — died a decade ago; do not exhume it.) Then experience, '
    'newest first: title, employer, dates, and the achievement bullets that are the document’s entire '
    'engine. Education — degree, school, date, GPA if strong and recent — flips above experience for '
    'current students. Skills last: concrete and checkable (software, languages, certifications), never '
    'traits (“hard worker” is a claim only bullets can prove).', bold_lead='Anatomy.')

h1(doc, 'Bullets that sell: the achievement engine')
figure(doc, os.path.join(FIG, 'ch13_bullet.png'),
    'Figure 3. The achievement bullet formula — action verb, task, measurable result.',
    'A three-part flow: action verb (Cut), the task (intake errors, by redesigning the tracking checklist), and the '
    'result (errors down 38 percent, zero audit findings), over the contrast: a duty bullet could be written by any '
    'holder of the job; an achievement bullet can only be written by you.')
para(doc, 'The résumé is won or lost at the bullet level, and the winning shape has three parts: an '
    'action verb first (led, built, cut, redesigned — past tense, never “responsible for”), the task '
    '(what you actually did, specifically), and the result (what changed because you did it, with the '
    'number when it has one). “Cut intake errors 38% by redesigning the sample-tracking checklist” '
    'audits perfectly against the shape. So does “Grew Instagram engagement 60% in one semester by '
    'shifting to short-form video.” The diagnostic for the failing version is brutal and useful: if any '
    'holder of the job could have written the bullet — “responsible for social media accounts,” '
    '“handled customer complaints” — it describes the job, not you. Achievement bullets can only be '
    'written by you. That is the entire difference, and the interview will be conducted almost entirely '
    'about the bullets that pass the test.')
para(doc, 'Numbers survive the scan; adjectives do not (Figure 2, and Chapter 4’s abstraction ladder '
    'wearing a suit). Quantify results where they exist — percentages, dollars, counts, time. Quantify '
    'SCALE where results were not yours to claim: “processed 200 orders daily,” “served an 80-seat '
    'dining room,” “supported a team of 6” — responsibility has a size even when outcomes belong to the '
    'team. Reconstruct honestly: count what is countable, estimate conservatively, and be ready to '
    'explain the basis, because “about 30 escalations a week” is defensible and invented precision is '
    'not (Chapter 9’s calibration). Where no number exists at all, name the outcome: “adopted by two '
    'other departments,” “still in use three years later.” Results without digits are still results.',
    bold_lead='Quantify everything quantifiable.')
para(doc, 'Tailoring is translation, not fabrication. Mirror the posting’s exact nouns — if they say '
    '“stakeholder communication” and your bullet says “client relations,” the keyword match (machine '
    'AND human) just missed, even though you meant the same thing. Reorder by their priorities: their '
    'must-haves rise into your top bullets; the achievement you love that they did not ask about sinks. '
    'The master-résumé workflow makes this sustainable: every bullet you have ever earned lives in one '
    'evergreen document, and each application is a selection pass, not a rewrite. Twenty minutes, '
    'honestly spent, per application — the campaign cadence depends on exactly this economy.',
    bold_lead='Tailoring: the posting is the answer key.')
para(doc, 'Early-career readers discard their best material because it did not happen in an office, and '
    'this section exists to stop them. Course projects count: “built a discounted-cash-flow model for a '
    '40-page equity report (team of 4, graded A)” is real analytical work with a named deliverable. '
    '“Unrelated” jobs never are: the barista who trained new hires, balanced a drawer, and held the line '
    'through the morning rush has supervision, cash controls, and composure under load — write THOSE, '
    'not the espresso. Leadership is a function, not a title: organized, scheduled, recruited, rebuilt '
    'the budget — the club treasurer has a finance bullet. The floor is honesty, not grandeur: small '
    'and true beats inflated every time, because Chapter 14 visits every line.',
    bold_lead='Early-career: you have more than you think.')

h1(doc, 'The ATS game')
figure(doc, os.path.join(FIG, 'ch13_ats.png'),
    'Figure 4. How the applicant tracking system reads you — parse, match, rank, and only then the human scan.',
    'A four-step flow: parse (your file becomes a database record), match (recruiters search keywords and filters), '
    'rank (high-match records surface), human scan (the seven-second read) — with the warning that parse failure '
    'means invisibility.')
para(doc, 'Demystify the machine and its rules become obvious. An ATS parses your file into a database '
    'record — name, employers, titles, dates, skills — and recruiters then search and filter those '
    'fields like any database. It does not “reject” with judgment; it ranks by match, and a low-keyword '
    'résumé is not declined — it simply never surfaces, which produces the same silence with less '
    'ceremony. Parse failure is the deeper trap: content the parser cannot extract (tables, text boxes, '
    'multi-column layouts, headers and footers, graphics) does not exist in your record at all. The '
    'human scan still follows for everyone who surfaces — you are writing for the machine first and the '
    'human second, in that order, with the same document.')
bullets(doc, [
    ('Harvest and mirror keywords honestly.', 'The posting’s repeated nouns are the search terms. Use '
     'their exact forms at least once; spell out AND abbreviate (“applicant tracking system (ATS)”) '
     'because you cannot know which form gets searched. Claim only what you can interview on — the '
     'keyword that surfaces you and the lie that sinks you can be the same word.'),
    ('Format for the parser.', 'Single column. Standard headings (“Experience,” “Education,” “Skills”) — '
     'the parser navigates by exactly these signposts. Standard fonts, real bullet characters, dates in '
     'one consistent MM/YYYY format. Nothing load-bearing in headers or footers.'),
    ('Skip the designer templates.', 'The prettiest résumés for sale online — icons, columns, skill '
     'meters, portrait sidebars — are the least parseable documents in the pile. Boring formatting is '
     'a feature. Save the visual talent for your portfolio.'),
    ('Submit what the posting asks for.', '.docx or PDF as instructed; when unstated, .docx is the '
     'safer parse. Name the file for the recipient: “Okafor-Resume-QualityAnalyst.docx” (Chapter 4’s '
     'attachment rule).'),
])
para(doc, 'On length: one page for early career — the second page of a thin history reads as padding, '
    'and the scan never reaches it. Two pages when genuinely earned, with page one able to stand alone. '
    'Either way, whitespace is scan infrastructure, not wasted space: readable margins and type beat '
    'the sixth bullet you crammed in by shrinking the font, because that bullet cost you the five '
    'above it.', bold_lead='One page or two.')

h1(doc, 'Cover letters: connection, not recap')
figure(doc, os.path.join(FIG, 'ch13_coverletter.png'),
    'Figure 5. The cover letter skeleton — hook, evidence, company clause, close.',
    'Four rows: the hook (their role plus your thesis), the evidence (two proofs aimed at their two biggest needs), '
    'the company clause (one sentence proving research), and the close (a confident ask for the conversation).')
para(doc, 'The cover letter’s job is the one thing the résumé cannot do: connect your evidence to THIS '
    'employer’s specific need, in prose, with a voice. It is a persuasive message (Chapter 8) where the '
    'product is you — three to four paragraphs, one page hard, and never a paragraph-form recap of the '
    'résumé the reader is already holding. When close calls get decided, this document decides them; it '
    'is also the purest writing sample in your application, which this course has now qualified you to '
    'treat as an advantage.')
para(doc, 'Three working openers, one anti-pattern. Lead with the fit: “Your quality analyst posting '
    'asks for audit experience and LIMS fluency — my two internships were exactly that combination.” '
    'Lead with the warm path when you have one: “Dr. Reyes suggested I contact you about the analyst '
    'opening” — the referral is the strongest first sentence in the genre. Or lead with their world: '
    '“Your Fargo expansion doubles your sample volume — that scaling problem is what my capstone '
    'modeled.” The anti-pattern is the autobiography opener (“I am a recent graduate of…”), which '
    'spends the hook position on information the résumé header already delivered.', bold_lead='Openings.')
para(doc, 'The middle paragraphs run the connection pattern: their need, named, then your evidence, '
    'matched. “You need someone who can run supplier audits solo by Q2. At Medline I ran the last four '
    'of my internship unassisted — including the corrective-action follow-ups.” Two of those pairings '
    'and the letter has done its whole job, because you have performed the recruiter’s fit-analysis FOR '
    'them. Add the company clause — one sentence proving you researched THEM specifically — and close '
    'with a confident ask for the conversation. Then proofread it like the writing sample it is.',
    bold_lead='The middle and close.')

h1(doc, 'The digital layer')
figure(doc, os.path.join(FIG, 'ch13_audit.png'),
    'Figure 6. The consistency audit — résumé, profile, and search results must tell one story.',
    'Three panels (the résumé’s paper story, the profile’s searchable story, and page-one search results) above the '
    'warning that dates and titles must match, because recruiters cross-check as a screening step.')
para(doc, 'You will be searched — assume it, because it is standard screening practice — so the only '
    'question is what they find. The professional profile is a landing page: a headline that says what '
    'you do and seek (“Finance graduate — audit & analysis | seeking healthcare analyst roles”), a '
    'competent current photo (the empty silhouette reads as a ghost account), and an About section that '
    'is your summary line expanded to three human sentences. Posting activity is optional; coherence is '
    'not. Run the consistency audit: search your own name, logged out, on two engines, and know page '
    'one before a recruiter does. Dates and titles must MATCH the résumé — discrepancies read as '
    'dishonesty even when they are sloppiness. Clean what is reachable, and remember Chapter 5’s '
    'permanence rule means “clean” is partial: consistency matters more than perfection, and the goal '
    'is that the person online and the person on paper are obviously colleagues.')
para(doc, 'Claims are cheap and artifacts are proof: one linked work sample outweighs three adjectives. '
    'Curate three to five best pieces — the analysis, the deck, the report — each framed in two lines '
    '(the problem, your move, the result: a STAR in caption form, previewing Chapter 14). Scrub before '
    'publishing: employer data, client names, and anything confidential gets anonymized or excluded, '
    'because showing your work must never mean leaking someone else’s (Chapter 5). And notice that '
    'this course has been quietly building your portfolio all term: the capstone feasibility report '
    '(Chapter 10) IS a portfolio piece. Write it knowing that.', bold_lead='Show the work.')

h1(doc, 'Integrity and the supporting cast')
para(doc, 'Résumé fraud has a property that makes it uniquely irrational: it survives hiring and '
    'detonates later. The inflated degree, the invented title, the stretched dates — all discoverable '
    'by a background check or a casual reference call, and all grounds for termination YEARS after '
    'hire, at whatever moment is maximally expensive. The gray areas are not gray: “anticipated” '
    'degrees dated as earned, solo credit for team work, gaps papered over with elastic dates. Frame '
    'honestly instead — a gap gets one true clause (“family caregiving, 2024”) and recruiters handle '
    'honest gaps routinely; what they never forgive is the discovered cover-up, which converts a '
    'neutral fact into a character verdict (Chapter 7’s pattern). The standard for every line: it '
    'survives a reference call to the person who was there. Write to that audit and the interview '
    'holds no fear.', bold_lead='The fireable lie.')
para(doc, 'References are a managed asset, not an afterthought. Ask permission with the phrasing that '
    'engineers a graceful exit: “Would you be comfortable being a STRONG reference for quality roles?” '
    '— the word “comfortable” lets a lukewarm reference decline, which protects you from the tepid '
    'endorsement everyone can hear (Chapter 6’s recommendation rules, from the other side). Brief them '
    'per application: the posting, your résumé version, what the employer will care about — a prepared '
    'reference is twice the reference. Never list anyone who has not said yes recently, and close the '
    'loop with outcomes and thanks regardless of result. References are network deposits with '
    'compounding interest.', bold_lead='References: ask, brief, thank.')

h1(doc, 'Case study: two candidates, one interview slot')
para(doc, 'Same degree, same GPA, comparable internships — a recruiter with one slot and two plausible '
    'files. Candidate A’s experience section: “Responsible for quality documentation and assisting '
    'with audits. Duties included maintaining files and supporting the quality team as needed.” '
    'Candidate B’s: “Maintained the document control system for 200+ SOPs; supported four supplier '
    'audits — flagged a labeling gap that became a corrective action.”')
para(doc, 'Run the seven seconds honestly. In A, the scan finds “responsible for,” “duties included,” '
    '“as needed” — job-description language that any holder of the position could have written, '
    'carrying zero digits and zero events. In B, it finds 200+, four, and a result with a name '
    '(“became a corrective action”). B is not more experienced; B is better WRITTEN — the same months, '
    'audited into evidence. B interviewed. A received the form email, and — this is the part worth '
    'sitting with — never learned why, because volume-game feedback is silence. The difference between '
    'the two files is precisely the content of this chapter, applied or not.')
bullets(doc, [
    ('The lesson about writing:', 'the variable was never the experience. It was the writing about the '
     'experience — which means the fix is in your hands before your next application.'),
    ('The lesson about evidence:', 'B’s bullets survive the audit: every number has a basis, every '
     'event has witnesses. Achievement writing and honesty are the same discipline, not a trade-off.'),
    ('The lesson about feedback:', 'rejections rarely explain themselves. The campaign’s tracker and '
     'version data are how you manufacture the feedback the process withholds.'),
])

h1(doc, 'Case study: the career changer’s ninety-day campaign')
para(doc, 'A restaurant general manager — eleven years, two locations, consistently strong stores — '
    'decided to move into corporate operations analysis. The volume-game version of her search had '
    'already failed before she changed methods: five weeks, sixty applications, two auto-rejections '
    'and fifty-eight silences. Her résumé led with “Restaurant General Manager” twice and a duties '
    'paragraph; every ATS keyword search for “operations analyst” sailed past it. She was not '
    'unqualified. She was untranslated.')
para(doc, 'The campaign rebuild took one weekend and ran ninety days. Role family: operations analysis '
    'in food-adjacent industries, where her domain knowledge was an asset rather than a category '
    'error. Target list: nineteen companies — distributors, food-service tech, franchise groups. The '
    'master résumé got the hybrid format: a skills-forward block (P&L management, scheduling '
    'optimization, inventory analytics, vendor negotiation) above the chronology, and every bullet '
    'rewritten on the formula with numbers she reconstructed from eleven years of weekly reports: '
    '“cut food cost 3.1 points in one year by rebuilding par levels from sales data” · “reduced '
    'weekly scheduling overruns 22% with a demand-based template later adopted by a second location.” '
    'The words “operations,” “analysis,” and “data” — the posting language of her target family — '
    'appeared wherever they were honestly true.')
para(doc, 'The networking layer did the heavy lifting. Two informational interviews (a supplier’s '
    'account manager she had negotiated with for years; an alumna in franchise analytics) produced '
    'vocabulary corrections (“call it ‘demand forecasting,’ not ‘guessing the rush’”), one warm '
    'referral, and — from the alumna — the observation that her scheduling template was, functionally, '
    'a forecasting model and belonged in a portfolio. She wrote it up as a two-page case (problem, '
    'method, result — Chapter 9’s shape), scrubbed of employer data, and linked it from her profile, '
    'whose headline now read “Operations leader moving into ops analytics — 11 years of P&L, '
    'forecasting, and inventory optimization in multi-unit food service.”')
para(doc, 'Ninety days: nineteen targets, fourteen tailored applications, two referrals, five '
    'first-round interviews, two finals, one offer — analyst, food-service distribution, at a modest '
    'pay cut she had planned for and recovered within two years. The postscript is the chapter in '
    'miniature: the hiring manager told her the two-page scheduling case was what moved her file — '
    '“everyone claims analytical skills; you attached evidence.” Nothing in her history changed in '
    'those ninety days. The translation did.')

h1(doc, 'Worked example: one posting, one tailored application')
para(doc, 'To make the workflow concrete, here is the twenty-minute tailoring pass, step by step, for a '
    'real-shaped posting: “Quality Assurance Analyst — medical device manufacturer. Requirements: '
    'document control experience; internal or supplier audit exposure; CAPA familiarity; Excel '
    'proficiency; strong written communication.”')
numbered(doc, [
    'Harvest the keywords (three minutes): document control · audit (internal/supplier) · CAPA · '
    'Excel · written communication. These five phrases, in their exact forms, must appear where '
    'honestly true.',
    'Select from the master résumé (five minutes): the 200+ SOP document-control bullet rises to '
    'position one. The supplier-audit bullet with the corrective-action result — which already '
    'contains CAPA’s meaning — gets the acronym added honestly: “…flagged a labeling gap that became '
    'a corrective action (CAPA).” The Excel-based trending bullet moves up; the social-media bullet '
    'from the campus job moves out.',
    'Retune the summary line (two minutes): “Quality graduate with document control and supplier '
    'audit experience across two internships, targeting QA analyst roles in medical devices.” Their '
    'nouns, your facts.',
    'Draft the cover letter’s two evidence pairings (seven minutes): need one — audits: “You need '
    'audit exposure; I supported four supplier audits at Medline, including corrective-action '
    'follow-ups.” Need two — written communication: “The posting asks for strong writing; the '
    'audit-summary format I drafted is still in use at the site.” Add the company clause (their '
    'recent 510(k) clearance, found in ten minutes of research) and the close.',
    'The last-thing check (three minutes, Chapter 4): file named “Lastname-Resume-QAAnalyst.docx” · '
    'dates consistent with the profile · every number defensible · one read-aloud pass of the letter.',
])
para(doc, 'Twenty minutes, because the master résumé and the story bank already existed. That is the '
    'entire secret of the campaign’s economics: the heavy writing happens once; each application is '
    'an act of selection and translation. Compare the volume game’s per-application cost — thirty '
    'seconds and no signal — and notice that twenty minutes is not the expensive option. It is the '
    'only one that converts.')

h1(doc, 'The employer’s side: how hiring actually works')
para(doc, 'Candidates strategize better when they can see the funnel from above, so here is the standard '
    'shape from the hiring side. A posting draws anywhere from dozens to several hundred applications. '
    'The ATS surfaces a search-ranked subset; a recruiter — often screening for a dozen openings at '
    'once — scans that subset in seconds each and advances perhaps ten to fifteen files to the hiring '
    'manager. The manager, whose actual job is not hiring, picks a handful for phone screens. Screens '
    'produce three to five interviews; interviews produce one offer, sometimes two. Every stage is a '
    'communication filter, and almost every stage is operated by someone with too little time reading '
    'documents written by people who assumed they had more.')
para(doc, 'Three strategic consequences follow. First, the recruiter and the hiring manager are '
    'different audiences (Chapter 2): the recruiter pattern-matches keywords and disqualifiers at '
    'speed; the manager reads for “can this person do MY problem.” The résumé must serve both — '
    'keywords for the first, achievement evidence for the second — which is exactly the two-layer '
    'design this chapter builds. Second, referrals matter because they bypass the funnel’s widest, '
    'most arbitrary stage: a referred file typically goes straight to a human. Third, silence is '
    'structural, not personal: nobody in that pipeline has time to explain a no. The campaign’s '
    'tracker exists because the system will never send you its feedback; you have to infer it from '
    'your own conversion data.')
para(doc, 'One more insight from the inside: postings are wish lists, not contracts. The “requirements” '
    'section typically describes the ideal candidate the team brainstormed, and hiring managers '
    'routinely interview people missing two or three listed items who are strong on the load-bearing '
    'ones. The practical rule: if you hit roughly 60–70% of the requirements including the clearly '
    'central ones, apply — with a cover letter that addresses the strongest gap head-on (Chapter 8’s '
    'two-sided move: “I haven’t used your LIMS specifically; I ran its closest competitor for two '
    'years”). Self-screening out of reach postings is the most common self-inflicted wound in early '
    'careers, and it is disproportionately committed by exactly the candidates who would have been '
    'fine.', bold_lead='Postings are wish lists.')

h1(doc, 'Deep dive: the platform as a search engine')
para(doc, 'Most candidates use professional platforms as a billboard — profile up, waiting. The '
    'campaign uses them as a search engine, in four specific ways. First, target-list building: the '
    'people-search filtered by company and role family shows you exactly who holds your target job at '
    'your target employers, what their paths were, and which skills recur in their profiles — free '
    'market research on the actual route in. Second, warm-path mapping: the “connections” layer shows '
    'which alumni, classmates, and former colleagues sit one hop from your targets; that map IS your '
    'referral strategy. Third, recruiter visibility: recruiters search profiles with the same keyword '
    'logic as the ATS, which is why your headline and skills section deserve the same mirroring '
    'discipline as your résumé — and why the open-to-work setting (visible to recruiters only, if '
    'discretion matters) is worth switching on during an active search.')
para(doc, 'Fourth, and least used: the posting archaeology. When a role interests you, search the '
    'company’s recent posts and news — funding, expansion, product launches, leadership changes. Ten '
    'minutes of this produces the company clause for your cover letter, two intelligent questions for '
    'the interview (Chapter 14), and occasionally the discovery that saves you months: the hiring '
    'freeze, the scandal, the acquisition that explains why the team is hiring at all. The platform '
    'is a research instrument wearing a social network’s clothes. Use it like Chapter 9 taught you to '
    'use any source: deliberately, with notes.')

h1(doc, 'Gaps, returns, and the nonlinear résumé')
para(doc, 'Career gaps are normal — caregiving, health, layoffs, education, immigration timelines, '
    'plain bad markets — and the professional handling is brief honest framing, not concealment. One '
    'true clause does the work: “Family caregiving, 2024” or “Completed treatment and returned to '
    'full-time work, 2023” sits in the chronology like any other entry, needs no elaboration, and '
    'pre-answers the question every reader was going to form anyway. What never works is the elastic '
    'date, the mystery hole, or the functional format deployed as camouflage — all three convert a '
    'neutral fact into an apparent secret, and secrets are what screening exists to catch.')
para(doc, 'Two additions strengthen a return. First, harvest the gap honestly: caregiving that involved '
    'scheduling, budgets, or advocacy produced real bullets; the layoff year that included a '
    'certification or freelance project produced entries, not absence. (Do not inflate — a gap is '
    'not a job — but do not zero out genuine work either.) Second, address momentum in the summary '
    'line when returning after years away: “Operations analyst returning to full-time work after a '
    'caregiving period — current on Excel/Power BI via [certificate], targeting supply-chain roles.” '
    'The sentence names the gap, kills the staleness worry, and points forward, which is all any '
    'reader needed. Recruiters reject mystery far more often than they reject history.',
    bold_lead='Returning with momentum.')

h1(doc, 'Red flags: reading the postings back')
para(doc, 'The screening runs both directions, and candidates — especially urgent ones — under-screen '
    'the other side. Legitimate red flags in postings and processes: compensation described only in '
    'upside language (“unlimited earning potential!”); vagueness about what the company actually '
    'sells; interview processes that are all charm and no substance (no one asked you anything hard — '
    'they are not evaluating, they are recruiting bodies); pressure tactics (“we need an answer '
    'today”); and any request for money, equipment purchases, or banking details before employment — '
    'the last category being outright scam territory that targets exactly new graduates, typically '
    'through fake remote postings and “accidental overpayment” check schemes. The rule from '
    'Chapter 10 applies verbatim: on the credibility ladder, an employer you cannot verify through '
    'independent sources is rung five, and rung five is never load-bearing — not for claims, and not '
    'for career decisions.')
para(doc, 'Softer signals deserve reading too. The posting rewritten and reposted every six weeks is '
    'telling you about turnover. The interviewer who cannot describe success in the role (Chapter '
    '14’s question, reversed) is telling you the role is unscoped. The team that bad-mouths the '
    'person you would replace is showing you how they will discuss you. None of these is '
    'disqualifying alone; all of them are data, and the campaign mindset — multiple live options, '
    'tracked — is what gives you the standing to weigh data instead of ignoring it. Desperation '
    'reads postings generously. Pipelines read them accurately.')

h1(doc, 'Workshop: one résumé section, made over')
para(doc, 'Theory teaches slower than examples, so here is one experience entry rebuilt in three passes — '
    'the makeover sequence you can run on your own document tonight. The raw material: a campus '
    'bookstore shift-supervisor job, two years, currently rendered as four duty bullets: “Responsible '
    'for opening and closing procedures. Supervised student employees. Handled customer service '
    'issues. Assisted with inventory and ordering as needed.”')
para(doc, 'Interview yourself with the counting questions: how many employees? (six per shift). How '
    'much cash? (a $4,000 drawer, reconciled daily, over two years — call it 500 reconciliations). '
    'Any events? (two textbook-rush seasons — the store’s peak weeks — staffed and scheduled; one '
    'register-system migration survived; a recurring shortage problem you traced to a receiving '
    'error). Any outcomes? (your shift’s drawer variance was the store’s lowest; the receiving fix '
    'stuck). Twenty minutes of honest excavation produced six numbers and two events the duty '
    'bullets had buried.', bold_lead='Pass one: excavate.')
para(doc, 'Run verb-task-result on the best material: “Supervised six student employees per shift '
    'across two years, including scheduling for both textbook-rush peaks (3× normal volume)” · '
    '“Reconciled a $4,000 drawer daily — 500+ closes with the store’s lowest variance record” · '
    '“Traced a recurring inventory shortage to a receiving-log error; the corrected process was '
    'adopted storewide.” Three bullets now, not four — the generic customer-service line died, '
    'because it was every retail job ever and defended nothing.', bold_lead='Pass two: rebuild.')
para(doc, 'For a quality/operations posting, the inventory bullet rises to the top and gains the '
    'field’s vocabulary honestly: “root-caused” for traced, if and only if you can say it out loud in '
    'the interview without flinching. For a people-management-flavored posting, the supervision '
    'bullet leads. The entry is one job, but it is no longer one story — the master résumé holds all '
    'three bullets, and each application chooses its lead. That is tailoring, mechanically: same '
    'truth, rotated toward the reader.', bold_lead='Pass three: aim.')

h1(doc, 'Money research before the money question')
para(doc, 'Salary research belongs at the START of the search, not the night before an offer call, '
    'because it shapes the target list itself. Three sources triangulate a defensible range: posted '
    'ranges (pay-transparency laws now require them in a growing list of states — read ten postings '
    'in your role family and the band emerges); aggregate sites (useful for the middle of the '
    'distribution, noisy at the edges); and humans — the informational interview question “what '
    'should someone at my level expect the range to be?” is entirely askable and produces the '
    'ground truth the websites smooth over. Write the range down with its basis, exactly like any '
    'Chapter 9 evidence: “$58–65K, from six posted ranges and two conversations, Fargo market, '
    '0–2 years.” Chapter 14 teaches the conversation that number funds; this chapter’s job is making '
    'sure the number exists before anyone asks.')

h1(doc, 'Five myths, retired')
para(doc, 'The tailoring myth — “a really good résumé works everywhere.” A really good MASTER résumé '
    'exists; every strong SENT résumé was aimed. The universal version is, by construction, optimized '
    'for nobody, and the funnel section explains what happens to unaimed files.', bold_lead='Myth one.')
para(doc, 'The creativity myth — “you have to stand out visually.” You have to stand out in the first '
    'seven seconds of CONTENT: a number, a title, a match. Visual novelty parses badly, screens '
    'worse, and reads as effort misallocated. The candidates who “stood out” in every recruiter '
    'story you will ever hear stood out on evidence.', bold_lead='Myth two.')
para(doc, 'The modesty myth — “the work speaks for itself.” The work is not in the room; the document '
    'is. Accurate, specific claims about real results are not bragging — they are the reader’s only '
    'access to the work (this chapter’s whole thesis, and the two-candidates case in one line).',
    bold_lead='Myth three.')
para(doc, 'The permission myth — “I’m not qualified until I meet every requirement.” Postings are wish '
    'lists (the funnel section); 60–70% with the load-bearing items covered is an application, not '
    'an imposture. The people reading this myth as true are disproportionately the ones the '
    'requirements were padded against.', bold_lead='Myth four.')
para(doc, 'The event myth — “the search starts when I need a job.” The network is built during '
    'employment (give-first, Chapter 11’s account), the master résumé grows a bullet at a time as '
    'wins happen, and the profile stays current in peacetime. Careers managed as pipelines never '
    'face the cold-start problem that careers managed as emergencies always do.', bold_lead='Myth five.')

h1(doc, 'Frequently asked questions')
para(doc, 'For a first professional résumé, almost never. U.S. norms exclude photos (bias-management '
    'practice), graphics die in the ATS, and the designer template signals effort spent on the wrong '
    'layer. The exception is portfolio-driven creative fields — and even there, the parseable plain '
    'version exists alongside the showpiece.', bold_lead='Should my résumé have any design at all?')
para(doc, 'Include it while current or strong and recent (above roughly 3.5, within a few years of '
    'graduation); drop it once experience carries the file. No GPA is not a confession — omission '
    'reads as “experience matters more now,” which becomes true faster than students expect.',
    bold_lead='GPA: include or omit?')
para(doc, 'Legally and practically, no — omit graduation years a decade or more back if age signaling '
    'concerns you, and current norms support dropping early-career entries entirely as they lose '
    'relevance. The chronology must stay honest for what it includes; it owes no completeness to '
    'decades that no longer predict your work.', bold_lead='Do I have to date everything?')
para(doc, 'Use AI the way Chapter 15 teaches everywhere else: critique loops on YOUR drafts (“find the '
    'weakest three bullets”), keyword harvesting from postings, first-pass phrasings you then verify '
    'and re-voice. Never let it invent numbers, inflate titles, or write claims you cannot interview '
    'on — the tool generates plausible, and plausible-but-unown-able is precisely the résumé failure '
    'mode. Every line still has to survive the reference call, and the reference has never met your '
    'chatbot.', bold_lead='Can I use AI on my résumé?')
para(doc, 'Follow up once after two silent weeks, once more after four, then let it go and keep the '
    'pipeline moving. Three-plus contacts converts persistence into pestering, and the silence was '
    'already an answer — structural, not personal, per the funnel section. The energy belongs to the '
    'next tailored application.', bold_lead='How many times can I follow up?')

h1(doc, 'Case study: the internship that became the offer')
para(doc, 'A junior accounting major treated her summer internship as a ten-week job. Her classmate '
    'treated his as a ten-week AUDITION run by this chapter’s rules, and the divergence is the case. '
    'Week one, he asked his supervisor Chapter 14’s question — “what would a great summer look like '
    'from your side?” — and wrote the answer down. It named two things: clean reconciliation work, '
    'and “less hand-holding by August.” Those two phrases became his private success criteria, and '
    'everything he logged all summer was evidence against them.')
para(doc, 'He kept a wins file — a running note of dates, numbers, and small events: the 300-invoice '
    'backlog cleared in week three; the reconciliation error he caught in week six (worth $4,100); '
    'the client call he handled solo in week eight. Fifteen minutes on Fridays, exactly the '
    'master-résumé habit this chapter prescribes, running in real time instead of from archaeology. '
    'He sent his supervisor the three-line status update every Friday without being asked '
    '(Chapter 11’s teammate contract), and in week nine he requested the exit conversation: what '
    'should I build next, and would you be comfortable as a strong reference?')
para(doc, 'The payoff cascaded. The wins file became four achievement bullets with numbers no memory '
    'could have reconstructed in December. The supervisor — briefed, closed-loop, and never '
    'surprised — became the referral that walked his full-time application past the portal in '
    'spring. And the exit conversation’s answer (“get comfortable with our consolidation software”) '
    'became the winter certificate that closed his one gap before the interview could find it. The '
    'offer, when it came, was the least surprising event of his senior year. His classmate — equally '
    'capable, equally liked — reconstructed her summer from memory in a December panic, and her '
    'bullets read like everyone else’s: responsible for, assisted with.')
bullets(doc, [
    ('The lesson about timing:', 'the search artifacts — bullets, references, keywords — are built '
     'DURING the experience or reconstructed badly after it. The wins file costs fifteen minutes a '
     'week and is the highest-yield document in this chapter.'),
    ('The lesson about the ask:', 'success criteria requested in week one converted a vague summer '
     'into an auditable one — the same criteria-first move Chapter 9 teaches for comparisons.'),
    ('The lesson about references:', 'a reference is GROWN — briefed, updated, thanked — not '
     'requested cold in application week.'),
])

h1(doc, 'Keeping morale during the silence')
para(doc, 'The search is a communication project, but it is also a psychological one, and the two '
    'interact: discouraged candidates write worse applications, which convert worse, which '
    'discourages. Three structural defenses. First, measure inputs, not outcomes: three tailored '
    'applications, one outreach, and one skill-hour per week are fully in your control; offers are '
    'not, and grading yourself on the uncontrollable is how motivation dies. The tracker makes the '
    'inputs visible — on a silent week you can still see a full one. Second, expect the base rates: '
    'even excellent campaigns run conversion funnels, and a dozen silences per interview is normal '
    'arithmetic, not a verdict (the funnel section explains exactly where the silence is '
    'manufactured). Third, keep one non-search project alive — the certificate, the portfolio '
    'piece, the volunteer analysis — because it generates fresh bullets AND fresh morale, and it '
    'gives every informational interview and follow-up something new to say. The candidates who '
    'interview best in month three are the ones whose month two produced something besides '
    'applications.')

h1(doc, 'The senior-year calendar (or: when to do all this)')
para(doc, 'The campaign has a season, and starting it in the right month is half its advantage. For a '
    'spring graduate: summer-before is pipeline season — the master résumé built from the wins file, '
    'the profile brought current, two or three informational interviews while everyone’s calendar is '
    'soft. September through November is the corporate recruiting wave: large employers fill spring '
    'start dates in fall, campus career fairs cluster here, and the candidates who arrive with '
    'tailored materials in week two out-convert the ones who discover the fair in week ten. December '
    'is maintenance — follow-ups, thank-yous, one certificate or portfolio piece. January through '
    'March is the second wave: mid-size and smaller employers, who hire closer to need, plus every '
    'posting the fall wave reopened. April is decision season, run by Chapter 14’s offer rules. The '
    'pattern generalizes beyond graduation: any search runs better as a scheduled campaign with '
    'seasons than as a reaction with a deadline.')
para(doc, 'Two calendar corollaries. First, the “I’ll start after finals / the holidays / this '
    'project” instinct always costs a full hiring wave — the postings do not wait for your semester '
    'to end, and three tailored applications a week fits inside any real schedule precisely because '
    'the master résumé makes each one a twenty-minute act. Second, deadlines cluster and portals '
    'crash (Chapter 10’s rule, verbatim): the application due at 11:59 on the 15th goes in on the '
    '12th, because the queue at the cliff edge is where careers get randomized.')

h1(doc, 'When the application isn’t a portal')
para(doc, 'Smaller employers, startups, and a surprising share of professional-services firms hire '
    'through an inbox, not an ATS — “send résumé and cover letter to careers@…” — and the genre '
    'shifts accordingly. The email IS the cover letter: subject line “Application — Quality Analyst '
    '— Jordan Okafor” (findable in a crowded inbox, per Chapter 5), the letter’s content as the '
    'body (slightly shortened — the hook, one need-evidence pairing, the company clause, the '
    'close), and the résumé attached as a PDF whose formatting you now fully control, since no '
    'parser stands between you and the reader. The mechanics chapter-check themselves: named '
    'attachment, verified recipient, last-thing check. Direct-inbox applications reward the '
    'campaign disproportionately — a researched, warm, specific email to a named human at a '
    'forty-person company converts at rates the portal world never sees, because almost nobody '
    'bothers to do it well.')

h1(doc, 'The application-day checklist')
para(doc, 'Everything above compresses, on the day you actually apply, to twelve checks. Run them in '
    'order; the whole list takes fifteen minutes on top of the tailoring pass.')
numbered(doc, [
    'The posting is saved as a file — postings vanish, and you will need its exact language for the '
    'interview.',
    'Keywords harvested; each appears in your documents wherever honestly true, in the posting’s '
    'exact form.',
    'The summary line names THIS role family, not your generic ambitions.',
    'Top three bullets match their top three requirements, in their order.',
    'Every number is one you can defend aloud; every claim survives the reference call.',
    'Single column, standard headings, no tables or text boxes; dates in one format.',
    'File named for the recipient: Lastname-Resume-RoleName.docx (or PDF as instructed).',
    'Cover letter: hook, two need-evidence pairings, company clause, confident close — one page.',
    'Names verified (the recruiter’s, the company’s — “Meridian” not “Meridien”), per Chapter 4.',
    'Profile dates and titles match the résumé you are sending today.',
    'Warm path checked: is there anyone who could refer this application before the portal gets it?',
    'Tracker row created: date, version, contact, follow-up date two weeks out.',
])

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Start the master résumé: every job, project, and role you have ever held, bulleted on the '
    'formula. Go count what you can count — the numbers exist in old schedules, reports, and inboxes.',
    'Rewrite your three weakest duty bullets as achievements. Apply the test: could anyone else in '
    'that job have written this line?',
    'Define your role family in one phrase and build the first ten rows of the target list.',
    'Run the consistency audit: your name, two search engines, logged out. Fix the top finding.',
    'Send one informational-interview ask this week, using the five-sentence outreach skeleton. You '
    'have a warmer network than you think — start with a professor or a former supervisor.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'The chapter reframes the application as a proposal in which you are the deliverable. Where does '
    'that framing genuinely help, and where could it push a candidate toward overclaiming? Use '
    'Chapter 8’s influence-vs-manipulation audit on your answer.',
    'Keyword mirroring is defended here as translation. Construct three examples along the spectrum '
    'from honest translation to keyword fraud, and state the test that separates them.',
    'The ATS is criticized for filtering out unconventional candidates. From the employer’s side, '
    'what problem is it solving? Propose one change to the system that serves both sides, and defend '
    'its costs.',
    'The career-changer case turned eleven years of “unrelated” work into analyst evidence. Take your '
    'own least-corporate experience and perform the same translation: what are its three strongest '
    'achievement bullets for your target field?',
    'Should employers search candidates’ personal social media at all? Argue both positions with '
    'this course’s frameworks (permanence, relevance, bias), then state and defend your policy.',
])

keyterms(doc, [
    ('Campaign search', 'the targeted strategy — researched employers, tailored applications, tracked '
     'pipeline, warm paths before portals — as against the volume game’s untailored spray.'),
    ('Role family', 'the defined category of positions (“quality roles in medical devices”) that makes '
     'research, tailoring, and keyword strategy possible.'),
    ('Warm path', 'any second-degree route to a referral — alumni, former colleagues, informational '
     'contacts — worked before the portal application when possible.'),
    ('Informational interview', 'a small, honest, dated ask for perspective from someone whose career '
     'view you need — never an ambush job request; closed twice (thanks, then outcomes).'),
    ('Seven-second scan', 'the recruiter’s first pass — top third, left edge, numbers — that the '
     'résumé must survive to earn a real read.'),
    ('Achievement bullet', 'action verb + task + measurable result; the line only you could write, '
     'as against the duty bullet any job holder could.'),
    ('Master résumé', 'the evergreen private document holding every bullet you have earned; each '
     'application is a twenty-minute selection from it, not a rewrite.'),
    ('Applicant tracking system (ATS)', 'the software that parses applications into searchable '
     'records; rank and filter decide who surfaces for human scanning.'),
    ('Parse failure', 'content the ATS cannot extract (tables, text boxes, headers, graphics) — '
     'invisible in your record, however good it looked on the page.'),
    ('Keyword mirroring', 'using the posting’s exact nouns for your real experience — translation, '
     'bounded by the rule that you claim only what you can interview on.'),
    ('Company clause', 'the cover letter’s one researched sentence about THIS employer — the '
     'anti-mail-merge signal.'),
    ('Consistency audit', 'the logged-out search of your own name plus the date/title match between '
     'résumé and profiles — run before recruiters run it for you.'),
])

quiz(doc, [
    ('The campaign beats the volume game primarily because:',
     ['It requires less total effort', 'Tailored applications with warm paths convert far better per application',
      'Recruiters penalize frequent applicants', 'Portals limit submissions per week']),
    ('The résumé’s one job is to:',
     ['Document your complete history', 'Survive the scan and earn the conversation',
      'Negotiate your starting salary', 'Replace the cover letter']),
    ('“Responsible for quality documentation” fails as a bullet because:',
     ['It lacks a period', 'Any holder of the job could have written it — no verb-task-result, no digits',
      'It is too short', 'Quality documentation is not a real duty']),
    ('When results were not yours to claim, the honest quantification move is:',
     ['Skip numbers entirely', 'Quantify the scale of responsibility — orders per day, seats, team size',
      'Estimate the team’s results as your own', 'Use stronger adjectives']),
    ('An ATS “rejects” low-keyword résumés by:',
     ['Emailing a denial', 'Never surfacing them in recruiter searches — silence, not judgment',
      'Flagging them for fraud', 'Forwarding them to competitors']),
    ('Parse failure means:',
     ['The file was too large', 'Content in tables, text boxes, or headers doesn’t exist in your database record',
      'The recruiter disliked the font', 'The posting expired']),
    ('The pure-functional (no-dates) résumé format is avoided because:',
     ['It is illegal in most states', 'Recruiters read it as concealment — the format itself becomes a red flag',
      'ATS systems charge more to parse it', 'It cannot include skills']),
    ('The cover letter’s middle paragraphs should:',
     ['Recap the résumé in prose', 'Pair the employer’s named needs with your matched evidence',
      'Explain every job change', 'Discuss salary expectations']),
    ('The consistency audit checks:',
     ['Grammar across documents', 'That dates and titles match between résumé, profiles, and what search results show',
      'Whether references responded', 'ATS keyword density']),
    ('The career-changer case’s central lesson is that:',
     ['Career changes require new degrees', 'Her history never changed — the translation of it did',
      'Networking replaces résumés', 'Pay cuts are always required']),
], ['b','b','b','b','b','b','b','b','b','b'])

references(doc, [
    'Bock, L. (2015). Work rules! Insights from inside Google. Twelve.',
    'Cialdini, R. B. (2021). Influence: The psychology of persuasion (new & expanded ed.). Harper Business.',
    'Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360–1380.',
    'Grant, A. (2013). Give and take: A revolutionary approach to success. Viking.',
    'Nielsen, J., & Pernice, K. (2010). Eyetracking web usability. New Riders. (The F-pattern research '
    'this chapter’s scan design applies.)',
    'Schullery, N. M., Ickes, L., & Schullery, S. E. (2009). Employer preferences for résumés and cover '
    'letters. Business Communication Quarterly, 72(2), 163–176.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch13-study-guide.docx')
finish(doc, os.path.abspath(out))
