from flowcite import enable_import_hooks, get_used_items

import sys
from flowcite.core.hooks import InjectionsFinder

def test_metadata_discovery():
    # En lugar de confiar en el import real (que puede estar cacheado)
    # probamos directamente el método de descubrimiento del finder
    finder = InjectionsFinder()
    
    # Probamos con 'pytest' que sabemos que tiene metadatos y está instalado
    finder._discover_and_register('pytest')
    
    from flowcite import get_used_items
    used = get_used_items()
    assert any(k.startswith('metadata:pytest') or k.startswith('discovered:pytest') for k in used.keys())
