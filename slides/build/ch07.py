# Chapter 7 — Negative Messages (45 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 7"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Negative Messages",
    "Saying no · delivering bad news · apologizing — the messages that test everything, when it matters most", D)
notes(s, "Chapter 7: bad news craft. Companion guide has both cases in full.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Stage", "the indirect pattern: honest buffer, reasons first, the no once, a concrete pivot."),
    ("Craft", "the news sentence between its two failure modes — evasion and cruelty."),
    ("Apologize", "with anatomy: own the act, name the impact, prevent, stop."),
    ("Beat", "the MUM effect: report problems small and early, paired with a plan."),
    ("Pair", "channels for consequential news: rich conversation first, written record same day."),
], D, nxt())
notes(s, "Objectives map to the bad-news-to-customers assignment.")

s = section_slide(prs, "01", "The indirect pattern",
    "Sequencing for a reader you are about to hurt.", D, nxt())
notes(s, "Section 1.")

s = flow_slide(prs, "Buffer → Reasons → News → Pivot", [
    ("BUFFER", "True common ground. One or two sentences. Promises NOTHING."),
    ("REASONS", "The real why, before the no — reaching a mind not yet defending itself."),
    ("THE NEWS", "Once. Clear. Brief. Owned."),
    ("PIVOT", "Whatever yes exists: alternative, partial, path back, referral."),
], D, nxt(), note_text="Not evasion — sequencing. Every fact arrives, in the order a human can hear it. Scope: consequential news only; trivial nos stay direct.")
notes(s, "The psychology: a blunt opening no turns the rest of your message into opposition research.")

s = two_col_slide(prs, "Buffers: the two fatal failure modes",
    "False hope", [
        "“Great news about your application process!”",
        "Converts disappointment into betrayal",
        "The reader replays your cheer as mockery",
    ],
    "Padding", [
        "Three paragraphs of weather before the point",
        "Reads as the writer stalling",
        "Stalling reads as dread — and dread is contagious",
        ("The craft:", "true · relevant · brief"),
    ], D, nxt(), right_fill=RGBColor(0xF7, 0xEA, 0xE8), right_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "Working buffers: agreement, appreciation, facts, good-news-first, understanding.")

s = bullets_slide(prs, "Reasons: the load-bearing middle", [
    ("Give the real reason when you can.", "Readers detect boilerplate; a true constraint respects them enough to argue with."),
    ("Frame on facts and shared interests,", "not personal judgment: “the budget closed in March” survives scrutiny; “not a priority” starts a war."),
    ("Explain — don't beg.", "If the decision is defensible, defend it plainly. If it isn't, the problem is the decision, not the paragraph."),
], D, nxt())
notes(s, "Refusals are won or lost here.")

s = two_col_slide(prs, "The news sentence: between evasion and cruelty",
    "The failure modes", [
        ("Evasion:", "“It may prove difficult at this juncture to accommodate…” — the reader must hunt for their own rejection"),
        ("Cruelty:", "“Denied. Your proposal failed on multiple criteria.” — the no, weaponized"),
        ("Camouflage:", "“A decision has been made” — owns nothing, fools no one"),
    ],
    "The craft", [
        "“We can't fund the March cohort this year.”",
        "Once — repetition grinds the wound",
        "Clear — never make them ask “is this a no?”",
        ("Softening that works:", "the subordinate clause — “Although we couldn't fund March, September…”"),
    ], D, nxt())
notes(s, "The one place the indirect pattern briefly becomes direct.")

s = icon_rows_slide(prs, "The pivot: every no carries whatever yes exists", [
    ("↪", "The alternative", "“September has space — I can hold a seat until Friday.”"),
    ("½", "The partial yes", "“We can fund two of the three positions.”"),
    ("🛤", "The path back", "“Resubmission opens August 1 — Q3 data would make yours lead the cycle.”"),
    ("→", "The referral", "“Meridian Labs runs exactly this analysis; ask for Dr. Chen.”"),
], D, nxt(), kicker="Concrete or nothing: “feel free to reach out in the future” is upholstery, not a pivot.")
notes(s, "If genuinely nothing exists, close with respect — no manufactured silver linings.")

s = section_slide(prs, "02", "Apologies",
    "The negative message about yourself — where directness IS the respect.", D, nxt())
notes(s, "Section 2.")

