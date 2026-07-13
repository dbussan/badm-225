# Chapter 12 — Business Presentations (43 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 12"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Business Presentations",
    "One takeaway · slides as billboards · delivery you can rehearse · nerves you can manage", D)
notes(s, "Chapter 12: the spoken genre. Everything from the writing chapters applies — plus a body, a voice, and a room.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Build", "a talk backward from its one repeatable takeaway — never forward from your slides."),
    ("Open", "with the audience's stakes, roadmap the middle, and close with the ask and the echo."),
    ("Design", "slides as billboards: one point each, takeaway titles, data the back row can read."),
    ("Deliver", "with rehearsed voice and body — and run nerves as fuel instead of freight."),
    ("Handle", "Q&A, hostile questions, cameras, and team handoffs without losing the room."),
], D, nxt())
notes(s, "Objectives map to the Chapter 12 practice bank and the course presentation assignment.")

s = stat_slide(prs, "The talk is the visibility event", "1:100",
    "You'll write a hundred documents for every talk you give — but the talks are where the organization actually watches you think.",
    [("Presentations compress judgment:", "selection, structure, and composure, performed live — the skills of this whole course, visible at once."),
     ("The fear is standard equipment:", "public-speaking anxiety is among the most common fears reported — the pros aren't fearless, they're rehearsed."),
     ("The good news:", "every part of a talk is buildable with technique. Nothing in this chapter requires talent."),
    ], D, nxt())
notes(s, "Framing: high stakes, learnable craft. The fear normalization matters — set it here and return to it in the delivery section.")

s = section_slide(prs, "01", "One takeaway",
    "Build backward from the sentence they'll repeat tomorrow.", D, nxt())
notes(s, "Section 1: purpose and audience for talks — the planning layer.")

s = bullets_slide(prs, "Start with the sentence they'll repeat", [
    ("Write the takeaway first:", "'Renew with TechServe — it saves $23K a year' — one sentence a listener could relay to someone who wasn't there."),
    ("If you can't write it, you're not ready to build slides.", "A talk without a takeaway is a document without a pyramid: material in search of a point."),
    ("Everything auditions against it:", "each slide, story, and number either serves the sentence or leaves the talk (Chapter 2's unity test, standing up)."),
    ("Say it early, prove it in the middle, say it again at the end.", "Audiences remember what's stated, supported, and repeated — not what's implied."),
], D, nxt())
notes(s, "The takeaway-first discipline is the single highest-leverage habit in presenting. It's the pyramid summit, spoken.")

s = bullets_slide(prs, "Audience analysis, standing up", [
    ("What do they already believe about this topic?", "You're moving them FROM somewhere — a talk that ignores the starting point moves no one."),
    ("What can they actually decide?", "Pitch the decision this room owns; asks above or below the room's authority land as noise."),
    ("How much do they know?", "The expert audience resents the basics; the general audience drowns without them — when mixed, layer (Chapter 2)."),
    ("How long is their attention, really?", "The 30-minute slot with phones out is a 10-minute attention budget — build for the real number."),
], D, nxt())
notes(s, "Same audience machinery as Chapter 2, with the live-room additions: authority and attention.")

s = two_col_slide(prs, "Informing and persuading are different builds",
    "The BRIEFING (informing)", [
        "Takeaway = the finding: 'the pilot worked; here's what we learned'",
        "Structure: answer first, then the evidence tour",
        "Success = the audience can explain it afterward",
        "Neutral tone; completeness matters (Chapter 9)",
    ],
    "The PITCH (persuading)", [
        "Takeaway = the ask: 'approve the two-bench rollout'",
        "Structure: AIDA on its feet (Chapter 8)",
        "Success = the audience does something afterward",
        "Objections pre-answered; one calibrated ask",
    ], D, nxt())
notes(s, "Most bad talks are category errors: a pitch built like a briefing (no ask) or a briefing built like a pitch (advocacy where analysis was owed).")

