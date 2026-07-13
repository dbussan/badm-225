# Chapter 6 — Positive and Neutral Messages (32 slides, delivery-neutral)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from decklib import *

D = "BADM 225 · Chapter 6"
prs = new_deck()
i = 0
def nxt():
    global i; i += 1; return i

s = title_slide(prs, "BADM 225 · PROFESSIONAL COMMUNICATION FOR BUSINESS",
    "Positive and Neutral Messages",
    "Requests · replies · claims · adjustments · goodwill — the everyday mail that builds your reputation", D)
notes(s, "Chapter 6: the messages you'll send most and think about least — which is why they're diagnostic.")
nxt()

s = bullets_slide(prs, "What you'll be able to do after this chapter", [
    ("Write", "requests that pass the complete-ask test — grantable without a clarifying question."),
    ("Reply", "answer-first, anticipate the next question, and end the thread."),
    ("File", "claims that recruit an advocate: record, facts, specific remedy, deadline, calm."),
    ("Grant", "claims the way that keeps customers: fix first, prevention sentence included."),
    ("Send", "goodwill that passes the five-quality test — the highest-return mail there is."),
], D, nxt())
notes(s, "Objectives map to the Chapter 6 bank and the introductory-letter assignment.")

s = section_slide(prs, "01", "Requests & replies",
    "Ask so people can say yes. Answer so threads end.", D, nxt())
notes(s, "Section 1.")

s = flow_slide(prs, "The direct request", [
    ("ASK", "First, in question form — questions politely demand answers."),
    ("EXPLAIN", "Why, and why THEM: “you ran last year's audit.”"),
    ("DETAIL", "Format, scope, access — a list they can work down."),
    ("CLOSE", "Deadline + its reason + goodwill."),
], D, nxt(), note_text="The complete-ask test: can the reader comply without asking you anything? A request that ends threads is a professional artifact.")
notes(s, "Two failure modes: the buried ask and the incomplete ask.")

s = flow_slide(prs, "The reply skeleton", [
    ("ANSWER", "“Yes — the room is yours, 2–4 Friday.” First word, not paragraph three."),
    ("DETAILS", "Everything they'd ask next: access, codes, capacity."),
    ("EXTRAS", "What they didn't ask but need: parking validation exists."),
    ("FORWARD", "“Anything else before Friday, just ask.”"),
], D, nxt(), note_text="The bar: your reply should END the thread, not extend it. Partial no? Lead with the yes you can give.")
notes(s, "Answer-first is Chapter 3's directness applied to the inbox.")

s = section_slide(prs, "02", "Claims & adjustments",
    "Complaining like a professional — and granting like one.", D, nxt())
notes(s, "Section 2.")

s = icon_rows_slide(prs, "Claim anatomy: a request wearing a grievance", [
    ("№", "The record first", "Order number, dates, product — findable in their system from sentence one."),
    ("📷", "Facts, calmly, with evidence", "Attach the photos. Skip the adjectives."),
    ("🎯", "The specific remedy", "Refund, replacement, repair — sellers grant specifics and stall vague unhappiness."),
    ("📅", "Deadline + confidence", "“I'm sure you'll want to make this right” recruits; sarcasm entrenches."),
], D, nxt())
notes(s, "The rep reading your claim didn't break your product — make it easy for them to become your advocate.")

s = flow_slide(prs, "Granting a claim: the adjustment", [
    ("GRANT", "Sentence one: “A replacement ships today, free.” Delay = manufactured dread."),
    ("EXPLAIN", "What happened, one clause, no blame opera."),
    ("PREVENT", "“We've switched your account to reinforced packaging” — THE confidence sentence."),
    ("RESTORE", "Forward-looking close. No groveling — spotlight on the fix, not the failure."),
], D, nxt(), note_text="Reciprocity economics: a customer rescued gracefully often becomes more loyal than one never disappointed (Cialdini, 2021).")
notes(s, "Good news = direct pattern. Always.")

s = bullets_slide(prs, "Case: the $60 intercept", [
    ("Cracked $1,900 instrument; textbook claim filed.", "New hire's draft: “While our packaging meets industry standards… we are willing on this occasion to…”"),
    ("The sales director's rewrite:", "same-day replacement + loaner + upgraded packaging + thanks for the photos. Cost: ~$60 freight."),
    ("Eighteen months later:", "the lab standardized on the supplier for three courses — citing “how they handle problems.”"),
    ("The lesson:", "a defensive grant spends the money AND forfeits the credit. If you're saying yes, say it first."),
], D, nxt())
notes(s, "Well-recovered failures beat uninterrupted service — the recovery proves the relationship.")