s = flow_slide(prs, "Apology anatomy (Lazare, 2004)", [
    ("OWN IT", "“I missed the deadline I committed to.” No “mistakes were made.” No “if you were offended.”"),
    ("NAME THE IMPACT", "“…which delayed your review a week.” Proof you understand the cost."),
    ("REPAIR + PREVENT", "What's happening now — and what stops a repeat. THE trust sentence."),
    ("STOP", "No third apology. The reader needs the fix, not your feelings."),
], D, nxt(), note_text="Most failed apologies fail at step one. “If you were offended” relocates the offense into the reader's sensitivity.")
notes(s, "One clean apology outperforms five grovels.")

s = section_slide(prs, "03", "Early and upward",
    "The MUM effect — and the career advantage of beating it.", D, nxt())
notes(s, "Section 3.")

s = stat_slide(prs, "Bad news travels slowest when it matters most", "MUM",
    "People delay, soften, and reroute bad news — even when blameless for it (Rosen & Tesser, 1970). It's why managers hear about problems six weeks late.",
    [("The protocol:", "report while it's small · pair it with a plan · calibrate honestly (“yellow, trending red”)."),
     ("The formula:", "own it → cause in one line → recovery plan with a date → the ask."),
     ("The career math:", "leaders trust big things to the people who told the truth about small things, early, on purpose."),
    ], D, nxt())
notes(s, "More than fifty years of replication. Chapter 1's upward filter, explained.")

s = bullets_slide(prs, "Channel and timing for consequential news", [
    ("Rich first:", "conversation or call — empathy has bandwidth, questions get absorbed, dignity stays private."),
    ("Record second, same day:", "terms, dates, next steps in writing."),
    ("Email-only for personal bad news reads as cowardice", "— because it usually is."),
    ("Timing:", "as early as certainty allows. Never Friday 4:55 as avoidance. Never “after the holidays” while they plan around a fiction."),
], D, nxt())
notes(s, "Chapter 1's pairing at its highest-stakes application.")

s = bullets_slide(prs, "Case: the same denial, twice", [
    ("Version A (email):", "“Your request has been denied as the program does not meet eligibility criteria. Consult the policy manual. Future requests should be submitted with closer attention…”"),
    ("What the employee hears:", "“you were careless” — a denial converted into a reprimand."),
    ("Version B (conversation + confirmation):", "true buffer, the real constraint stated checkably, an owned no — and two concrete yeses (covered fall program; travel days as work time)."),
    ("Eleven extra minutes.", "One version books a withdrawal that compounds through the grapevine; the other, a deposit: “she fought for me and the policy blocked it.”"),
], D, nxt())
notes(s, "Identical no; opposite relationships.")

s = bullets_slide(prs, "Case: the slipping launch", [
    ("Week 3: launch will slip a month.", "Account lead: “Why alarm them with maybes? Wait for the retest.” PM overrules — calls the client that afternoon."),
    ("The structure:", "known · unknown · recovery plan · “new date confirmed by Tuesday; updates weekly.”"),
    ("The retest fails too. The slip grows.", "The client extends the contract anyway — citing the vendor management."),
    ("The control group:", "an identical slip on another account, held for certainty. That client learned four days out — from their own integration team."),
], D, nxt())
notes(s, "Trust was staked on the reporting, not the outcome — and the reporting held. The client ALWAYS finds out; the only variable is from whom.")

s = two_col_slide(prs, "Two refusals you can reuse this week",
    "To a colleague", [
        "“Thanks for thinking of me — I've enjoyed the past two panels.",
        "I'm committed to the audit closeout through the 22nd, and panel prep deserves real attention, so I have to pass this cycle.",
        "Dana ran the rubric with me last year and would be excellent; happy to brief whoever steps in.”",
    ],
    "To a customer (claim denial)", [
        "“Thanks for the photos — they made review easy.",
        "The damage is consistent with a post-delivery drop, which warranty and carrier coverage don't extend to. We can't replace at no cost.",
        "What we can do: repair at $180 — a third of replacement — scheduled this week. And the reinforced case on p. 12 prevents exactly this break.”",
    ], D, nxt())
notes(s, "Both from the guide's worked examples: buffer, reasons, one no, concrete pivot.")

s = section_slide(prs, "04", "Saying no, genre by genre",
    "The pattern is one; the craft is knowing how it bends per situation.", D, nxt())
notes(s, "Section 4: applied refusals. Same skeleton — buffer, reasons, one no, pivot — tuned to four recurring situations.")

