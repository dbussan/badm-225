# Chapter 13 — The Job Search and Résumés in the Digital Age (46 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 13"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "The Job Search and Résumés in the Digital Age",
    "The search as a campaign · bullets that sell · the ATS game · the digital layer that interviews first", D)
notes(s, "Chapter 13: Unit 5 opens. The most personally urgent chapter in the course — every skill so far, aimed at the student's own next job.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Run", "the search as a targeted campaign — researched employers, tracked pipeline, warm paths in."),
    ("Network", "without the ick: small honest asks, informational interviews, give-first maintenance."),
    ("Write", "résumé bullets on the achievement pattern: action verb, task, measurable result."),
    ("Beat", "the applicant tracking system honestly: mirrored keywords, parseable formatting."),
    ("Pair", "the résumé with a cover letter that connects YOUR evidence to THEIR need."),
    ("Align", "the digital layer — profile, portfolio, search results — with the paper story."),
], D, nxt())
notes(s, "Objectives map to the Chapter 13 practice bank and the résumé assignment.")

s = stat_slide(prs, "The first read is a scan", "~7 sec",
    "Recruiter eye-tracking studies consistently find the first résumé pass lasts seconds, not minutes — a scan of names, titles, dates, and keywords.",
    [("The design consequence:", "your best material must live where the scan goes — top third, left edge, bolded titles (the F-pattern, Chapter 3, applied to you)."),
     ("The writing consequence:", "every bullet competes for a seconds-long audition — flabby bullets don't lose slowly, they lose instantly."),
     ("The strategic consequence:", "the résumé's job is not to get you the job. It's to survive the scan and get you the conversation."),
    ], D, nxt())
notes(s, "Ladders/TheLadders eye-tracking work is the usual citation — keep it approximate. The 'survive the scan' reframe governs the whole chapter.")

s = section_slide(prs, "01", "The search as a campaign",
    "Researched targets, tracked pipeline, warm paths — not a hundred identical arrows.", D, nxt())
notes(s, "Section 1: strategy before documents. The campaign frame beats the application-spray frame on every measured outcome.")

s = two_col_slide(prs, "Two ways to run a search",
    "The VOLUME game", [
        "Same résumé to 200 postings",
        "Competing at the widest point of the funnel",
        "No research, so no tailoring, so no signal",
        "Feels productive; converts at lottery rates",
    ],
    "The CAMPAIGN", [
        "15–25 researched targets that actually fit",
        "Each application tailored to the posting's language",
        "Warm paths hunted before the portal is touched",
        "Slower per application; wildly better per offer",
    ], D, nxt())
notes(s, "The campaign math: tailored applications with referrals convert at multiples of cold portal submissions. Effort concentrated beats effort scattered.")

s = bullets_slide(prs, "Build the target list like an analyst", [
    ("Define the role family first:", "'quality roles in medical devices' beats 'anything in business' — focus is what makes research possible."),
    ("Research each target like Chapter 8 taught:", "their products, their pain, their language — the job posting is a requirements document; read it like one."),
    ("Mine the posting for the employer's OWN words:", "those exact phrases are your keyword list, your cover letter's vocabulary, and your interview prep."),
    ("Tier the list:", "dream targets get the full campaign; solid fits get strong tailoring; the rest aren't on the list — that's the point of a list."),
], D, nxt())
notes(s, "The posting-as-requirements-document reframe converts application writing into the proposal writing students already learned (Chapter 10).")

s = bullets_slide(prs, "Track the pipeline or lose it", [
    ("One sheet, one row per application:", "company, role, date, version sent, contact, status, next action — the search is a project; run it like one (Chapter 9)."),
    ("Every application gets a follow-up date", "when you submit it — two weeks silent means a polite nudge, not a shrug."),
    ("Track which versions convert:", "if the analyst résumé gets callbacks and the coordinator one doesn't, the data just told you something."),
    ("The tracker keeps you honest on volume:", "three tailored applications a week, every week, beats thirty in a panicked weekend."),
], D, nxt())
notes(s, "The tracker converts an anxious open-ended ordeal into a managed process with statuses — psychologically as valuable as it is tactically.")

