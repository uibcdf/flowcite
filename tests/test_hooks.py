import sys
from flowcite import add_injection, enable_import_hooks, get_used_items

def test_import_hook():
    # Registramos una inyección para un módulo que no esté cargado (o uno ficticio)
    # Para el test, usaremos uno que sepamos que no está en sys.modules o lo borramos
    module_name = 'math' # math siempre está, pero podemos probar la lógica
    add_injection(module_name, ['paper:math'])
    
    enable_import_hooks()
    
    # Forzamos la 'importación' (o el trigger del finder)
    # En un entorno real, 'import math' dispararía find_spec
    import math
    
    # El finder debería haber activado la cita
    used = get_used_items()
    # Nota: Si 'math' ya estaba cargado, el finder no se dispara para find_spec 
    # a menos que sea un módulo nuevo. Para el test, vamos a usar un nombre falso.
    
    fake_module = 'non_existent_science_lib'
    add_injection(fake_module, ['paper:fake'])
    
    # Intentamos importar el falso
    try:
        __import__(fake_module)
    except ImportError:
        pass # No nos importa que falle el import, queremos ver si el finder se activó
    
    used = get_used_items()
    assert 'paper:fake' in used
    assert fake_module in used['paper:fake']
