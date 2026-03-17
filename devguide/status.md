# Current Project Status (Version 0.4.0)

This document reflects the technical reality of the 0.4.0 release.

## What is working (DONE)
- **Item Registry:** Data structure to define articles, repositories, etc.
- **BibTeX Loader:** Robust internal parser for `.bib` files.
- **Auto-Discovery:** Automatic detection of `CITATION.cff` and package metadata (PEP 621).
- **Standard Injections:** Built-in citations for NumPy, SciPy, Matplotlib, and MolSysSuite.
- **Plugin System:** Automatic loading of citation packs via entry points.
- **Metadata Cache:** Local storage for DOI results in `~/.cache/flowcite`.
- **DueCredit Bridge:** Interoperability with DueCredit.
- **CLI Tool:** Command-line reporter `flowcite <session_file>`.
- **Provenance Graph:** Hierarchical visualization of *why* each item was cited.
- **CSL-JSON Export:** Standard format for Zotero/Mendeley integration.
- **LaTeX/PDF Generator:** Directly generate and compile (`pdflatex`) citation documents.
- **Deep API Inspection:** Automatic citation tracking via AST analysis (`auto_track_calls`).
- **Collaborative Web UI:** Temporary local web dashboard via `serve_ui()`.
- **Jupyter Integration:** Rich HTML representation via `flowcite.summary()`.
- **Markdown Enrichment:** Clickable titles (DOI/URL) and formatted author lists.
- **Import Hooks:** Automatic citation triggering on `import`.
- **Auto-Reminder:** Optional `atexit` hook for end-of-session alerts.
- **Persistence:** JSON-based session recovery.
- **Combined Reporting:** `flowcite.dump()` for multi-format output.
- **DOI Enrichment:** Automatic metadata fetching from Crossref.

## Future Strategic Concepts (WIP/TODO for 1.0.0)
- **Stable API:** Hardening the core for long-term support.
- **Cloud Sync:** Aggregate reports from multiple users/machines.
- **IDE Extensions:** Real-time citation hints in VSCode/PyCharm.
