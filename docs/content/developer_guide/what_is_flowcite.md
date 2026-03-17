# What is FlowCite?

**FlowCite** is a lightweight Python library designed to provide **runtime-aware citation and acknowledgement tracking**.

## The Problem
Scientific software often relies on multiple algorithms, datasets, and third-party libraries. However, typical citation practices are "all or nothing": if you import a library, you're often asked to cite its main paper, even if you only used a small, unrelated part of it. Conversely, many important contributions (like specific algorithms or datasets used conditionally) go uncredited.

## The Solution
FlowCite allows developers to:
1.  **Register items statically:** Define what *can* be cited (papers, repos, datasets).
2.  **Bind them to code:** Associate these items with specific functions or classes.
3.  **Track usage dynamically:** At runtime, FlowCite records only what was *actually* executed.

## Core Philosophy
*   **Minimal Overhead:** Tracking should not significantly impact performance.
*   **Optional Dependency:** A host library should work perfectly even if FlowCite is not installed.
*   **Aesthetic & Flexible:** Reports should look great in Jupyter Notebooks and be exportable to standard formats like BibTeX or JSON.
*   **Interoperable:** Respect and complement existing tools like `duecredit`.
