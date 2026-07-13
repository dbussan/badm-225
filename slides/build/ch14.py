# Chapter 14 — Interviewing and Follow-Up (33 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 14"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Interviewing and Follow-Up",
    "STAR stories · the questions you ask · salary talk · the follow-through that separates finalists", D)
notes(s, "Chapter 14: the interview as a communication genre — preparation, performance, and the paperwork afterward.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Prepare", "a STAR story bank that covers the ten questions you already know are coming."),
    ("Perform", "in every format: phone screen, video, behavioral, panel — with the specifics of each."),
    ("Ask", "questions that signal you're already thinking like someone doing the job."),
    ("Handle", "money: researched ranges, calm anchoring, and negotiating the offer you receive."),
    ("Follow through", "like a professional: the specific thank-you, the patient cadence, the graceful no — and the graceful yes."),
], D, nxt())
notes(s, "Objectives map to the Chapter 14 practice bank.")

s = section_slide(prs, "01", "Before: preparation is the interview",
    "The performance is decided mostly by what happens the week before.", D, nxt())
notes(s, "Section 1: prep — research, stories, logistics.")

s = icon_rows_slide(prs, "Know the format you're walking into", [
    ("📞", "The phone screen", "20–30 minutes, usually HR: verifying basics, salary range, communication skills. Stand up, smile — it's audible."),
    ("🎥", "The video interview", "Live or recorded one-way. All of Chapter 12's camera rules apply, plus the specifics later this deck."),
    ("🧩", "The behavioral interview", "'Tell me about a time…' — past behavior as evidence of future behavior. STAR territory."),
    ("👥", "The panel", "Several interviewers, divided roles. Answer to the asker, sweep the room, get every name for the thank-yous."),
    ("🧪", "The case or working session", "Solve something live. They're watching the HOW: your questions, structure, and composure more than the answer."),
], D, nxt())
notes(s, "Format determines prep. Ask the recruiter what the format is — asking is itself a professional signal.")

s = bullets_slide(prs, "Research them like Chapter 8 taught", [
    ("The company:", "what they sell, who they sell it to, what's changing — recent news, the expansion, the product launch."),
    ("The role:", "the posting reread as a requirements document — their must-haves become your story selection."),
    ("The people:", "your interviewers' backgrounds and paths; 'I saw you moved from the bench to management' opens real conversation."),
    ("The killer output:", "three researched facts you can deploy naturally — research shown beats research claimed (Chapter 13's cold-email lesson)."),
], D, nxt())
notes(s, "Interview research is the same discipline as proposal research: their pain, their language, their world.")

s = flow_slide(prs, "STAR: the answer architecture", [
    ("SITUATION", "Where and when — two sentences of stage-setting, no more"),
    ("TASK", "What YOU were responsible for in it"),
    ("ACTION", "What you specifically did — 'I,' not 'we,' for your parts"),
    ("RESULT", "What changed, with the number if it has one — plus what you learned"),
], D, nxt(), note_text="Ninety seconds to two minutes. The most common failure is a vague, collective middle — 'we sort of handled it' — with no measurable end.")
notes(s, "STAR is the behavioral-interview standard because it forces evidence. The I-vs-we discipline is where team players undersell themselves.")

s = bullets_slide(prs, "Build the story bank before you need it", [
    ("Eight stories cover almost every question:", "a conflict, a failure, a deadline crunch, a leadership moment, a persuasion, a mistake owned, an initiative, a team win."),
    ("Source them from everywhere legitimate:", "jobs, courses, clubs, the capstone — Chapter 13's rule: it doesn't need an office to count."),
    ("Write them out once, bullet them small:", "full prose to find the shape; then index cards (S/T/A/R beats) so they stay conversational, not recited."),
    ("Map stories to THIS employer's needs:", "the posting's top three requirements each get a designated story — that's the tailoring step."),
], D, nxt())
notes(s, "The story bank converts interview prep from cramming into rehearsal. Eight stories, honestly built, cover a hundred question phrasings.")

