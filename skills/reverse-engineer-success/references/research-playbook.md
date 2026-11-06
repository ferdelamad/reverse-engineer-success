# Research playbook

How to research each stage, in order of how much the evidence is worth. Skip anything that doesn't apply to the target's field.

## Tools

Use the strongest available option for each job, and record in the report what you couldn't reach.

| Job | Best | Fallback |
|---|---|---|
| Read X | Browser with the user's login | Public mirror such as `https://api.fxtwitter.com/<handle>/status/<id>`, then web search |
| Broad web research | A web research agent, if one is connected | Several targeted web searches and page fetches |
| Business data | Paid tools the user has connected (Ahrefs, Semrush, DataForSEO) | Public pages and the bundled scripts |
| Blocked sites | Another source | Record the gap |

### Reading X

- Timelines render client-side. Page text extraction may return only the first post. An accessibility tree shows the whole timeline with text cut short, so use it to find post IDs, then open each post to read it in full.
- Screenshots are the only way to read charts and dashboards attached to posts. Open `<post URL>/photo/1`.
- A long post may be an X Article at `x.com/<handle>/article/<id>`.

Useful searches:

```text
conversation_id:<post id> from:<handle>     their replies under a post
from:<handle> (MRR OR revenue OR customers) min_faves:30
from:<handle> (launched OR shipped OR "new app" OR sold)
from:<handle> filter:links                  posts with product links
from:<handle> (failed OR mistake OR deindexed OR churn OR "didn't work")
from:<handle> since:YYYY-MM-DD until:YYYY-MM-DD
```

Sort by Top for what spread, and by Latest for caveats.

## Finding the claims

Priority order:

1. **Their replies under the main post.** People ask how it works, and answers name tools, channels and models.
2. **Later follow-ups.** Corrections often arrive days later, with less reach.
3. **Long posts, articles and interviews.** Methods are often spelled out here.
4. **Regular updates.** Monthly numbers show the trend beyond a single chart.
5. **Earlier posts.** They show how the story changed.

Read attached images. Check the axis, the time window and any prior-period line, which can show more than the caption does.

Also note who endorses the post and why. An endorser who sells related tools has an incentive to promote it.

## Tracing ownership

The aim is to tie claims to products without guessing. Follow the chain until it stops:

1. **Their own links:** posts with store links, domains or demos are the strongest evidence.
2. **Store publishers:** look up an app with `https://itunes.apple.com/lookup?id=<track id>`, then pull the catalogue with `ios_catalog.py <artist id>`. Google Play package names often reveal the developer prefix.
3. **Company sites:** portfolio pages, footers, and privacy and terms pages often name the entity and list other products.
4. **Developer records:** GitHub profiles and organizations, npm, PyPI, pub.dev and similar registries.
5. **Public directories:** Product Hunt, Indie Hackers, verified revenue listings, Crunchbase, interviews and podcasts.

**Labeling:** the subject's own link or statement is Confirmed. Matching names or categories alone are Inferred. If products stay unnamed, record Unknown and move on. A founder's silence on product names is common, and more digging tends to reach personal data rather than better evidence.

## Measuring what's live

Look for first-party numbers before estimates:

- **Public stats:** developer tools sometimes publish `/stats`, `/open`, or a JSON endpoint. Check the page's source or text for an API link. These can include traffic, sign-ups and usage.
- **Registries:** npm download history, including the period before launch, since a reused package name can inflate totals. GitHub stars and forks are interest, not users.
- **Stores:** Play install bands, ratings and recent reviews. App Store ratings from the lookup API cover one country.
- **Sitemaps:** show page volume and what's being built.
- **Pricing pages:** show the real business model.
- **Third-party estimates:** use Similarweb, Ahrefs or Semrush if reachable, and label them Estimate.

### Reading the output

- Blog URL counts can include pagination.
- `lastmod` means last modified, not published. A spike can be a bulk edit.
- A missing payment signal doesn't prove a provider isn't used.
- First-party analytics can undercount, especially for developer audiences that block trackers.
- Download and install numbers include updates, repeat installs and CI.
- If a number's time window isn't stated, infer it from the data and label the window as Inferred.

### Calibrating the claim

Pair numbers to find what they imply: users to subscribers, traffic to revenue, or total revenue divided by products. A single paired ratio often says more than a headline number. Where you can, do this arithmetic explicitly and show it.

Label any scenario math with its assumptions: what it would take to reach a given revenue at the current price and sign-up rate.

## Outside evidence

Search for:

- **Competitors:** free and paid, with real pricing. Check how much of the product is already free or open source.
- **Failures:** "I tried X and failed", "0 traffic", "shut down", and forum threads in the relevant community. Vendor data can be useful when it admits losses.
- **Base rates:** independent datasets on typical outcomes in the field.
- **Platform risk:** the rules of whoever controls distribution, from primary sources: search engines, app stores, social platforms and payment processors.
- **Structural shifts:** changes in technology or regulation that weaken the model.

Keep a note of which sources you read in full and which you know only by title. Use only the former as evidence.

Some communities block automated tools. If so, say so in the report and suggest the user read those threads by hand.

## Judging the opportunity

Assess the reader's version, not the subject's business. Cover:

- **Demand:** evidence people pay for this, and how they find it.
- **Competition:** who already does it, and what's free.
- **Economics:** rough unit economics, using real prices and labeled assumptions.
- **Moat:** what the subject has that doesn't transfer, and what the reader has that the subject doesn't.
- **Fit:** the reader's goal. A weak business can still be a good learning project, and that deserves a separate answer from whether it would make money.
- **Angle:** the most promising narrower or different version, if there is one.
- **Smallest test:** the cheapest way to find out, with a pass mark, before building much.

Choose one verdict: **Pursue**, **Pursue a narrower version**, **Learning project only**, or **Skip**. Give the reasoning, the strongest counterargument and what would change your mind.

If the evidence supports a clear no, say so plainly and offer the most useful alternative.
