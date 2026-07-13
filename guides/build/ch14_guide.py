# Chapter 14 study guide — Interviewing and Follow-Up (25+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(14, 'Interviewing and Follow-Up',
    'STAR stories · the questions you ask · salary talk · the follow-through that separates finalists')

h1(doc, 'Why this chapter exists')
para(doc, 'The interview is three things at once, and preparing for all three is the chapter. It is an '
    'audit of your résumé — every line you wrote in Chapter 13 is now fair game for five minutes of '
    'questioning, which is why that chapter insisted you write nothing you could not defend. It is a live '
    'sample of your communication — the employer is watching you structure answers, listen, handle '
    'pressure, and ask questions, because how you communicate in the interview is the best available '
    'preview of how you will communicate in the job. And it is a preview of your follow-through — the '
    'thank-you, the promised materials, the graceful handling of whatever verdict arrives, all of which '
    'get read as samples of your professional reliability (Chapter 11’s account, opened at hello).')
para(doc, 'The liberating fact about interviews is how preparable they are. The questions are drawn from '
    'a small, well-known repertoire; the formats are catalogued; the money conversation follows a script '
    'you can research and rehearse; and the follow-through is a set of genres this course has already '
    'taught. Interviewing well is not charisma. It is Chapter 12’s lesson again — rehearsal beats '
    'talent — applied to a twenty-minute conversation whose outline you can largely predict. This guide '
    'covers the before (research, stories, logistics), the during (formats, the classics, your '
    'questions, composure), the money, and the after — plus two extended cases and a complete worked '
    'story-bank example.')

h1(doc, 'Before: preparation is the interview')
para(doc, 'Interviews are decided mostly in the week before them. The candidate who arrives with '
    'researched specifics, rehearsed stories, and tested logistics is running a different event than '
    'the candidate improvising from memory — and interviewers can tell within minutes which one sat '
    'down. Preparation splits into three workstreams: know them, know your stories, and kill the '
    'unforced errors.')
h2(doc, 'Know the format you’re walking into')
para(doc, 'Ask the recruiter what the process looks like — the asking itself signals professionalism — '
    'because each format rewards different preparation. The phone screen (20–30 minutes, usually HR) '
    'verifies basics, salary range, and communication skills; stand up and smile while you talk, '
    'because both are audible. The video interview, live or recorded one-way, inherits every camera '
    'rule from Chapter 12. The behavioral interview — “tell me about a time…” — treats your past '
    'behavior as evidence of future behavior and is STAR territory, the heart of this chapter. The '
    'panel puts several interviewers with divided roles in one room: get every name in seat order, '
    'answer to the asker while sweeping the room, and note that the quiet panelist is often the veto. '
    'The case or working session asks you to solve something live and scores the HOW: your clarifying '
    'questions, your structured thinking aloud, your visible self-correction — Chapter 9’s '
    'criteria-first discipline, performed.')
h2(doc, 'Research them like Chapter 8 taught')
para(doc, 'The research targets are the company (what they sell, to whom, what is changing — the '
    'expansion, the product launch, the recent news), the role (the posting reread as a requirements '
    'document, its must-haves mapped to your stories), and the people (your interviewers’ paths, '
    'findable in two minutes each — “I saw you moved from the bench to management” opens real '
    'conversation and signals preparation without a word of flattery). The output that matters: three '
    'researched facts you can deploy naturally in answers and questions. Research SHOWN beats research '
    'claimed — the same lesson Chapter 13’s cold outreach taught, now at conversational range.')
h2(doc, 'Kill the unforced errors')
para(doc, 'Logistics failures are the cheapest interview losses and the most preventable. The dry run: '
    'route, parking, or platform link tested the day before — arriving flustered spends the composure '
    'budget the first five minutes need. Dress one notch above the role’s daily norm, and when unsure, '
    'ask the recruiter; it is a normal question. Bring the kit: printed résumés (three), your questions '
    'written down, interviewer names, a working pen, water. Arrive ten minutes early — not thirty, '
    'which converts you into a lobby-management problem. And remember that the interview starts in the '
    'parking lot: the receptionist’s impression of candidates gets solicited far more often than '
    'candidates ever learn, and the driver you cut off in the lot has a badge and a desk somewhere '
    'upstairs.')

h1(doc, 'The story bank: STAR before you need it')
figure(doc, os.path.join(FIG, 'ch14_star.png'),
    'Figure 1. STAR — situation, task, action, result — the architecture of a behavioral answer.',
    'A four-step flow: situation (where and when, two sentences), task (what you were responsible for), action (what '
    'you specifically did — I, not we), and result (what changed, with the number and what you learned), with the '
    'warning that the classic failure is a vague collective middle with no measurable end.')
para(doc, 'Behavioral questions dominate modern interviewing for a defensible reason: past behavior '
    'predicts future behavior better than hypothetical virtue does. The answer architecture is STAR: '
    'Situation (where and when — two sentences of stage-setting, no more), Task (what YOU were '
    'responsible for in it), Action (what you specifically did — “I,” not “we,” for your parts; the '
    'interviewer is hiring you, not your former team), and Result (what changed, with the number when '
    'it has one, plus the learning when it fits). Ninety seconds to two minutes total. The classic '
    'failure is the vague collective middle — “we sort of handled it” — which converts your best '
    'material into unverifiable fog and leaves the interviewer nothing to score.')
figure(doc, os.path.join(FIG, 'ch14_storybank.png'),
    'Figure 2. The eight-story bank — conflict, failure, deadline, leadership, persuasion, mistake, initiative, team win.',
    'Eight labeled cells covering the story types that answer nearly every behavioral question, with the note to '
    'source them from jobs, courses, clubs, and the capstone, writing each once and indexing by beats.')
para(doc, 'Eight prepared stories cover almost every behavioral question ever asked: a conflict (worked '
    'through, not won), a failure (owned, with what changed), a deadline crunch, a leadership moment '
    '(with or without a title), a persuasion (moving people you could not command — Chapter 8, lived), '
    'a mistake owned (fast, clean admission — Chapter 16’s principle as autobiography), an initiative '
    '(unasked, delivered), and a team win (with your “I” identifiable inside the “we”). Source them '
    'anywhere legitimate: jobs, course projects, clubs, the capstone — Chapter 13’s rule that '
    'experience does not need an office applies to stories too. Write each one out in full prose once, '
    'to find its shape and verify its facts; then compress to beat cards (S/T/A/R, one line each) so '
    'the delivery stays conversational rather than recited. Finally, map the bank to THIS employer: '
    'the posting’s top three requirements each get a designated lead story. That mapping step is the '
    'tailoring pass of Chapter 13, applied to speech.')
para(doc, 'One craft note on the failure and mistake stories, because they are the ones students fear '
    'and interviewers weight: choose real ones with real costs, spend one sentence on the ownership '
    'and most of the answer on the repair and the change. “I missed a regression in code review; the '
    'client found it. I owned it in standup the same day, wrote the checklist that would have caught '
    'it, and we adopted it team-wide — zero repeats in the year since.” The interviewer is not '
    'hunting for flawless people; they are screening for how you metabolize being wrong, because '
    'everyone is sometimes wrong and only some people convert it into systems (Chapter 4, Chapter 9, '
    'Chapter 16 — the whole course agrees on this one).')

