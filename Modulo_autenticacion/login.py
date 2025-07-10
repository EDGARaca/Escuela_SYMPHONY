# --- login.py ---

# Diccionario que simula una base de datos de usuarios con correos, contraseñas y roles
usuarios = {
    "manuel@gmail.com": {"contraseña": "1234", "rol": "Docente"},
    "jessica@gmail.com":  {"contraseña": "5678", "rol": "Estudiante"},
    "ashley@gmail.com":   {"contraseña": "abc123", "rol": "Auxiliar_Administrativa"},
    "ruben@gmail.com":   {"contraseña": "abc123", "rol": "Auxiliar_Contable"},
    "carlos@gmail.com":   {"contraseña": "abc123", "rol": "Director"},
    "donald@gmail.com":   {"contraseña": "abc123", "rol": "Aspirante"},
}

# Función que verifica si el correo y contraseña son válidos, y retorna el rol asociado
def iniciar_sesion(correo, contraseña):
    if correo in usuarios and usuarios[correo]["contraseña"] == contraseña:
        return usuarios[correo]["rol"]  # Devuelve el rol si las credenciales son válidas
    else:
        return None  # Devuelve None si la validación fallas