s = bullets_slide(prs, "Logistics: the unforced errors", [
    ("The dry run:", "route, parking, or platform link tested the day before — arriving flustered spends your composure budget before hello."),
    ("Dress one notch above the role's daily norm;", "when unsure, ask the recruiter — 'what's the dress expectation?' is a normal question."),
    ("Bring the kit:", "printed résumés, your questions written down, names of interviewers, a pen that works, water."),
    ("Arrive ten minutes early — not thirty:", "early enough to breathe, not so early you're a lobby management problem."),
    ("The interview starts in the parking lot:", "the receptionist's impression gets asked for more often than candidates ever learn."),
], D, nxt())
notes(s, "The receptionist line is true and memorable — many hiring managers explicitly ask front desk staff about candidate behavior.")

s = section_slide(prs, "02", "During: the performance",
    "Composure, evidence, and the questions that flow both ways.", D, nxt())
notes(s, "Section 2: the interview itself.")

s = bullets_slide(prs, "The first five minutes", [
    ("The greeting is a rehearsable skill (Chapter 11):", "name, eye contact, firm-normal handshake, and the small talk played straight — it's the warm-up they're grading too."),
    ("'Tell me about yourself' is not an invitation to biography:", "it's your summary line (Chapter 13), expanded to sixty seconds: what you are, your evidence, why you're HERE."),
    ("Present-past-future is the clean shape:", "'I'm a finance grad with audit internships (present); I built X at Y (past); this role is exactly the next step (future).'"),
    ("Rehearse it like the talk's first minute (Chapter 12):", "scripted, owned, delivered through the adrenaline window."),
], D, nxt())
notes(s, "'Tell me about yourself' opens nearly every interview and is the most preparable moment in it. Present-past-future prevents the childhood-onward ramble.")

s = bullets_slide(prs, "The classics, and what they're actually asking", [
    ("'Why do you want to work here?'", "= 'did you research us?' Answer with their specifics: the product, the expansion, the fit."),
    ("'What's your greatest weakness?'", "= 'are you self-aware and improving?' A real (non-fatal) weakness + the visible fix: 'I over-prepared presentations; I've moved to timed rehearsal passes.'"),
    ("'Why are you leaving?' / 'the gap?'", "= 'is there a red flag?' One honest, forward-facing sentence — never a grievance tour (Chapter 7's tone rules)."),
    ("'Where do you see yourself in five years?'", "= 'is this role a fit or a layover?' Ambition aligned with the role's actual path."),
], D, nxt())
notes(s, "Decoding the question behind the question converts each classic from a trap into a prompt. The weakness answer spec — real, non-fatal, actively fixed — is the one they'll quote back.")

s = bullets_slide(prs, "Behavioral vs. situational: the pivot", [
    ("Behavioral asks about the past:", "'tell me about a time you missed a deadline' → deploy the story bank, STAR shape."),
    ("Situational asks hypotheticals:", "'what would you do if a client demanded a refund policy exception?' → answer the principle, THEN ground it: 'here's how that actually played out when…'"),
    ("The grounding pivot is the power move:", "a hypothetical answered with real evidence outranks a hypothetical answered with hypothetical virtue."),
    ("No story fits? Say how you'd think:", "name the factors you'd weigh (Chapter 9's criteria-first) — structured thinking IS the answer they're scoring."),
], D, nxt())
notes(s, "The pivot from hypothetical to evidence is the single best interview technique nobody teaches undergraduates.")

s = bullets_slide(prs, "Your questions are half the interview", [
    ("Prepared, written down, and specific to them:", "'What does success in this role look like at ninety days?' signals you're already thinking inside the job."),
    ("Ask about the work, the team, the path:", "'What separates the good hires from the great ones here?' — interviewers love answering this, and the answer is gold."),
    ("Never open with salary, vacation, or remote days:", "logistics questions before fit questions reframe you as a buyer of perks, not a solver of problems."),
    ("'No questions' reads as no interest.", "Always three ready; two will usually survive the conversation."),
], D, nxt())
notes(s, "The questions segment is scored as heavily as the answers — it's the interview's sample of the candidate's curiosity and preparation.")

