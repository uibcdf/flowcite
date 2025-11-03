# Reporting

At the end of a script or notebook, call:

```python
import flowcite
print(flowcite.report(format="markdown"))
```
Available formats: `markdown`, `text`, `bibtex`, `json`.