s = bullets_slide(prs, "Refusing a favor or invitation", [
    ("Fast beats padded.", "A quick, warm no lets them ask the next person today; a slow, agonized no costs them the week you spent dreading it."),
    ("One real reason, not three excuses.", "'I'm committed through the 22nd' closes the case; a pile of small excuses invites rebuttal of each."),
    ("Protect the relationship, not the fiction.", "Never invent a conflict — invented conflicts get discovered at exactly the wrong party."),
    ("Pivot if you mean it, close if you don't.", "'Ask me again for the spring cycle' is a promise; don't issue it as decoration."),
], D, nxt())
notes(s, "Low-stakes refusals are where students practice the pattern safely. The speed point is underrated: slow nos are a tax on the asker.")

s = bullets_slide(prs, "Refusing an internal proposal", [
    ("Honor the work first — specifically.", "'The vendor comparison in section two is the best I've seen this year' — a real buffer, because real effort preceded the no."),
    ("Give the decision-grade reason.", "Budget, timing, strategy conflict — the actual constraint, stated so the proposer could verify it."),
    ("Separate the idea's fate from the person's.", "'This isn't fundable this cycle' must not decode as 'stop bringing me ideas' — say the second part out loud: 'bring me the Q4 version.'"),
    ("A no without a reason teaches people to stop proposing.", "The long-term cost of lazy refusals is an organization that goes quiet (Chapter 1's upward filter, self-inflicted)."),
], D, nxt())
notes(s, "The audience for an internal refusal is bigger than the proposer — everyone watching learns whether proposing is safe here.")

s = bullets_slide(prs, "Turning down a candidate", [
    ("Tell them promptly.", "Every day of silence after their interview is a day they held their life in a hold pattern for you."),
    ("Buffer with the true positive,", "then the news in one clean sentence: 'we've offered the role to another candidate.' No euphemism maze."),
    ("Don't machine-audit them.", "A rejection is not the moment for a feedback report; offer feedback only if they ask and you can give it usefully."),
    ("Leave the door authentically.", "'I'd genuinely encourage you to apply for the analyst opening in the fall' — only if true; candidates remember which companies meant it."),
], D, nxt())
notes(s, "Candidates talk, review sites exist, and today's rejected applicant is next year's client-side buyer. The rejection letter is brand communication.")

s = bullets_slide(prs, "The policy no: refusing a customer request", [
    ("Explain the policy's why, not just its existence.", "'Returns close at 90 days because we can't resell after that window' beats the wall of 'per our policy.'"),
    ("Never hide behind the system.", "'The system won't let me' reads as 'I stopped trying' — because it is."),
    ("Find the adjacent yes.", "Can't refund? Maybe credit. Can't expedite? Maybe partial-ship. The pivot slide's four moves apply verbatim."),
    ("Know your own escalation line.", "If you'd grant it as the manager, escalate it as the rep — routing a borderline case up IS good refusal craft."),
], D, nxt())
notes(s, "Policy nos are where companies bleed goodwill invisibly. The 'adjacent yes' habit converts a stonewall into a negotiation.")

s = two_col_slide(prs, "The discount request: two refusals",
    "Version A", [
        "'Unfortunately we are unable to offer discounting at this time due to company policy.'",
        "No reason a reader could verify",
        "No pivot — the sentence is a wall",
        "Customer hears: 'we don't value you enough to explain'",
    ],
    "Version B", [
        "'Our pricing stays flat because we don't pad list prices for negotiation — everyone gets the same number.'",
        "'What I can do: waive onboarding ($400) and lock this rate for 24 months.'",
        "The no arrives WITH its logic and a real yes",
        "Customer hears: 'the price is honest and they worked for me'",
    ], D, nxt(), left_fill=RGBColor(0xF7, 0xEA, 0xE8), left_head_color=RGBColor(0xB2, 0x3A, 0x31))
notes(s, "Same policy, same no. Version B converts pricing rigidity into a fairness story and still finds a concession that costs less than a discount.")

s = section_slide(prs, "05", "Criticism and performance feedback",
    "Negative news about someone's work — delivered so the work improves.", D, nxt())
notes(s, "Section 5: feedback. The negative message where the reader has to keep working with you tomorrow.")

s = flow_slide(prs, "The SBI-R skeleton", [
    ("SITUATION", "Anchor it: 'In Tuesday's client call…' — not 'you always…'"),
    ("BEHAVIOR", "What happened, observably: 'the pricing slide had last quarter's numbers.'"),
    ("IMPACT", "The consequence: 'the client caught it, and we spent ten minutes rebuilding credibility.'"),
    ("REQUEST", "The forward ask: 'run the numbers check before client decks — want me to show you my checklist?'"),
], D, nxt(), note_text="Behavior is the hinge: 'the slide was wrong' can be fixed; 'you're careless' can only be resented.")
notes(s, "Situation-Behavior-Impact plus the request. Every element is checkable — which is what makes it hearable.")

