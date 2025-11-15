---
id: 0002
title: Add code quality standards to constitution
stage: constitution
date: 2025-11-13
surface: agent
model: gemini
feature: none
branch: master
user: ISMAIL AHMED SHAH
command: /sp.constitution
labels: ["constitution", "code quality", "standards"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Update @.specify/memory/constitution.md to improve Code Quality Standards

- All functions must include type hints on parameters and return types
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions)
- Lines must be under 100 characters
- No magic numbers; use named constants
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`
--- Content from referenced files ---
Content from @C:\Code\spec-kit\spec-kit-plus-calculator\.specify\memory\constitution.md:
<!--
<Sync Impact Report>
Version change: Initial → 1.0.0
Modified principles:
  - Library-First
  - CLI Interface
  - Test-First (NON-NEGOTIABLE)
  - Integration Testing
  - Observability
  - Versioning & Breaking Changes
Added sections:
  - Additional Constraints
  - Development Workflow
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - Command files in .gemini/commands/: ✅ updated
Follow-up TODOs: None
</Sync Impact Report>
-->
# Spec-Kit Plus Calculator Constitution

## Core Principles

### Library-First
Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries

### CLI Interface
Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats

### Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced

### Integration Testing
Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas

### Observability
Text I/O ensures debuggability; Structured logging required

### Versioning & Breaking Changes
MAJOR.MINOR.BUILD format; Semantic versioning strictly followed

## Additional Constraints

All development must adhere to the principles outlined in the .specify/memory/constitution.md. Any deviations require explicit architectural decision records (ADRs).

## Development Workflow

Code reviews are mandatory for all changes. All new features and bug fixes must include corresponding unit and integration tests. Automated CI/CD pipelines will enforce code quality and testing standards.

## Governance

This Constitution supersedes all other practices. Amendments require documentation, approval via an ADR, and a migration plan. All pull requests and code reviews must verify compliance with these principles. Complexity must be justified and documented. The .specify/memory/constitution.md file serves as the single source of truth for project principles.

**Version**: 1.0.0 | **Ratified**: 2025-11-13 | **Last Amended**: 2025-11-13
--- End of content ---

## Response snapshot

Constitution updated to version 1.1.0. No files require manual follow-up. Suggested commit message: `docs: amend constitution to v1.1.0 (add code quality standards)`

## Outcome

- ✅ Impact: Added new 'Code Quality Standards' section to the project constitution.
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated.
- 🔁 Next prompts: Continue with further constitution updates or proceed to feature specification.
- 🧠 Reflection: Successfully added code quality standards to the constitution, including type hinting, docstrings, naming conventions, line length, and magic numbers.

## Evaluation notes (flywheel)

- Failure modes observed: Attempted to use bash script in PowerShell environment for PHR creation.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure cross-platform compatibility for PHR creation scripts or use agent-native tools consistently.