s = two_col_slide(prs, "Video interviews: live and one-way",
    "Live video", [
        "Chapter 12's camera rules: lens at eye level, light in front, energy +20%",
        "Notes are legal — brief, near the lens, glanced not read",
        "Tech-check thirty minutes early; have the phone-number fallback",
        "Pause for the lag: half a beat after they finish prevents the talk-over",
    ],
    "One-way (recorded) screens", [
        "It's a teleprompter test — treat each prompt as a STAR from the bank",
        "Use the prep time; if retakes are allowed, one retake max (Chapter 12)",
        "Look at the LENS, not your own preview tile",
        "Same energy as live — the recording flattens harder than the call",
    ], D, nxt())
notes(s, "One-way screens are now common at volume employers and students find them alien — naming the genre and its rules removes most of the dread.")

s = bullets_slide(prs, "The question that shouldn't have been asked", [
    ("Some questions touch protected ground:", "age, family plans, religion, origin — usually clumsiness, occasionally worse."),
    ("The composed move: answer the legitimate concern underneath", "— 'if you're asking about availability, my schedule fully covers the role's hours' (Chapter 7's de-escalation, seated)."),
    ("You may decline gracefully:", "'I'd rather keep the focus on the role — and I'm confident nothing in my situation affects it.'"),
    ("And you may note it:", "how an organization interviews is data about how it manages. You're evaluating them too — that's not a slogan, it's the actual structure of the meeting."),
], D, nxt())
notes(s, "The concern-beneath-the-question technique keeps the candidate in control without a confrontation they didn't choose. The 'you're evaluating them' close resets the power frame honestly.")

s = section_slide(prs, "03", "Money",
    "Researched, calm, and later than they'd like.", D, nxt())
notes(s, "Section 3: salary — the conversation students fear most and prepare for least.")

s = bullets_slide(prs, "Salary talk: research before the range", [
    ("Know the market number before any interview:", "salary sites, posted ranges (required in more states every year), and what the informationals told you."),
    ("When asked early, give the researched range:", "'From what I've seen for this role in this region, $58–65K — and I'm flexible for the right fit.' Calm, sourced, unapologetic."),
    ("A range anchors without cornering (Chapter 8):", "the bottom of your range should be a number you'd actually accept."),
    ("Deflecting is also legal:", "'I'd like to understand the full role first — what's the budgeted range?' Asking THEIR range first is fair play, and increasingly just answered."),
], D, nxt())
notes(s, "Pay transparency laws have changed this conversation — many postings now carry ranges. The researched-range script removes the panic from the early question.")

s = bullets_slide(prs, "Negotiating the offer you receive", [
    ("An offer is the START of a conversation,", "and negotiating it — professionally — is expected: 'I'm excited about this role. Given the audit experience I'd bring, is there flexibility toward $63K?'"),
    ("Negotiate ONCE, with a reason attached:", "the evidence-based single ask (Chapter 8's calibrated ask) — serial nibbling burns the goodwill you're about to live on."),
    ("The package is wider than the salary:", "start date, signing bonus, development budget, remote days — when the number is fixed, the terms often aren't."),
    ("Get the final version in writing before resigning anything", "(Chapter 6's confirmation rule, at maximum personal stakes)."),
], D, nxt())
notes(s, "'Negotiate once, with a reason' is the professional pattern: employers report respecting the single evidence-backed ask and resenting the nibble sequence.")

s = section_slide(prs, "04", "After: the follow-through",
    "Where finalists separate — mostly by doing what they said.", D, nxt())
notes(s, "Section 4: everything after the handshake — the genre work that Chapter 6 trained.")

