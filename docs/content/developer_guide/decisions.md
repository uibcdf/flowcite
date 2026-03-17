# Technical Decision Log

## Decisions Made
1.  **Singleton/Class-based Registry and Collector:** It was decided to use class methods to ensure there is only one global state per process, facilitating use from anywhere within a host library.
2.  **Python 3.10+:** This version is required to take advantage of `typing` improvements and future annotations.

## Pending Decisions
1.  **External Dependencies:** Should we use an external library for BibTeX (more robust but adds a dependency) or write our own parser (lightweight but limited)?
2.  **Import Hooks:** How aggressive should we be in intercepting third-party imports?
3.  **Nested Scope:** How should the Collector behave if a tracked function calls another tracked function? Should citations be duplicated or heirarchized?
