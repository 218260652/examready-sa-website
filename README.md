# ExamReady SA — Official website source

A responsive, **static** landing page for the ExamReady SA educational Android app. It is independent of the original ChatGPT Sites deployment and does **not** contain the Android app source.

## What is included
- Single accessible HTML file with embedded CSS and small navigation script; no frameworks or third-party assets.
- Subjects and evidence-based feature descriptions for Grades 10–12.
- Optional WhatsApp study-group link with a phone-number visibility warning.
- Links to the original site and privacy page.
- Honest download status: the APK is not yet on permanent public hosting. **Do not** advertise the old ChatGPT session link as a reliable public download.

## Publish for free on GitHub Pages

**This repository is the public website-only project.** The Android source remains private in `218260652/examready-sa`.

1. Open this repository → **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, and press **Save**.
3. When published, the default URL should be `https://218260652.github.io/examready-sa-website/`. Verify it loads before publicising.
4. When you purchase your domain, configure **Custom domain** in Settings → Pages and DNS with your domain registrar. For `www.yourdomain.co.za`, the CNAME target will be `218260652.github.io`. Do not add a CNAME file until you own the domain.

## Updating APK downloads safely

The app is currently a debug-signed prototype, and GitHub Actions artifacts require access and expire. Do not use an expiring build artifact or a private-repository link as the public APK URL. When the owner has a reviewed, properly signed release APK, publish a stable file (for example via a public GitHub Release or approved host), verify its URL, and **then** replace the button in the download section.

## Future changes

- Keep site content and Android source separately.
- Remove the existing-site fallback link only after public APK hosting works.
- Check WhatsApp invite validity periodically; link is owner-supplied.
- The static site does not collect personal data, use analytics or serve ads.
- Preserve accessible mobile navigation and reduced-motion support.

## Android app source

Android app is in the **private** repository \`218260652/examready-sa\`. This public website repository is a standalone presentation, not a GitHub deployment of the existing ChatGPT Sites project.