h1(doc, 'During: the performance')
h2(doc, 'The first five minutes')
para(doc, 'The greeting is a rehearsable skill (Chapter 11’s introductions): name, eye contact, '
    'firm-normal handshake, and small talk played straight — it is the warm-up act, and it is being '
    'graded. Then comes the most predictable and most preparable moment in all of interviewing: '
    '“tell me about yourself.” It is not an invitation to biography. It is your Chapter 13 summary '
    'line, expanded to sixty seconds on the present-past-future skeleton: what you are now (“a finance '
    'graduate with two audit internships”), the evidence from the past (“at Medline I ran four '
    'supplier audits solo, including the corrective-action follow-ups”), and why you are HERE (“this '
    'role is exactly the next step — quality analysis at scale, in devices”). Script it, rehearse it '
    'aloud like Chapter 12’s first minute, and let it carry you through the adrenaline window on '
    'autopilot.')
h2(doc, 'The classics, decoded')
figure(doc, os.path.join(FIG, 'ch14_classics.png'),
    'Figure 3. The classic questions — and the real question underneath each.',
    'Four rows decoding classic questions: why do you want to work here (did you research us), your greatest weakness '
    '(are you self-aware and improving), why are you leaving or the gap (any red flags), and five years from now '
    '(fit or layover).')
para(doc, 'Every classic question has a question underneath it, and decoding the real one converts a '
    'trap into a prompt. “Why do you want to work here?” means “did you research us?” — answer with '
    'their specifics: the product, the expansion, the fit between the role and your evidence. “What is '
    'your greatest weakness?” means “are you self-aware and improving?” — the spec is a real, '
    'non-fatal weakness plus the visible fix: “I over-prepared presentations to the point of '
    'inefficiency; I’ve moved to timed rehearsal passes — three, aloud, done.” (Neither the '
    'disguised brag — “I care too much” — nor the fatal confession — “deadlines slip past me” — '
    'passes; the first insults the interviewer’s intelligence and the second answers a different '
    'question than was asked.) “Why are you leaving?” and “what about the gap?” mean “is there a red '
    'flag?” — one honest, forward-facing sentence, never a grievance tour, because every negative '
    'sentence about a former employer is silently transcribed as a preview of how you will one day '
    'describe THIS one (Chapter 7’s tone rules). And “where do you see yourself in five years?” means '
    '“is this role a fit or a layover?” — ambition aligned with the role’s actual path.')
h2(doc, 'Behavioral versus situational: the grounding pivot')
para(doc, 'Behavioral questions ask about the past (“tell me about a time you missed a deadline”); '
    'deploy the bank, STAR shape. Situational questions ask hypotheticals (“what would you do if a '
    'client demanded a policy exception?”); answer the principle briefly, then GROUND it: “here’s how '
    'that actually played out when…” — pivoting from hypothetical virtue to real evidence. The '
    'grounded answer outranks the purely hypothetical one every time, because anyone can describe '
    'ideal behavior and only your record proves yours. When no story fits, narrate how you would '
    'think instead: name the factors you would weigh, in order (Chapter 9’s criteria-first) — '
    'structured thinking is itself the answer being scored.')
h2(doc, 'Your questions are half the interview')
figure(doc, os.path.join(FIG, 'ch14_questions.png'),
    'Figure 4. The questions you ask — the role, the craft, the team; never logistics first.',
    'Four rows: the role (what does success at ninety days look like), the craft (what separates good hires from '
    'great ones), the team (how disagreement gets handled), and the warning that salary and perks questions asked '
    'first reframe the candidate as a perk shopper.')
para(doc, 'When the interviewer says “what questions do you have for me?”, the interview has not ended — '
    'it has changed direction, and this segment is scored as heavily as your answers, because your '
    'questions are the best sample of your curiosity and preparation. Bring three, written down '
    '(consulting notes is a professional act, not a weakness). The reliable excellent ones: “What does '
    'success in this role look like at ninety days?” (you are already thinking inside the job — and '
    'the answer is your onboarding map if hired); “What separates the good hires from the great ones '
    'here?” (interviewers love answering it, and the answer is gold); “How does the team handle '
    'disagreement?” (culture, made checkable — Chapter 11’s ground rules, asked from outside). Never '
    'open with salary, vacation, or remote policy: logistics before fit reframes you as a shopper of '
    'perks rather than a solver of problems, and the moment for those questions is the offer stage, '
    'when you hold the leverage anyway. And “no questions, I think you covered everything” reads as '
    'no interest — always three ready, knowing two may survive the conversation.')
h2(doc, 'The question that shouldn’t have been asked')
para(doc, 'Some questions touch legally protected ground — age, family plans, religion, national '
    'origin, health. Most arrive as clumsiness rather than malice, and the composed response answers '
    'the legitimate concern underneath without surrendering the protected information: asked about '
    'family plans, “if you’re asking about availability — my schedule fully covers the role’s hours, '
    'including the quarter-end pushes.” You may also decline gracefully: “I’d rather keep us on the '
    'role — and I’m confident nothing in my situation affects it.” Both moves are Chapter 7’s '
    'de-escalation seated in a chair: address the interest, skip the bait, stay warm. And note it '
    'privately: how an organization interviews is data about how it manages. You are evaluating them '
    'too — that is not a self-esteem slogan; it is the actual structure of the meeting.')

h1(doc, 'The money')
figure(doc, os.path.join(FIG, 'ch14_salary.png'),
    'Figure 5. The money conversation — the researched range early, the single reasoned ask at offer, everything in writing.',
    'Two panels show scripts for the early salary question (a calm researched range) and offer negotiation (one ask '
    'with a reason), above notes that the package is wider than the salary and that final terms go in writing before '
    'any resignation.')
para(doc, 'Chapter 13 put the research first: before any interview, you hold a written range with its '
    'basis — posted ranges, aggregate sites, and what the informationals told you. The range is what '
    'converts the feared early question into a routine exchange. Asked “what are your salary '
    'expectations?” in a screen, the script is calm, sourced, and unapologetic: “From what I’ve seen '
    'for this role in this region, $58–65K — and I’m flexible for the right fit.” A range anchors '
    'without cornering (Chapter 8’s anchoring, applied to yourself); its bottom must be a number you '
    'would genuinely accept. Deflection is also legal and increasingly just answered: “I’d like to '
    'understand the full role first — what’s the budgeted range?” Pay-transparency laws have made '
    'asking their range first ordinary practice; use it.')
para(doc, 'An offer is the start of a conversation, and negotiating it professionally is expected — '
    'recruiters budget for it, and the candidates who skip it out of gratitude or fear leave real '
    'money on the table at the one moment leverage favors them. The pattern is once, with a reason: '
    '“I’m excited about this role. Given the supplier-audit experience I’d bring, is there flexibility '
    'toward $63K?” — the single evidence-backed ask (Chapter 8’s calibrated ask), not a nibble '
    'sequence, which burns the goodwill you are about to live on. When the number is fixed, the '
    'package often is not: start date, signing bonus, development budget, remote days, review timing — '
    'all legitimately in play. And the closing rule carries maximum stakes: get the final version in '
    'writing before resigning anything (Chapter 6’s confirmation discipline). Offers evaporate, '
    'terms drift, and the email that says “confirming: $62K, start date July 14, $2K development '
    'budget” is the only version of events that survives a hiring manager’s departure.',
    bold_lead='Negotiating the offer.')

