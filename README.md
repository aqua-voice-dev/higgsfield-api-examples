# Higgsfield API examples

*Unofficial community examples for Higgsfield API. Not affiliated with Higgsfield. All trademarks belong to their owners.*

Small, self-contained examples for working with the Higgsfield API and its CLI. The public pages document the CLI commands and the per-model prices but not the raw HTTP endpoints, so these examples cover exactly that: setting up the CLI for an agent, estimating cost before you run a job, and a prompt you can paste into Claude Code. For the request format itself, read docs.higgsfield.ai after creating a key.

> Need generation in a backend rather than in an agent? [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=higgsfield-api-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
| --- | --- |
| `examples/setup.sh` | Installs the CLI, signs in, adds the skills package; the three commands from the CLI page. |
| `examples/cost_estimate.py` | Estimates the cost of a video or image job from the prices shown on the Explore page. |
| `examples/agent_prompt.md` | The prompt from the CLI page that sets up Higgsfield inside Claude Code, plus follow-up prompts. |

## Setup

The CLI is a Node package, so you need `node` and `npm` on the path. Sign-in happens in a browser window opened by `higgsfield auth login`, which means the setup script is meant for a laptop, not a headless server. For server code, create a key on the [API keys page](https://open.higgsfield.ai/api-keys) and export it:

```bash
export HIGGSFIELD_API_KEY=YOUR_KEY_HERE
```

None of the examples print or store the key.

## examples/setup.sh

Runs `npm i -g @higgsfield/cli`, then `higgsfield auth login`, then `npx skills add higgsfield-ai/skills`. Each step is guarded so the script stops on the first failure. The CLI source is at github.com/higgsfield-ai/cli if you want to read what the login step does before running it.

## examples/cost_estimate.py

The Explore page lists a discounted and a list price per model. The script hard-codes the numbers that were displayed at the time of the snapshot (Seedance 2.5 at 0.144 / s discounted and 0.2057 / s list, Kling 3.0 4K at 0.042 / s and 0.084 / s, Genjutsu Motion Transfer at 0.159 / s and 0.318 / s, Cinema Studio 4.0 at 0.2057 / s, Marketing Studio Image at 0.0121 and 0.0162 per image) and prints both totals for a given duration or image count. The currency is not labelled on the card, so the script prints bare numbers. Update the table when the pricing page changes.

```bash
python3 examples/cost_estimate.py seedance-2.5 30
python3 examples/cost_estimate.py marketing-studio-image 200
```

## examples/agent_prompt.md

The CLI page provides a prompt to paste into Claude Code that walks the agent through install, login and skills. The file reproduces it and adds two follow-up prompts that map to the skill groups the page lists (UGC factory, Marketing). Nothing in it assumes an endpoint; the agent uses the CLI.

## When to use Synexa instead

These examples are about the agent and CLI route because that is what Higgsfield documents publicly. If what you actually need is a plain HTTP call from a worker process, with a Python SDK, a single endpoint for image, video and audio models, and a bill that is per run instead of per second, that is what [Synexa](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=higgsfield-api-examples&utm_content=readme-top&utm_term=tier-r) does. Keep Higgsfield for the models only it hosts; use Synexa for the boring generation jobs in your pipeline.

[Try Synexa - one API for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=higgsfield-api-examples&utm_content=readme-top&utm_term=tier-r)
