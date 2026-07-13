/* ============================================================
   BADM 225 — shared course configuration
   Loaded by BOTH index.html (practice/homework/quiz) and exam.html
   (midterm/final) via <script src="config.js"></script>. Edit THIS
   ONE FILE to change the secret or update sections — no need to
   touch index.html or exam.html directly, and no risk of the two
   files' lists drifting out of sync with each other.
   ============================================================ */

/* INSTRUCTOR: change this to any private phrase before sharing the site.
   Completion codes are only verifiable against this same secret in the
   Instructor Tools panel. Changing it invalidates any codes already
   issued under the old secret, so pick it once per term and leave it. */
const SECRET='xC5HdRKpNu3k33MMQunh8YLZ';

/* INSTRUCTOR: list every course/section you're currently teaching here —
   any number of entries, across any number of institutions. Students pick
   from this list instead of typing it, so the gradebook can never fragment
   from typos or inconsistent formatting ("Sec 1" vs "1" vs "Section 1").

   Suggested format, one string per section:
     "SCHOOL · COURSE · TERM · CRN 12345 · Section 001"

   To add a course or section: add another quoted string below (comma
   after each one except the last), save, and redeploy. To retire a past
   term's section, just delete its line — completion codes and gradebook
   rows already recorded for it are unaffected either way. */
const SECTIONS=[
  'UND · BADM 225 · Fall 2026 · CRN ????? · Section 001',
  'KYSU · BADM 225 · Fall 2026 · CRN ????? · Section 001',
];

/* INSTRUCTOR: passcode for Instructor Tools (the gradebook, in index.html) and the
   exam-link builder (in exam.html, when visited with no link parameters). Change it
   to anything you like. This is a light deterrent for a shared or public computer —
   like SECRET above, it lives in this file's plain text, so it stops casual clicking,
   not someone who reads the page source. Unlocking is remembered only for the current
   browser tab session (it clears when the tab/browser closes). */
const INSTRUCTOR_PASSCODE='badm225-instructor';