h1(doc, 'After: the follow-through')
figure(doc, os.path.join(FIG, 'ch14_followup.png'),
    'Figure 6. After the handshake — thank-yous within a day, a shaped wait, and grace at every outcome.',
    'A four-step timeline: individual thank-yous within 24 hours, one polite nudge at the promised deadline, a second '
    'nudge two weeks later, and a gracious reply at any outcome — plus the tip to ask the timeline in the room.')
para(doc, 'The thank-you message is a working document, not a courtesy stamp. Within 24 hours, to each '
    'interviewer individually — pull the names from your panel notes; the identical CC’d blast undoes '
    'the gesture. Reference a specific moment from the conversation (“your point about the '
    'supplier-audit backlog”), because specificity proves presence (the five-quality rules, Chapter 6). And '
    'let it do one useful thing: reinforce your strongest fit, or repair a stumble — “I gave a thin '
    'answer on LIMS; the fuller picture is two sentences: I ran its closest competitor for two years, '
    'and the migration playbook I wrote is in my portfolio.” The repair function is the underused '
    'one: the thank-you is a legitimate second chance at one flubbed answer, taken by almost nobody.',
    bold_lead='The thank-you that works.')
para(doc, 'Shape the wait before it starts by asking, in the room, “what are the next steps, and when '
    'should I expect to hear?” Now silence has a shape: the promised date passes, and one polite nudge '
    'goes out — two lines, warm, no grievance: “Following up on the analyst role — I remain very '
    'interested. Any update on timing?” Two silent weeks later, one more. Then let it go and keep the '
    'pipeline moving (Chapter 13’s tracker): three-plus contacts converts persistence into pestering, '
    'and the silence was already an answer — structural, not personal. One accelerant is honest and '
    'effective: a competing offer, disclosed straight. “I’ve received another offer with a Friday '
    'deadline — is a decision on your side possible this week?” It speeds real interest and reveals '
    'the absence of it, and both are information you need.', bold_lead='The wait, managed.')
para(doc, 'Every exit from the process is a relationship event. Rejected: reply anyway — almost no one '
    'does — “thank you for the process; I’d welcome consideration for future analyst openings.” '
    'Recruiters keep files, and graciousness gets filed too (the silver-medalist case below is this '
    'sentence, dramatized). Offered: evaluate before celebrating — the role, the manager, the path, '
    'the package, and everything the interviews revealed about how the place actually runs '
    '(Chapter 13’s red-flags section, final reading). Declining an offer: prompt, warm, final — '
    '“I’ve accepted a role elsewhere that fits my path; thank you, sincerely” — because burned '
    'bridges are all toll bridges eventually. And resigning the old job: two weeks’ written notice, '
    'gratitude regardless of the tenure’s private truth, full effort through the last hour. The exit '
    'IS the reference (Chapter 11).', bold_lead='Grace at every outcome.')

h1(doc, 'Case study: the silver medalist')
para(doc, 'She finished second for the analyst role — a strong final round, a warm rejection call, the '
    'kind of loss that most candidates archive with a sigh. Her reply took four minutes to write and '
    'redirected her career: thanks for a genuinely well-run process, one sentence of continued '
    'interest, and one question — “if you’re willing: what would have made the difference?” The '
    'recruiter, disarmed by the grace and the specificity, answered honestly: the winner had deeper '
    'supplier-audit exposure.')
para(doc, 'What she did with that sentence is the case. She spent two months closing exactly that gap — '
    'a supplier-audit module in a professional certificate, plus a shadow assignment she negotiated '
    'in her current role — and then sent the two-line update nobody sends: “You mentioned '
    'supplier-audit depth; took that seriously. Certificate finished, and I’ve now supported three '
    'supplier audits end-to-end.” No ask attached (Chapter 6’s selfless S). When the winner left in '
    'month five — new hires leave at the highest rate of any tenure cohort — there was no new '
    'posting and no new interview loop. There was a phone call, and the call was to her.')
bullets(doc, [
    ('The lesson about processes:', 'they end; impressions don’t. Recruiters and managers keep mental '
     '(and literal) files of impressive silver medalists, and openings recur far more often than '
     'candidates model.'),
    ('The lesson about feedback:', 'the “what would have made the difference?” question converts a '
     'rejection into a diagnostic — and it is answerable precisely because the stakes are over.'),
    ('The lesson about the update:', 'the no-ask progress note is the highest-signal, lowest-cost '
     'message in the entire search genre. It proves coachability, follow-through, and continued '
     'interest in nine seconds of reading.'),
])

h1(doc, 'Case study: the interview that was actually four interviews')
para(doc, 'A finance senior drew a full onsite loop for a rotational analyst program: an HR screen, a '
    'hiring-manager behavioral, a case session with two analysts, and a wrap-up with the program '
    'director. He prepared as if it were one interview, and it nearly cost him — because a loop is '
    'four different audiences (Chapter 2) asking four different real questions, and his day turned on '
    'recognizing that in time.')
para(doc, 'The HR screen asked “are you consistent and viable?” — his dates, his range (researched, '
    'delivered calmly), his authorization status. The hiring manager asked “can you do MY problem?” — '
    'behavioral questions aimed at deadlines and data quality, which his story bank covered, though '
    'he noticed her energy rise only when his answers carried numbers. The case session asked “how do '
    'you think when nobody has pre-chewed the problem?” — a margin-erosion puzzle where his '
    'instinct to fill silence with talk nearly sank him, until he remembered the working-session '
    'protocol: clarify first (“is this one product or the category?”), structure aloud (“I’d check '
    'price, mix, and input costs, in that order”), and land a verdict under uncertainty (“given the '
    'data as presented, I’d investigate mix first — here’s why”). And the director’s wrap-up asked '
    '“will you stay and grow?” — five-year questions his present-past-future frame handled, plus his '
    'own three questions, which visibly landed: the ninety-day success question earned him a '
    'four-minute answer and a tour of the actual dashboard.')
para(doc, 'He got the offer, and the debrief email he sent himself that night (Chapter 12’s '
    'self-review habit) is the case’s takeaway list: the same stories flexed to four different '
    'emphases; the case session was won by protocol, not brilliance; and every interviewer answered '
    'a DIFFERENT real question, so uniform preparation would have been wrong preparation. Loops are '
    'not one interview four times. They are four audiences, one candidate, and a day-long test of '
    'Chapter 2.')

h1(doc, 'Worked example: one story, four costumes')
para(doc, 'To make the bank’s flexibility concrete, here is one real-shaped story — the bookstore '
    'inventory-shortage fix from Chapter 13’s makeover — worn four ways. The facts never change; the '
    'emphasis rotates to the question asked.')