s = flow_slide(prs, "Building the talk, in order", [
    ("TAKEAWAY", "The one repeatable sentence — written first"),
    ("THREE POINTS", "The MECE reasons that carry it (Chapter 9)"),
    ("EVIDENCE", "Per point: a number, a story, or a demonstration"),
    ("OPEN + CLOSE", "Built LAST, once you know what they frame"),
    ("SLIDES", "Built last of all — the talk exists before the deck"),
], D, nxt(), note_text="Slides come LAST. A talk built by opening PowerPoint first becomes a tour of slides — structure by template, not by thought.")
notes(s, "The build order is the anti-pattern-breaker: students who start in the slide tool produce slide-shaped talks.")

s = section_slide(prs, "02", "Openings and closings",
    "The two moments every audience remembers.", D, nxt())
notes(s, "Section 2: the frame. Primacy and recency — audiences retain beginnings and endings disproportionately.")

s = bullets_slide(prs, "Openings that earn the next ten minutes", [
    ("Open with their stakes, not your name.", "'Every week, this lab loses thirty tech-hours to duplicate entry' beats 'Hi, I'm… and today I'll talk about…'"),
    ("Strong openers:", "the striking number, the short story, the question they can't unhear, the before/after — all pointed at the takeaway."),
    ("Never open with an apology", "('I'm not much of a presenter,' 'there wasn't much time') — you're teaching the room how little to expect."),
    ("Memorize the first minute cold.", "It's the nerves' worst window and the audience's judgment window — script it, rehearse it, own it."),
], D, nxt())
notes(s, "The memorized first minute is the practical nerve hack: it carries you through peak adrenaline on autopilot until your footing arrives.")

s = bullets_slide(prs, "The roadmap: tell them where this is going", [
    ("After the hook, the map:", "'I'll show you the problem's cost, the fix we piloted, and the decision I'm asking for.'"),
    ("Three stops, named memorably —", "the roadmap is your pyramid's second layer, read aloud."),
    ("The map is a promise;", "keep it visibly: 'that's the cost — now the fix' lets the audience always know where they are."),
    ("Lost audiences don't re-engage.", "Unlike readers, listeners can't scroll back — signposting isn't style, it's the only navigation they get."),
], D, nxt())
notes(s, "The no-scroll-back point is the deep difference between writing and speaking: redundancy that would be padding on the page is navigation in the air.")

s = bullets_slide(prs, "Closings: the ask and the echo", [
    ("Never end on Q&A —", "take questions, THEN close. The last thing in the room should be your sentence, not a stranger's tangent."),
    ("The close has two beats:", "the echo ('renew with TechServe — $23K a year') and the ask ('I need the committee's decision by the 25th')."),
    ("Make the ask concrete and dated", "(Chapter 6's rule, spoken): 'think it over' converts nobody; 'approve the pilot today' converts the convinced."),
    ("'Thank you' is not a closing.", "It's a signal you ran out of material. Close with the takeaway; the thanks can ride along after."),
], D, nxt())
notes(s, "Questions-then-close is the structural fix most student talks need — it costs nothing and reclaims the recency effect.")

s = bullets_slide(prs, "Transitions carry the structure out loud", [
    ("Between points, land and launch:", "'So the current process costs $67K — that's the problem. Here's the fix we tested.'"),
    ("The mini-summary is the listener's save point:", "every few minutes, one sentence of 'where we've been' rescues everyone who drifted."),
    ("Number the journey:", "'the second of three reasons' does for a talk what headings do for a memo (Chapter 3)."),
    ("Silence is a transition too:", "a two-second pause before a big point is a spotlight; constant talking is fog."),
], D, nxt())
notes(s, "Spoken transitions must be heavier than written ones — the listener has no visual paragraph breaks. The pause-as-spotlight point sets up the voice toolbox.")

s = section_slide(prs, "03", "The body of the talk",
    "Three points, proven three ways.", D, nxt())
notes(s, "Section 3: the middle — selection and evidence.")

s = bullets_slide(prs, "Three points, not eleven", [
    ("Working memory applies to listeners double", "(Miller, 1956) — they can't re-read, so three chunked points is the ceiling, not a style choice."),
    ("Depth beats coverage:", "three points with evidence outperform seven points with adjectives — the dilution effect works on rooms too (Chapter 8)."),
    ("Cut by the takeaway test:", "the fascinating tangent that doesn't serve the sentence goes to the appendix slide — or the parking lot."),
    ("If it must be eleven things,", "it's a document, not a talk. Send the memo; present the three that matter."),
], D, nxt())
notes(s, "The eleven-things line gives students permission to convert overloaded talks back into documents — often the genuinely right call.")

