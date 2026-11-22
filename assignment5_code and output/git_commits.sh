#!/bin/bash
# Creates the repo history with one commit per task. Edit user.name/user.email first.
git init -b main
git config user.name  "Your Name"
git config user.email "you@example.com"
git add .gitignore requirements.txt README.md && git commit -m "chore: add README, requirements and gitignore"
git add Task_A1 && git commit -m "A1: add SQLite schema and CSV vs SQL timing"
git add Task_A4 && git commit -m "A4: measure print vs logging overhead"
git add Task_B1/complete_code.py Task_B1/output_complete_code.txt && git commit -m "B1: complete TODOs, add >999 check"
git add Task_B1/cleaning_pipeline.py Task_B1/output_cleaning_pipeline.txt && git commit -m "B1: cleaning pipeline with before/after output"
git add Task_B1 && git commit -m "B1: SQLite load, queries, charts and pandas comparison"
git add Task_B2 && git commit -m "B2: adversarial inputs, parameterised SQL, executemany timing"
git add Task_B3 && git commit -m "B3: compare loops, pandas, SQL and running sum; profile"
git add Task_B4 && git commit -m "B4: sentiment scorer, summariser, agreement test and index"
git tag -a v1.0 -m "Assignment 5 submission"
git log --oneline
