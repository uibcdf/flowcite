# Current Project Status (Version 0.2.0)

This document reflects the technical reality of the 0.2.0 release.

## What is working (DONE)
- **Item Registry:** Data structure to define articles, repositories, etc.
- **BibTeX Loader:** Robust internal parser for `.bib` files.
- **Auto-Discovery:** Automatic detection of `CITATION.cff` and package metadata (PEP 621).
- **Standard Injections:** Built-in citations for NumPy, SciPy, Matplotlib, and MolSysSuite.
- **Provenance Graph:** Hierarchical visualization of *why* each item was cited.
- **CSL-JSON Export:** Standard format for Zotero/Mendeley integration.
- **Jupyter Integration:** Rich HTML representation via `flowcite.summary()`.
- **Markdown Enrichment:** Clickable titles (DOI/URL) and formatted author lists.
- **Import Hooks:** Automatic citation triggering on `import` via `sys.meta_path`.
- **Auto-Reminder:** Optional `atexit` hook for end-of-session alerts.
- **Persistence:** JSON-based session recovery.
- **Combined Reporting:** `flowcite.dump()` for multi-format output.
- **DOI Enrichment:** Automatic metadata fetching from Crossref.

## Work in Progress (WIP for 0.3.0)
- **Plugin System:** External citation packs.
- **DueCredit Bridge:** Direct interoperability with DueCredit.

## To be implemented (TODO)
- **Metadata Cache:** Persistent storage for DOI results.
- **CLI Tool:** Command-line reporter for stored sessions.