s = bullets_slide(prs, "Evidence variety: number, story, demonstration", [
    ("Numbers convince the analyst:", "one strong figure per point, sourced, rounded for the ear — '$67K a year' lands; '$66,847.13' evaporates."),
    ("Stories convince everyone else:", "ninety seconds, named human, real stakes, pointed at the takeaway — narrative is the brain's native format."),
    ("Demonstrations convince the skeptics:", "the live before/after beats both — with a recorded backup for when the demo gods are angry (see the case)."),
    ("Rotate the three:", "a talk that's all numbers is an actuarial table; all stories, a campfire. Each point gets its best-fit proof."),
], D, nxt())
notes(s, "Ear-rounding numbers is a spoken-genre rule students haven't met: precision that works on the page dies in the air.")

s = bullets_slide(prs, "Business storytelling without the campfire", [
    ("The four-beat skeleton:", "a person, a problem, what they tried, what changed — sixty to ninety seconds, no subplot survives."),
    ("Real and checkable:", "'a lab tech named Priya, on the Tuesday shift' — invented stories are discovered, and the discovery costs everything (Chapter 8's truth test)."),
    ("The story serves the point, announced:", "land it — 'that's what thirty lost hours a week looks like' — or the room enjoys it and misses it."),
    ("One story per talk does real work.", "Three stories is a variety show; the number-story-demo rotation keeps proportion."),
], D, nxt())
notes(s, "The 'announce the point' rule fixes the most common story failure: the anecdote that entertained but never attached to the argument.")

s = section_slide(prs, "04", "Slides",
    "Billboards, not documents — the audience reads or listens, never both.", D, nxt())
notes(s, "Section 4: slide design. The attention economics come first; the rules follow from them.")

s = icon_rows_slide(prs, "The billboard rules", [
    ("1", "One point per slide", "The slide makes the claim; YOU carry the detail. More points = a document leaking into the room."),
    ("👀", "Readable in three seconds", "If the back row must study it, it's competing with you — and the slide always wins."),
    ("🔤", "Big type, few words", "Sentence-fragment bullets, generous space — if it needs 14-point type, it needs fewer words."),
    ("🖼", "Visuals that ARE the point", "The chart, the photo, the diagram — decoration is noise wearing a picture costume."),
    ("⬛", "The empty slide is legal", "Nothing on screen = all eyes on you. Use it for the story and the big ask."),
], D, nxt(), kicker="Audiences read faster than you talk — whatever's on screen, they've finished before you have.")
notes(s, "The read-vs-listen conflict is the physics under every rule. The blank-slide permission genuinely surprises students.")

s = two_col_slide(prs, "The deck and the document are different artifacts",
    "The PRESENTATION deck", [
        "Billboards — one claim, big type, visual proof",
        "Meaningless without the speaker (by design)",
        "Built for the room's attention",
    ],
    "The LEAVE-BEHIND (slide-doc)", [
        "Sections, takeaway titles, full evidence — readable alone",
        "Built for the forward, the absent, the archive (Chapter 9)",
        "Send it AFTER — announce it up front so nobody transcribes",
    ], D, nxt())
notes(s, "'A copy of everything comes to you after this' is the one-sentence fix for the note-taking room — it buys back all the eyes. One deck cannot do both jobs.")

s = bullets_slide(prs, "Takeaway titles, on slides too", [
    ("The title line carries the claim:", "'Pilot cut intake time 38%' — not 'Pilot Results' (Chapter 9's chart-title rule, at 30 points bold)."),
    ("Read the deck by titles only:", "if the title sequence tells the whole story, the deck is built; if it reads 'Background, Data, Discussion' — it isn't."),
    ("Takeaway titles survive the skim:", "the exec who flips your leave-behind in ninety seconds gets the entire argument from titles alone."),
    ("They discipline you, too:", "a slide whose honest title you can't write is a slide that doesn't know its job. Cut it."),
], D, nxt())
notes(s, "The titles-only test is the headings-only test from Chapter 3, ported. Same audit, new artifact.")

