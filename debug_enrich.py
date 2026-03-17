from flowcite import Registry, register_item, enrich_all
import json

register_item(id="test", doi="10.1038/nmeth.1618")
print(f"Before: {Registry.items['test']}")
enrich_all()
print(f"After: {Registry.items['test']}")