s = bullets_slide(prs, "The warm path: referrals move résumés", [
    ("A referred résumé skips the pile's worst odds —", "referrals convert to interviews at several times the portal rate at most employers."),
    ("Warm doesn't mean connected-at-birth:", "alumni, former colleagues, that guest speaker, the friend's manager — second-degree paths are everywhere once mapped."),
    ("The ask is small and specific (Chapter 8):", "'Would you be willing to submit my résumé for req 4471?' — never 'can you get me a job?'"),
    ("Work the path BEFORE applying when possible:", "the referral attached to a fresh application beats the one chasing a two-week-old rejection."),
], D, nxt())
notes(s, "The sequencing rule (path before portal) is the tactical detail students don't know and recruiters confirm.")

s = section_slide(prs, "02", "Networking",
    "Small honest asks of people positioned to answer them.", D, nxt())
notes(s, "Section 2: networking, de-icked. It's Chapter 6 requests plus Chapter 8 laddering, aimed at career information.")

s = bullets_slide(prs, "Networking without the ick", [
    ("Reframe: you're not asking for a job —", "you're asking for twenty minutes of perspective from someone who has the view you need."),
    ("People genuinely like giving advice:", "the informational ask flatters honestly ('you've done what I'm attempting') and costs the giver little."),
    ("Start with the network you already have:", "professors, classmates, past supervisors, family friends — the map is bigger than it feels."),
    ("It's a lifetime system, not a job-search sprint:", "the network built only when needy smells needy — see the give-first slide."),
], D, nxt())
notes(s, "The reframe does the heavy lifting: students hate 'networking' because they picture the transactional version. The advice-ask version is just... professional curiosity.")

s = bullets_slide(prs, "The informational interview", [
    ("The ask:", "'Could I take twenty minutes of your time to ask how you got from QA tech to quality manager?' — specific, small, dated, flattering-because-true."),
    ("Come with five real questions,", "ask three, listen hard (Chapter 1): their path, what the work is actually like, what separates good hires."),
    ("Never ambush with a job request —", "the meeting's integrity is the meeting's value. If they offer to pass your résumé, that's THEIR move."),
    ("Close the loop twice:", "thanks within a day, and the 'your advice worked' note weeks later — the second one is the one nobody sends and everybody remembers (Chapter 6)."),
], D, nxt())
notes(s, "The no-ambush rule is ethical AND tactical: the informational that stays informational produces more referrals than the one that pivots.")

s = bullets_slide(prs, "The outreach message, engineered", [
    ("Subject or opener names the connection:", "'Dr. Reyes suggested I reach out' or 'Fellow Bison in med devices' — the warm element goes first."),
    ("One sentence of who you are,", "one of why THEM specifically ('your path from bench to management'), then the small dated ask."),
    ("Make yes effortless:", "'any twenty minutes in the next two weeks — I'll work around your calendar' (Chapter 8's friction rule)."),
    ("Five sentences, total.", "The life story goes in the conversation, not the cold message — this is a knock, not a memoir."),
], D, nxt())
notes(s, "The five-sentence spec with the cold-email anatomy from Chapter 8. Students can template this today.")

s = bullets_slide(prs, "Maintain the network: give first, always", [
    ("Send value with no ask attached:", "the article that fits their project, the intro they'd want, congratulations on the promotion (Chapter 6's five-S notes)."),
    ("Deposit before you need to withdraw", "(Chapter 11's trust account, career edition) — the network built during employment is the one that works between jobs."),
    ("Keep loose ties warm cheaply:", "a two-line check-in twice a year keeps a contact live; silence for five years then a favor request reads exactly like what it is."),
    ("Track it lightly:", "a birthdays-and-projects note per contact turns 'networking' into remembering — which is all it ever was."),
], D, nxt())
notes(s, "Grant's giver research (Chapter 6) underwrites this slide. The loose-ties point is Granovetter: weak ties carry the most job information.")