s = bullets_slide(prs, "Criticism that lands", [
    ("Private, always.", "Public correction is punishment theater; the audience learns fear, not the lesson."),
    ("Prompt, not ambush.", "Feedback about March delivered in June is an indictment, not a correction — nothing can be done about March in June."),
    ("The behavior, never the person.", "'This report buries the recommendation' is workable; 'you're a poor writer' is a verdict (Chapter 4's review rules, higher stakes)."),
    ("One thing at a time.", "The six-issue feedback session fixes zero issues; pick the one that matters most this month."),
    ("End at the future.", "The last sentence is what happens next, not a replay of the failure."),
], D, nxt())
notes(s, "Five rules, all violations common. The 'one thing' rule is the least practiced — feedback hoarding produces annual avalanches.")

s = two_col_slide(prs, "Feedback failure modes",
    "The sandwich (praise-criticism-praise)", [
        "Predictable structure teaches people to dread compliments",
        "The criticism gets lost in the bread on purpose — that's the problem",
        "Better: honest sequencing — real praise when earned, clear criticism when needed, separately",
    ],
    "The other classics", [
        ("The drive-by:", "criticism in passing, in chat, at 4:58 — stakes deserve a conversation"),
        ("The vague wince:", "'just tighten it up' — unactionable disappointment"),
        ("The pile-on:", "saving twelve items for one meeting — an avalanche is not feedback"),
        ("The proxy:", "criticism routed through a third person arrives as gossip"),
    ], D, nxt())
notes(s, "The sandwich critique matters: it's still taught, and it trains teams to distrust praise. Honest, kind, separate is the replacement.")

s = bullets_slide(prs, "Taking criticism about your work", [
    ("First response: understand, not defend.", "'Can you show me where it lost you?' — the defensive reflex kills the information flow permanently."),
    ("Extract the checkable core.", "Even badly delivered criticism usually contains a real stumble — mine it for the data and discard the delivery."),
    ("Close the loop visibly.", "'I reworked the opening per your note — better?' teaches people that feedback to you is a good investment."),
    ("You're allowed to disagree — after understanding.", "'I see why it read that way; here's why I kept it' is a professional sentence. Reflexive rejection isn't."),
], D, nxt())
notes(s, "Mirror of Chapter 4's receiving-edits slide, at relationship stakes. People stop giving feedback to those who bleed on them — and being feedback-starved is a career ceiling.")

s = section_slide(prs, "06", "Anger and de-escalation",
    "When the negative message is the one arriving — flaming, at 9 a.m.", D, nxt())
notes(s, "Section 6: handling incoming heat. The skill that makes everything else in the chapter possible under fire.")

s = bullets_slide(prs, "Answering the angry email", [
    ("Do not match the temperature.", "Anger answered with anger produces a thread nobody survives with dignity — one of you has to be the professional; it's you."),
    ("Acknowledge the frustration as real,", "without conceding facts you haven't verified: 'I understand this outage hit you mid-launch — let me find out exactly what happened.'"),
    ("Answer the substance, skip the bait.", "The three insults get no reply; the two legitimate questions get complete ones. Watch the thread cool."),
    ("Shift channels deliberately.", "Two hot replies means pick up the phone — voice carries the empathy that text strips (Chapter 1's richness, applied)."),
], D, nxt())
notes(s, "The selective-response move — answer substance, ignore bait — is the single most effective de-escalation technique in writing, and it's teachable.")

s = flow_slide(prs, "The de-escalation sequence", [
    ("ACKNOWLEDGE", "Their experience is real before anything else: 'that delay cost you a weekend.'"),
    ("ALIGN", "Signal the shared goal: 'we both need this live before Monday.'"),
    ("INFORM", "Facts, cleanly: what happened, what's known, what isn't yet."),
    ("ACT", "The concrete step, with a time: 'you'll have the patch or a call from me by 3:00.'"),
], D, nxt(), note_text="Skipping ACKNOWLEDGE and jumping to facts reads as 'your anger is irrelevant' — and re-arms it. The sequence exists because the order matters.")
notes(s, "Four beats, in order. Most technical people skip straight to INFORM and are baffled when accurate information makes things worse.")

