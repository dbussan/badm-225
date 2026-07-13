# Chapter 12 study guide — Business Presentations (28+ pages, original)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from guidelib import *

FIG = os.path.join(os.path.dirname(__file__), 'fig')
doc = new_doc(12, 'Business Presentations',
    'One takeaway · slides as billboards · delivery you can rehearse · nerves you can manage')

h1(doc, 'Why this chapter exists')
para(doc, 'You will write perhaps a hundred documents for every presentation you give — and the presentations '
    'will shape your reputation out of all proportion to that ratio. A talk is the one professional moment when '
    'the organization watches you think in real time: selecting what matters, structuring it under a clock, '
    'holding composure when the projector dies or the third question has teeth. Every skill this course has '
    'built — the pyramid, the audience analysis, the revision discipline, the persuasive machinery — performs '
    'in public here, compressed into twenty minutes with your name on the door.')
para(doc, 'Two beliefs sabotage most student presenters, and this chapter is engineered against both. The first '
    'is that presenting is a talent — some people “are” good speakers — when every component of a talk is '
    'buildable with technique: the structure is Chapter 9’s pyramid spoken aloud, the slides follow rules you '
    'can check, and delivery responds to rehearsal the way any physical skill does. The second is that the fear '
    'is disqualifying. Public-speaking anxiety is among the most commonly reported fears in survey after survey; '
    'the professionals you admire are not unafraid — they are rehearsed, and rehearsal is available to you at '
    'the same price they paid.')
para(doc, 'The chapter runs the full arc: building the talk (backward, from one sentence), framing it (openings, '
    'roadmaps, closings), proving it (numbers, stories, demonstrations), showing it (slides as billboards), '
    'delivering it (voice, body, nerves), and surviving its unscripted parts (Q&A, hostile questions, dead '
    'demos, team handoffs). Two extended cases and a complete worked example close it out.')

h1(doc, 'Build backward from one sentence')
figure(doc, os.path.join(FIG, 'ch12_buildorder.png'),
    'Figure 1. The build order — takeaway first, slides last.',
    'A five-step flow: takeaway (the one repeatable sentence, written first), three points (the MECE reasons), evidence '
    '(number, story, demonstration), open and close (built once you know what they frame), and slides last — with a note '
    'that a talk built by opening the slide tool first becomes a tour of slides.')
para(doc, 'Before anything else, write the sentence a listener could repeat tomorrow to someone who wasn’t '
    'there: “Renew with TechServe — it saves $23K a year.” “The pilot worked; roll it out to both benches.” '
    '“Our response times are the reason we’re losing renewals, and the fix costs less than one lost account.” '
    'That sentence is the pyramid summit from Chapter 9, spoken. If you cannot write it, you are not ready to '
    'build slides — you have material in search of a point, and twenty minutes of someone else’s attention is '
    'a rude place to go searching.', bold_lead='The takeaway first.')
para(doc, 'Everything in the talk then auditions against the sentence. Each candidate slide, story, statistic, '
    'and tangent either serves it or leaves — the unity test from Chapter 2, applied at podium stakes. This '
    'audition is where good talks are actually made, because the discipline of cutting fascinating-but-off-point '
    'material is what separates a briefing from a tour of everything the presenter knows. Say the takeaway '
    'early, prove it in the middle, and say it again at the end: audiences remember what is stated, supported, '
    'and repeated — not what is implied.')
para(doc, 'Slides come last in the build order for a structural reason: the slide tool imposes its own '
    'sequence — title layout, bullet layout, next slide — and a talk born inside it becomes slide-shaped: '
    'structure by template rather than by thought. Build the argument first, in an outline or on index cards; '
    'the deck is then a set of visual aids for a talk that already exists, which is the only thing a deck '
    'should ever be.', bold_lead='Why slides come last.')

h2(doc, 'Audience analysis, standing up')
para(doc, 'Chapter 2’s machinery transfers whole, with three live-room additions. First, authority: pitch the '
    'decision this room can actually make. An ask above the room’s authority is a rehearsal nobody needed; an '
    'ask below it wastes the assembled seniority. Second, starting position: you are moving the audience FROM '
    'somewhere — what do they currently believe about this topic, and who in the room is invested in the '
    'current answer? A talk that ignores the starting point moves no one, however elegant. Third, attention: '
    'the thirty-minute slot with phones on the table is a ten-minute attention budget wearing a longer '
    'calendar hold. Build for the real number: your strongest material in the first third, and structural '
    'landmarks (the roadmap, the mini-summaries) that let drifting attention re-board.')
para(doc, 'Distinguish, too, which of two genres you are performing. The briefing informs: its takeaway is a '
    'finding, its structure is answer-first evidence, and its success test is whether the audience can explain '
    'the matter afterward. The pitch persuades: its takeaway is an ask, its structure is Chapter 8’s AIDA on '
    'its feet, and its success test is whether the audience does something. Most bad talks are category '
    'errors — a pitch built like a briefing (all context, no ask) or a briefing built like a pitch (advocacy '
    'where analysis was owed, which Chapter 9 taught you to treat as a completeness violation).')

h1(doc, 'The frame: openings, roadmaps, closings')
figure(doc, os.path.join(FIG, 'ch12_frame.png'),
    'Figure 2. The frame of a talk — hook, roadmap, body, Q&A, then the close.',
    'Five rows: the hook (their stakes in sentence one, never an apology), the roadmap (three named stops), the body '
    '(three proven points), Q&A taken before the close, and the close (the echo plus the ask — thank you is not a closing).')
para(doc, 'Audiences disproportionately retain beginnings and endings — the primacy and recency effects that '
    'Chapter 3 exploited on the page operate even more strongly in the air, because listeners cannot scroll '
    'back. The frame is therefore where preparation concentrates: the first minute and the last are the two '
    'stretches every competent presenter scripts word for word.')
para(doc, 'Open with the audience’s stakes, not your own credentials: “Every week, this lab loses thirty '
    'tech-hours to duplicate entry” beats “Hi, I’m… and today I’d like to talk about workflow optimization” '
    'by the full distance between attention and patience. The working openers are a short list: the striking '
    'number, the sixty-second story, the question the room can’t unhear, the before-and-after. All of them '
    'point at the takeaway. And one anti-rule outranks the rest: never open with an apology — for your nerves, '
    'your slides, or your preparation time. An apologetic opening teaches the room exactly how little to '
    'expect, and rooms are obedient students.', bold_lead='The hook.')
para(doc, 'After the hook, the map: “I’ll show you what the problem costs, the fix we piloted, and the '
    'decision I’m asking for.” Three stops, named memorably — the pyramid’s second layer read aloud. The '
    'roadmap is a promise, and keeping it visibly (“that’s the cost; now the fix”) is the navigation system '
    'listeners otherwise lack. On the page, a lost reader re-reads; in a talk, a lost listener is simply '
    'gone, politely nodding, until something signals where they are. Signposting is not style. It is the '
    'only scroll bar the audience gets.', bold_lead='The roadmap.')