s = section_slide(prs, "03", "Goodwill",
    "The highest-return mail you will ever send.", D, nxt())
notes(s, "Section 3.")

s = icon_rows_slide(prs, "The five-quality test", [
    ("S", "Specific", "“Your triage of Saturday's outage saved the launch” — the named act proves you noticed."),
    ("S", "Sincere", "No agenda in the envelope. A thank-you that pivots to a favor was an invoice."),
    ("S", "Short", "Three sentences beat three paragraphs."),
    ("S", "Spontaneous", "Sent promptly — not at review season."),
    ("S", "Selfless", "About them. “No reply needed.”"),
], D, nxt())
notes(s, "Thanks, congratulations, sympathy — the messages nobody requires and everybody remembers.")

s = bullets_slide(prs, "The hard one: sympathy", [
    ("Send it.", "Silence from colleagues wounds more than clumsy words ever could."),
    ("Keep it brief, warm, unhurried:", "“No reply needed” is part of the gift."),
    ("Ink for milestones:", "in a digital century, handwriting is the costly signal."),
    ("And never AI-drafted (Chapter 15):", "the entire content of the message is that a human paused."),
], D, nxt())
notes(s, "The one category where the medium and effort ARE the message.")

s = stat_slide(prs, "Goodwill capital compounds", "5 min",
    "A specific thank-you costs five minutes and deposits for years: credit given publicly, favors before asks, references you never requested.",
    [("The research:", "habitual givers — generous WITH boundaries — end up overrepresented at the top of success distributions (Grant, 2013)."),
     ("The mechanism:", "reciprocity, among the most robust findings in influence science (Cialdini, 2021)."),
     ("The move:", "send one five-quality note this week. Actually send it."),
    ], D, nxt())
notes(s, "Chapter 16's deposits-before-withdrawals, at everyday scale.")

s = section_slide(prs, "04", "Instructions",
    "Messages people follow with their hands.", D, nxt())
notes(s, "Section 4.")

s = icon_rows_slide(prs, "Instructions that don't generate tickets", [
    ("1.", "One step, one action, one line", "Numbered, imperative verbs first: “Click… Enter… Save…”"),
    ("⚑", "Preconditions before step 1", "The VPN password needed at step 6 is a landmine if discovered at step 6."),
    ("✓", "Checkpoints after key steps", "“You'll see a green banner” — readers know they're still on the path."),
    ("⚠", "Warnings BEFORE the step they protect", "A caution after the damage line is an autopsy."),
    ("🧪", "Test on ONE novice", "Their first confusion is your revision list — forty tickets cheaper."),
], D, nxt())
notes(s, "Judged by a brutal metric: the support questions generated.")

s = bullets_slide(prs, "Case: the announcement that stranded three VIPs", [
    ("One 68-word sentence", "containing five actions, two branches (vehicle, international), and a buried warning."),
    ("Result:", "forty help-desk tickets and a follow-up beginning “To clarify our previous communication…”"),
    ("The rewrite:", "subject “Registering visitors — new required steps (2 min)”; numbered standard path; branches as labeled variants; warnings BEFORE their steps."),
    ("The prevention:", "one staff member outside Facilities, walking it cold, would have found every landmine in five minutes."),
], D, nxt())
notes(s, "Paragraph-prose instructions are where clarity goes to die.")

s = two_col_slide(prs, "Two five-minute templates",
    "The complete request", [
        "“Could you send the Q2 vendor report by Thursday noon?",
        "I'm compiling the renewal recommendation (due Friday); yours is the last dataset.",
        "Needed: summary tab as PDF + raw sheet, same format as Q1.",
        "Thursday noon keeps us on schedule — thank you!”",
    ],
    "The goodwill note", [
        "“Dana — your catch on the calibration drift saved us a failed audit finding;",
        "the assessor specifically noted the logs were clean.",
        "I've told Dr. Reyes the same. Thank you.”",
        ("Count the S's:", "specific, sincere, short, spontaneous, selfless."),
    ], D, nxt())
notes(s, "Both from the study guide's worked examples.")

s = section_slide(prs, "05", "The business letter",
    "The formal channel that signals: this one counts.", D, nxt())
notes(s, "Section 5: letters. Rare enough now that using one is itself a message — which is exactly why the format survives.")