s = section_slide(prs, "03", "Résumé strategy",
    "One document, one job: get the conversation.", D, nxt())
notes(s, "Section 3: the résumé at the strategic level, before the bullets.")

s = bullets_slide(prs, "What a résumé is (and isn't)", [
    ("It's an ad for an interview,", "not an autobiography — completeness is not a virtue; relevance is the only virtue."),
    ("It's a claims document that will be audited:", "every line is fair game in the interview — write nothing you can't discuss for five minutes."),
    ("It's tailored per target family:", "one master document holds everything; each sent version selects what THIS posting values."),
    ("It's judged as a writing sample first:", "before anyone weighs your experience, they've weighed your formatting, precision, and typos (Chapter 4 — at maximum stakes)."),
], D, nxt())
notes(s, "The writing-sample point reframes the whole course as résumé prep: the document IS the first work product the employer sees.")

s = two_col_slide(prs, "Chronological or hybrid?",
    "REVERSE-CHRONOLOGICAL (default)", [
        "Experience newest-first with dates — the format recruiters and ATS parse best",
        "Best when your history points at the target role",
        "Gaps are visible — handle them honestly (later slide)",
    ],
    "HYBRID (skills-forward)", [
        "A skills/summary block up top, chronology beneath",
        "Best for career changers and thin-experience starters — leads with what transfers",
        ("Avoid pure-functional (no dates):", "recruiters read it as 'hiding something' — because it usually is"),
    ], D, nxt())
notes(s, "The pure-functional warning is consensus recruiter advice. Hybrid gets career-changers the benefit without the red flag.")

s = icon_rows_slide(prs, "Résumé anatomy, top to bottom", [
    ("📇", "Header", "Name large, then city, phone, professional email, LinkedIn — no street address, no photo (US norms), no 'Résumé' title."),
    ("🎯", "Summary line (optional, earned)", "One tailored sentence of what you are and bring — or nothing. Objectives about YOUR hopes died a decade ago."),
    ("💼", "Experience", "Newest first: title, employer, dates — then the achievement bullets that are the document's whole engine."),
    ("🎓", "Education", "Degree, school, date; GPA if strong and recent. Flips above experience for current students."),
    ("🛠", "Skills", "Concrete and checkable: software, languages, certifications — never 'hard worker' (that's a bullet's job to prove)."),
], D, nxt(), kicker="Every section answers the scan's question: 'is this person plausible for THIS role?'")
notes(s, "The objectives-are-dead note and the student education-flip are the two most-asked format questions, answered.")

s = bullets_slide(prs, "The summary line: one sentence, fully loaded", [
    ("The pattern:", "what you are + strongest credential + what you're aimed at: 'Finance graduate with two audit internships and advanced Excel, targeting analyst roles in healthcare.'"),
    ("Tailored per application —", "it's the thesis of THIS version of you; the summary that fits every job fits none."),
    ("Earn it or cut it:", "a vague summary ('motivated professional seeking opportunities') is negative space — it spends the scan's best seconds on nothing."),
    ("It's your pyramid summit (Chapter 9):", "the one sentence the recruiter should carry into the pile discussion."),
], D, nxt())
notes(s, "The summary is optional but the discipline isn't: knowing your one-sentence thesis improves every other line even if you cut the summary itself.")

s = section_slide(prs, "04", "Bullets that sell",
    "Action verb, task, measurable result — the achievement engine.", D, nxt())
notes(s, "Section 4: the bullet workshop. This is where résumés are won.")

