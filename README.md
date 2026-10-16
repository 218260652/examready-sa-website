# ExamReady SA Android downloads

This repository serves the verified ExamReady SA APK through GitHub Pages:
https://218260652.github.io/examready-sa-website/

## Release v1.2.4

The app contains 9,340 original practice records across 11 subjects. Accounting, Business Studies and Economics each have 500 records for each of Grades 10, 11 and 12 (4,500 additional records). Each new grade-subject pool revisits 20 skill families through 25 numeric or contextual variants. They are not official DBE exam questions, independently educator-moderated content or a complete CAPS course.

Release verification evidence is stored beside the APK in `downloads/ExamReadySA-v1.2.4-verification.json`. The permanent signing certificate SHA-256 is `dd4c342fcfa66ac2d9b7b37c1a4cd55d4c998be78dbe2479489b031d6fe38dc2`.

## Preserve progress

Install the new APK over production-signed v1.2.2 or v1.2.3. Do not uninstall first. Release checks must verify real in-place upgrades preserve existing scores, question coverage, topic totals and history. All 4,840 previous question IDs, prompts, options and answer indices remain intact.

Pre-v1.2.2 test APKs use a different debug certificate and cannot upgrade in place to the permanent certificate. Uninstalling those old builds may erase local progress. Do not tell these users that progress preservation is guaranteed.

## Publishing order

1. Build, test, sign with the permanent key, and verify the package, version and signature in the private Android repository.
2. Complete signed offline smoke tests and progress-preserving upgrades from both production baselines.
3. Upload the verified APK and verification report here.
4. Confirm GitHub Pages serves the exact APK bytes and checksum.
5. Only then update `updates/latest.json`, `updates/android.json` and this download page.
6. Confirm the live page and update policies reflect the published release.

Keep `minimumSupportedVersionCode` at 1 so updates remain optional and offline learners are not stranded. Never raise the minimum before a compatible signed update is live and tested. The app reads `https://218260652.github.io/examready-sa-website/updates/android.json`; pre-v1.2.2 builds may use a former update URL.

The single download page loads `updates/latest.json`, validates its fields, and checks the APK is present with the expected file size before enabling its download button. No advertising credentials, signing keys or learner progress belong in this repository.
