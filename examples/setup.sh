#!/usr/bin/env bash
# Install the Higgsfield CLI, sign in, and add the skills package.
# The three commands are the ones shown on higgsfield.ai/cli.
# Sign-in opens a browser, so run this on a machine with a display.
set -euo pipefail

if ! command -v npm >/dev/null 2>&1; then
  echo 'npm not found; install Node.js first' >&2
  exit 1
fi

echo '1/3 installing @higgsfield/cli'
npm i -g @higgsfield/cli

echo '2/3 signing in (a browser window will open)'
higgsfield auth login

echo '3/3 adding the skills package'
npx skills add higgsfield-ai/skills

echo 'done. Try asking your agent to generate an image or video.'
