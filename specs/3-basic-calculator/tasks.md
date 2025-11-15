# Tasks: Basic Calculator Operations

**Input**: Design documents from `/specs/3-basic-calculator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: The tasks below follow a TDD approach as requested.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan (`src/calculator`, `tests/unit`, `tests/integration`).
- [x] T002 Initialize `pytest` configuration in `pytest.ini`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T003 Create `src/calculator/__init__.py`.
- [x] T004 Create `src/calculator/operations.py` with placeholder functions for `add`, `subtract`, `multiply`, `divide`.
- [x] T005 Create `src/calculator/cli.py` with placeholder for CLI logic.
- [x] T006 Create `src/main.py` as the entry point for the CLI.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Add Two Numbers (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to add two numbers so that I can get their sum.

**Independent Test**: Can be fully tested by providing two numbers and verifying the sum.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [US1] Write unit tests for `add` function in `tests/unit/test_operations.py`.

### Implementation for User Story 1

- [x] T008 [US1] Implement `add` function in `src/calculator/operations.py`.
- [x] T009 [US1] Refactor `add` function and tests.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Subtract Two Numbers (Priority: P1)

**Goal**: As a user, I want to subtract two numbers so that I can get their difference.

**Independent Test**: Can be fully tested by providing two numbers and verifying the difference.

### Tests for User Story 2 ⚠️

- [x] T010 [US2] Write unit tests for `subtract` function in `tests/unit/test_operations.py`.

### Implementation for User Story 2

- [x] T011 [US2] Implement `subtract` function in `src/calculator/operations.py`.
- [x] T012 [US2] Refactor `subtract` function and tests.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Multiply Two Numbers (Priority: P1)

**Goal**: As a user, I want to multiply two numbers so that I can get their product.

**Independent Test**: Can be fully tested by providing two numbers and verifying the product.

### Tests for User Story 3 ⚠️

- [x] T013 [US3] Write unit tests for `multiply` function in `tests/unit/test_operations.py`.

### Implementation for User Story 3

- [x] T014 [US3] Implement `multiply` function in `src/calculator/operations.py`.
- [x] T015 [US3] Refactor `multiply` function and tests.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: User Story 4 - Divide Two Numbers (Priority: P2)

**Goal**: As a user, I want to divide two numbers so that I can get their quotient.

**Independent Test**: Can be fully tested by providing two numbers (non-zero divisor) and verifying the quotient.

### Tests for User Story 4 ⚠️

- [x] T016 [US4] Write unit tests for `divide` function in `tests/unit/test_operations.py`, including division by zero.

### Implementation for User Story 4

- [x] T017 [US4] Implement `divide` function in `src/calculator/operations.py`.
- [x] T018 [US4] Refactor `divide` function and tests.

---

## Phase 7: CLI Integration

**Purpose**: Connect the calculator operations to the command-line interface.

- [x] T019 Implement CLI logic in `src/calculator/cli.py` to call the operations.
- [x] T020 Write integration tests for the CLI in `tests/integration/test_cli.py`.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [x] T021 Add docstrings and type hints to all functions.
- [x] T022 Run `mypy` for static analysis and fix any issues.
- [x] T023 Run `pytest --cov` to ensure 100% test coverage.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Stories (Phases 3-6)**: Depend on Foundational phase completion.
- **CLI Integration (Phase 7)**: Depends on User Stories completion.
- **Polish (Phase 8)**: Depends on CLI Integration completion.

### User Story Dependencies

- All user stories are independent and can be implemented in any order after the Foundational phase, but following the priority order is recommended.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Complete Setup + Foundational.
2. Add User Story 1 → Test independently.
3. Add User Story 2 → Test independently.
4. Add User Story 3 → Test independently.
5. Add User Story 4 → Test independently.
6. Complete CLI Integration and Polish phases.
