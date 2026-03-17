# Current Project Status

This document reflects the technical reality as of today.

## What is working (DONE)
- **Item Registry:** Data structure to define articles, repositories, etc.
- **BibTeX Loader:** Load citation items directly from `.bib` files (zero-dependency).
- **Bindings:** Ability to associate items with functions/classes.
- **Basic Collector:** In-memory mechanism to record what has been used in the current session.
- **Decorators:** `@scoped_usage` to automatically mark the use of a function.
- **Context Managers:** Ability to use `with flowcite.scope(...):` to track specific code blocks.
- **Provenance Graph:** Hierarchical visualization of *why* each item was cited.
- **BibTeX Generator:** Robust mapping for articles, software, and generic entries.
- **CSL-JSON Export:** Standard format for integration with Zotero/Mendeley.
- **Jupyter Integration:** Rich visual representation (HTML) via `flowcite.summary()`.
- **Markdown Enrichment:** Clickable titles (DOI/URL) and formatted author lists.
- **Import Hooks:** Automatic detection of third-party library usage via `sys.meta_path`.
- **Auto-Reminder:** Optional `atexit` hook to remind users about citations at the end of a session.
- **Basic Formats:** Export to Text, Markdown, and JSON.

## Work in Progress (WIP)
- **DOI Enrichment:** Automatically fetch metadata from DOIs if internet is available.

## To be implemented (TODO)
- **Persistence:** Option to save the citation trace to a file for long sessions.
- **Plugin System:** External citation packs for major libraries.