bullets(doc, [
    ('Asked for initiative:', 'S/T: recurring inventory shortages, nobody assigned. A: “I pulled '
     'three months of receiving logs on my own time and traced the variance to a logging error at '
     'delivery.” R: “the corrected process was adopted storewide — variance under 1% since.” The '
     'emphasis: nobody asked; I noticed; I acted.'),
    ('Asked for persuasion:', 'same S/T. A: “the receiving lead had run her process for nine years — '
     'I brought her the logs privately, asked her read on them first, and let the fix become ours '
     'rather than mine.” R: same. The emphasis: Chapter 16’s let-the-idea-be-theirs, lived.'),
    ('Asked for analysis:', 'same S/T. A: “I ruled out theft and miscounting by cross-checking '
     'shrinkage against shift patterns before touching the receiving hypothesis.” R: same. The '
     'emphasis: criteria-first elimination, data before conclusions.'),
    ('Asked for a mistake:', 'the honest variant: “my first theory was theft, and I said so too '
     'early — to the wrong person. I walked it back the same day, apologized to the shift I’d '
     'implicated, and rebuilt trust by showing the full analysis when it was actually done.” The '
     'emphasis: owned fast, repaired visibly.'),
])
para(doc, 'One event, four true tellings — which is why eight stories cover a hundred questions. Build '
    'each story once with ALL its facets noted, and the interview becomes selection rather than '
    'recall: the same twenty-minute economy that made Chapter 13’s tailoring sustainable.')

h1(doc, 'Deep dive: the phone screen, minute by minute')
para(doc, 'The screen is the most underestimated stage — twenty to thirty minutes that decide whether '
    'anyone senior ever reads your file, conducted by a recruiter running a checklist. Minutes one to '
    'five: logistics and rapport, and your voice is the entire medium — stand up (posture is audible), '
    'smile (also audible), and take the call somewhere silent with your résumé, the posting, and your '
    'range in front of you. Minutes five to fifteen: the verification pass — walk-me-through-your-résumé '
    '(present-past-future, expanded per stop), availability, authorization, sometimes the salary '
    'question (your researched range, delivered calmly — the screen is exactly where it arrives). '
    'Minutes fifteen to twenty-five: two or three light behavioral questions, screening for '
    'communication quality as much as content — answer in tight STAR, ninety seconds, no rambling, '
    'because the recruiter is literally scoring “communicates clearly” on a form. Final minutes: your '
    'two questions (keep one logistics-flavored — “what does the rest of the process look like, and '
    'when should I expect to hear?” — which is also the shaped-wait setup), and a clean close: “I’m '
    'genuinely interested — I’d welcome the next conversation.” Enthusiasm stated plainly is not '
    'desperation; recruiters advance candidates they are confident will say yes.')

h1(doc, 'Deep dive: the camera between you')
para(doc, 'Live video interviews inherit Chapter 12’s full camera kit: lens at eye level, light in '
    'front of the face, the frame from mid-chest up with headroom, and energy raised roughly twenty '
    'percent because the camera flattens everything. Look AT the lens when delivering key answers — '
    'the lens is their eyes — and park your notes just beneath it so glances stay honest. Two '
    'video-specific disciplines: the lag pause (wait half a beat after the interviewer finishes; the '
    'talk-over that lag produces reads as interrupting even when it is physics), and the tech '
    'rehearsal thirty minutes early with the phone-number fallback written on paper, because “can '
    'you hear me now?” is a first impression too. Dress fully — the standing-up moment happens more '
    'than anyone admits — and stage the background: tidy, neutral, nothing you would not want '
    'discussed.')
para(doc, 'The one-way (recorded) screen — prompts on screen, camera recording, no human — is now '
    'standard at volume employers and feels alien precisely because the conversational feedback loop '
    'is gone. Reframe it as a teleprompter test: each prompt is a behavioral question, so deploy the '
    'story bank in STAR exactly as if a person had asked. Use every second of prep time the platform '
    'offers; look at the LENS, not your own preview tile (disable self-view if allowed — watching '
    'yourself is a composure tax); keep answers inside the time limit with one beat to spare; and if '
    'retakes are allowed, cap yourself at one — Chapter 12’s clean-take rule, because the fifth '
    'attempt is stiffer than the first and the afternoon is gone. Same energy as live: the recording '
    'flattens harder than the call.', bold_lead='The one-way screen.')

h1(doc, 'Deep dive: panels and working sessions')
para(doc, 'The panel adds audience mechanics to everything above. Collect every name in seat order as '
    'introductions happen — you will need them for eye contact now and individual thank-yous tonight. '
    'Answer to the asker, then sweep: open on the questioner, distribute the middle of the answer '
    'across the room, land back on the asker (Chapter 12’s eye-contact-in-sentences, seated). Read '
    'the roles as they emerge — the technical panelist probing depth, HR tracking consistency with '
    'your file, the manager testing fit — and let one answer nod to each where it can. And attend to '
    'the quiet panelist: they are frequently the veto vote, and bringing them in with your eyes even '
    'when they never speak is the difference between a room you addressed and a room you worked.')
para(doc, 'The working session — solve this case, analyze this dataset, respond to this scenario — '
    'scores the HOW. The protocol: clarify before computing (“is this one product or the category? '
    'what’s the decision this analysis serves?”) because diving in unquestioning is the classic '
    'fail; think aloud in structure (“I’d check price, mix, and input costs, in that order, '
    'because…”) since silent brilliance scores as silence; correct course visibly when a path dies '
    '(“actually, that assumption breaks here — adjusting”) because self-monitoring is precisely '
    'what they are hiring; and land a verdict under uncertainty (“given what’s here, I’d '
    'investigate mix first”) because the verdict habit (Chapter 10) is what separates analysts '
    'from narrators. You are allowed to be wrong in a case session. You are not allowed to be '
    'structureless.', bold_lead='The working session.')

h1(doc, 'Reading the room mid-interview')
para(doc, 'Interviews are conversations, and conversations broadcast feedback continuously '
    '(Chapter 1’s nonverbals) — candidates just forget to read it while managing their own nerves. '
    'Watch for the drift: checked watches, flat follow-ups, the interviewer glancing at their own '
    'notes mid-answer — all mean wrap this answer; the two-minute STAR has a ninety-second version, '
    'and deploying it is a skill they notice. Watch for the lean-in: forward posture and follow-up '
    'questions mean go deeper, and “want the detail on how we caught it?” offers depth without '
    'imposing it. Match the register you find: a formal panel gets formal; a conversational manager '
    'gets conversational — mirroring the room is fit, demonstrated live. And hold your nerve through '
    'the post-answer silence: interviewers take notes, and the three quiet seconds after your answer '
    'are not failure — filling them with backpedaling (“…but maybe that’s not what you meant…”) '
    'converts a good answer into a nervous one. Let it land (Chapter 12’s pause, received rather '
    'than performed).')

