# Custom Domain And Email Setup

This repo is ready for a custom domain, but the final switch still needs a
domain you control and access to its DNS records.

## Recommended end state

- Website: `https://www.andrewbalmer.bio/` or `https://andrewbalmer.bio/`
- Professional email alias: `hello@andrewbalmer.bio` or `andrew@andrewbalmer.bio`
- GitHub Pages remains the publishing target

## Repo settings to change when a domain is chosen

1. Update `_config.yml`
2. Set `url` to the full custom-domain URL
3. Set `baseurl` to `""`
4. Set `custom_domain` to the bare domain or full URL
5. Add a `CNAME` file at the repo root containing the chosen hostname

## DNS checklist

- Point the chosen hostname at GitHub Pages using the records recommended in
  GitHub Pages settings
- Enable HTTPS once the certificate is issued
- Keep `www` and apex-domain behaviour explicit so there is one canonical URL

## Email routing checklist

- Keep mailbox hosting separate from the website
- Create forwarding aliases for public-facing contact addresses
- Route the alias to the inbox you actually monitor
- Add SPF, DKIM, and DMARC records once the email-routing provider is chosen

## Suggested launch sequence

1. Buy the domain
2. Add DNS records for GitHub Pages
3. Update `_config.yml`
4. Add `CNAME`
5. Push and verify HTTPS
6. Add forwarding aliases
7. Replace `ab69@sanger.ac.uk` with the new public-facing alias where desired
