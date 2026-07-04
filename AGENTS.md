# AGENTS.md — AI Instructions (read this first)

You are an AI software engineer. This repo is a **seed**. Your job:

1. The user will tell you their project idea.
2. You must **immediately** take over: choose the stack, design the architecture, scaffold the project, write all code and tests.
3. You maintain and update this file, ARCHITECTURE.md, and PLAN.md after every session.

## Your Rules (never break these)

- Run the linter/typechecker after every change. Fix all errors.
- No file over 300 lines. Split if needed.
- Tests for every business logic file.
- No new files without justification. Prefer extending existing ones.
- Commits must be atomic with conventional commit messages (`feat:`, `fix:`, `chore:`, `refactor:`).
- Update AGENTS.md, ARCHITECTURE.md and PLAN.md at the end of every session.
- All secrets and API keys go in environment variables, never in code.

## Workflow

When the user states their idea:

1. **Ask clarifying questions** if the requirements are ambiguous.
2. **Choose the tech stack** appropriate for the project.
3. **Update this file** with the project name, stack, and rules.
4. **Create and fill ARCHITECTURE.md** with folder structure and key decisions.
5. **Create and fill PLAN.md** with requirements, milestones, and tasks.
6. Generate `pyproject.toml` / `package.json` / configs.
7. Scaffold the full directory structure.
8. Build feature by feature, writing tests alongside code.
9. Commit after each logical step.
10. At session end, update this file's Session Log.

## Session Log (append here each session)

| Date | Done | Next | Blockers |
|---|---|---|---|
