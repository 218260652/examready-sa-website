# ExamReady SA Android downloads

This repository serves the verified ExamReady SA APK through GitHub Pages:
https://218260652.github.io/examready-sa-website/

## Release v1.2.6

The app provides 9,340 original practice records across 11 South African school subjects. v1.2.6 improves the optional Study tools pilot: tutor answers are organized into clear explanations and source-page references; quizzes present one question at a time with separate answer submission, explanations and a final review; flashcards use a designed flip-card view with optional Cloudflare-generated illustrations.

Study tools require internet. When a learner chooses a PDF, DOCX or TXT file, its text is sent to the staging AI service to generate study material. Cloudflare receives only a short image prompt when an illustration is requested. Do not upload sensitive documents. Exam practice and saved progress stay on the device and continue to work offline.

The release verification report is stored beside the APK at `downloads/ExamReadySA-v1.2.6-verification.json`. The APK SHA-256 is `03764b25cfe82a44ba1e45bc1673c359bb992d088dd40c7bc4df223e2655bb37`. Its permanent signing certificate SHA-256 is `dd4c342fcfa66ac2d9b7b37c1a4cd55d4c998be78dbe2479489b031d6fe38dc2`.

Practice coverage includes Mathematics, Mathematical Literacy, Life Sciences, Physical Sciences, History, Agricultural Sciences, Geography, English First Additional Language, Accounting, Business Studies and Economics. Each of the three commerce subjects has 500 original practice records for Grades 10, 11 and 12. Records are practice material, not official DBE questions or a complete CAPS course.

## Preserve progress

Install over production-signed v1.2.2, v1.2.3, v1.2.4 or v1.2.5. Do not uninstall first. Release checks verified in-place upgrades and preserved scores, question coverage, topic totals and history. The original 4,840 question IDs, prompts, options and answer indices remain intact.

Pre-v1.2.2 test APKs use a different debug certificate and cannot upgrade in place to the permanent certificate. Uninstalling those old builds may erase local progress. Do not tell these users that progress preservation is guaranteed.

## Publishing order

1. Build, test, sign with the permanent key, and verify the package, version and signature in the private Android repository.
2. Complete signed offline smoke tests and progress-preserving upgrades.
3. Upload the verified APK and version-specific verification report here.
4. Confirm GitHub Pages serves the exact APK bytes and checksum.
5. Update `updates/latest.json`, `updates/android.json` and this download page.
6. Confirm the live page and update policy reflect the release.

Keep `minimumSupportedVersionCode` at 1 so updates remain optional and offline learners are not stranded. The app reads `https://218260652.github.io/examready-sa-website/updates/android.json`. The download page validates the release metadata and APK size before enabling its download button. Never commit signing keys, API credentials or learner progress to this repository.
