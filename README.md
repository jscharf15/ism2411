# ISM2411 — Python for Business

**Name:** Jonathan Scharf

**Semester:** Fall 2026

**Instructor:** Dr. Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, final_price

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
```

## Reflection
**1.**

```
521fe57 (HEAD -> main, origin/main, origin/HEAD) add venv/ to .gitignore to keep local virtual environments out of the repo
09ea3f5 add README with module listing and run instructions
a9a520f add module 7 functions: calculate_tax, apply_discount, final_price
c96e05a add Python, OS, and editor exclusions to .gitignore
e0a9a03 Create .gitignore
1bb2bc3 Initial commit
```
The commit history shows that they work in small, clear steps and build things in a logical order to keep the project organized. However, the first .gitignore commit message, “Create .gitignore,” only describes the action and doesn’t explain what the file does. Next time, they should write commit messages that clearly state the purpose of each change so any reader can understand it.

**2.** Before this module, I would just edit the same file in VS Code and hope it still worked. Now, with Git, I can edit files and return to a previous commit in my git log if something breaks. From now on, I will commit a working version of a file before changing anything, so I always have a safe version to return to.

**3.** One thing I would add to my `.gitignore` is `venv/`. This folder should not be tracked because it is specific to my computer and it is large, filled with packages that are not my own work. It can also be recreated with one command, so there is no need to store it in the repo.
