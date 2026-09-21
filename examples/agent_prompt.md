# Setting up Higgsfield inside Claude Code

The CLI page (higgsfield.ai/cli) gives a prompt you paste into Claude Code.
Reproduced here so it lives next to the other examples.

## Step 1: paste this into Claude Code

```
Set up Higgsfield for me so I can generate images and videos from here.
1. Install the CLI: run `npm i -g @higgsfield/cli`.
2. Authenticate: run `higgsfield auth login` and complete the sign-in in the browser it opens.
3. Install the companion skills: run `npx skills add higgsfield-ai/skills`.
Once that's done, let me know when it's ready.
```

## Step 2: finish the browser sign-in

The agent will pause at step 2 until you complete the login in the browser.

## Step 3: ask for something

Two follow-up prompts that map to skill groups listed on the page:

```
Using the Higgsfield UGC factory skill, make a 15-second 9:16 product video
for the attached product photo. Casual piece-to-camera delivery, short CTA.
```

```
Using the Higgsfield Marketing skill, generate three campaign images for a
spring sale banner, 16:9, same product in each.
```

Every run is billed to the account you signed in with; check the usage page
on open.higgsfield.ai after the first few jobs.
