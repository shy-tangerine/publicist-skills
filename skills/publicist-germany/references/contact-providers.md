# Contact providers for Germany

Read this file only after verifying the journalist, outlet, beat, and recent work from editorial sources.

## Primary route: news aktuell zimpel

[zimpel](https://www.newsaktuell.de/zimpel/) is a German PR and media-contact database maintained by news aktuell. It covers journalists, editorial desks, blogs, podcasts, and influencers; its research team says it continuously verifies and updates records. Users can search by topic, region, and media type, build press lists, send personalized HTML mailings, and review delivery and open metrics.

Use it when the user's subscription exposes the required records and functions:

1. Search only after defining the story and target beat.
2. Verify the current role and recent coverage on the outlet's own site; a zimpel record is structured discovery evidence, not proof of story fit.
3. Record `provider=zimpel`, query date, filters, record type, and the contact route returned.
4. Prefer a named editorial route or shared desk address appropriate to the topic over a guessed personal address.
5. Treat zimpel's mailing function as an external action: present the exact list and copy before sending.

The [zimpel FAQ](https://www.newsaktuell.de/faq/mediendatenbank-zimpel/) describes daily maintenance, list building, sending, delivery data, and shared editorial inboxes. The [zimpel terms](https://www.newsaktuell.de/agb/zimpel/) make access and permitted functions depend on the signed license; they also distinguish zimpel system data from customer-maintained records.

## Published editorial routes

Check the author page, masthead, `Impressum`, newsroom directory, editorial desk, tip page, and contact form first. Preserve the URL and stated purpose. Under the Germany workflow, finding an address does not itself make unsolicited advertising email permissible.

## Secondary enrichment

Hunter, Clay, and Apollo are not German media databases. Use them only as a fallback for a known, already-qualified person where the user's policy and the Germany legal gate permit the lookup. Label returned data `provider-supplied` or `inferred`; technical verification is not consent or editorial relevance.

## Minimum output

Return name, outlet, beat, fit evidence, route, provenance (`published`, `zimpel`, `provider-supplied`, or `inferred`), verification date, and next step. Use `UNRESOLVED` when evidence is missing.

Optional background: [localized media-contact infrastructure](https://github.com/shy-tangerine/publicist-skills/blob/main/wiki/public-relations/localized-media-contact-infrastructure.md). The installed guidance above is sufficient for the workflow.

### zimpel licensed-data retention

Current zimpel terms impose stricter handling than a normal reusable contact list. System data generally may not be transferred to third parties without prior written permission. An export used outside zimpel is limited to one use within at most **2 days after export**; permanent external storage of zimpel system data is not permitted. Do not copy licensed zimpel contacts into a durable Publicist dossier.

Bloggers and other social-media influencers are a separate case: zimpel's terms require the customer to obtain the recipient's own prior consent for press-material email, and those email addresses are not included in export. Press-material mailings must include an opt-out; suppress future contact when the recipient objects.

