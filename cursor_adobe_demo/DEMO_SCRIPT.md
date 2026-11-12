# Cursor ADM Adobe: interview cheat sheet

## Opening (30 seconds)
"Given your monorepos and the need for consistent, high-quality engineering, let's take a small but representative export pipeline bug and work from understanding the code through to a reviewed fix. I'll show how I choose context and model and where an engineer retains control. It's a toy example, not a Photoshop simulation."

## Before starting
1. Install Cursor and Python 3.10+; open `creative-export-demo` as the workspace.
2. Open a terminal and run `python -m unittest discover -s tests -v` (baseline passes).
3. Run `python -m creative_export.cli sample_assets demo_output`; inspect the two identical output paths.
4. Verify Cursor's current Ask, Plan, Agent, and optionally Debug modes, active model, project rule and agent terminal approvals.
5. Ensure the workspace is locally indexed. Never paste confidential Adobe code into a personal demo.
6. Initialize Git and commit the unmodified starting files. This makes resetting easier.

## 0:00–1:15 Explore (Ask)
Prompt: "Read the project as a new engineer. Trace how an .asset input becomes an exported preview and manifest entry. Which files are responsible for destination paths? Explain why campaign/hero.asset and social/hero.asset collide. Cite specific functions. Do not edit anything."
Value: understand unfamiliar multi-file dependencies. Context: show the files Cursor selected and explicitly add pipeline.py and manifest.py if necessary.

## 1:15–2:45 Plan
Prompt: "Plan the smallest safe change to prevent output collisions when nested source folders contain the same basename. Preserve relative folder structure, the CLI and manifest format. Include tests for both contents, unique manifest outputs, nested directory creation and existing flat-file behavior. Point out edge cases and tradeoffs. Do not implement yet."
Value: architecture decisions before code. Interrogate the plan: should the export path be derived from a trusted source-relative Path?

## 2:45–5:15 Implement (Agent)
Prompt: "Implement the approved plan. Keep changes limited to what is needed. Follow repository rules, add a regression test and run the full unittest suite. Report modified files and any limitations."
Value: orchestrated multi-file edits + terminal execution. Show model choice: Auto for routine task or a consciously selected reasoning model for nuanced architecture; avoid guarantees about comparative performance.

## 5:15–6:15 Test & debug
Show tests ran and inspect the resulting distinct destinations. If something fails, ask Agent to diagnose test output. Use Debug mode only if runtime evidence is genuinely useful rather than forcing a fake Debug demo.

## 6:15–7:30 Review
Open the agent diff and ask: "Summarize behavior changes, possible regressions, and remaining risks. Do not modify code." Show acceptance/rejection, checkpoint options and Git for durable history.

## 7:30–8:00 Close
"We moved from unfamiliar code to a tested, reviewed change in one environment. For Adobe, the next question isn't whether this toy issue works, but whether these workflows consistently improve outcomes on real repos under your security and code-review standards. Which team would make a sensible controlled evaluation?"

## Important limitations
- This is a simple sample, not evidence about the performance of codebase indexing on Adobe-sized monorepos.
- Cursor doesn't guarantee error-free code; tests and human review remain important.
- Ask, Plan, Agent, tests and diff review are not exclusive to Cursor.
- Security posture requires evaluation of model routing, data processing, Privacy Mode, agent execution permissions and enterprise controls.

## Useful test questions
- What would you change in the plan before it touches production?
- When does codebase context become too broad and noisy?
- What do you need to see before trusting an agent-generated PR?
- Where would Cursor need to outperform your current tools to justify broader adoption?