s = bullets_slide(prs, "Data on slides: the two-second read", [
    ("One chart, one point, announced in the title", "— the full Chapter 9 canon applies, at projection distance."),
    ("Strip to the point:", "gridlines, legends, and six data series die at the back row — highlight THE line, gray the context."),
    ("Round for the ear, label for the eye:", "say '$67K'; let the slide hold the precise figure for the skeptic."),
    ("Never apologize for a busy slide", "('I know this is hard to read…') — if you know, why is it here? Rebuild it or cut it."),
], D, nxt())
notes(s, "The apology line is the tell of an unrebuilt slide. 'Highlight the one line, gray the rest' is the single most useful data-slide repair.")

s = bullets_slide(prs, "Slide hygiene: the quiet credibility layer", [
    ("One template, consistently:", "same fonts, same colors, same title position — every deviation is a speed bump the audience feels."),
    ("Contrast that survives the projector:", "the elegant gray-on-white that worked on your laptop vanishes under fluorescent light. Test at distance."),
    ("Accessibility is part of the craft:", "high contrast, 24-point floors, color never carrying meaning alone (Chapter 9), alt text on the shared copy."),
    ("Proofread the deck like a document:", "the typo on screen is a typo at billboard scale, with witnesses (Chapter 4)."),
], D, nxt())
notes(s, "Hygiene items are invisible when right and loud when wrong. The projector-contrast warning saves real presentations.")

s = section_slide(prs, "05", "Delivery",
    "Voice and body are instruments — rehearsal is how you tune them.", D, nxt())
notes(s, "Section 5: delivery and nerves. The most feared section and the most technique-rich.")

s = stat_slide(prs, "Everyone's nervous; the rehearsed are nervous AND ready", "3×",
    "Rehearsing a talk aloud three times, in realistic conditions, is the single most reliable anxiety reducer in the speaker's toolkit.",
    [("Nerves are arousal, not verdict:", "the same adrenaline reads as dread or as readiness — preparation is what flips the label."),
     ("Aloud means aloud:", "reading slides silently rehearses nothing — the mouth, the transitions, and the clock only train out loud."),
     ("Realistic means standing,", "projecting, with the clicker and the timer — the conditions you'll actually face."),
    ], D, nxt())
notes(s, "The reframe (arousal, not verdict) is well-supported performance psychology; the three-aloud-passes spec is the actionable floor.")

s = bullets_slide(prs, "Rehearsal that actually works", [
    ("Pass one: find the shape.", "Talk through it rough — discover where the transitions stick and what runs long."),
    ("Pass two: fix and time it.", "Cut to 90% of the slot; Q&A and reality always eat the margin."),
    ("Pass three: simulate.", "Standing, aloud, timed, with one human or a camera — review the recording once, kindly."),
    ("Rehearse transitions hardest:", "openings and slide-to-slide joins are where talks stumble; the middles carry themselves."),
    ("Don't memorize the middle:", "memorize the first minute, the transitions, and the close — the rest stays conversational from bullets."),
], D, nxt())
notes(s, "Selective memorization is the practical answer to 'script or wing it?' — script the load-bearing joints, converse the spans.")

s = icon_rows_slide(prs, "The voice toolbox", [
    ("🐢", "Pace", "Nerves accelerate everyone. Aim slower than natural — what feels sluggish inside sounds composed outside."),
    ("⏸", "The pause", "Two silent seconds after a big point is emphasis; filling every gap with 'um' spends it. Silence is a power tool."),
    ("📶", "Volume & projection", "Speak to the back row's chair. Variation is emphasis; monotone is a lullaby with data."),
    ("🎵", "Pitch & inflection", "Downward inflection ends claims with authority; uptalk turns findings into questions? Don't."),
], D, nxt())
notes(s, "Each tool is practicable in one rehearsal pass. The uptalk line, delivered as written, teaches itself.")