s = flow_slide(prs, "The achievement bullet formula", [
    ("ACTION VERB", "Led, built, cut, redesigned — first word, past tense, no 'responsible for'"),
    ("THE TASK", "What you actually did, specifically"),
    ("THE RESULT", "The number, the outcome, the change — what was different because you did it"),
], D, nxt(), note_text="'Cut intake errors 38% by redesigning the sample-tracking checklist' — verb, task, result. Every bullet auditions against this shape.")
notes(s, "The formula is the chapter's core deliverable. Students should leave able to rewrite any duty bullet into this shape.")

s = two_col_slide(prs, "Duty bullets vs. achievement bullets",
    "Duties (what the job was)", [
        "'Responsible for social media accounts'",
        "'Handled customer complaints'",
        "'Assisted with inventory management'",
        "Any holder of the job could write these",
    ],
    "Achievements (what YOU did with it)", [
        "'Grew Instagram engagement 60% in one semester by shifting to short-form video'",
        "'Resolved ~30 escalations weekly; kept satisfaction above 4.5/5 through a system migration'",
        "'Rebuilt the count process, cutting monthly variance from 4% to under 1%'",
        "Only YOU can write these — that's the point",
    ], D, nxt(), left_fill=RGBColor(0xF7, 0xEA, 0xE8), left_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "'Any holder could write it' is the duty-bullet test. The rewrite direction is always: what changed because it was YOU in the chair?")

s = bullets_slide(prs, "Quantify everything quantifiable", [
    ("Numbers survive the scan;", "adjectives don't — '60%', '$12K', '30 per week', 'team of 6' are what a seven-second read retains (Chapter 4's abstraction ladder)."),
    ("Scale counts even without outcomes:", "'processed 200 orders daily' and 'served 80-seat dining room' quantify responsibility when results weren't yours to claim."),
    ("Reconstruct honestly:", "count, estimate conservatively, and be ready to explain the basis — 'about 30 a week' is defensible; invented precision isn't (Chapter 9's calibration)."),
    ("Can't quantify? Name the outcome:", "'adopted by two other departments' and 'still in use three years later' are results without digits."),
], D, nxt())
notes(s, "The conservative-reconstruction license is what students need to hear: most real work IS countable if they think back deliberately.")

s = bullets_slide(prs, "Tailoring: the posting is the answer key", [
    ("Mirror their nouns exactly:", "if they say 'stakeholder communication' and you say 'client relations,' the keyword match — human or ATS — just missed."),
    ("Reorder by their priorities:", "their must-haves go in your top bullets; your favorite achievement they didn't ask about moves down."),
    ("The master-résumé workflow:", "keep every bullet you've ever earned in one document; each application selects and reorders — tailoring in 20 minutes, not 3 hours."),
    ("Tailor honestly:", "mirroring means translating your real experience into their vocabulary — never claiming theirs (see: integrity)."),
], D, nxt())
notes(s, "The master-résumé workflow is the practical unlock — it converts tailoring from a rewrite into a selection, which is why campaigns can sustain it.")

s = bullets_slide(prs, "Early-career: you have more than you think", [
    ("Course projects count:", "'Built a 10-K analysis model for a 40-page equity report (team of 4, graded A)' is real analytical work — name the deliverable."),
    ("Jobs 'unrelated' to the target never are:", "the barista who trained new hires and balanced the drawer has supervision, cash controls, and peak-hour composure — write THOSE."),
    ("Leadership is a function, not a title:", "organized, scheduled, recruited, ran — the club treasurer who rebuilt the budget has a finance bullet."),
    ("The floor is honesty, not grandeur:", "small and true beats inflated every time — the interview will visit every line (next chapter)."),
], D, nxt())
notes(s, "The chapter's most encouraging slide, and the most needed: students discard their best material because it didn't happen in an office.")

s = section_slide(prs, "05", "The ATS game",
    "Software reads first. Format for the parser, write for the human.", D, nxt())
notes(s, "Section 5: applicant tracking systems — the mechanical gate before any human scan.")