para(doc, 'Between points, land and launch: “So the current process costs $67K a year — that’s the problem. '
    'Here’s the fix we tested.” The landing sentence is a save point for everyone who drifted; the launch '
    'sentence is the next chapter’s title, spoken. Number the journey (“the second of three reasons”), and '
    'let silence transition too: a two-second pause before a big point is a spotlight, and a room that has '
    'been listening to continuous talking will look up at the quiet.', bold_lead='Transitions.')
para(doc, 'Take questions BEFORE the close, never after. A talk that ends on Q&A ends on a stranger’s '
    'tangent — or worse, on the hostile question’s echo. Answer the last question, then close: the echo '
    '(“renew with TechServe — $23K a year”) and the ask (“I need the committee’s decision by the 25th”). '
    'The ask is concrete and dated, exactly as Chapter 6 taught for written requests; “think it over” '
    'converts nobody, while “approve the pilot today” converts everyone who was already persuaded and '
    'flushes out the objections of everyone who wasn’t. And “thank you” is not a closing — it is a signal '
    'that you ran out of material one sentence too early. Close with the takeaway; gratitude can ride along '
    'behind it.', bold_lead='The close.')

h1(doc, 'The body: three points, proven three ways')
para(doc, 'Miller’s working-memory constraint (Chapter 3) applies to listeners at double strength: they '
    'cannot re-read, so three chunked points is a ceiling, not a style preference. Depth beats coverage — '
    'three points with real evidence outperform seven points with adjectives, because the dilution effect '
    '(Chapter 8) works on rooms exactly as it works on readers: audiences average your arguments rather than '
    'summing them. When the material genuinely is eleven things, you are holding a document, not a talk. '
    'Send the memo; present the three things that matter; put the rest in the leave-behind.')
para(doc, 'Each point then gets its best-fit proof, and the strongest talks rotate three kinds. Numbers '
    'convince the analysts: one strong figure per point, sourced, and rounded for the ear — “$67K a year” '
    'lands; “$66,847.13” evaporates somewhere over the third row. (Precision that works on the page dies in '
    'the air; the exact figure lives on the slide or in the leave-behind for the skeptic who wants it.) '
    'Stories convince everyone else: sixty to ninety seconds, a named human, real stakes, no subplot — and '
    'the point announced when it lands: “that’s what thirty lost hours a week looks like.” A story that '
    'entertains without attaching to the argument is a pleasant hole in your time budget. Demonstrations '
    'convince the skeptics: the live before-and-after beats both other proofs when it works — and it '
    'requires the backup recording for when it doesn’t, a rule the first case study will price for you.')
para(doc, 'Business storytelling deserves its own caution: the story must be true and checkable. “A lab '
    'tech named Priya, on the Tuesday shift” is evidence; an invented composite presented as fact is a '
    'time bomb with your name on it, because someone eventually asks Priya. Chapter 8’s truth test governs '
    'the podium as it governs the page — and one story per talk, doing real argumentative work, is the '
    'right dose. Three stories is a variety show.')

h1(doc, 'Slides: billboards, not documents')
figure(doc, os.path.join(FIG, 'ch12_billboard.png'),
    'Figure 3. Billboard or document — the presentation deck and the leave-behind are different artifacts.',
    'Two panels: the presentation deck (one point per slide, readable in three seconds, big type, meaningless without the '
    'speaker by design) versus the leave-behind (sections, takeaway titles, full evidence, readable alone, sent after), '
    'with the tip to announce the leave-behind up front.')
para(doc, 'One fact of attention physics generates every slide rule: the audience reads faster than you '
    'talk, and it cannot read and listen at once. Whatever is on the screen, the room has finished it '
    'before you have — and while they read, you are background audio. The choice is therefore structural: '
    'either the slide is a billboard (one point, three-second read, then eyes back on you) or the slide is '
    'the show and you are its narrator. The billboard rules follow directly.')
bullets(doc, [
    ('One point per slide.', 'The slide makes the claim; you carry the detail. A slide making four points '
     'is a document leaking into the room.'),
    ('Readable in three seconds, from the back row.', 'If it must be studied, it competes with you — and '
     'the slide always wins.'),
    ('Big type, few words.', 'Sentence-fragment bullets, generous space. If the content needs 14-point '
     'type to fit, the slide needs fewer words, not smaller type.'),
    ('Visuals that ARE the point.', 'The chart, the photo, the diagram — decoration is noise wearing a '
     'picture costume, and stock-photo handshakes fool no one.'),
    ('The empty slide is legal.', 'Blank the screen (most presenter tools map it to the B key) for the '
     'story and the big ask: nothing on screen means every eye on you, which is sometimes exactly the design.'),
])
para(doc, 'The deck you present and the document you send afterward are different artifacts, and one deck '
    'cannot do both jobs. The presentation deck is billboards — deliberately meaningless without you. The '
    'leave-behind (the slide-doc) carries sections, takeaway titles, and the full evidence, readable '
    'alone by the absent, the forwarded-to, and the archive. Build both when stakes justify it, and announce '
    'the leave-behind in your first minute: “a full copy comes to you after this.” That one sentence buys '
    'back every eye that would otherwise spend your talk transcribing it.', bold_lead='The two artifacts.')
para(doc, 'Slide titles carry takeaways, exactly as chart titles did in Chapter 9: “Pilot cut intake time '
    '38%” — never “Pilot Results.” Run the titles-only test before you rehearse: read the deck by its title '
    'lines alone. If the sequence tells the whole story, the deck is built; if it reads “Background, '
    'Approach, Data, Discussion,” you have section labels where claims should be. Takeaway titles also '
    'survive the skim: the executive who flips your leave-behind in ninety seconds gets the entire argument '
    'from titles — which, for that reader, IS the presentation.', bold_lead='Takeaway titles.')
para(doc, 'Data slides obey Chapter 9’s full canon at projection distance: one chart, one point, announced '
    'in the title, axes honest. Then strip for the back row — gridlines lightened, legends replaced by '
    'direct labels, and of six data series, THE line highlighted while the rest gray into context. Say the '
    'round number; let the slide hold the precise one. And never apologize for a busy slide: “I know this '
    'is hard to read” is a confession that you knew and showed it anyway. Rebuild it or cut it.',
    bold_lead='Data slides.')
para(doc, 'Last, hygiene — invisible when right, loud when wrong. One template throughout: same fonts, '
    'colors, and title positions, because every deviation is a speed bump the audience feels without '
    'naming. Contrast tested at distance under real light: the elegant pale gray that worked on your laptop '
    'vanishes under conference-room fluorescents. Accessibility as part of craft: 24-point body floors, '
    'color never carrying meaning alone, alt text in the shared copy. And the deck proofread like a '
    'document (Chapter 4), because a typo at billboard scale has witnesses.', bold_lead='Slide hygiene.')

h1(doc, 'Delivery: instruments you can tune')
para(doc, 'Delivery intimidates because it feels like personality — but it decomposes into voice, body, and '
    'nerves, and each responds to specific technique. Start with the finding that reframes everything: '
    'stage fright is arousal, not verdict. The racing pulse and cold hands are the same physiology as '
    'readiness; preparation is what flips the label your brain applies. Performance psychology has '
    'demonstrated the reframe repeatedly — speakers who relabel “I’m anxious” as “I’m ready” perform '
    'measurably better with identical adrenaline. You do not need less arousal. You need more rehearsal '
    'and a better label.')
