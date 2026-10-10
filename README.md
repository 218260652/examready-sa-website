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

## v1.2.2 release status

Public v1.2.2 (version code 10) is now live on GitHub Pages after the release workflow checked its SHA-256 checksum, Android signing certificate, package name and version:

- APK: `downloads/ExamReadySA-v1.2.2.apk`
- File SHA-256: `e5a846ae56df82b7ed5bd4ce12e593c81be6c39cf49377ada32126563469c226`
- Release signing certificate SHA-256: `dd4c342fcfa66ac2d9b7b37c1a4cd55d4c998be78dbe2479489b031d6fe38dc2`
- Latest metadata: `updates/latest.json` and `updates/android.json` report version 1.2.2, minimum 1 (optional updates).

**Migration warning:** Old v1.2.1 and earlier debug-signed APKs cannot upgrade in place to v1.2.2 due to the different signing certificate. Uninstalling these older versions may erase quiz progress. The owner approved the one-time reinstall for migration. Future updates must use the same production release key to support in-place updates.

The production signing workflow is in the private Android repo at `.github/workflows/signed-release.yml`. Configuring its two GitHub Actions signing secrets and running a signed build on GitHub are **separate pending tasks** and must not be confused with this independently verified public v1.2.2 APK. Never add private key or password to a commit.

The old ChatGPT Sites update URL used by pre-v1.2.2 APKs cannot be remotely redirected; only installations of v1.2.2 or higher query the new GitHub Pages policy.
