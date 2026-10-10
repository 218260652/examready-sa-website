# ExamReady SA – Android update downloads

This public GitHub Pages repository serves **one purpose**: downloading the latest ExamReady SA Android APK.

Current address: https://218260652.github.io/examready-sa-website/

## How releases work

- \`index.html\` shows a single download button.
- \`updates/latest.json\` declares the current version and file name.
- The APK must be uploaded as \`downloads/ExamReadySA-v1.2.1.apk\` (the exact path in the manifest) **before** the button becomes enabled. The page checks the file with a same-origin HEAD request, avoiding dead download links.
- \`updates/android.json\` is a schema-compatible update-policy example for the Android app. **Important:** the existing installed Android app currently fetches its policy from **examready-sa.ramashiaemily.chatgpt.site**, NOT this GitHub Pages URL. Updating this file does not change existing installed APKs.

## Uploading the current APK

The verified Android debug APK has SHA-256:
\`f2f7de0c8cdc0401c134a5e75b7b120b1fde076fbb47eec9da2817e6741fe538\`

1. Download the tested \`ExamReadySA-1.2.1-WhatsApp-Group.apk\` provided in the ChatGPT conversation.
2. Rename the file to \`ExamReadySA-v1.2.1.apk\`.
3. Upload it into the \`downloads/\` folder of this repository on the \`main\` branch. GitHub web uploads allow this size. Do not upload it to the private Android repository.
4. Wait for GitHub Pages to publish the latest commit; reload the website. The button activates when the file becomes available.
5. Verify the downloaded APK SHA-256 against the value above.

## Future updates

For each new version:
1. Build and test the APK first.
2. Sign it with the **same stable signing key** as previously distributed builds so Android installs can update in place and preserve progress. Debug keys are not suitable for durable public production updates.
3. Upload the new APK to \`downloads/\`.
4. Update \`updates/latest.json\` with the new version name, code, file name, size and SHA-256 in the same commit or after uploading.
5. Do **not** increase the minimum-supported version until the download is live, tested and consistently signed. Do not publish forced-update instructions that strand users.

The original ChatGPT Sites URL and app update checker are separate; migrating the existing Android update-check URL requires an Android app code change and a new APK. This site intentionally has no promotional content, analytics, external scripts or optional study-group links.

## v1.2.2 migration status

The Android v1.2.2 source now points its update checker and update button to this GitHub Pages download website. The new debug APK built and passed emulator testing.

**Hold public release:** On 10 October 2026, a certificate comparison confirmed that the installed v1.2.1 testing APK and newly built v1.2.2 testing APK have different signing certificates. Android will refuse to install the latter over the former. Uninstalling the old APK can erase locally saved learner progress.

The public download and update manifest must stay at v1.2.1 until the signing and migration plan is settled. No automated v1.2.2 publishing workflow is enabled. Do not raise latestVersionCode or minimumSupportedVersionCode prematurely.

Use a securely stored permanent signing key for future releases, and test upgrading between two consecutive production-signed builds before promising update-in-place support.