h2(doc, 'Rehearsal that actually works')
figure(doc, os.path.join(FIG, 'ch12_rehearsal.png'),
    'Figure 4. Three rehearsal passes, all aloud — shape, time, simulate — memorizing only the joints.',
    'Three boxes: pass one finds the shape, pass two times the talk to ninety percent of the slot, pass three simulates '
    'standing and recorded, with a note to memorize only the first minute, the transitions, and the close.')
para(doc, 'Three aloud passes are the reliable minimum, and “aloud” is the load-bearing word: reading slides '
    'silently rehearses nothing — the mouth, the transitions, and the clock only train out loud. Pass one '
    'finds the shape: talk it through rough, discover where the joins stick and what runs long. Pass two '
    'fixes and times: cut to ninety percent of the slot, because Q&A and reality always eat the margin — '
    'the talk that fits exactly in rehearsal runs over in the room, and running over is stealing (from the '
    'next presenter, from the room’s calendar, from your own close). Pass three simulates: standing, '
    'projecting, with the clicker and a timer, ideally recorded on a phone — then review the recording '
    'once, kindly, with the delivery checklist beside you.')
para(doc, 'Memorize selectively. Full-script memorization produces recitation and catastrophic failure '
    'modes (one lost sentence strands you); pure improvisation wastes the frame. The professional pattern '
    'scripts the joints — the first minute (which carries you through peak adrenaline on autopilot), the '
    'transitions (where talks actually stumble), and the close (which must land verbatim) — and leaves the '
    'middles conversational, delivered from bullet-level notes. Joints scripted, spans conversational: it '
    'is the same division of rigidity and flexibility that makes bridges work.')
h2(doc, 'The voice')
figure(doc, os.path.join(FIG, 'ch12_voice.png'),
    'Figure 5. The voice toolbox — pace, pause, volume, inflection.',
    'Four rows: pace (aim slower than natural), the pause (two silent seconds as a spotlight), volume (speak to the back '
    'row, variation is emphasis), and inflection (downward endings state; uptalk turns findings into questions).')
para(doc, 'Nerves accelerate everyone, so aim slower than feels natural — what registers as sluggish from '
    'inside sounds composed from the fifth row. The pause is the most underused tool in the kit: two silent '
    'seconds after a big point function as a spotlight, while the same gap filled with “um” spends the '
    'emphasis on nothing. (Filler words are not a moral failure; they are what the mouth does while the '
    'brain loads. The pause is simply choosing to load in silence, and one rehearsal pass focused on it '
    'moves most speakers dramatically.) Project to the back row’s chair, and vary — volume variation is '
    'emphasis, monotone is a lullaby with data in it. And watch inflection: downward endings state claims '
    'with authority; uptalk turns findings into questions and confidence into a request for permission.')
h2(doc, 'The body')
para(doc, 'Plant the stance — weight even, shoulders open — because the sway and the lean broadcast exactly '
    'the nerves you are managing. Make eye contact in sentences: land one complete thought on one person, '
    'then move to another; the lighthouse sweep that “covers” the room connects with nobody. Keep hands '
    'above the waist, describing — gesture reinforces shape and size naturally when you let it; pockets '
    'and clasped hands read as guarded. Move with purpose or stand still: crossing the stage to mark a '
    'topic change is punctuation; pacing is a metronome the audience cannot unsee. And on every slide '
    'glance, run touch-turn-talk: look at the screen, turn back to the room, THEN speak. The screen '
    'cannot hear you, and a room addressed via projection wall stops trying to.')
h2(doc, 'The nerves field kit')
para(doc, 'For the hour before: slow exhales, twice as long as the inhale — the one physiological lever '
    'that reliably downshifts arousal on demand. For the first minute: the script (see rehearsal) carries '
    'you through the adrenaline spike on autopilot. For the room: find the three friendly faces — every '
    'room has them — and open to them; confidence is borrowable. For the blank moment, have the protocol '
    'BEFORE you need it: pause, look at the slide title, breathe, resume. The room reads two silent '
    'seconds as thoughtfulness; the panic is only visible from inside. And hold the base truth: the '
    'audience wants you to succeed. Nobody came hoping for a bad talk. The room is on your side until '
    'proven otherwise, and it almost never has to be proven otherwise.')

h1(doc, 'On camera: live calls and recorded talks')
para(doc, 'The webcam presentation is now a permanent professional genre with its own physics. Live on '
    'camera: lens at eye level and LOOK at it for key lines — the lens is the room’s eyes, and notes taped '
    'just beneath it keep your gaze honest (Chapter 1’s virtual nonverbals). Energy up roughly twenty '
    'percent: the camera flattens affect, so conversational-you arrives as flat-you, and slightly-too-much '
    'arrives as engaged. Shorter arcs with more checkpoints: screen attention decays faster than room '
    'attention, so structure twenty minutes as three chapters with questions between rather than one pour. '
    'Run the tech rehearsal ten minutes early — screen share, audio, slide advance — because the fumbling '
    'open costs more on camera than in person. And pre-send the deck: a dead screen-share then becomes '
    '“go to slide four” instead of dead air. The failure plan is part of the presentation.')
para(doc, 'The recorded (asynchronous) presentation inverts several live rules. Viewers hold a skip bar, so '
    'front-load harder than you would live: takeaway inside the first thirty seconds or the viewer is gone. '
    'Chapter the recording — timestamps or section markers make the roadmap clickable. Shorter is a '
    'feature: the eight-minute focused recording beats the forty-minute meeting capture for every future '
    'viewer, forever. Pair it with text (Chapter 5’s rule): the video carries tone and demonstration; the '
    'written summary carries the searchable decisions. And accept one clean take: minor stumbles read as '
    'human; re-record only for structural failure. Five takes chasing flawlessness produce a stiff sixth '
    'take and a lost afternoon.')

h1(doc, 'Q&A: where credibility is confirmed or refunded')
figure(doc, os.path.join(FIG, 'ch12_qa.png'),
    'Figure 6. The Q&A protocol — restate, answer briefly, bridge home, commit when stumped.',
    'A four-step flow: restate the question, answer briefly then stop, bridge stray questions back to the takeaway, and '
    'commit to a dated follow-up when stumped — with the tip to prepare the five questions that could sink the talk.')
para(doc, 'Audiences discount the scripted portion of a talk — they know you rehearsed it — and weight the '
    'unscripted portion, because Q&A is where they watch you think without a net. The protocol: restate or '
    'repeat each question first (the room hears it, the recording captures it, and you buy five seconds of '
    'thought). Answer the question asked, briefly, then stop — the three-minute answer to a ten-second '
    'question loses the room you just won, and rambling answers read as insecurity even when they are '
    'thorough. Bridge stray questions home: “that’s really phase two — for today’s decision, here’s what '
    'matters,” courteous and back on the takeaway. And when stumped, never bluff: “good catch — I’ll verify '
    'and reply to the group by Friday” is credible, while an improvised statistic is a time bomb that '
    'Chapter 4’s verification rules already taught you not to plant. Then actually reply by Friday: the '
    'follow-through IS the answer (Chapter 11).')