h1(doc, 'The internal interview: higher familiarity, higher tax')
para(doc, 'Interviewing where you already work invites coasting — they know me — and the panel notices '
    'coasting fastest in exactly the candidate they know. Prepare MORE, not less: assume the panel '
    'knows nothing, because formally, they must evaluate what you present, not what they remember. '
    'Re-introduce your evidence: your daily visibility is not a story bank, and “you’ve all seen my '
    'work” is not an answer — the internal candidate who STARs their own known projects reads as '
    'rigorous, not redundant. Handle the awkwardness in the open: your current manager should hear '
    'about your candidacy from you, early (“I’ve told my team I’m pursuing this” beats being '
    'discovered pursuing it, per Chapter 7’s early-disclosure rule), and colleagues who also applied '
    'get graciousness before and after. And if you lose, run the silver-medalist play inside the '
    'building, where it works even better: the feedback ask, the visible gap-closing, the next '
    'opening — with the advantage that everyone watches you handle the loss, and handling it well is '
    'itself a promotion argument.')

h1(doc, 'Evaluating the offer: the decision you rehearsed for')
para(doc, 'The offer call triggers a decision that deserves the same rigor as any Chapter 9 '
    'comparison: criteria first, then evidence. Build the matrix before the emotions arrive — the '
    'role (the actual daily work, per the ninety-day answers you collected), the manager (the single '
    'strongest predictor of early-career experience; you interviewed them too, whether they knew it '
    'or not), the path (what the role becomes in two years, and whether anyone you met had walked '
    'it), the package (salary against your researched range, plus the wider terms), and the '
    'signals (everything the process revealed — how they treated your time, how they handled your '
    'questions, what the red-flags reading of Chapter 13 surfaced). Weight the criteria BEFORE '
    'scoring the offer (Chapter 9’s anti-rigging rule, self-applied), because post-hoc weighting is '
    'how people talk themselves into shiny mistakes. Ask for the time you need — “can I have until '
    'Friday?” is routine, and pressure to decide same-day is itself a signal. And decide, then '
    'commit (Chapter 11): the accepted offer ends the search, including the tempting loose ends. '
    'Recruiters who learn you kept shopping after accepting file THAT, too.')

h1(doc, 'Case study: the same question, three candidates')
para(doc, 'One hiring manager, one week, one question asked identically of three finalists for a '
    'coordinator role: “Tell me about a time you had to deliver bad news.” The transcript patterns '
    'are the chapter in miniature.')
para(doc, 'Candidate one answered in theory: “I believe transparency is important, so I always '
    'communicate proactively and honestly…” — ninety seconds of principle, zero events. Sincere, '
    'unusable: nothing to verify, nothing to score, and the manager’s note read “couldn’t produce '
    'an example.” The hypothetical answer to a behavioral question is a category error, and it is '
    'the single most common one.')
para(doc, 'Candidate two had the event but not the architecture: a rambling six-minute account of a '
    'delayed shipment, rich in context (the vendor’s history, the weather, a coworker’s vacation), '
    'in which the candidate’s own actions surfaced twice, vaguely, as “we kept everyone in the '
    'loop.” The manager’s note: “was she even the one who handled it?” The material was probably '
    'strong. The telling buried it — the collective middle, the missing result, the situation that '
    'ate the answer.')
para(doc, 'Candidate three ran STAR in a hundred and five seconds: the client expecting Friday '
    'delivery (S), her account to manage (T), the call she made Tuesday — the day the slip was '
    'confirmed, not Thursday — with the revised date and a partial-delivery option she had already '
    'cleared with operations (A), and the outcome: the client took the partial, the account renewed, '
    'and “I learned to never let a deadline die silently — the Tuesday call is now my rule” (R, with '
    'the learning). The note: “does the Chapter 7 thing instinctively — hire.” The manager had never '
    'read Chapter 7. The candidate had simply prepared the story — which is to say, the difference '
    'between the three was not their histories. It was whether the history had been written down, '
    'shaped, and rehearsed before someone asked.')

h1(doc, 'The interviewer’s scorecard: what the form actually says')
para(doc, 'Structured interviews — the kind serious employers run — end with the interviewer filling '
    'out a form, and knowing the form’s shape changes how you answer. Typical dimensions: '
    'communication (clear, organized answers — STAR is literally the rubric’s friend), technical or '
    'functional depth (evidence at the right altitude for the role), problem-solving (the '
    'working-session protocol, scored), culture-and-values fit (usually behavioral evidence against '
    'named company values — read those values the night before; they are on the website because '
    'interviewers are told to probe them), and motivation (the decoded “why us?” answer). Each '
    'dimension gets a rating and — this is the part candidates forget — a required EXAMPLE: the '
    'form says “cite specific evidence,” which means your job in every answer is to hand the '
    'interviewer a sentence they can transcribe. “Cut intake errors 38% by redesigning the '
    'checklist” gets written down verbatim. “I’m very detail-oriented” gives them nothing to '
    'transcribe, and untranscribed answers do not survive the debrief meeting where hire decisions '
    'actually happen. You are not talking to the interviewer. You are writing, through them, to a '
    'form and a meeting you will never see.')

h1(doc, 'Assessment days and group formats')
para(doc, 'Volume employers and rotational programs sometimes run assessment days: multiple '
    'candidates, group exercises, observed discussions, and a rotation of short interviews. The '
    'group exercise — six candidates, one problem, observers with clipboards — is the format '
    'students misread most, because the instinct is to compete for airtime, and airtime is not the '
    'rubric. Observers score contribution quality (the missing fact, the structuring move, the '
    'summary that lands a decision — Chapter 11’s meeting craft, performed), collaboration (building '
    'on others by name: “extending Maya’s point…”), and facilitation instincts (drawing out the '
    'quiet candidate scores higher than outshouting the loud one — “we haven’t heard Jordan’s take” '
    'is the single most reliably scored sentence in the genre). The candidate who dominates loses '
    'to the candidate who makes the GROUP smarter, every time, because the employer is not hiring a '
    'gladiator; they are casting a team. Treat fellow candidates as colleagues from minute one — '
    'some of them, in four months, will be.')

h1(doc, 'Case study: the offer weighed — and declined')
para(doc, 'Two offers arrived nine days apart. Offer A: $64K, a prestige-brand employer, a rotational '
    'title, and a process that had been chronically disorganized — three rescheduled interviews, a '
    'ghosted week, interviewers who had not read her file, and a hiring manager who answered the '
    'ninety-day success question with “we’ll figure that out when you’re here.” Offer B: $58K at a '
    'mid-size firm nobody at her graduation party would recognize — and a process that had been '
    'crisp at every touch: prepared interviewers, a manager who answered the success question with '
    'specifics and introduced her to the analyst she would replace (who was being promoted, and '
    'said so happily), and a same-week decision delivered when promised.')
para(doc, 'The criteria matrix — built before the offers, per this chapter — is what kept the '
    'decision honest. On brand and salary, A won. On manager, path, and process signals, B swept: '
    'the disorganization of A’s process WAS data (Chapter 13’s red-flags reading — how they hire '
    'is how they manage), and the promoted predecessor at B was the single strongest path evidence '
    'a candidate can find. She negotiated B’s offer once, with a reason (the $64K competing '
    'number, disclosed honestly), landed at $61K plus a development budget, confirmed in writing, '
    'and declined A promptly and warmly. Eighteen months later the postscript wrote itself: A’s '
    'rotational cohort had 40% attrition and her would-have-been manager was gone; she had shipped '
    'two systems at B and been promoted on the predecessor’s schedule. The $6K she “lost” at '
    'signing had cost A’s cohort members far more in stalled first years. The matrix knew.')
