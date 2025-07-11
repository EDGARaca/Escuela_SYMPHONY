# --- gestor_personas.py ---

import json
import os

archivo_personas = "personas.json"

# Función para cargar el archivo JSON
def cargar_personas():
    if os.path.exists(archivo_personas):
        with open(archivo_personas, "r") as f:
            return json.load(f)
    return {}

# Consultar persona por ID
def consultar_persona(id_persona):
    personas = cargar_personas()
    return personas.get(id_persona)

# Modificar datos de una persona por ID
def modificar_persona(id_persona, nuevos_datos):
    personas = cargar_personas()
    if id_persona in personas:
        personas[id_persona].update(nuevos_datos)
        with open(archivo_personas, "w") as f:
            json.dump(personas, f, indent=4)
        return True
    return False

# Eliminar una persona por ID
def eliminar_persona(id_persona):
    personas = cargar_personas()
    if id_persona in personas:
        del personas[id_persona]
        with open(archivo_personas, "w") as f:
            json.dump(personas, f, indent=4)
        return True
    return False