para(doc, 'The hostile question gets Chapter 7’s machinery, standing up. Depersonalize on arrival: answer '
    'the substance inside the hostility and let the bait fall — the room is watching your temperature, not '
    'the questioner’s. Concede what is true (“you’re right that the pilot was one team”) and attach the '
    'context (“which is why the metrics were agreed with finance in advance”) — the two-sided move earns '
    'more credibility under attack than any defense. Cap exchanges at two: “let’s take this offline — I '
    'want the detail” returns the room to everyone who owns it, and refuses the duel that hijacks talks. '
    'Prepare all of this in advance by writing the five questions you would ask if you wanted to sink your '
    'own talk. You already know what they are; the only question is whether you draft the answers before '
    'or after the room asks.', bold_lead='The hostile question.')

h1(doc, 'Team presentations: one talk, several voices')
para(doc, 'The team talk fails in predictable ways — four solo acts stapled together, handoffs improvised as '
    '“um, I guess now Maya will…”, six presenters shrugging at each other during Q&A — and each failure has '
    'a structural fix. Build ONE talk: a single pyramid with one designer, divided after the structure '
    'exists (Chapter 10’s team-writing rules on their feet). Script the handoffs as rehearsed lines: '
    '“…and that’s the cost case. Maya will show you the pilot that answers it” — name, topic, momentum. '
    'Route Q&A through a lead who assigns each question by name: “Priya ran that analysis — Priya?” '
    'Match register across speakers: one deck, one formality level, one pace zone. And remember that idle '
    'presenters are still on stage: the teammate checking his phone during your section is the slide the '
    'audience remembers. Team rehearsal is where all five fixes install — one full simulate pass together '
    'is the minimum, handoffs included.')

h1(doc, 'Case study: the demo that died and the talk that didn’t')
para(doc, 'A vendor team presented to a client’s leadership: the contract hinged on a live demonstration of '
    'the sample-intake workflow. Ninety seconds in, the staging server began returning errors — in front of '
    'the CTO, the CFO, and the quality director, on the vendor’s own product. The junior engineer reached '
    'for the keyboard to debug. The presenter did something better rehearsed: one sentence — “the demo gods '
    'have voted; here’s the recording from this morning” — and the backup video was playing within twenty '
    'seconds, the same workflow narrated live over it, the schedule intact.')
para(doc, 'Unpack what made the recovery possible, because none of it was improvised. The backup recording '
    'existed BECAUSE the team treated the demo as evidence with a failure mode (this chapter’s evidence '
    'rotation) — recorded that morning, on the same build, queued on a second laptop. The one-liner was '
    'scripted: the team had literally rehearsed the failure branch, the way pilots rehearse engine-out '
    'procedures. And the narration skills — voice, pacing, takeaway titles on the video’s chapters — were '
    'the same delivery craft the live demo would have used. The talk’s architecture survived because the '
    'demo was a proof INSIDE the structure, not the structure itself.')
para(doc, 'The contract closed that month, and the client’s CTO later told the account manager which moment '
    'had sold it: not the workflow, the recovery. “That’s how they’ll handle OUR incidents.” Audiences '
    'evaluate the unscripted moment as a sample of future behavior — which means composure under failure '
    'is not damage control. It is a product feature, and it is rehearsable.')
bullets(doc, [
    ('The lesson about evidence:', 'every live demonstration is a bet; the backup recording is the hedge '
     'that costs twenty minutes and saves contracts.'),
    ('The lesson about rehearsal:', 'rehearse the failure branches, not just the happy path — the scripted '
     'recovery line is what keeps ninety seconds of server errors from becoming the story.'),
    ('The lesson about audiences:', 'the room prices your worst moment, not your average one — and a '
     'well-handled worst moment can outsell a flawless run.'),
])

h1(doc, 'Case study: the conference talk, rebuilt')
para(doc, 'An operations manager was invited to present her team’s intake-automation project at a regional '
    'industry conference — twenty minutes, two hundred strangers, her first talk outside her own building. '
    'Draft one was the internal deck: forty-one slides, dense with implementation detail, titled things like '
    '“Phase 2 Architecture” and “Validation Approach.” It had served the ops committee well. It would have '
    'died at the conference, and her rehearsal recording told her so: eleven minutes in, she was on slide '
    'nine, narrating configuration decisions to an audience that, she suddenly realized, would never '
    'configure anything of hers.')
para(doc, 'The rebuild started where this chapter starts: the sentence. For THIS audience — peers from other '
    'labs, shopping for ideas — the takeaway was not her architecture. It was “a two-person team can '
    'automate intake in ninety days without buying a platform — here’s the map.” Three points assembled '
    'under it: what it cost (the honest number, including the two failed weeks), what it returned (38% '
    'intake-time reduction, zero transcription findings), and what she would do differently (the '
    'validation sequencing that cost the two weeks). Forty-one slides became fourteen billboards; the '
    'implementation detail moved to a leave-behind with her contact information — announced in minute one, '
    'which converted note-takers back into listeners.')
para(doc, 'She scripted the joints and rehearsed three passes, the last one recorded standing in a '
    'conference-room simulation of the venue. The hook came from her own incident log: “Last March, one '
    'transposed sample ID cost us eleven days and a client. This March, that error is impossible. Twenty '
    'minutes, and I’ll show you the ninety days between those sentences.” Q&A produced the sink-the-talk '
    'question she had prepped — “this only worked because your volume is small” — and the two-sided answer '
    '(“you’re right that 600 samples a week is the ceiling for this design; here’s the fork I’d take at '
    'higher volume”) earned her the hallway conversation that mattered: two labs asked for the map, and '
    'one of them, eight months later, asked for her. The talk was a job interview she didn’t know she was '
    'giving — most good talks are.')

h1(doc, 'Worked example: a ten-minute pitch, end to end')
para(doc, 'Because structure is easier to copy than invent, here is a complete outline for a ten-minute '
    'internal pitch — the analyst from Chapter 8’s pilot case, asking the ops committee to approve the '
    'full rollout. Ten minutes, eight billboards, every joint scripted.')
numbered(doc, [
    'Minute 0–1, the hook (scripted): “Six months ago this committee bet $2,400 on a pilot. This morning '
    'the pilot finished paying that back for the ninth time. I’m here for the other two benches.” Slide 1: '
    'title billboard — “Roll out barcode intake: $23K/yr, 14-month payback.”',
    'Minute 1–2, the roadmap: “Three things: what the pilot proved, what the rollout costs, and the one '
    'risk worth discussing.” Slide 2: three named stops.',
    'Minute 2–4, point one — the pilot’s numbers. Slide 3: one chart, takeaway title (“Intake time fell '
    '38% and stayed there”), THE line highlighted. Slide 4: “Zero transcription findings in 90 days” with '
    'the auditor’s one-sentence quote. Transition (scripted): “Those are the returns. Here’s the bill.”',
    'Minute 4–6, point two — cost, framed. Slide 5: “$24K against the $67K the current process burns '
    'annually” — the status quo priced, Chapter 8 style. Verbal detail: itemization exists in the '
    'leave-behind; the room hears only the frame.',
    'Minute 6–8, point three — the risk, conceded first. Slide 6: “The honest risk: two benches migrate '
    'during Q4 audit prep.” The two-sided move: “here’s the mitigation we already tested — staggered '
    'cutover with the old system running until sign-off.”',
    'Minute 8–9, Q&A (before the close, always). The five prepared hostile questions include the sink '
    'question: “what breaks at 900 samples a week?” — answer drafted, with its number.',
    'Minute 9–10, the close (scripted): echo — “the pilot proved it: $23K a year is sitting in the intake '
    'queue” — then the ask: “I need this committee’s approval today to hold the vendor’s pricing through '
    'the 25th.” Slide 8: the ask, dated, alone on the screen.',
])
para(doc, 'Note what the outline does NOT contain: an agenda slide, a company history, an architecture '
    'tour, or a “questions?” slide as the final frame. Every minute serves the sentence, the evidence '
    'rotates (chart, quote, frame, concession), and the last thing on screen is the decision. Steal the '
    'skeleton; replace the numbers.')