s = bullets_slide(prs, "The message you must never send", [
    ("The 9 p.m. flame reply:", "write it if you must — in a document, never in the reply window with a live To: field."),
    ("Sleep is an editor.", "Overnight, the devastating rebuttal becomes visibly career-limiting; the morning edit is always shorter and always calmer."),
    ("Sarcasm reads twice as hostile in print", "and lives forever (Chapter 5's permanence — your worst sentence is a screenshot on layaway)."),
    ("The test before sending anything heated:", "would you stand behind every sentence in a meeting with both your managers present? That meeting is one forward away."),
], D, nxt())
notes(s, "Chapter 1's composure rule with mechanics. The 'draft outside the reply window' trick prevents the classic catastrophe of the accidental send.")

s = bullets_slide(prs, "Case: the thread one calm reply ended", [
    ("Eleven messages deep:", "two departments, escalating CCs, bolded accusations about a missed handoff — the thread had become the conflict."),
    ("The reply that ended it", "answered only the two factual questions, owned the one piece that was genuinely hers, proposed a 15-minute call, and CC'd no one new."),
    ("The call took nine minutes.", "The written summary afterward — three lines, decisions and owners — was the first message in the thread anyone kept."),
    ("The lesson:", "in a hot thread, the person who narrows the audience, owns their piece, and changes the channel is the one everyone remembers as the adult."),
], D, nxt())
notes(s, "Every element is teachable: selective response, ownership, channel shift, CC discipline, written confirmation. The 'adds no new CCs' detail is the quiet masterstroke.")

s = section_slide(prs, "07", "Bad news at scale",
    "Crisis communication: the chapter's rules, under stadium lights.", D, nxt())
notes(s, "Section 7: organizational crisis. Same anatomy — own, inform, act — executed publicly and fast.")

s = flow_slide(prs, "The crisis response sequence", [
    ("ACKNOWLEDGE FAST", "Hours, not days. Silence gets narrated by everyone except you."),
    ("FACTS + HONEST UNKNOWNS", "What you know, what you don't yet — stated as confidently as the knowns."),
    ("THE ACTION", "What's being done right now, and who owns it."),
    ("THE CADENCE", "'Next update at 4:00' — a promised rhythm kills the refresh-and-rumor cycle."),
    ("FOLLOW THROUGH", "Keep every promised update, especially the ones where nothing changed."),
], D, nxt(), note_text="The cadence is the underrated step: a promised 4:00 update, kept, buys calm that no wording can.")
notes(s, "Crisis compresses the MUM effect to hours. The 'honest unknowns' move — saying clearly what you don't know yet — is what separates credible statements from lawyerly ones.")

s = bullets_slide(prs, "The holding statement: when you know almost nothing", [
    ("You can always say four true things:", "we know something happened · we're investigating now · here's who's affected as far as we know · here's when we'll say more."),
    ("Never speculate to fill the silence.", "The guessed cause you retract tomorrow costs more credibility than a day of 'we're still confirming.'"),
    ("Never minimize on arrival.", "'A small number of accounts' announced before you've counted becomes the quote in every follow-up story."),
    ("The holding statement buys time honestly —", "which is its entire job. It promises the next communication, not the answers."),
], D, nxt())
notes(s, "The first hours, operationalized. Minimizing-before-counting is the classic self-inflicted wound — the correction becomes a second story.")

s = two_col_slide(prs, "Crisis communication: the record",
    "What works", [
        "Named human spokesperson, consistent across updates",
        "Plain language — jargon reads as evasion under stress",
        "Affected people hear it from you before the press does",
        "Sympathy stated plainly: 'we're sorry this happened to you' (see the legal slide — sympathy ≠ admission)",
    ],
    "What fails, every time", [
        "'We take this very seriously' as the entire content",
        "Passive camouflage: 'access was gained,' 'errors occurred'",
        "Legal review that strips every human sentence",
        "The staged apology that arrives after the stock dip, not the harm",
    ], D, nxt())
notes(s, "The failure column is recognizable from every mishandled breach of the last decade. Passive camouflage callbacks: Chapter 3's incident report case.")

s = bullets_slide(prs, "Case: two product recalls", [
    ("Company A announced the recall itself,", "the day the defect was confirmed: plain-language notice, prepaid return labels, a named VP on every update, weekly cadence until closed."),
    ("Company B waited for the regulator,", "issued a statement 'out of an abundance of caution' that named no defect, and routed press questions to a form."),
    ("A year later:", "Company A's recall is a customer-service case study its own sales team cites. Company B's is the first search result for its brand."),
    ("The asymmetry:", "the recall cost both companies the same money. The narration cost one of them the reputation."),
], D, nxt())
notes(s, "Composite case built on the recurring public pattern. The point for students: the event is rarely the reputational damage — the handling is.")