bullets(doc, [
    ('The lesson about signals:', 'the process is a free sample of the management. Weigh it like '
     'one — chronically disorganized hiring predicts chronically disorganized everything.'),
    ('The lesson about paths:', 'the happily promoted predecessor is worth more than $6K of '
     'salary. Ask to meet the person you’d replace; the answer to the REQUEST is data even when '
     'the meeting never happens.'),
    ('The lesson about method:', 'criteria weighted before offers arrive are the only defense '
     'against prestige and recency doing your deciding for you.'),
])

h1(doc, 'Workshop: your résumé is the question bank')
para(doc, 'Interviewers build their questions from your résumé while sitting in the lobby — which '
    'means you can pre-run the interview tonight with a highlighter and the audit method. Pass '
    'one: for every bullet, generate the obvious probe — a number invites “how did you measure '
    'that?”, a team win invites “what was YOUR part?”, a tool claim invites “walk me through how '
    'you used it.” Write the probe in the margin; if you cannot answer one fluently, the bullet is '
    'either overclaimed (fix the résumé — Chapter 13’s audit standard) or under-rehearsed (fix '
    'you). Pass two: hunt the seams — gaps, short stints, the pivot from chemistry to finance — '
    'and script the one honest forward-facing sentence each seam gets. Pass three: map bullets to '
    'the story bank — every strong bullet should have a story behind it, and every banked story '
    'should surface at least one bullet; orphans on either side are prep work. Thirty minutes, and '
    'you have converted your own document from ambush surface into home turf. The candidates who '
    'seem unshakeable in interviews are not quicker on their feet. They have simply already heard '
    'every question, from themselves, on Tuesday.')

h1(doc, 'Five myths, retired')
para(doc, 'Retired by every structured-interview study: preparation raises validity for both sides — '
    'the prepared candidate gives the interviewer MORE signal, not less. What reads as inauthentic '
    'is recitation, and the beat-card discipline exists precisely to prevent it. “Just be yourself” '
    'is advice from people who were never nervous.', bold_lead='Myth: preparation makes you fake.')
para(doc, 'The firm handshake and confident opening matter less than folklore claims, and the final '
    'impression — your questions, your close, the thank-you — enjoys recency effects folklore '
    'ignores (Chapter 12’s frame, applied to you as the content). Strong finishes rescue average '
    'starts far more often than the reverse.', bold_lead='Myth: it’s decided in the first ten seconds.')
para(doc, 'Interviewers systematically favor candidates who ask good questions and listen well over '
    'candidates who monologue impressively — the interview is a conversation sample, and '
    'conversation is bidirectional (Chapter 1). Airtime is not evidence.',
    bold_lead='Myth: talk more, impress more.')
para(doc, 'Negotiating a reasoned ask does not cost offers; recruiters budget for it, and the '
    'research on negotiation regret runs overwhelmingly one direction. What costs offers is the '
    'nibble sequence, the ultimatum, and the bluffed competing offer — manner, not the ask itself.',
    bold_lead='Myth: negotiating will make them rescind.')
para(doc, 'Rejections are mostly fit-and-numbers events inside a funnel you cannot see — the other '
    'finalist’s supplier-audit depth, the hiring freeze, the internal candidate. The '
    'silver-medalist play exists because processes end and impressions persist; taking the loss as '
    'a verdict on your worth misreads both the system and your evidence.',
    bold_lead='Myth: rejection means you failed.')

h1(doc, 'Second-round and final-round dynamics')
para(doc, 'Later rounds change the question being asked. The first round screened for “can they?”; '
    'finals screen for “will they, here, with us?” — which shifts the evidence you should '
    'volunteer. Expect deeper probes on fewer topics (the panel has compared notes; the thing that '
    'concerned anyone WILL return, so the concerns question from the FAQ is your preemptive '
    'tool). Expect repeated questions across interviewers — answer them consistently but not '
    'identically; the debrief compares transcripts, and identical phrasings read as recitation '
    'while contradictions read as invention. Expect more selling in your direction: finals are '
    'where they show you the good conference room, and recruiting charm is data about their '
    'interest but not about the job — keep your red-flags reading running even while being '
    'courted. And expect the closing dynamics to invert: by the final round, “do you have '
    'questions?” is genuinely load-bearing, because your questions now signal how you would '
    'decide, and deciders are what finals are hiring. The strongest final-round question in most '
    'processes: “what would make the person in this role indispensable to you a year from now?” — '
    'it converts the interview’s last five minutes into the job’s first planning meeting.')

h1(doc, 'Worked examples: three thank-yous, annotated')
para(doc, '“Ms. Chen — thank you for this afternoon. Your walkthrough of the ninety-day expectations '
    'made the role concrete, and the audit-backlog challenge you described is exactly the kind of '
    'problem I ran at Medline. I remain very interested, and I’m glad to provide anything further. — '
    'Jordan.” Four sentences: the specific moment (ninety-day walkthrough), the fit reinforcement '
    '(backlog → Medline), the plain interest statement, the open door. Nothing else belongs.',
    bold_lead='The standard, done well.')
para(doc, '“Mr. Okafor — thank you for today’s conversation. One addition: my answer on LIMS '
    'undersold the relevant experience — I administered its closest competitor for two years, '
    'including a version migration, and the transition playbook I wrote is linked in my portfolio. '
    'The parallel is close enough that I’d expect a short ramp. Thanks again for a rigorous '
    'interview — I enjoyed it. — Jordan.” The repair is one move, evidence-shaped, no groveling: '
    'not “I’m sorry I froze” but here is the fuller answer. One repair per note, maximum; a '
    'thank-you that relitigates three answers is a transcript of anxiety.',
    bold_lead='The repair, done well.')
para(doc, '“Dear team — thanks so much everyone!! I really enjoyed meeting you all and I think I '
    'would be a great fit for your company. Hope to hear from you soon!!!” — sent to five people '
    'as one CC. Every failure is instructive: no names (the panel roster existed), no specifics '
    '(interchangeable with every other candidate’s note), enthusiasm doing the work evidence '
    'should, and punctuation Chapter 5 already prosecuted. The note is not neutral; it actively '
    'converts a decent interview into a weaker file, because it is the last writing sample they '
    'see.', bold_lead='The counterexample.')

h1(doc, 'Case study: the bombed interview, recovered')
para(doc, 'The case session went badly: he misread the dataset’s units in the first five minutes, '
    'built ten minutes of analysis on the error, and caught it himself only when a panelist’s '
    'question made the impossibility obvious. The freeze lasted a visible five seconds. What '
    'happened next is why the case is in this guide: he named it plainly — “I misread thousands '
    'as units, which invalidates everything I just did; let me redo the two calculations that '
    'matter” — redid them aloud in four minutes, landed a corrected verdict, and finished with '
    '“and that error is exactly why my first move on real data is a units-and-totals sanity '
    'check; today I skipped my own rule.”')