h1(doc, 'Deep dive: speaking without a deck')
h2(doc, 'Impromptu answers: the PREP skeleton')
para(doc, 'Most professional speaking is not presentations — it is the meeting moment when someone turns to '
    'you and says “what do you think?” The unprepared answer rambles toward a point it discovers en route; '
    'the professional answer runs a pocket structure. PREP: Point (“I’d renew, not rebid”), Reason (“the '
    'switching costs eat two years of any savings”), Example (“when we rebid the courier contract in 2024, '
    'the transition consumed the entire first-year discount”), Point again (“so I’d renew, and spend our '
    'leverage on terms instead”). Thirty seconds, shaped like the pyramid, and deliverable with zero notice '
    'because the shape is memorized even when the content is fresh.')
para(doc, 'PREP also buys composure: the structure occupies the panicked first second (“what’s my Point?”) '
    'that would otherwise fill with “um, well, I mean, it depends.” It depends is where impromptu answers '
    'go to die — everything depends; the room asked what you THINK. State the point, flag the dependency '
    'inside the reason (“unless the vendor’s Q3 pricing surprises us”), and let the caveat live inside a '
    'committed answer rather than in place of one. Chapter 9’s calibration vocabulary — “my read is,” '
    '“I’d want to verify, but directionally” — lets you commit honestly at every confidence level.')
h2(doc, 'Panels: the shared stage')
para(doc, 'Panel appearances reward different craft than solo talks. Prepare three portable points — '
    'takeaway-grade sentences you can deploy whatever the moderator asks — and bridge to them the way '
    'politicians do, but honestly: answer the actual question first, then connect it to your point. Keep '
    'answers to sixty seconds; panels are conversations, and the panelist who monologues becomes the '
    'panelist the moderator stops calling on. Disagree with fellow panelists the way Chapter 11 taught — '
    'about the idea, by name, warmly: “Maria’s right about the cost curve; where I’d push back is the '
    'timeline.” Panel disagreement, done well, is the most watchable thing on any stage, and the audience '
    'remembers who made it generative rather than awkward. And when you are NOT speaking, you are still on '
    'camera: the visible listening — notes, nods, attention — is your slide.')
h2(doc, 'Introducing a speaker, and being introduced')
para(doc, 'The introduction is a sixty-second genre with exactly three jobs: why this topic matters to THIS '
    'audience, why this speaker has the standing to address it, and the handoff by name. Write it with the '
    'speaker’s input, keep credentials to the two that matter (Chapter 10’s staffing rule at podium scale), '
    'and land the name last, clearly — it cues the applause. When you are the one introduced, send the '
    'introducer that sixty-second draft yourself: the speakers who seem effortlessly well-introduced wrote '
    'the introduction. That is not vanity; it is the same courtesy as briefing your references (Chapter 13).')

h1(doc, 'Deep dive: the slide makeover clinic')
para(doc, 'Theory teaches slower than examples. Here is one slide, rebuilt in three passes — the makeover '
    'sequence you can run on any inherited deck.')
para(doc, 'Title: “Q3 Support Metrics Review.” Body: eleven bullets mixing ticket volumes, response times, '
    'staffing notes, and one buried sentence — “escalations from the Meridian account tripled after the '
    'June migration.” A 6-series line chart with a legend, gridlines, and no highlighted line. Font: '
    '16-point, shrinking to 12 where the bullets ran long. This slide is a document page wearing a '
    'projector. The room will read it for forty silent seconds, find eleven facts and no point, and check '
    'their phones.', bold_lead='The original.')
para(doc, 'Ask the Chapter 9 question: what is the ONE claim this slide exists to make? The presenter, '
    'pressed, says: “support is fine overall, but the Meridian escalations are a fire.” That is two '
    'claims — so it is two slides. The eleven bullets sort into three piles: evidence for claim one, '
    'evidence for claim two, and detail that belongs in the leave-behind (most of it).',
    bold_lead='Pass one: find the claim.')
para(doc, 'Slide A gets the takeaway title “Support held steady through Q3 — one exception,” a single '
    'summary figure, and nothing else. Slide B gets “Meridian escalations tripled after the June '
    'migration,” the chart cut from six series to one highlighted line (Meridian) with the other five '
    'grayed to context, the June migration marked with a vertical line, and the legend replaced by a '
    'direct label. The claim, the evidence, the cause candidate — three seconds, readable from the back.',
    bold_lead='Pass two: rebuild as billboards.')
para(doc, 'The eleven bullets, the staffing notes, and the full six-series data move to the leave-behind, '
    'where they gain headings and takeaway titles of their own (the slide-doc rules above). The '
    'presenter’s speaking notes absorb the connective tissue. Total content lost: zero. Total content '
    'findable: all of it, for the first time. The makeover took eleven minutes, and the Meridian fire — '
    'the thing the original slide had buried in bullet nine — became the meeting’s decision item, which '
    'was the point of having a meeting.', bold_lead='Pass three: relocate the evidence.')

h1(doc, 'Deep dive: walking an audience through a chart')
para(doc, 'Data slides fail live in a way they never fail on paper: the presenter throws a full chart onto '
    'the screen and keeps talking, while the room stops listening to decode axes. The fix is progressive '
    'disclosure — narrating the chart the way you would give directions, one landmark at a time.')
numbered(doc, [
    'Orient before data: “On the left, intake time in minutes; along the bottom, the twelve weeks of the '
    'pilot.” Two seconds that buy the whole room a shared map. Skipping orientation is why half of any '
    'audience is still decoding your axes when your point arrives.',
    'Anchor the baseline: “The flat line at nine minutes is where we started — that’s manual intake.” Now '
    'every future movement has meaning.',
    'Reveal the story in beats, building the chart in stages if the tool allows: “Week three, barcode '
    'goes live — watch the drop. Week five, it stabilizes at 5.6. And this gap” — pointing — “is the 38%.”',
    'Land the takeaway title out loud, verbatim: “Intake time fell 38% and stayed there.” The title, the '
    'chart, and the sentence now agree, which is what makes the point stick.',
    'Preempt the axis skeptic: if the axis is cropped or the period selected, SAY so before the sharpest '
    'analyst in the room says it for you (Chapter 9’s honest-display rules, performed).',
])
para(doc, 'One chart, walked well, outperforms five charts flashed. If the talk needs five charts, it '
    'usually needs two charts and a leave-behind — the data version of three points, not eleven.')