s = bullets_slide(prs, "The thank-you that does work", [
    ("Within 24 hours, to each interviewer, individually", "— pull the names from the panel; the identical CC'd blast undoes the gesture."),
    ("Reference a specific moment:", "'your point about the supplier audit backlog' — specificity proves presence (the five-S rules, Chapter 6)."),
    ("Do one useful thing:", "reinforce your strongest fit, or repair a stumble: 'I gave a thin answer on LIMS — here's the fuller picture in two sentences.'"),
    ("Email is the norm;", "a mailed note on top is the costly signal for the roles that merit it (Chapter 6's ink rule)."),
], D, nxt())
notes(s, "The repair function is underused: the thank-you is a legitimate second chance at one flubbed answer.")

s = bullets_slide(prs, "The wait: a cadence, not a vigil", [
    ("Ask the timeline in the room:", "'What are the next steps, and when should I expect to hear?' — now the silence has a shape."),
    ("Deadline passes → one polite nudge:", "'Following up on the analyst role — I remain very interested. Any update on timing?' Two lines. That's the whole genre."),
    ("Silence after two follow-ups is an answer;", "keep the pipeline moving (Chapter 13's tracker) — the search isn't over until the start date."),
    ("Other offer in hand? Say so, straight:", "'I've received another offer with a Friday deadline — is a decision on your side possible this week?' It accelerates real interest and reveals the rest."),
], D, nxt())
notes(s, "The competing-offer script is honest leverage — recruiters confirm it works exactly when the interest was real, which is the information the candidate needs anyway.")

s = bullets_slide(prs, "Rejection, offer, and the graceful exit", [
    ("Rejected: reply anyway (almost no one does).", "'Thank you for the process — I'd welcome consideration for future analyst openings.' Recruiters keep files; graciousness gets filed too (Chapter 7)."),
    ("Offered: evaluate before celebrating —", "role, manager, path, package, and what the interviews revealed about how the place actually runs."),
    ("Declining an offer: prompt, warm, and final:", "'I've accepted a role elsewhere that fits my path — thank you, sincerely.' Burned bridges are all toll bridges eventually."),
    ("Resigning the old job: two weeks written notice,", "gratitude regardless of the tenure's truth, full effort through the last hour — the exit is the reference (Chapter 11)."),
], D, nxt())
notes(s, "Every path out of the process is a relationship event: the reply-to-rejection habit alone has restarted careers.")

s = bullets_slide(prs, "Case: the silver medalist", [
    ("She finished second for the analyst role.", "Her rejection reply thanked the panel and asked one question: 'what would have made the difference?'"),
    ("The recruiter answered honestly (supplier-audit depth),", "and she spent two months closing exactly that gap — then sent the two-line update: 'took your feedback; here's what I did with it.'"),
    ("When the winner left in month five,", "there was no new posting. There was a phone call."),
    ("The lesson:", "processes end; impressions don't. The follow-through WAS the qualification — the second interview was just paperwork."),
], D, nxt())
notes(s, "Composite of a pattern every recruiter recognizes: silver medalists who handle the loss well are the first call at the next opening.")

s = bullets_slide(prs, "The panel, played well", [
    ("Get every name at the start", "— write them in seat order; you'll need them for eye contact now and thank-yous tonight."),
    ("Answer to the asker, then sweep:", "open on the questioner, distribute the middle to the room, land back on the asker (Chapter 12's eye-contact-in-sentences)."),
    ("Read the roles:", "the technical panelist wants depth, HR wants consistency, the manager wants fit — one answer can nod to each."),
    ("The quiet panelist matters most:", "they're often the veto. Bring them in with your eyes even when they never speak."),
], D, nxt())
notes(s, "Panel mechanics in four habits. The seat-order name trick is small and solves the most common panel embarrassment.")