s = bullets_slide(prs, "When a letter is the right channel", [
    ("Crossing the organizational boundary.", "Customers, officials, other firms — the letter is the org-to-org and person-to-org register."),
    ("Ceremony is part of the content.", "Offers, awards, formal thanks, resignations — the formality honors the moment."),
    ("Legal and contractual weight.", "Notices, agreements, and anything a lawyer may one day wave — letters are built to be exhibits."),
    ("The scarcity works for you.", "In an inbox century, letterhead is the costly signal: someone composed, printed, and signed this."),
], D, nxt())
notes(s, "The letter didn't die; it specialized. Students will write fewer letters than emails — but the letters will matter more per document.")

s = icon_rows_slide(prs, "Letter anatomy, top to bottom", [
    ("🏛", "Letterhead + date", "Who's writing and when — the date matters legally; write it unambiguously (July 15, 2026)."),
    ("📍", "Inside address + salutation", "The recipient's name, title, organization, address — then 'Dear Ms. Okafor:' with the name verified (Chapter 4)."),
    ("¶", "Body in block format", "Everything flush left, blank line between paragraphs — the modern default. Direct pattern applies: point in paragraph one."),
    ("✒", "Complimentary close + signature block", "'Sincerely,' then four blank lines for ink, then typed name and title."),
    ("📎", "Notations", "'Enclosure' and 'cc:' lines at the bottom — the letter's version of the attachment paperclip."),
], D, nxt())
notes(s, "Format walk-through — block format only, since it's the modern standard. The salutation-name verification callback to Chapter 4 is deliberate.")

s = bullets_slide(prs, "The introductory letter — this unit's assignment", [
    ("Paragraph one: who you are and why you're writing.", "Both, in two sentences — the reader shouldn't finish the paragraph still wondering."),
    ("Paragraph two: the substance.", "What you offer or ask, with the specifics that make a response possible (the complete-ask standard again)."),
    ("Paragraph three: the forward close.", "The concrete next step — who contacts whom, how, by when."),
    ("The register check:", "warmer than a memo, tighter than a chat — professional, but a human being wrote it."),
], D, nxt())
notes(s, "Direct setup for the assignment. The three-paragraph skeleton is the request flow from Section 1 dressed in letter format.")

s = section_slide(prs, "06", "Announcements, confirmations, welcomes",
    "The quiet genres that keep organizations running on rails.", D, nxt())
notes(s, "Section 6: three routine positive genres students will send weekly for the rest of their careers.")

s = bullets_slide(prs, "Good-news and neutral announcements", [
    ("Lead with the news, not the process.", "'The office closes at noon on July 3' — never 'As part of our ongoing commitment to work-life balance…'"),
    ("Answer the reader's three questions in order:", "What's changing? Am I affected, and how? What do I do, by when?"),
    ("One channel for questions, named.", "'Questions: reply to Dana, not all' — or the announcement becomes forty separate conversations."),
    ("Time it for the affected, not the announcer.", "News that changes Monday's work goes out Thursday, not Monday at 8:59."),
], D, nxt())
notes(s, "Announcements are downward communication (Chapter 1) at its most routine — and the genre where corporate throat-clearing is most epidemic.")

s = bullets_slide(prs, "Confirmations: the thread-enders", [
    ("Restate the terms, don't reference them.", "'Confirming: 500 units at $12.40, delivered June 30 to the Fargo warehouse' — the numbers live IN the confirmation."),
    ("Send it while memory is fresh.", "Same day as the call or meeting; a confirmation of last week's conversation confirms nobody's memory."),
    ("Invite correction explicitly.", "'If any detail doesn't match your notes, tell me by Friday' — silence then becomes agreement, fairly."),
    ("This is the record being born.", "Chapter 5's graduation rule: spoken agreements become written ones, or they become disputes."),
], D, nxt())
notes(s, "The confirmation is the cheapest litigation insurance ever invented, and it doubles as courtesy. The explicit correction window is the professional touch.")

s = bullets_slide(prs, "The welcome message", [
    ("To a new colleague or client, day one:", "warmth plus logistics — what happens next, where things live, who their humans are."),
    ("Name a person, not a department.", "'Your first stop is Maya (maya@…), who runs onboarding' beats 'contact HR with any questions.'"),
    ("One first step, not twelve.", "The welcome that lists everything due in month one reads as a warning. Give the next action and the map's location."),
    ("It sets the relationship's tone —", "the first message anyone receives from you or your team is the one they'll remember as 'what this place is like.'"),
], D, nxt())
notes(s, "Welcomes are goodwill messages with an operations payload. The named-human rule echoes the OOO slide in Chapter 5.")