s = bullets_slide(prs, "The body: stance, eyes, hands, feet", [
    ("Plant the stance:", "weight even, shoulders open — the sway and the lean broadcast the nerves you're managing."),
    ("Eye contact in sentences:", "land a full thought on one person, then move — the lighthouse sweep connects with no one."),
    ("Hands above the waist, describing:", "gesture reinforces shape and size naturally; pockets and clasps read as guarded."),
    ("Move with purpose or stand still:", "cross the stage to change topics; pacing is a metronome the audience can't unsee."),
    ("On the slide glance:", "look, turn back, THEN talk — the screen can't hear you, and the room stops trying."),
], D, nxt())
notes(s, "The touch-turn-talk rule fixes the most common physical habit: presenting to the projection wall.")

s = bullets_slide(prs, "Nerves in the moment: the field kit", [
    ("Before: slow exhales, twice as long as the inhale", "— the one physiological lever that actually downshifts arousal on demand."),
    ("The first minute is scripted (see: openings)", "— autopilot carries you through the adrenaline spike."),
    ("Find the three friendly faces", "and open to them; every room has them, and confidence is borrowable."),
    ("When you blank: pause, look at the slide title, breathe.", "The room reads two silent seconds as thoughtfulness — the panic is only visible from inside."),
    ("The audience wants you to succeed.", "Nobody came hoping for a bad talk — the room is on your side until proven otherwise."),
], D, nxt())
notes(s, "The blank-recovery protocol matters most: knowing there's a procedure removes half the fear of needing it.")

s = section_slide(prs, "06", "On camera",
    "The webcam talk and the recorded lecture are their own genre.", D, nxt())
notes(s, "Section 6: virtual and asynchronous presenting — now a permanent professional genre.")

s = bullets_slide(prs, "Presenting on a live video call", [
    ("Lens at eye level, look AT it for key lines", "— the lens is the room's eyes; your notes sit just beneath it (Chapter 1's virtual nonverbals)."),
    ("Energy up 20%:", "the camera flattens everything — conversational-you arrives as flat-you; slightly-too-much arrives as engaged."),
    ("Shorter arcs, more checkpoints:", "attention decays faster on screens — make it 'three five-minute chapters with questions between,' not one twenty-minute pour."),
    ("Run the tech rehearsal:", "screen share, audio, the slide advance — ten minutes early, every time. The fumbling open costs more on camera than in person."),
    ("Have the failure plan:", "deck sent in advance means a dead screen-share becomes 'go to slide 4' instead of dead air."),
], D, nxt())
notes(s, "The +20% energy rule and the pre-sent deck are the two highest-value virtual habits.")

s = bullets_slide(prs, "The recorded (async) presentation", [
    ("Recorded talks get the skip bar —", "front-load harder than live: takeaway in the first thirty seconds, or the viewer is gone."),
    ("Chapter it:", "timestamps or section markers let viewers navigate — the roadmap, made clickable."),
    ("Shorter is a feature:", "the 8-minute focused recording beats the 40-minute meeting capture for every future viewer."),
    ("Pair with text (Chapter 5's rule):", "the recording carries tone; the written summary carries the searchable decisions."),
    ("One clean take beats five perfect ones:", "minor stumbles read as human; re-record only for structural failures."),
], D, nxt())
notes(s, "Async presenting is where this course's delivery-neutral design pays off — students in online sections live in this genre.")

s = section_slide(prs, "07", "Q&A and team talks",
    "The unscripted parts — where credibility is confirmed or refunded.", D, nxt())
notes(s, "Section 7: questions and multi-presenter craft.")

s = bullets_slide(prs, "Q&A craft", [
    ("Repeat or restate the question first:", "the room hears it, the camera records it, and you buy five seconds of thinking."),
    ("Answer the question asked — briefly —", "then stop. The three-minute answer to a ten-second question loses the room you just won."),
    ("'I don't know' with a delivery date beats a bluff:", "'I'll have that number to you Friday' is credible; improvised statistics are time bombs (Chapter 12 meets Chapter 4's verification)."),
    ("Bridge stray questions home:", "'that's really about phase two — for TODAY'S decision, here's what matters' — courteous, and back on the takeaway."),
    ("Plant the seeds:", "prepare for the five questions you'd ask if you wanted to sink this talk. You know what they are."),
], D, nxt())
notes(s, "The five-hostile-questions prep is the pre-mortem from Chapter 8, applied to the podium.")

