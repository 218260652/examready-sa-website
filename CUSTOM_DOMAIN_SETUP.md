# ExamReady SA custom-domain deployment checklist

Domain: `examready-sa.com`
GitHub Pages repository: `218260652/examready-sa-website`

**Do not merge or activate until domain ownership is confirmed.** This preparation branch is not the live site.

## Registrar / DNS provider setup (account owner required)

1. Register and pay for `examready-sa.com` with Axxess (if not already done).
2. Use one DNS provider. If choosing Cloudflare Free, first add the registered domain to Cloudflare and then enter **the actual Cloudflare nameservers assigned to this domain** at Axxess; do not use sample nameserver placeholders.
3. At the authoritative DNS provider, set four A records for host `@`:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
4. Set a CNAME record `www` -> `218260652.github.io` (not the path or repository name).
5. Preserve any existing required mail DNS records; avoid wildcard DNS.
6. Verify domain ownership in GitHub if possible, then activate the apex custom domain on the repository's **Settings > Pages > Custom domain**. On branch-based publishing, a root `CNAME` file is used; on GitHub Actions publishing, the Pages setting must be used because a repository `CNAME` is ignored.
7. Wait for DNS and GitHub HTTPS certificate provisioning; enable **Enforce HTTPS** when available.
8. Test `https://examready-sa.com/`, `https://www.examready-sa.com/`, the APK download button, and existing app update URLs. Do not assume the Android app's API/update location changes when the website domain changes.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
