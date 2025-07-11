# --- registrar_persona.py ---

import json
import os

# Ruta del archivo donde se almacenarán los datos de las personas
archivo_personas = "personas.json"

# Función que registra una nueva persona y la guarda en el archivo
def registrar_persona(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                      email, fecha_nacimiento, identificacion, direccion, celular,
                      tipo_persona, genero):
    
    # Verificamos si ya existe el archivo de personas
    if os.path.exists(archivo_personas):
        with open(archivo_personas, "r") as f:
            personas = json.load(f)
    else:
        personas = {}

    # Se genera un ID automático (tipo y número de personas registrados)
    nuevo_id = f"{tipo_persona[:3].upper()}-{len(personas) + 1}"

    # Creamos el registro completo con todos los datos incluidos
    personas[nuevo_id] = {
        "primer_nombre": primer_nombre,
        "segundo_nombre": segundo_nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento,
        "identificacion": identificacion,
        "direccion": direccion,
        "celular": celular,
        "genero": genero,
        "tipo": tipo_persona
    }

    # Guardamos el diccionario en formato JSON
    with open(archivo_personas, "w") as f:
        json.dump(personas, f, indent=4)

    return nuevo_id