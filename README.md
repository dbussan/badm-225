# Business Communication — Homework, Practice & Quizzes (Chapters 1–14)

A single-file website (`index.html`) with **224 original multiple-choice questions** (16 per chapter),
**28 writing prompts** with model guidance, and three modes per chapter:

| Mode | What it does |
|---|---|
| **Practice** | Instant feedback with one-line explanations; writing prompts with model guidance. |
| **Homework (graded)** | All 16 questions, no feedback until submit; generates a tamper-evident **completion code** the student pastes into your LMS. |
| **Quiz (timed)** | 10 random questions, 12 minutes, auto-submits at zero; also generates a completion code. A **Comprehensive Quiz** (20 questions, 25 minutes, all chapters) is in the sidebar. |

All content is original material written for this course. The site is not affiliated with,
and does not reproduce content from, any textbook or publisher.

---

## Host it free on GitHub Pages (about 3 minutes)

1. Go to **github.com** and sign in (or create a free account).
2. Click **New repository** → name it something like `bcomm-practice` → set it to **Public** → **Create repository**.
3. On the new repo page, click **“uploading an existing file”**, drag in `index.html`, and click **Commit changes**.
4. Go to **Settings → Pages** (left sidebar). Under **Branch**, choose `main` and folder `/ (root)`, then **Save**.
5. Wait ~1 minute. Your site is live at:
   `https://YOUR-USERNAME.github.io/bcomm-practice/`
   Share that link with students (or link it inside your LMS).

To update the site later, upload a new `index.html` over the old one (Add file → Upload → Commit).

---

## BEFORE you deploy: change the secret

Open `index.html` in any text editor, find this line near the top of the `<script>` section:

```js
const SECRET='CHANGE-ME-BEFORE-DEPLOY-2026';
```

Change it to any private phrase. Completion codes are only verifiable against the same secret,
which prevents students from generating valid codes on an unmodified copy of the file.

---

## Grading workflow (how you see scores)

1. In your LMS (Blackboard, Canvas, etc.), create one **text-entry assignment** per homework or quiz
   (e.g., “Ch. 7 Homework — paste your completion code”).
2. Students complete the work on the site and paste the code (looks like `BC2-…-a1b2c3d4`).
3. You open the site’s **Instructor Tools** (sidebar), paste one or many codes, and click **Verify**.
   Each valid code decodes to: type (HW/QZ), chapter, **score**, student **name and ID**, date, and time-on-task.
   Any altered code shows **INVALID**.

## FERPA notes

- The site is **fully static**: no server, no database, no cookies, no analytics, no transmission.
  Names, IDs, answers, and scores exist only in the student’s own browser and vanish on reload.
- Grades enter your records **only** through your LMS assignment — i.e., education records stay
  inside your institution’s FERPA-covered systems. GitHub never holds student data.
- Recommend students enter their **university ID** (never an SSN or personal data).

## Honest integrity limits

Completion codes are **tamper-evident** (any edit invalidates them), but this is a client-side tool,
not a proctored platform — a determined student could read the page source. It is appropriate for
low-stakes homework and practice quizzes. Run high-stakes exams inside your LMS.
