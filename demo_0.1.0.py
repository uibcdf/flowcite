import flowcite
from pathlib import Path
import time

# 1. Activamos la persistencia (por si el script falla)
flowcite.enable_persistence("session_cache.json")

# 2. Registramos un ítem solo con DOI (sin metadatos)
print("Registry: Registering item with DOI...")
flowcite.register_item(id="matplotlib:paper", doi="10.1038/nmeth.1618")

# 3. Enriquecemos metadatos desde Crossref
print("Enrichment: Fetching metadata from Crossref...")
flowcite.enrich_all()

# 4. Simulamos un flujo de trabajo con jerarquía
@flowcite.scoped_usage("plotting_workflow")
def run_analysis():
    with flowcite.scope("initialization"):
        flowcite.track_item("matplotlib:paper")
        time.sleep(0.1)
    
    with flowcite.scope("heavy_computation"):
        # Simulamos una inyección de una lib externa
        flowcite.add_injection("numpy", ["paper:numpy"])
        flowcite.enable_import_hooks()
        import numpy # Esto disparará la cita automáticamente
        time.sleep(0.1)

print("Workflow: Running scientific analysis...")
run_analysis()

# 5. Generamos el "Citation Package"
print("Reporting: Dumping all formats to './citation_package/'...")
flowcite.dump("citation_package", formats=["markdown", "bibtex", "provenance", "csl-json"])

# 6. Mostramos el resumen (en un script sale como texto, en Jupyter saldría HTML)
print("\n--- QUICK SUMMARY ---")
print(flowcite.report(format="text"))

print("\nDone! Check the 'citation_package' directory for all files.")