para(doc, 'His thank-you that evening ran the repair pattern: one sentence owning the stumble, two '
    'sentences on the sanity-check protocol he actually uses, no groveling. The debrief, he '
    'later learned from the manager who hired him, had split: two interviewers scored the error '
    'harshly, but the panel chair argued the recovery WAS the evaluation — “everyone here has '
    'built on a bad assumption; I want the ones who catch it out loud and fix it fast.” The '
    'scorecard’s problem-solving row, on three of four forms, cited the recovery verbatim. '
    'Chapter 12’s demo case taught that audiences price the worst moment; this case adds the '
    'employment corollary — interviewers price the RESPONSE to the worst moment, because the '
    'worst moment is the only part of the interview that reliably predicts a Tuesday in month '
    'three.')

h1(doc, 'What happens after the final round')
para(doc, 'Between “we’ll be in touch” and the offer call sits machinery worth understanding. The '
    'debrief: interviewers meet (or thread) with their scorecards, and the transcribable evidence '
    'you handed them does the arguing in your absence — this is why the form-writing framing '
    'matters. Reference checks: expect two or three calls to the people you briefed (Chapter 13), '
    'typically confirming dates, titles, and the flavor of your contributions; your prepared, '
    'recently-thanked references answer warmly and specifically, which is the whole reason the '
    'ask-brief-thank protocol exists. Background verification: employment dates, degrees, sometimes '
    'credit or records depending on the role — all of it checking the claims you made, which is why '
    'Chapter 13’s audit standard (“every line survives the reference call”) was never rhetorical. '
    'And sometimes: silence, because approvals stall, budgets freeze, and reorganizations eat '
    'requisitions — none of which anyone will tell you, which is why the shaped-wait cadence exists '
    'and why the pipeline keeps moving until a start date is signed. The stretch between final '
    'round and offer is where candidates most often undo themselves: the anxious daily follow-up, '
    'the social-media vaguepost about “big news coming,” the resignation tendered on a verbal '
    'promise. The professional plays it exactly as boring as it is.')

h1(doc, 'Presence: the dress and grooming question, settled')
para(doc, 'The rule is one notch above the role’s daily norm: a suit where business casual reigns, '
    'business casual where the floor wears polos, and when in doubt, the recruiter answers “what’s '
    'the dress expectation?” without judging the question. The deeper principle is subtraction — '
    'dress so nothing about your appearance becomes a topic, because every minute the interviewer '
    'spends processing your outfit is a minute of evidence you did not get to give. Fit and repair '
    'beat price: the pressed, fitting, unremarkable outfit from anywhere outperforms the expensive '
    'wrinkle. Grooming is the same subtraction logic, plus the sensory floor — light or no '
    'fragrance (interview rooms are small and allergies are real), and nothing that jingles, '
    'clicks, or requires adjusting on camera. For video: solids over patterns (cameras moiré on '
    'stripes), and the full-dress rule from the virtual section. None of this is fashion advice. '
    'It is Chapter 1’s nonverbal channel, managed so the verbal channel gets the whole budget.')

h1(doc, 'The week-of checklist')
numbered(doc, [
    'Five days out: confirm the logistics in writing — time, format, names, address or link. '
    '(“Looking forward to Thursday at 2:00 with you and Ms. Chen” catches errors while they’re '
    'cheap.)',
    'Four days out: research refreshed — the three deployable facts, interviewer paths, and the '
    'company’s values page (the scorecard’s culture dimension is built from it).',
    'Three days out: story bank mapped to this posting’s top three requirements; the résumé '
    'question-bank audit run with the margin probes.',
    'Two days out: mock run — the sixty-second opener aloud, two STAR answers aloud, your three '
    'questions rehearsed. Video? Full tech rehearsal at the actual hour, for the actual light.',
    'Day before: dry run of route or platform; kit packed (résumés, notes, pen, water); outfit '
    'chosen and checked; salary range card written; early night. No new prep after dinner — '
    'Chapter 12’s content-freeze rule applies to interviews too.',
    'Day of: arrive ten early; phone silenced BEFORE the lobby; kind to everyone from the parking '
    'lot in; slow exhale at the door; opener on autopilot; notes out with your questions. Then '
    'trust the week.',
])

h1(doc, 'Frequently asked questions')
para(doc, 'Yes — bullet-level notes are professional, and consulting them visibly (“I want to make '
    'sure I ask this precisely”) reads as prepared. What you cannot do is read answers: notes are '
    'for YOUR questions, names, and the two facts you refuse to misstate.',
    bold_lead='Can I bring notes into the interview?')
para(doc, 'A day is fine; same-hour is fine; what matters is within 24 and individually. If you '
    'interviewed Friday afternoon, Monday morning beats Saturday night — arrival during business '
    'hours reads better than timestamp devotion.', bold_lead='How fast must the thank-you go?')
para(doc, 'Tell the truth at the resolution the question deserves: “the role and I weren’t a fit, '
    'and the parting was mutual” covers most terminations without the autopsy. Never lie — '
    'reference and background checks exist — and never grievance-tour (Chapter 7). One '
    'forward-facing sentence, then bridge to the evidence for THIS role.',
    bold_lead='What if I was fired?')
para(doc, 'Practice with it the way Chapter 15 prescribes for everything: generate likely questions '
    'from a posting, drill STAR answers aloud against a chatbot, ask it to attack your weakest '
    'story. Do not bring it INTO the interview (yes, including the earpiece — people have tried; '
    'people have been caught), and do not let it write answers you have not lived: the follow-up '
    'question finds the seam in one exchange.', bold_lead='Can AI help me prep?')
para(doc, 'Once, briefly, at the end: “before we wrap — is there anything in my background giving '
    'you pause that I could speak to?” It is the two-sided move (Chapter 8) as a closing question, '
    'it surfaces the objection while you are still in the room to answer it, and interviewers '
    'remember the candidates composed enough to ask it.',
    bold_lead='Should I ask about their concerns directly?')

h1(doc, 'Nerves, one more time')
para(doc, 'Chapter 12 taught the arousal reframe — the pulse and the readiness share one chemistry, and '
    'preparation is what relabels it. Interviews add a wrinkle worth naming directly: unlike a scheduled '
    'talk, an interview is a live back-and-forth with a stranger judging you, and the fear is not '
    'irrational — something real is at stake. The antidote is not pretending otherwise; it is the same '
    'one this whole chapter has been building toward. Preparation converts an unstructured threat into a '
    'structured, rehearsed event: the opener is scripted, the stories are banked, the questions are '
    'written, the range is researched. What remains genuinely unscripted — the exact wording of each '
    'question — is a small enough surface that the rest of your nervous system can treat the whole '
    'event as familiar. Walk in able to say, honestly, “I have done everything that was mine to do '
    'before this room.” That sentence, more than any breathing exercise, is what actually calms '
    'candidates who have done the work in this guide.')