h1(doc, 'Deep dive: presenting to every room')
para(doc, 'A talk built for the median listener quietly taxes everyone else. Inclusive presenting is '
    'mostly a checklist of small mechanics with large reach — and every item also improves the talk for '
    'the median listener, which is the pattern accessibility usually follows.')
bullets(doc, [
    ('Say what the slide shows.', 'Screen-reader users, phone-bridge listeners, and the back row all '
     'depend on the narration carrying the visual: “the highlighted line — Meridian — triples after '
     'June.” If your talk works as a podcast, it works.'),
    ('Repeat audience questions into the microphone', 'before answering — the room’s hard-of-hearing '
     'contingent is always larger than it looks, and recordings without repeated questions are half a '
     'conversation.'),
    ('Color never carries meaning alone', '(Chapter 9): the highlighted line is also thicker and labeled; '
     'the red/green status pair gets icons or words.'),
    ('Caption every recording.', 'Auto-captions are near-free and imperfect; a five-minute cleanup makes '
     'the recording usable by everyone, searchable by anyone, and skimmable by the impatient — which is '
     'everyone.'),
    ('Mind the idiom load for global audiences.', 'Sports metaphors, cultural references, and speed are '
     'the three walls non-native listeners hit (Chapter 1’s plain-language rule, spoken). Slower, plainer, '
     'and with the takeaway on the slide in text — the same moves that serve the distracted native listener.'),
    ('Offer the material two ways.', 'The leave-behind plus the recording plus the live talk is not '
     'redundancy; it is the same argument at three attention budgets.'),
])

h1(doc, 'Case study: the webinar half the audience heard')
para(doc, 'A product manager ran a customer webinar — two hundred registrants, a forty-minute walkthrough of '
    'the new release, a genuinely strong deck. The failure was invisible from inside: she presented from a '
    'dual-monitor setup, shared the wrong screen for the first six minutes (the audience watched her email '
    'client while she narrated slides only she could see), and never knew, because she had disabled the chat '
    'to “reduce distraction.” When a colleague finally phoned her, she recovered the share — flustered — and '
    'spent the rest of the session behind her own agenda, rushing the demo, skipping the Q&A she had '
    'promised. The recording, unedited and uncaptioned, went out anyway. Attendance at the NEXT webinar '
    'was ninety-one.')
para(doc, 'Run the diagnosis with this chapter’s checklist and the failure decomposes into five skipped '
    'rules, none of them exotic. No tech rehearsal (the wrong-screen share dies in a ten-minute soundcheck). '
    'No monitored chat — the parallel channel existed precisely to catch what she could not see, and she '
    'had turned it off. No co-pilot: webinars at scale need a second human watching the audience’s '
    'experience, exactly as team presentations assign Q&A routing. No failure plan — a pre-sent deck would '
    'have made even six broken minutes survivable (“slide four, everyone”). And no recovery composure: the '
    'rushed remainder cost more than the broken opening, because audiences forgive glitches and remember '
    'panic (the demo case’s lesson, inverted).')
para(doc, 'The repair for round two was mechanical, not motivational: a fifteen-minute tech rehearsal with '
    'the co-pilot, chat on and owned by the co-pilot, deck pre-sent, captions on the recording, and — the '
    'detail worth stealing — a printed index card taped below her webcam reading “SHARE CHECK: what do THEY '
    'see?” Attendance recovered in two cycles. Virtual presenting is not harder than live presenting; it '
    'is differently instrumented, and the instruments have to be checked because the feedback loop that a '
    'live room provides for free — two hundred faces — is exactly what the screen removes.')

h1(doc, 'The week-of timeline: a presenter’s checklist')
para(doc, 'Preparation distributes badly under deadline pressure — everything crowds into the anxious final '
    'evening unless it is scheduled earlier on purpose. The timeline below front-loads what benefits from '
    'distance and leaves the final day almost empty, which is itself a nerve-management strategy.')
bullets(doc, [
    ('A week out:', 'takeaway sentence final; three points and evidence chosen; the deck drafted as '
     'billboards; the leave-behind split off. Run the titles-only test and the first aloud pass (shape).'),
    ('Three days out:', 'second aloud pass (time) — cut to 90% of the slot. Draft the five sink-the-talk '
     'questions and outline their answers. Send pre-reads if the format uses them.'),
    ('Two days out:', 'third pass (simulate), standing and recorded. Review the recording once, kindly, '
     'for pace and filler only. Fix the two worst joints; resist rebuilding the deck — late structural '
     'surgery creates more failure than it removes.'),
    ('The day before:', 'logistics only. Room or platform tested, backup recording queued, deck pre-sent '
     'where applicable, clothes chosen, clicker batteries confirmed. No new content after tonight: the '
     'talk is what it is, and the remaining variable is you, rested.'),
    ('The day of:', 'arrive or log in early enough to breathe. Tech check. The slow-exhale protocol in '
     'the final ten minutes. First minute rehearsed once, quietly, from memory. Then trust the '
     'preparation — the room wants you to succeed, and this time you have given it every reason to.'),
])
para(doc, 'Notice the shape: content freezes 48 hours out. The single most common self-inflicted wound in '
    'presenting is the night-before rebuild — new slides that have never been rehearsed, delivered by a '
    'presenter who traded sleep for them. The checklist exists to make that rebuild structurally '
    'unnecessary, because everything it would fix was fixed on Tuesday.')

h1(doc, 'Workshop: building the ninety-second story')
para(doc, 'The story slot in the evidence rotation deserves a construction sequence, because “tell a story” '
    'is advice the way “be confident” is advice — true and unusable. Here is the build, run on a real '
    'example for the intake-automation pitch.')
numbered(doc, [
    'Start from the point, not the anecdote: the story must prove “manual intake produces expensive '
    'errors.” Inventory your true material for the incident that best carries exactly that weight — not '
    'the funniest incident, the load-bearing one.',
    'Cast one named human: “Priya, our senior tech on the Tuesday shift.” Named people carry stakes; '
    '“a staff member” carries paperwork.',
    'Compress to four beats (Chapter 12’s skeleton): the person and the normal (“Priya, mid-shift, '
    'forty samples in the queue”); the problem (“two vials, one transposed digit”); what it cost (“eleven '
    'days of rework and a client who now audits everything we send”); what changed (“under barcode intake, '
    'that transposition is physically impossible”).',
    'Cut the subplot. The vendor’s role, the meeting that followed, the policy memo — all true, all '
    'gone. Ninety seconds holds one arc.',
    'Land it, out loud: “that’s what one digit costs at manual speed.” The point, announced, is what '
    'converts a story the room ENJOYED into a story the room USES.',
    'Verify it like a claim (Chapter 4): would Priya recognize this telling? Would the client? Stories '
    'travel — tell only the version that survives arrival.',
])
para(doc, 'Rehearse the story separately from the talk — it is the one component that improves most per '
    'pass, because timing and emphasis are the whole craft. And retire stories that stop being true: the '
    '“current process” anecdote from two systems ago, still circulating in a veteran’s talks, is the '
    'spoken version of the stale wiki page (Chapter 5).')