s = bullets_slide(prs, "How the ATS actually reads you", [
    ("It parses your file into a database record:", "name, employers, titles, dates, skills — then recruiters search and filter those fields."),
    ("It doesn't 'reject' with judgment;", "it ranks and filters by match — a low-keyword résumé isn't declined, it's just never surfaced. Same outcome, no email."),
    ("Parse failure = invisibility:", "content the parser can't extract (tables, text boxes, headers, graphics) simply doesn't exist in your record."),
    ("Human review still follows:", "the ATS decides who gets scanned; the scan decides who gets called. You're writing for both, in that order."),
], D, nxt())
notes(s, "Demystification slide: the ATS is a database with search, not an AI judge. That model makes all the formatting rules obvious rather than superstitious.")

s = bullets_slide(prs, "Keyword mirroring, done honestly", [
    ("Harvest the posting's repeated nouns:", "the skills, tools, and phrases that appear twice are the search terms — list them before writing."),
    ("Use their exact form at least once:", "'Microsoft Excel (pivot tables, VLOOKUP)' catches both the tool search and the skill search."),
    ("Spell out AND abbreviate:", "'applicant tracking system (ATS)' — you don't know which form the recruiter searches."),
    ("Only claim what you can interview on:", "keywords you can't discuss are landmines you planted for yourself — the match gets you scanned; the lie gets you remembered."),
], D, nxt())
notes(s, "Mirroring is translation, not fabrication — the integrity line recurs deliberately.")

s = bullets_slide(prs, "Formatting that parses", [
    ("Single column, standard headings:", "'Experience,' 'Education,' 'Skills' — the parser is looking for exactly these signposts."),
    ("No tables, text boxes, icons, or photos;", "no content in headers/footers — the classic parse-killers, all of them common in 'designer' templates."),
    ("Standard fonts, real bullet points, dates as MM/YYYY", "in a consistent format the date-parser recognizes."),
    ("Submit what the posting asks for:", ".docx or PDF as instructed — when unstated, .docx is the safer parse; keep both current."),
], D, nxt())
notes(s, "The designer-template warning matters most: the prettiest résumés students buy are the least parseable. Boring formatting is a feature.")

s = bullets_slide(prs, "One page or two — and the whitespace budget", [
    ("Early career: one page.", "The second page of a thin history reads as padding — and the scan never reaches it anyway."),
    ("Experienced: two pages when EARNED,", "with page one able to stand entirely alone."),
    ("Whitespace is scan infrastructure:", "0.7-inch margins and readable type beat cramming — the sixth bullet you saved by shrinking the font cost you the five above it."),
    ("Cut by relevance, not by recency:", "the high-school job goes before the strong-but-old achievement bullet does."),
], D, nxt())
notes(s, "The length question, answered with the scan model rather than folklore: density that defeats the seven-second read defeats the résumé.")

s = section_slide(prs, "06", "Cover letters",
    "The document that connects your evidence to their need.", D, nxt())
notes(s, "Section 6: cover letters — shorter treatment, but the genre still decides close calls and signals writing skill directly.")

s = flow_slide(prs, "The cover letter skeleton", [
    ("THE HOOK", "Their role + your thesis: why this fit is real"),
    ("THE EVIDENCE", "Two proofs from your record, aimed at their two biggest needs"),
    ("THE COMPANY CLAUSE", "One sentence proving you researched THEM specifically"),
    ("THE CLOSE", "Confident ask for the conversation + logistics"),
], D, nxt(), note_text="Three to four paragraphs, one page hard. It's a persuasive message (Chapter 8) where the product is you.")
notes(s, "The skeleton maps to AIDA. The company clause is the anti-mail-merge signal — one specific sentence separates you from the template pile.")

