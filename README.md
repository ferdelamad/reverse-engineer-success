# reverse-engineer-success

A Claude Code skill that works out how a person or company actually succeeds, using public evidence, and tells you whether a similar path is worth pursuing for you.

Give it an X profile or post. You get:

- **A Markdown report** with the full research and an evidence log
- **A shareable page** with the blueprint and every source link, published as a Claude artifact when that's available

## Why it exists

A viral post is a claim, and the headline often isn't the real business. The useful detail tends to be in replies, later caveats, store listings, sitemaps, public stats and the failures of people who tried the same thing. This skill runs that process consistently, and labels every claim by how well it's supported.

## What's in the report

1. What the business really is
2. Step-by-step blueprint
3. Key numbers
4. What to copy and what to avoid
5. Risks and what would change this view
6. Opportunity assessment, tailored to your goal and situation
7. Unknowns
8. Sources

Claims are labeled **Confirmed**, **Self-reported**, **Estimate**, **Secondary**, **Inferred** or **Unknown**.

## Install

```bash
git clone https://github.com/ferdelamad/reverse-engineer-success.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/reverse-engineer-success/skills/reverse-engineer-success" ~/.claude/skills/reverse-engineer-success
```

Then start a new Claude Code session.

## Usage

```text
/reverse-engineer-success https://x.com/<handle>/status/<id>
```

Or just ask:

```text
This founder says SEO got them to $10k MRR. Is it real, and could I do something similar?
```

It asks a few questions about your goal and resources first, so the verdict fits you. A full run takes a while and uses a lot of tokens.

## What works best

It uses whatever you have and tells you what it couldn't check.

| Tool | What it adds |
|---|---|
| Browser access with your X login | Reads replies, timelines and charts. This makes the biggest difference |
| A web research tool or MCP server | Broader, faster research |
| Ahrefs, Semrush or DataForSEO | Traffic and keyword data |
| Python 3 | Runs the bundled scripts, with no packages to install |

Without X access, results are weaker, because replies and follow-ups are where much of the evidence sits.

## Limits

- **It can't see private data.** Private revenue and unnamed products stay Unknown.
- **Survivorship bias.** It starts from someone who looks successful. It searches for failures to offset this, but can't fully remove it.
- **It works best on public footprints.** Founders and developers leave more evidence than people whose work is private.
- **It isn't advice.** Self-reported numbers aren't audited, and the report isn't financial or legal advice.

## Responsible use

The skill is for studying public business activity. It collects business information only, stops on private individuals, records blocked sites as gaps instead of working around them, and doesn't submit forms without approval. Please keep reports fair, and check claims about real people before sharing them.

Follow the terms of the sites and tools you use.

## License

[MIT](LICENSE)