h1(doc, 'The recognition moment: toasts, thanks, and send-offs')
para(doc, 'Sooner than you expect, someone will hand you a glass or a microphone and thirty seconds: the '
    'retirement send-off, the launch toast, the award introduction. The genre has exactly three beats — '
    'the specific (one true, concrete detail: “Dana answered my 2 a.m. audit question in nine minutes”), '
    'the meaning (what that detail says about the person or the moment), and the raise (“to Dana — who '
    'never once made a question feel small”). Thirty to sixty seconds, no biography, no inside jokes '
    'that exclude half the room, and absolutely no improvised roasting — the recognition moment runs on '
    'Chapter 6’s five-quality rules, spoken, and “specific” is what separates the toast people remember from '
    'the generic warmth they forget before the glasses land. Prepare it in the hallway if that is all '
    'the notice you get: one detail, one meaning, one raise. PREP’s gentler cousin.')

h1(doc, 'The executive readout: presenting to the people with the pen')
para(doc, 'Presenting upward compresses every rule in this chapter. Executive audiences are the most '
    'time-poor, the most interruption-prone, and the most decision-oriented room you will face — and they '
    'reward a specific adaptation of the standard build. The takeaway moves even earlier: many executive '
    'readouts open with the ask on slide one, before any context, because the room may be down to fifteen '
    'minutes at any moment and the decision must survive the truncation. (This is Chapter 3’s direct '
    'pattern at its logical extreme: assume the meeting could end after your first ninety seconds, and '
    'front-load accordingly.)')
para(doc, 'Expect and welcome interruption. Executives navigate by question, not by roadmap — the talk you '
    'rehearsed as a sequence will be consumed as a conversation, and the presenters who thrive treat every '
    'interruption as the room steering toward what it needs. This changes rehearsal: instead of practicing '
    'the linear run, practice entering each slide cold (“if they jump to cost, slide five stands alone”), '
    'which billboards with takeaway titles make possible and document-slides make impossible. Keep a '
    'backup-appendix section — the detail slides you hope not to need — and jump to them by number when '
    'the CFO asks the depth question: “slide fourteen has that breakdown.” Nothing builds executive '
    'confidence faster than a presenter who anticipated the question and can navigate to its answer in '
    'four seconds.')
para(doc, 'Two more adaptations. First, pre-wire (Chapter 8): the executive readout should ratify '
    'conversations already had, not ambush the room — surprises produce deferrals, and “let’s revisit '
    'next quarter” is where asks go to die. Second, end with the decision restated and OWNED: “so we’re '
    'approved for the two-bench rollout, vendor pricing held through the 25th — I’ll confirm in writing '
    'this afternoon.” The written confirmation (Chapter 6) converts the room’s nod into a record before '
    'the nod fades. Executive yeses are perishable; refrigerate them in email.')

h1(doc, 'After the talk: the follow-through')
para(doc, 'The talk ends; the genre does not. Within the hour, the promised artifacts move: the '
    'leave-behind to the full list, the decision confirmation to the approvers, the “I’ll get you that '
    'number by Friday” items into your own tracker with dates (Chapter 11’s follow-through list — the '
    'place presentation reputations are actually finished). Within the day, the specific thank-yous: the '
    'colleague who staged the demo, the sponsor who pre-wired the room (five-quality rules, Chapter 6). And '
    'within the week, the self-review: watch the recording once if one exists, note the two joints that '
    'stuck, and file the improvements where your NEXT talk’s checklist will find them. Presenters improve '
    'between talks or not at all — the room only ever sees the result.')

h1(doc, 'Five myths, retired')
para(doc, 'Retired by the arousal-reframe research and by every green room in the world. The pros are not '
    'calm; they are rehearsed, and their adrenaline is running the same chemistry as yours. The myth is '
    'harmful because it converts normal physiology into evidence of unfitness — students feel the pulse '
    'and conclude they are “not presenters,” when the pulse is the species, not the verdict.',
    bold_lead='Myth: good presenters are naturally calm.')
para(doc, 'The most tired advice in the genre, and structurally wrong: a joke that lands buys you ten '
    'seconds; a joke that dies costs the first minute you most needed. Humor that emerges from real '
    'material — the honest aside, the self-aware recovery — outperforms the imported opener every time. '
    'Open with their stakes; be funny later, if you are.', bold_lead='Myth: open with a joke.')
para(doc, 'Eye contact with humans, in sentences, is the actual skill (and looking at foreheads reads as '
    'exactly what it is). The over-the-heads trick survives because it feels safer for the speaker — which '
    'is the tell: it is anxiety management disguised as technique, and the audience can feel the vacancy.',
    bold_lead='Myth: look just over their heads.')
para(doc, 'Gestures suppressed die hard: speakers who pin their hands broadcast tension from every other '
    'channel instead. Hands above the waist, describing what the words describe, is both more natural and '
    'more persuasive — the nonverbal channel agreeing with the verbal one (Chapter 1).',
    bold_lead='Myth: keep your hands still.')
para(doc, 'The deck is the cheapest part of the talk and the most-fiddled, because slide polishing FEELS '
    'like preparation while requiring no courage. An evening spent on pass-three rehearsal moves a talk '
    'further than a week of template surgery. Budget accordingly: the audience remembers one sentence and '
    'the hard moment — neither lives in the deck.', bold_lead='Myth: better slides make a better talk.')

h1(doc, 'Frequently asked questions')
para(doc, 'Slower than yesterday, as a starting bias — nerves accelerate everyone, and nobody in the history '
    'of business presentations has been criticized for being slightly too clear. The real metric is variation: '
    'a deliberately slowed sentence before the big number, a quicker pass through the familiar. Constant '
    'anything — fast or slow — is the actual enemy.', bold_lead='How fast should I talk?')
para(doc, 'Yes, and openly: bullet-level cards or the presenter view, glanced at joints. What reads as '
    'unprofessional is not notes — it is READING, head down, in document sentences. If your notes are '
    'takeaway fragments, glancing at them looks like exactly what it is: a prepared person checking the map.',
    bold_lead='Can I use notes?')
para(doc, 'Aim for one slide per 45–90 seconds of billboard-style talk, but treat the number as a smell test, '
    'not a law: a talk that needs 60 slides in 20 minutes is flipping too fast to land anything, and a talk '
    'with 4 slides in 30 minutes had better be an extraordinary story. The real constraint is the takeaway '
    'test, slide by slide.', bold_lead='How many slides for a twenty-minute talk?')
para(doc, 'Neither. Memorize the joints — first minute, transitions, close — and converse the middles from '
    'bullets. Full scripts produce recitation and catastrophic single-point failure; pure improvisation '
    'squanders the two moments (first and last) that audiences weight most.', bold_lead='Script or wing it?')
para(doc, 'Take it as data about the slide, not the audience: phones come out when the screen stopped '
    'earning attention. Land a pause, change the energy, move to the story or the demonstration — the '
    'recovery tools are the same ones that would have prevented the drift. And check the clock honestly: '
    'rooms have attention budgets (this guide’s audience section), and running long is the fastest way to '
    'spend one.', bold_lead='What if people start checking phones?')

