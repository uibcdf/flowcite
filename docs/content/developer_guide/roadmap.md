# Roadmap & Future Directions

This document outlines where FlowCite is heading and the milestones we aim to achieve.

## Vision
To become the standard "citation engine" for the Python scientific ecosystem, making attribution effortless for both developers and users.

## Milestones

### v0.2 (Current Phase) - Core Refinement
- [ ] **Robust BibTeX Generation:** Move beyond the current stub to a full-featured BibTeX renderer.
- [ ] **Import Hooks (Injections):** Implement automatic tracking of 3rd-party libraries via import hooks.
- [ ] **Optional Dependency Pattern:** Formalize and document the recommended way for libraries to include FlowCite as an optional dependency.

### v0.3 - UX & Ecosystem
- [ ] **Jupyter/IPython Integration:** Rich HTML representation of reports in notebooks.
- [ ] **JSON Schema:** Define a formal schema for FlowCite data to allow for external tool integration.
- [ ] **DueCredit Bridge:** An exporter that feeds FlowCite data into `duecredit`'s reporting engine.

### v0.4 - Automation & Discovery
- [ ] **Plugin System:** Allow external libraries to ship their own FlowCite "citation packs" that are discovered automatically.
- [ ] **CLI Tool:** A command-line interface to inspect or aggregate reports from multiple runs.

### v1.0 - Stability & Community
- [ ] **Stable API:** Lock down the core API for long-term support.
- [ ] **Comprehensive Documentation:** Full API reference and tutorial suite.
- [ ] **Community Adoption:** Getting FlowCite integrated into major UIBCDF tools (TopoMT, MolSysMT).