s = bullets_slide(prs, "The hostile question, handled", [
    ("Depersonalize on arrival:", "answer the substance inside the hostility and skip the bait — the room is watching your temperature, not theirs (Chapter 7)."),
    ("Concede what's true:", "'you're right that the pilot was one team' — then the context: 'which is why the metrics were agreed with finance in advance.'"),
    ("Never argue one-on-one past two exchanges:", "'let's take this offline — I want the detail' returns the room to everyone who owns it."),
    ("The stumped moment:", "acknowledge, commit, deliver — 'good catch; I'll verify and reply to the group by Friday.' Then actually do it (Chapter 11's follow-through)."),
], D, nxt())
notes(s, "The two-exchange rule prevents the duel that hijacks talks. Everything here is composure mechanics from Chapter 7, standing up.")

s = bullets_slide(prs, "Team presentations: one talk, several voices", [
    ("One structure, one designer:", "the talk is built as ONE pyramid, then divided — not stapled from four solo acts (Chapter 10's team-writing rules)."),
    ("Handoffs are rehearsed lines:", "'…and that's the cost case. Maya will show you the pilot that answers it.' Name, topic, momentum — no 'um, I guess now…'"),
    ("Everyone owns Q&A routing:", "the lead routes each question to its expert by name; six people shrugging at each other is the classic team-talk death."),
    ("Match the register:", "agree on formality, pace, and slide style — one deck, one voice, several speakers."),
    ("Idle presenters are still on stage:", "the teammate checking their phone during your section is the slide everyone remembers."),
], D, nxt())
notes(s, "The idle-presenter warning lands hardest — students have all seen it and never audited themselves for it.")

s = bullets_slide(prs, "Case: the demo that died and the talk that didn't", [
    ("Ninety seconds into the live demo,", "the staging server returned errors in front of the client's leadership team."),
    ("The presenter didn't debug on stage.", "One sentence — 'the demo gods have voted; here's the recording from this morning' — and the backup video ran."),
    ("The recording showed the same workflow,", "narrated live; the ask stayed on schedule; the contract closed that month."),
    ("The client's CTO later said the recovery", "sold them harder than the demo would have: 'that's how they'll handle OUR incidents.' Composure is a product feature."),
], D, nxt())
notes(s, "The backup-recording rule from the evidence slide, paying off. The CTO's read is the meta-lesson: audiences evaluate the recovery as a sample of future behavior.")

s = takeaways_slide(prs, [
    "Build backward from one repeatable sentence; slides come last, not first.",
    "Open with their stakes, roadmap the middle, close with the ask AND the echo — after Q&A.",
    "Three points, proven with a rotation of number, story, and demonstration.",
    "Slides are billboards: one point, three-second reads, takeaway titles, blank when you matter more.",
    "Rehearse aloud three times; memorize the first minute, the transitions, and the close.",
    "Q&A: restate, answer briefly, bridge home — and never bluff what you can deliver Friday.",
], D, nxt(), site_note="Practice now: course site → Chapter 12 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The audience will forget your slides by lunch. They will remember one sentence and how you handled the hard moment — so choose the sentence, and rehearse the moment.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Take a talk you've given or seen: what WAS its one repeatable sentence? If you can't state it, diagnose why.",
    "Rebuild a documented bad slide (you've all seen one) into a billboard. What moved to the speaker's notes?",
    "Which delivery habit is your tell under nerves — pace, uptalk, the slide-wall stare? What's the rehearsal fix?",
    "Design the five hostile questions for your own upcoming presentation — and draft the concede-then-context answers.",
    "Live demo or recorded backup: argue the risk math for a career-stakes pitch.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 12 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 12 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Build:", "Your course presentation with this chapter's order: takeaway → three points → evidence → frame → slides."),
    ("Rehearse:", "Three aloud passes, one recorded — review it once, kindly, with the delivery slides open."),
    ("Coming next:", "Unit 5 — Chapter 13: the job search and résumés, where you become the product and the proposal."),
], D, nxt())
notes(s, "Delivery-neutral closing. Unit 4 complete.")

out = os.path.join(os.path.dirname(__file__), "..", "ch12-business-presentations.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