s = bullets_slide(prs, "The case or working session, played well", [
    ("Ask clarifying questions FIRST", "— the point of the exercise is watching you scope a problem; diving in unquestioning is the classic fail."),
    ("Think aloud, structured:", "'I'd weigh three factors…' — they're scoring the reasoning, not the trivia (Chapter 9's criteria-first, performed)."),
    ("Wrong turn? Correct visibly:", "'actually, that assumption breaks here — let me adjust' demonstrates exactly the self-monitoring they're hiring."),
    ("Land on a recommendation:", "even under uncertainty, close with 'given all that, I'd do X first' — the verdict habit (Chapter 10) is what separates analysts from narrators."),
], D, nxt())
notes(s, "The working session is the interview format most like the actual job — which is why 'perform the reasoning' is the whole instruction.")

s = bullets_slide(prs, "Reading the room mid-interview", [
    ("Watch for the drift (Chapter 1's nonverbals):", "checked watches and flat follow-ups mean wrap the answer — the two-minute STAR has a ninety-second version."),
    ("Leaning in means go deeper:", "'want the detail on how we caught it?' offers depth without imposing it."),
    ("Match their register:", "a formal panel gets formal; a conversational manager gets conversational — mirroring the room is fit, demonstrated live."),
    ("Silence after your answer isn't failure:", "interviewers take notes. Let it sit (Chapter 12's pause) — filling it with backpedaling converts a good answer into a nervous one."),
], D, nxt())
notes(s, "Mid-interview calibration — the live-audience version of audience analysis. The backpedal warning fixes a real and common self-inflicted wound.")

s = bullets_slide(prs, "The internal interview: same rules, higher familiarity tax", [
    ("Prepare MORE, not less:", "interviewing where you work invites coasting — and the panel notices coasting fastest in the candidate they already know."),
    ("Re-introduce yourself formally:", "assume the panel knows nothing; your daily visibility is not a STAR bank — evidence still has to be presented."),
    ("Handle the awkward openly:", "your current manager, the colleagues who also applied — 'I've told my team I'm pursuing this' beats being discovered pursuing it (Chapter 7)."),
    ("If you lose, run the silver-medalist play", "inside the building: the feedback ask, the visible gap-closing, the next opening. It works even better internally."),
], D, nxt())
notes(s, "Internal candidacy is common early-career and never taught. The overprepare instruction is the whole slide in two words.")

s = takeaways_slide(prs, [
    "Eight STAR stories, written and rehearsed, cover nearly every behavioral question — build the bank first.",
    "Decode the question behind the classics; ground every hypothetical in real evidence.",
    "Your prepared questions are half the score: ask about success, the team, the path — never perks first.",
    "Money: researched range, delivered calmly, negotiated once with a reason — and confirmed in writing.",
    "The thank-you is specific, individual, and useful within 24 hours; the follow-up cadence is polite and finite.",
    "Every exit — rejection, decline, resignation — is a relationship event. Handle it like the reference it becomes.",
], D, nxt(), site_note="Practice now: course site → Chapter 14 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The interview is an audit of your résumé, a sample of your communication, and a preview of your follow-through. You can rehearse all three — so rehearse all three.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame. Unit 5 complete.")

s = discussion_slide(prs, "Discussion questions", [
    "Draft your eight-story STAR bank as headlines. Which posting requirement has no story — and what's your plan for it?",
    "Script your sixty-second 'tell me about yourself' in present-past-future. Read it aloud; cut what you stumbled on.",
    "Role-play the early salary question with a partner: range, deflection, and the follow-up. Which felt strongest?",
    "You bombed one answer in an otherwise strong interview. Draft the thank-you that repairs it without groveling.",
    "Argue it: is the one-way video interview a fair screen or a dignity tax? What would you change about the genre?",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 14 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 14 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Build:", "Your STAR bank — eight stories, indexed to the classic questions, rehearsed aloud once."),
    ("Rehearse:", "A mock interview with a classmate or the campus career center; review it with Chapter 12's delivery checklist."),
    ("Coming next:", "Unit 6 — Chapter 15: AI, agents, and professional communication — the tools that draft, and the judgment that ships."),
], D, nxt())
notes(s, "Delivery-neutral closing. Unit 5 complete.")

out = os.path.join(os.path.dirname(__file__), "..", "ch14-interviewing-and-follow-up.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
