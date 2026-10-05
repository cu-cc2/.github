# AGENTS.md

Instructions, conventions, and guidelines for AI agents working in this repository.

---

## 📌 Repository Overview

This repository (`cu-cc2`) contains course materials, lab experiments, assignments, and curated LeetCode solutions for the **Chandigarh University Competitive Coding 2** course.

The repository root is organized as a special GitHub profile repository within `.github/`.

---

## 📁 Directory Structure

```text
cu-cc2/
├── .github/
│   ├── profile/
│   │   └── README.md          # Profile README with Table of Contents & problem listings
│   ├── solutions/             # Python solutions for LeetCode problems
│   │   ├── 33.py
│   │   ├── 78.py
│   │   ├── 84.py
│   │   └── ...
│   ├── assignments/           # Lab assignments and problem statements
│   └── AGENTS.md              # Agent guidelines
└── AGENTS.md                  # Agent guidelines (workspace root)
```

---

## ⚙️ Coding Standards & Constraints

### 1. Python Solutions (`solutions/<number>.py`)
- **No Type Hints:** **DO NOT** use Python type annotations or hints (e.g., do not use `nums: List[int] -> List[List[int]]` or `from typing import List`). Always use plain Python function definitions:
  ```python
  class Solution:
      def subsets(self, nums):
          # implementation
  ```
  This preserves consistency with all existing solutions across the repository.
- **LeetCode Compatibility:** Every solution file should contain a primary `class Solution:` matching the standard LeetCode signature.
- **Multiple Approaches:** When providing multiple solutions or approaches for a problem:
  - Keep `class Solution:` as the primary/recommended approach.
  - Name secondary approaches descriptively, e.g., `class SolutionBacktracking:`.
  - Add clear comments identifying each approach (e.g., `# Approach 1: Bit Manipulation (Bitmasking)`).
- **Minimal Dependencies:** Use only Python standard library modules when necessary (e.g. `from collections import deque`). Avoid external dependencies.

---

## 📝 Profile README Conventions (`profile/README.md`)

- **Problem Entry Format:** Add each problem link using the established HTML/Markdown format:
  ```markdown
  - <a href="https://leetcode.com/problems/<problem-slug>/" target="_blank"><Number>. <Title></a> - [🐍 Solution](../solutions/<Number>.py)
  ```
  - Ensure links include `target="_blank"`.
  - Use the snake emoji `[🐍 Solution](../solutions/<Number>.py)` for the solution link.
- **Table of Contents Synchronization:**
  - Whenever a new experiment heading is added (e.g., `### Experiment 5`), the Table of Contents at the top of `README.md` must be updated with the corresponding anchor link (e.g., `  - [Experiment 5](#experiment-5)`).

---

## 🏷️ Commit Message Conventions

Commit messages should strictly follow the **Conventional Commits** specification:
- `feat: add solution for LeetCode problem <number> - <title> and update README`
- `docs: update profile README with <description>`
- `refactor: optimize <function_name> for problem <number>`
- `chore: update <description>`