h1(doc, 'The last mile: three sentences worth memorizing')
para(doc, 'If nothing else from this chapter survives to interview day, these three sentences do more '
    'work than any other single habit here. First, the opener: your sixty-second present-past-future, '
    'spoken so often in rehearsal that it arrives without a script the moment nerves spike. Second, '
    'the recovery line for the moment something goes wrong — a blanked answer, a misread question, a '
    'stumbled number — “let me back up and take that more carefully” buys the two seconds every '
    'composed recovery in this guide actually needed. Third, the close: “I’m genuinely excited about '
    'this — what would be a good next step?” State interest plainly; asking for the next step turns '
    'a passive ending into a small, professional ask (Chapter 6’s dated-request instinct, one last '
    'time). None of the three requires talent. All three require having said them out loud before the '
    'room asks for them.')

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Draft your eight-story bank as headlines tonight; write ONE story in full prose, then compress '
    'it to beat cards. One per day finishes the bank in a week.',
    'Script your sixty-second “tell me about yourself” on present-past-future. Rehearse it aloud '
    'twice — once into your phone; listen back kindly.',
    'Write your researched salary range with its basis (Chapter 13’s money section), and rehearse '
    'saying it aloud once. The number spoken calmly in practice arrives calmly in the screen.',
    'Draft your three questions for a real target employer. Test each: does it prove preparation, '
    'and would the answer actually inform your decision?',
    'Mock interview with a classmate or the career center — thirty minutes, behavioral questions '
    'from your own résumé’s lines. Every line, remember, is fair game.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'STAR is criticized as producing over-rehearsed, formulaic answers. Where is the line between '
    'prepared and canned — and what, specifically, keeps a beat-card answer conversational?',
    'The weakness question persists despite everyone knowing its games. Defend it from the '
    'employer’s side: what does a good answer actually reveal? Then design a better question that '
    'reveals the same thing.',
    'Should candidates always negotiate offers? Construct the cases where the single reasoned ask is '
    'wrong — and what the professional alternative is in each.',
    'The silver-medalist case rests on behavior almost no candidate performs. Why not? Name the '
    'psychological frictions, and the reframe that dissolves each.',
    'One-way video interviews scale screening but strip the conversation both directions. Argue the '
    'fairness question from candidate and employer sides, and propose the format that keeps the '
    'efficiency while restoring what matters most.',
])

keyterms(doc, [
    ('Behavioral interview', 'the format that treats past behavior as evidence of future behavior — '
     '“tell me about a time…” — answered with STAR.'),
    ('STAR', 'Situation, Task, Action, Result: the ninety-second architecture of a behavioral '
     'answer, with “I” actions and a measurable end.'),
    ('Story bank', 'the eight prepared stories (conflict, failure, deadline, leadership, persuasion, '
     'mistake, initiative, team win) that cover nearly every behavioral question — written once, '
     'indexed by beats, mapped to each posting.'),
    ('Present-past-future', 'the sixty-second “tell me about yourself” skeleton: what you are, the '
     'evidence, why you’re here.'),
    ('Grounding pivot', 'answering a hypothetical (situational) question with the principle, then '
     'real evidence: “here’s how that actually played out when…”'),
    ('The question beneath the classic', 'the decoding habit: every standard question (“greatest '
     'weakness?”) has a real question underneath (“self-aware and improving?”) that the answer '
     'should serve.'),
    ('Researched range', 'the salary band with a written basis — posted ranges, aggregates, '
     'informational conversations — held BEFORE any interview.'),
    ('Single reasoned ask', 'the offer-negotiation pattern: one evidence-backed request, then '
     'decide — never the nibble sequence.'),
    ('Repair thank-you', 'the follow-up message that fixes one flubbed answer in two sentences — '
     'the interview’s only legitimate second chance.'),
    ('Shaped wait', 'the follow-up cadence made possible by asking the timeline in the room: nudge '
     'at the promised date, once more two weeks later, then release.'),
    ('Silver-medalist play', 'the post-rejection sequence — gracious reply, feedback question, '
     'visible gap-closing, no-ask update — that converts a loss into the next opening’s first call.'),
    ('Working-session protocol', 'clarify first, structure aloud, self-correct visibly, land a '
     'verdict under uncertainty — how live case interviews are scored.'),
])

quiz(doc, [
    ('The STAR structure’s most common failure is:',
     ['Too much detail in the situation', 'A vague, collective middle — “we handled it” — with no measurable result',
      'Numbers in the result', 'Stories drawn from coursework']),
    ('“What is your greatest weakness?” is really asking:',
     ['For a disqualifying confession', 'Whether you are self-aware and visibly improving',
      'Whether you will criticize past employers', 'For a disguised strength']),
    ('When a situational (hypothetical) question arrives, the strongest move is:',
     ['Decline to speculate', 'State the principle, then ground it in a real example from your record',
      'Ask for more hypothetical detail', 'Recite the relevant policy']),
    ('Candidates should never open their questions segment with salary or perks because:',
     ['Those topics are illegal to discuss', 'Logistics before fit reframes you as a perk shopper — the leverage moment is the offer stage anyway',
      'Interviewers never know the range', 'It shortens the interview']),
    ('Asked for salary expectations in an early screen, the professional response is:',
     ['“Whatever you think is fair”', 'A calm researched range whose bottom you would genuinely accept',
      'Refusing until an offer exists', 'A single non-negotiable number']),
    ('Offer negotiation should be:',
     ['Avoided by grateful candidates', 'One evidence-backed ask, then a decision — with final terms in writing before resigning anything',
      'A multi-round nibble across every term', 'Conducted only through lawyers']),
    ('The thank-you message’s underused function is:',
     ['Restating the résumé', 'Repairing one weak answer in two sentences',
      'Requesting salary reconsideration', 'Thanking the receptionist']),
    ('Asking “what are the next steps, and when should I expect to hear?” exists to:',
     ['Signal impatience', 'Give the silence a shape — enabling a polite, finite follow-up cadence',
      'Lock the employer to a deadline', 'Replace the thank-you note']),
    ('The silver-medalist case turns on which message?',
     ['A complaint about the decision', 'The no-ask progress update after visibly closing the named gap',
      'A demand for detailed feedback', 'A LinkedIn endorsement request']),
    ('An interview loop (screen, behavioral, case, wrap-up) is best understood as:',
     ['One interview repeated four times', 'Four different audiences asking four different real questions',
      'A test of stamina', 'Four chances to give identical answers']),
], ['b','b','b','b','b','b','b','b','b','b'])

references(doc, [
    'Bolles, R. N. (2022). What color is your parachute? Ten Speed Press.',
    'Cialdini, R. B. (2021). Influence: The psychology of persuasion (new & expanded ed.). Harper Business.',
    'Huffcutt, A. I. (2011). An empirical review of the employment interview construct literature. '
    'International Journal of Selection and Assessment, 19(1), 62–81.',
    'Janz, T. (1982). Initial comparisons of patterned behavior description interviews versus '
    'unstructured interviews. Journal of Applied Psychology, 67(5), 577–580.',
    'Lazear, E. P., & Gibbs, M. (2014). Personnel economics in practice (3rd ed.). Wiley. (Turnover '
    'and hiring-cost context for the negotiation section.)',
    'Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in '
    'personnel psychology. Psychological Bulletin, 124(2), 262–274. (Why structured, behavioral '
    'formats dominate.)',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch14-study-guide.docx')
finish(doc, os.path.abspath(out))