s = bullets_slide(prs, "Openings that aren't 'I am writing to apply'", [
    ("Lead with the fit, not the fact of applying:", "'Your quality analyst posting asks for audit experience and LIMS fluency — my two internships were exactly that combination.'"),
    ("Or lead with the warm path:", "'Dr. Reyes suggested I contact you about the analyst opening' — the referral is your strongest opener when you have it."),
    ("Or lead with their world:", "'Your Fargo expansion doubles your sample volume — that scaling problem is what my capstone modeled.'"),
    ("Never lead with your autobiography:", "'I am a recent graduate of…' is on the résumé; the letter's job is connection, not recap."),
], D, nxt())
notes(s, "Three working openers, one anti-pattern. All three front-load the reader's interest (Chapter 8's hook discipline).")

s = two_col_slide(prs, "The middle paragraph: recap vs. connection",
    "Recap (wasted)", [
        "'As my résumé shows, I completed two internships and maintained a 3.8 GPA while working part-time…'",
        "Restates the document they're already holding",
        "Proves nothing except that you can summarize yourself",
    ],
    "Connection (working)", [
        "'You need someone who can run supplier audits solo by Q2. At Medline I ran the last four of my internship unassisted — including the corrective-action follow-ups.'",
        "Their need, named → your evidence, matched",
        "Does the recruiter's fit-thinking FOR them",
    ], D, nxt(), left_fill=RGBColor(0xF7, 0xEA, 0xE8), left_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "The connection pattern is need→evidence, explicitly paired. Two of these paragraphs and the letter has done its whole job.")

s = section_slide(prs, "07", "The digital layer",
    "You will be searched. Decide what they find.", D, nxt())
notes(s, "Section 7: the online presence — Chapter 5's permanence and Chapter 1's standing portfolio, at hiring stakes.")

s = bullets_slide(prs, "The professional profile, built like a landing page", [
    ("Headline says what you do and seek,", "not just your current title: 'Finance graduate — audit & analysis | seeking healthcare analyst roles.'"),
    ("Photo: competent and current —", "plain background, professional-casual; the empty silhouette reads as a ghost account."),
    ("The About section is your summary line, expanded:", "three sentences of thesis, evidence, direction — written in first person, sounding like a human."),
    ("Activity is optional; coherence isn't:", "you needn't post — but what's visible should agree with the résumé's story (next slide)."),
], D, nxt())
notes(s, "Landing-page framing: the profile's job is that a recruiter arriving cold leaves knowing your thesis. Same summit as the résumé.")

s = bullets_slide(prs, "The consistency audit", [
    ("Search your own name, logged out,", "on two engines — page one is your first impression; know it before they do."),
    ("Dates and titles must MATCH the résumé:", "discrepancies read as dishonesty even when they're sloppiness — recruiters cross-check as a screening step."),
    ("Clean the reachable past:", "old public posts, photos, and bios that contradict the professional story — Chapter 5's permanence means 'clean' is partial, so consistency matters more than perfection."),
    ("The goal (Chapter 5):", "the person online and the person on paper are obviously colleagues — not strangers, not aliases."),
], D, nxt())
notes(s, "The logged-out search is the actionable step; the date-match rule is the specific thing recruiters actually check.")

s = bullets_slide(prs, "Show the work: portfolios and samples", [
    ("Claims are cheap; artifacts are proof:", "the analysis, the deck, the report, the code — one linked sample outweighs three adjectives."),
    ("Curate to three to five best pieces,", "each with a two-line frame: the problem, your move, the result (a STAR in caption form)."),
    ("Scrub before you publish:", "employer data, client names, and anything confidential gets anonymized or excluded — showing work never means leaking it (Chapter 5)."),
    ("Course work counts here too:", "the capstone feasibility report from Chapter 10 IS a portfolio piece — write it knowing that."),
], D, nxt())
notes(s, "The capstone-as-portfolio note closes a loop across the course: the assignments are designed to be showable.")

s = section_slide(prs, "08", "Integrity and the last mile",
    "References, honesty, and the two-candidate case.", D, nxt())
notes(s, "Section 8: the ethics floor and the supporting cast.")

