<!--
<Sync Impact Report>
Version change: 1.0.0 → 1.1.0
Modified principles: None
Added sections:
  - Code Quality Standards
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

## Code Quality Standards

### Type Hinting
All functions MUST include type hints on parameters and return types.
Example: `def add(a: float, b: float) -> float:`

### Docstrings
All functions MUST include docstrings explaining their purpose, parameters, and return values.
Example: `"""Add two numbers and return the sum."""`

### Naming Conventions
All code MUST follow PEP 8 naming conventions (e.g., `lowercase_with_underscores` for functions and variables, `CamelCase` for classes).

### Line Length
Lines MUST be kept under 100 characters for readability.

### Magic Numbers
Magic numbers MUST be replaced with named constants to improve clarity and maintainability.
Bad example: `if x > 10:`
Good example: `if x > MAX_POWER_EXPONENT:`

## Governance

This Constitution supersedes all other practices. Amendments require documentation, approval via an ADR, and a migration plan. All pull requests and code reviews must verify compliance with these principles. Complexity must be justified and documented. The .specify/memory/constitution.md file serves as the single source of truth for project principles.

**Version**: 1.1.0 | **Ratified**: 2025-11-13 | **Last Amended**: 2025-11-13