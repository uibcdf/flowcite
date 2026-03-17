# Roadmap

## Phase 1: Core Consolidation (0.1.0) - [DONE]
*   [x] Refactor the BibTeX generator to be robust.
*   [x] Implement the documented and tested 'Optional Dependency' pattern.
*   [x] Add the Context Manager for granular tracking.

## Phase 2: Automation & Metadata (0.2.0) - [DONE]
*   [x] Launch `flowcite.contrib.jupyter` for rich visualization.
*   [x] Improve the Markdown format to include clickable DOI links.
*   [x] Auto-discovery of `CITATION.cff` and package metadata.
*   [x] Standard Injections (NumPy, SciPy, MolSysSuite).
*   [x] CSL-JSON and Provenance Graph support.
*   [x] DOI Enrichment (Crossref).
*   [x] Session Persistence and Auto-reminders.

## Phase 3: Ecosystem & Connectivity (0.3.0) - [IN PROGRESS]
*   [ ] **Plugin System (Entry Points):** Allow external libraries to ship citation packs.
*   [ ] **Metadata Cache:** Persistent storage for fetched DOI metadata to work offline.
*   [ ] **DueCredit Bridge:** Export/Forward citations to DueCredit.
*   [ ] **CLI Tool:** Command-line interface to inspect saved sessions.

## Future Strategic Concepts (Ideas & Proposals)
1.  **Collaborative Web UI:** A temporary web server to view citations interactively.
2.  **PDF/Latex Templates:** Direct generation of "References" sections.
3.  **Deep API Inspection:** Detect algorithm usage via AST analysis (very advanced).