s = bullets_slide(prs, "The fireable lie (and its legal cousins)", [
    ("Résumé fraud survives hiring:", "the inflated degree or invented title is grounds for termination when discovered — YEARS later, at the worst possible moment."),
    ("The gray areas aren't:", "'anticipated' degrees dated as earned, solo credit for team work, stretched dates over gaps — all of it is checkable, and checking is the industry."),
    ("Frame honestly instead:", "gaps get one true clause ('family caregiving, 2024') — recruiters handle honest gaps fine; they never forgive discovered cover-ups (Chapter 7's pattern)."),
    ("The standard:", "every line survives a reference call to the person who was there. Write to that audit."),
], D, nxt())
notes(s, "The termination-later point is what students underweight: the lie doesn't expire when hired — it compounds.")

s = bullets_slide(prs, "References: ask, brief, thank", [
    ("Ask permission, every time:", "'Would you be comfortable being a strong reference for quality roles?' — the phrasing lets a lukewarm reference decline, which protects you (Chapter 6)."),
    ("Brief them per application:", "send the posting, your résumé version, and what the employer will care about — a prepared reference is twice the reference."),
    ("Never list, never surprise:", "no one appears on your sheet who hasn't said yes recently; the ambushed reference sounds ambushed, and it costs you."),
    ("Close the loop (Chapter 6):", "tell them the outcome, thank them regardless — references are network deposits with compounding interest."),
], D, nxt())
notes(s, "The 'comfortable being a STRONG reference' phrasing is the load-bearing detail — it engineers the graceful out.")

s = bullets_slide(prs, "Case: two candidates, one interview slot", [
    ("Same degree, same GPA, comparable internships.", "Candidate A: 'Responsible for quality documentation and assisting with audits.'"),
    ("Candidate B:", "'Maintained the doc control system for 200+ SOPs; supported four supplier audits — flagged a labeling gap that became a corrective action.'"),
    ("The recruiter's seven seconds", "found numbers, verbs, and a result in B — and a job description in A. B interviewed; A never learned why."),
    ("The lesson:", "the difference wasn't the experience — it was the WRITING about the experience. That's this course's entire thesis, in one screening decision."),
], D, nxt())
notes(s, "The closing case makes the chapter's stakes concrete: identical inputs, divergent outcomes, and writing was the variable.")

s = takeaways_slide(prs, [
    "Run a campaign: researched targets, a tracked pipeline, warm paths before portals.",
    "Network with small honest asks; give first; keep the loop closed twice.",
    "Every bullet on the formula: action verb + task + measurable result — duties describe jobs; achievements describe YOU.",
    "Beat the ATS honestly: their exact keywords, single-column parseable formatting, claims you can interview on.",
    "The cover letter connects need to evidence — never recaps; the digital layer must agree with the paper story.",
    "Write to the audit: every line survives the reference call and the follow-up question.",
], D, nxt(), site_note="Practice now: course site → Chapter 13 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The résumé that gets the interview isn't the one with the best experience. It's the one where the best experience is findable in seven seconds and defensible for an hour.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Rewrite three duty bullets from your own résumé on the achievement formula. What did you have to go count?",
    "Map your second-degree network for one dream employer. How many warm paths did you actually find?",
    "Where's the ethical line between keyword mirroring and keyword fraud? Build the test with examples.",
    "Audit your own name's search results, logged out. What would a recruiter conclude — and what's your 30-day fix?",
    "Argue it: should early-career résumés include a summary line, or is it wasted scan time? Use the seven-second model.",
], D, nxt())
notes(s, "Async-ready. Question one produces the best homework artifacts.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 13 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 13 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Build:", "Your master résumé — every bullet you've earned, achievement-formatted — then tailor one version to a real posting."),
    ("Audit:", "Your digital layer against the consistency checklist; fix the top three findings."),
    ("Coming next:", "Chapter 14 — interviewing and follow-up: where every résumé line gets its five-minute audit."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch13-job-search-and-resumes.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
