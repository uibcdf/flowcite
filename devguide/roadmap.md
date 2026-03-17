# Roadmap

## Phase 1: Core Consolidation (0.1.0) - [DONE]
*   [x] Refactor the BibTeX generator to be robust.
*   [x] Implement the documented and tested 'Optional Dependency' pattern.
*   [x] Add the Context Manager for granular tracking.

## Phase 2: User Experience (0.2.0) - [IN PROGRESS]
*   [x] Launch `flowcite.contrib.jupyter` for rich visualization.
*   [x] Improve the Markdown format to include clickable DOI links.
*   [ ] Define the official JSON schema.

## Phase 3: Ecosystem (v0.4+)
*   [ ] Implement the bridge with `duecredit`.
*   [ ] Create a library of 'Standard Injections' for common scientific packages (NumPy, SciPy, MDTraj).
*   [ ] Plugin discovery system.
*   [ ] **Import Hooks:** Automatic detection of third-party library usage.

## Future Strategic Concepts (Ideas & Proposals)
To become an essential tool in scientific workflows (like the MolSysSuite ecosystem), FlowCite must integrate seamlessly into the researcher's daily life. The following concepts are proposed for future exploration:

1.  **Provenance Graph (Traceability Tree):** Instead of a flat list, generate a hierarchical tree showing exactly *why* a citation was triggered (e.g., `molsysmt.convert -> mdtraj.compute_distances -> MDTraj Paper`). This provides absolute transparency.
2.  **CSL-JSON Export:** Support `csl-json` format out-of-the-box. This is the modern standard for direct, drag-and-drop import into reference managers like Zotero, Mendeley, and EndNote.
3.  **Auto-Reminder (`atexit` hook):** Implement an optional `flowcite.enable_auto_reminder()` that uses Python's `atexit`. When a long script finishes, it prints a polite, non-intrusive message in the terminal: *"ℹ️ FlowCite: Your analysis utilized 3 components requiring citation. Run `flowcite.report()` to view."*
4.  **Zero-Config Items (DOI Auto-resolution):** Allow developers to register items using only a DOI. FlowCite would query the Crossref API (or similar) to automatically fetch title, authors, year, and journal, drastically reducing boilerplate code in host libraries.
