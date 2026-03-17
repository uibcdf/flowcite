# Pending Decisions & Design Challenges

As a developer, these are the open questions where your input is most needed.

## 1. Import Hooks vs. Manual Injections
- **Current state:** We have a placeholder for `mark_import`.
- **Challenge:** Implementing a transparent import hook (like `duecredit` does) is powerful but can be fragile or interfere with other tools. 
- **Decision needed:** Should we prioritize "zero-config" import hooks or stick to explicit registration in the host library?

## 2. Scoped Tracking (Context Managers)
- **Current state:** We have `@scoped_usage` as a decorator.
- **Challenge:** Sometimes tracking needs to happen within a specific block of code, not a whole function.
- **Decision needed:** Implementation of a `with flowcite.scope(...):` context manager and how it interacts with the global collector.

## 3. Persistent vs. In-Memory Registry
- **Current state:** The registry is entirely in-memory and volatile.
- **Challenge:** Some workflows might want to "remember" citations across different processes or save them to a file automatically.
- **Decision needed:** Should FlowCite support a local cache/database, or keep it strictly per-session?

## 4. BibTeX Complexity
- **Current state:** Very basic mapping.
- **Challenge:** BibTeX is complex and varied. 
- **Decision needed:** Should we bundle a full BibTeX library (like `bibtexparser`) as a dependency, or keep FlowCite "zero-dependency" and implement a robust but custom generator?

## 5. Rich Notebook UI
- **Current state:** Markdown strings.
- **Challenge:** Users love interactive or pretty-formatted citations in Jupyter.
- **Decision needed:** How much "styling" should FlowCite handle vs. providing raw data for the user to style?