s = section_slide(prs, "08", "The fine print",
    "Law, culture, and the ethics of sequencing.", D, nxt())
notes(s, "Section 8: the boundaries around the craft — what negative messages must respect beyond the reader's feelings.")

s = bullets_slide(prs, "Negative messages have legal gravity", [
    ("Everything is discoverable —", "including the snarky draft you deleted and the 'candid' chat beside the official letter (Chapter 5's permanence, with subpoenas)."),
    ("Sympathy is not admission.", "'We're sorry this happened to you' is human; 'this was our fault' is a legal conclusion — know which one you're authorized to write."),
    ("References and rejections:", "stick to verifiable facts and the decision itself; characterizations of the person are where defamation exposure lives."),
    ("When liability is plausible, loop in counsel —", "but fight for the human sentences. 'Legally clean and emotionally dead' is a failure mode too, and it also ends up in court."),
], D, nxt())
notes(s, "Not legal advice — professional awareness. The sympathy-vs-admission distinction is the practical one students will actually use.")

s = bullets_slide(prs, "Bad news across cultures", [
    ("Directness is calibrated locally.", "The clean, owned no this chapter teaches reads as refreshing in low-context cultures — and as brutal in high-context ones (Chapter 1)."),
    ("Watch for the soft no.", "'This would be very difficult' or 'we will study it carefully' IS the refusal in much of the world; pressing for a 'real answer' insults twice."),
    ("Preserve face deliberately.", "Bad news delivered so the receiver can maintain dignity in front of their own organization is a design requirement, not a nicety."),
    ("When cultures mix, name the norm.", "'I'm going to be very direct, in the way of my field' — announcing your register buys tolerance for it."),
], D, nxt())
notes(s, "The chapter's pattern is not culturally universal in its calibration — the sequence survives, the bluntness dial moves. The soft-no decoder is immediately practical.")

s = bullets_slide(prs, "The ethics line: sequencing is not spin", [
    ("The test:", "after your indirect message, does the reader know everything a blunt version would have told them? If yes — craft. If no — deception with a structure."),
    ("Buffers may not promise,", "reasons may not be invented, pivots may not be decorative. Every element carries a truth requirement."),
    ("Delay is a decision with an owner.", "'Waiting for certainty' past the point of usefulness is the MUM effect wearing a prudence costume — see the slipping-launch case."),
    ("The publicity test (Chapter 1) applies to structure:", "would you be comfortable explaining WHY you ordered the message this way? 'So they'd hear the reasons first' survives. 'So they wouldn't notice' doesn't."),
], D, nxt())
notes(s, "The chapter's own integrity check. Indirectness is defensible exactly as far as it serves the reader's ability to hear — one inch past that, it's manipulation.")

s = takeaways_slide(prs, [
    "Indirect structure is sequencing, not evasion: reasons reach an unwounded mind; every fact arrives.",
    "Buffers: true, relevant, brief — never false hope, never padding.",
    "The news sentence: findable, unambiguous, once, owned.",
    "Every no carries whatever yes exists — concretely, or not at all.",
    "Apologies: own the act, name the impact, prevent, stop.",
    "Beat the MUM effect: small, early, with a plan. Rich first, record second, never Friday 4:55.",
], D, nxt(), site_note="Practice now: course site → Chapter 7 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "The reader always finds out. The only variable you control is whether they find out from you, early, with a plan — or from the grapevine, late, with a grievance.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "When is directness the KINDER structure for bad news? Build the decision rule with two real examples.",
    "Describe a rejection you received that was well done. What will you steal from it?",
    "Why do organizations reward MUM-effect behavior while claiming to want transparency? What changes the incentive?",
    "Take a public corporate apology and rewrite its worst sentence to pass the anatomy.",
    "Draft the structure for announcing a price increase to loyal customers: what buffers, reasons, and pivots honestly exist?",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 7 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 7 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Apply:", "This chapter IS the toolkit for the bad-news-to-customers assignment."),
    ("Read:", "The Chapter 7 Study Guide — both cases in full, plus the apology anatomy."),
    ("Coming next:", "Chapter 8 — persuasive messages: moving readers who could say no toward yes."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch07-negative-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