s = bullets_slide(prs, "Recommendations and referrals", [
    ("Vouch only for what you observed.", "'She ran our audit for two years; the findings were clean twice' — specifics are the currency, adjectives are filler."),
    ("The genre runs on YOUR credibility.", "Every inflated recommendation you sign devalues the next one — recommenders get reputations too."),
    ("Can't recommend honestly? Decline honestly.", "'I don't think I'm the right reference for this role' is kinder than a visibly tepid letter — and everyone can read tepid."),
    ("Make referrals a warm handoff:", "introduce both parties, state why the match makes sense, then step out and let them work."),
], D, nxt())
notes(s, "Recommendations sit at the boundary of goodwill and risk: generous by nature, but written on the recommender's credit. The tepid-letter point matters — damning with faint praise is a real signal recipients decode.")

s = bullets_slide(prs, "Praise travels up, credit travels down", [
    ("Praise in public, correct in private.", "The goodwill note's public cousin: recognition in the channel, the meeting, the newsletter."),
    ("CC the manager — as a gift.", "'CCing Dr. Reyes so she knows what your triage saved us' turns a thank-you into a career artifact."),
    ("Pass credit downward relentlessly.", "'The analysis is Maya's' costs nothing and is remembered forever — hoarded credit is remembered too."),
    ("Written praise is permanent praise.", "The five-quality note that reaches a personnel file outlives every hallway compliment."),
], D, nxt())
notes(s, "The routing rules of goodwill: direction and visibility multiply the same five minutes of writing. Ties to Grant's giver research from the stat slide.")

s = bullets_slide(prs, "Case: the confirmation that settled the dispute", [
    ("A phone agreement on custom terms:", "extended payment window in exchange for a larger order — nothing signed, deal moving fast."),
    ("The account manager sent a five-line confirmation", "same afternoon: quantities, prices, the nonstandard window, and 'flag anything that doesn't match by Thursday.'"),
    ("Eight months later, new management disputed the terms.", "The email — dated, acknowledged, uncorrected — ended the argument in one meeting."),
    ("The lesson:", "confirmations feel like busywork on the day you send them. They are the only version of events that survives personnel changes."),
], D, nxt())
notes(s, "The case argues the habit: confirm while it's friendly, because you can't confirm after it isn't. Links Chapter 5's permanence section to a positive outcome.")

s = takeaways_slide(prs, [
    "Ask first, in question form; detail to the complete-ask standard; close with a dated reason.",
    "Answer in the first word; anticipate the next question; end the thread.",
    "Claims: record, facts, specific remedy, deadline — confidence recruits an advocate.",
    "Adjustments: grant first, explain without opera, include the prevention sentence.",
    "Goodwill passes five-quality; ink for milestones; never AI — the pause is the message.",
    "Instructions: numbered, imperative, preconditions first, warnings before their steps, tested on a novice.",
], D, nxt(), site_note="Practice now: course site → Chapter 6 → Practice, then the graded homework before the weekly deadline.")
notes(s, "Recap.")

s = quote_slide(prs, "Worth keeping",
    "Nobody remembers who answered routine mail adequately. Everybody remembers who made things easy — and who said thank you.",
    "this chapter, compressed", D, nxt())
notes(s, "Closing frame.")

s = discussion_slide(prs, "Discussion questions", [
    "Bring a request that failed the complete-ask test. What did the round trips cost?",
    "When did a company's complaint handling change your loyalty — either direction? Map it against the adjustment flow.",
    "Everyone agrees goodwill notes matter; almost nobody sends them. Name the frictions — and the one you'll remove.",
    "Autopsy instructions that generate repeated questions where you work or study. Which element is missing?",
    "Should front-line staff grant borderline claims without approval? Argue the reciprocity math.",
], D, nxt())
notes(s, "Async-ready.")

s = bullets_slide(prs, "Your next steps", [
    ("Practice:", "Course site → Chapter 6 → Practice questions (instant feedback, unlimited tries)."),
    ("Graded:", "Complete the Chapter 6 homework on the site; paste your completion code into the Blackboard assignment before the weekly deadline."),
    ("Write:", "Your introductory letter (this unit's assignment) — Figure 1's request pattern in letter dress."),
    ("Send:", "One real five-quality goodwill note this week. Note what comes back."),
    ("Coming next:", "Chapter 7 — negative messages: when the answer is no and the reader's day is about to get worse."),
], D, nxt())
notes(s, "Delivery-neutral closing.")

out = os.path.join(os.path.dirname(__file__), "..", "ch06-positive-and-neutral-messages.pptx")
prs.save(out)
print("Saved", os.path.abspath(out), "slides:", i)
