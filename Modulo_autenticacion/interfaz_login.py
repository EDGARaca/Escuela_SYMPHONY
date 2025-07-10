# --- interfaz_login.py ---

# Importamos tkinter para construir la interfaz gráfica
import tkinter as tk

# Importamos messagebox para mostrar mensajes emergentes
from tkinter import messagebox

# Importamos la función de login desde el módulo login.py
from login import iniciar_sesion

# Función que se ejecuta cuando el usuario presiona el botón "Iniciar sesión"
def verificar_credenciales():
    correo = entry_correo.get()        # Obtenemos el correo ingresado
    contraseña = entry_contraseña.get()# Obtenemos la contraseña ingresada

    rol = iniciar_sesion(correo, contraseña)  # Validamos credenciales

    if rol:
        # Si las credenciales son válidas, mostramos un mensaje de bienvenida y el rol
        messagebox.showinfo("Inicio de sesión", f"Acceso concedido.\nBienvenido/a como {rol}.")
    else:
        # Si no son válidas, se muestra un mensaje de error
        messagebox.showerror("Error", "Correo o contraseña incorrectos.")

# ----- Construcción de la interfaz gráfica -----

ventana = tk.Tk()                           # Creamos la ventana principal
ventana.title("Login de Usuario SYMPHONY") # Título de la ventana
ventana.geometry("500x250")                # Tamaño de la ventana

# Etiqueta y campo de entrada para correo electrónico
tk.Label(ventana, text="Correo electrónico:").pack(pady=5)
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack()

# Etiqueta y campo de entrada para contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contraseña = tk.Entry(ventana, width=40, show="*")
entry_contraseña.pack()

# Botón que ejecuta la función de verificación
tk.Button(ventana, text="Iniciar sesión", command=verificar_credenciales).pack(pady=20)

# Inicia el bucle principal para mostrar la interfaz
ventana.mainloop()