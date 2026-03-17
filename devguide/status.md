# Current Project Status (Version 0.3.0)

This document reflects the technical reality of the 0.3.0 release.

## What is working (DONE)
- **Item Registry:** Data structure to define articles, repositories, etc.
- **BibTeX Loader:** Robust internal parser for `.bib` files.
- **Auto-Discovery:** Automatic detection of `CITATION.cff` and package metadata (PEP 621).
- **Standard Injections:** Built-in citations for NumPy, SciPy, Matplotlib, and MolSysSuite.
- **Plugin System:** Automatic loading of citation packs via entry points.
- **Metadata Cache:** Local storage for DOI results in `~/.cache/flowcite`.
- **DueCredit Bridge:** Direct interoperability with DueCredit via `export_to_duecredit()` (DOI-aware).
- **CLI Tool:** Command-line reporter `flowcite <session_file>`.
- **Provenance Graph:** Hierarchical visualization of *why* each item was cited.
- **CSL-JSON Export:** Standard format for Zotero/Mendeley integration.
- **Jupyter Integration:** Rich HTML representation via `flowcite.summary()`.
- **Markdown Enrichment:** Clickable titles (DOI/URL) and formatted author lists.
- **Import Hooks:** Automatic citation triggering on `import` via `sys.meta_path`.
- **Auto-Reminder:** Optional `atexit` hook for end-of-session alerts.
- **Persistence:** JSON-based session recovery.
- **Combined Reporting:** `flowcite.dump()` for multi-format output.
- **DOI Enrichment:** Automatic metadata fetching from Crossref.

## Future Strategic Concepts (WIP/TODO for 0.4.0+)
- **Reference Section Generator:** Directly generate PDF/LaTeX bibliographies.
- **Deep API Inspection:** Detect algorithm usage via AST analysis.
- **Collaborative Web UI:** Interactive citation dashboard.