h1(doc, 'Putting it to work this week')
numbered(doc, [
    'Write the one-sentence takeaway for your course presentation — before touching the slide tool. Test '
    'it: could a classmate repeat it tomorrow?',
    'Run the titles-only test on any deck you have — yours or a colleague’s. If the titles read as section '
    'labels, rewrite three of them as claims and watch the deck improve without touching a chart.',
    'Record ninety seconds of yourself presenting anything, phone propped on books. Review once, kindly, '
    'for two items only: pace and filler. One targeted rehearsal pass beats general anxiety every time.',
    'Draft the five questions that could sink your next talk, and outline the concede-then-context answer '
    'to the worst one.',
    'Build your backup plan: for any demo, the recording; for any screen-share, the pre-sent deck. Twenty '
    'minutes of hedge, permanently installed.',
])

h1(doc, 'Discussion questions')
numbered(doc, [
    'Recall the best presentation you have ever seen. Which of this chapter’s choices was it making — and '
    'which rule, if any, did it break successfully? What let it get away with that?',
    'The chapter claims slides come last. Argue the strongest case for the opposite workflow — then '
    'identify which kind of presenter, preparing which kind of talk, that case actually fits.',
    'Where is the line between rounding for the ear (“$67K”) and misleading simplification? Construct the '
    'test, using Chapter 9’s honest-display rules as the base.',
    'Uptalk, filler words, and vocal fry attract disproportionate criticism — sometimes fairly, sometimes '
    'as bias wearing a style guide. Which delivery feedback is legitimate craft, and which is policing? '
    'Build your standard.',
    'The demo case argues that audiences price your worst moment. Does that make live demonstrations '
    'irrational? When is the live demo still worth the bet, and what makes it so?',
])

keyterms(doc, [
    ('Takeaway', 'the one sentence a listener could repeat tomorrow to someone who wasn’t there — written '
     'first, proven in the middle, echoed at the close.'),
    ('Build order', 'takeaway → three points → evidence → frame → slides. The slide tool comes last so the '
     'talk’s structure comes from thought, not template.'),
    ('Roadmap', 'the three named stops announced after the hook — the pyramid’s second layer, read aloud; '
     'the only navigation listeners get.'),
    ('Billboard rule', 'one point per slide, readable in three seconds, with the speaker carrying the '
     'detail — because audiences read faster than you talk and cannot do both.'),
    ('Leave-behind (slide-doc)', 'the standalone document version of the talk — full evidence, takeaway '
     'titles — sent after, and announced up front to buy back the room’s eyes.'),
    ('Titles-only test', 'reading a deck by its title lines alone; if they tell the whole story as claims, '
     'the deck is built (the headings-only test of Chapter 3, ported).'),
    ('Evidence rotation', 'proving points with a mix of numbers (for analysts), stories (for everyone), '
     'and demonstrations (for skeptics) — each with its failure mode hedged.'),
    ('Joints and spans', 'the selective-memorization pattern: script the first minute, transitions, and '
     'close; leave the middles conversational from bullets.'),
    ('Touch-turn-talk', 'the slide-glance discipline: look at the screen, turn back to the room, then '
     'speak — never presenting to the projection wall.'),
    ('Bridge', 'the Q&A move that returns stray questions to the takeaway: acknowledge, then “for today’s '
     'decision, here’s what matters.”'),
    ('Arousal reframe', 'relabeling pre-talk adrenaline as readiness rather than fear — the '
     'performance-psychology finding that identical physiology performs differently under different labels.'),
    ('Failure branch rehearsal', 'practicing the recovery moves — backup recording, scripted recovery '
     'line, blank-moment protocol — with the same seriousness as the happy path.'),
])

quiz(doc, [
    ('The correct first step in building a presentation is:',
     ['Choosing a slide template', 'Writing the one repeatable takeaway sentence',
      'Drafting the opening story', 'Booking the room']),
    ('Slides come last in the build order because:',
     ['The slide tool imposes template-shaped structure on talks born inside it', 'Slide software is unreliable',
      'Slides are optional in business talks', 'Designers should build them instead']),
    ('A talk should end with:',
     ['Q&A, so the audience leaves engaged', 'A summary of every slide',
      '“Thank you” and contact information', 'The echo of the takeaway plus a concrete, dated ask — after questions']),
    ('The billboard rule exists because:',
     ['Projectors distort small text', 'Templates default to large fonts',
      'Audiences read faster than speakers talk and cannot read and listen at once', 'Executives dislike detail']),
    ('“Pilot cut intake time 38%” beats “Pilot Results” as a slide title because:',
     ['It is shorter', 'It carries the claim — surviving both the skim and the room’s three-second read',
      'It includes a number, which templates require', 'It avoids the passive voice']),
    ('The rehearsal spec calls for cutting the talk to 90% of its slot because:',
     ['Q&A and reality eat the margin — the exactly-fitting talk runs over', 'Rehearsals always run fast',
      'Shorter talks need less evidence', 'Timers are unreliable']),
    ('When stumped in Q&A, the professional move is:',
     ['A confident approximate answer', 'Ruling the question out of scope',
      'Deferring to a teammate immediately', 'Acknowledging, committing to a dated follow-up, and delivering it']),
    ('The hostile-question protocol caps direct exchanges at two because:',
     ['Three exchanges exceed most time limits', 'Hostile questioners tire quickly',
      'Longer duels hijack the room from everyone who owns it', 'Moderators require it']),
    ('For recorded (async) presentations, the takeaway belongs in the first thirty seconds because:',
     ['Recording software trims openings', 'Viewers hold a skip bar — unearned patience does not exist asynchronously',
      'Async audiences are less intelligent', 'Titles cannot carry takeaways']),
    ('The demo case’s deepest lesson is that:',
     ['Audiences price the worst moment — and a rehearsed recovery can outsell a flawless run', 'Live demos should be abandoned',
      'Staging servers are unreliable', 'Backup recordings are legally required']),
], ['b', 'a', 'd', 'c', 'b', 'a', 'd', 'c', 'b', 'a'])

references(doc, [
    'Anderson, C. (2016). TED talks: The official TED guide to public speaking. Houghton Mifflin Harcourt.',
    'Brooks, A. W. (2014). Get excited: Reappraising pre-performance anxiety as excitement. Journal of '
    'Experimental Psychology: General, 143(3), 1144–1158.',
    'Duarte, N. (2008). Slide:ology: The art and science of creating great presentations. O’Reilly Media.',
    'Mayer, R. E. (2009). Multimedia learning (2nd ed.). Cambridge University Press.',
    'Miller, G. A. (1956). The magical number seven, plus or minus two. Psychological Review, 63(2), 81–97.',
    'Minto, B. (2009). The pyramid principle (3rd ed.). Financial Times Prentice Hall.',
    'Reynolds, G. (2011). Presentation zen (2nd ed.). New Riders.',
])

out = os.path.join(os.path.dirname(__file__), '..', 'ch12-study-guide.docx')
finish(doc, os.path.abspath(out))
