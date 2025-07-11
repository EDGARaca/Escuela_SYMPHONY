# --- interfaz_persona.py ---

import tkinter as tk
from tkinter import messagebox

# Importamos funciones del backend
from registrar_persona import registrar_persona
from gestor_personas import consultar_persona, modificar_persona, eliminar_persona

# --- Funciones de interacción ---

def registrar():
    datos = {
        "primer_nombre": entry_primer_nombre.get(),
        "segundo_nombre": entry_segundo_nombre.get(),
        "primer_apellido": entry_primer_apellido.get(),
        "segundo_apellido": entry_segundo_apellido.get(),
        "email": entry_email.get(),
        "fecha_nacimiento": entry_fecha.get(),
        "identificacion": entry_id.get(),
        "direccion": entry_direccion.get(),
        "celular": entry_celular.get(),
        "tipo_persona": entry_tipo.get()
    }

    if not all(datos.values()):
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    id_generado = registrar_persona(**datos)
    messagebox.showinfo("Registro exitoso", f"ID asignado: {id_generado}")
    limpiar_campos()

def consultar():
    id_buscar = entry_busqueda.get()
    persona = consultar_persona(id_buscar)

    if persona:
        entry_primer_nombre.delete(0, tk.END)
        entry_primer_nombre.insert(0, persona["primer_nombre"])

        entry_segundo_nombre.delete(0, tk.END)
        entry_segundo_nombre.insert(0, persona["segundo_nombre"])

        entry_primer_apellido.delete(0, tk.END)
        entry_primer_apellido.insert(0, persona["primer_apellido"])

        entry_segundo_apellido.delete(0, tk.END)
        entry_segundo_apellido.insert(0, persona["segundo_apellido"])

        entry_email.delete(0, tk.END)
        entry_email.insert(0, persona["email"])

        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, persona["fecha_nacimiento"])

        entry_id.delete(0, tk.END)
        entry_id.insert(0, persona["identificacion"])

        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, persona["direccion"])

        entry_celular.delete(0, tk.END)
        entry_celular.insert(0, persona["celular"])

        entry_tipo.delete(0, tk.END)
        entry_tipo.insert(0, persona["tipo"])

        messagebox.showinfo("Consulta", f"Datos cargados de {id_buscar}")
    else:
        messagebox.showerror("Consulta", "ID no encontrado.")

def modificar():
    id_modificar = entry_busqueda.get()
    nuevos_datos = {
        "primer_nombre": entry_primer_nombre.get(),
        "segundo_nombre": entry_segundo_nombre.get(),
        "primer_apellido": entry_primer_apellido.get(),
        "segundo_apellido": entry_segundo_apellido.get(),
        "email": entry_email.get(),
        "fecha_nacimiento": entry_fecha.get(),
        "identificacion": entry_id.get(),
        "direccion": entry_direccion.get(),
        "celular": entry_celular.get(),
        "tipo": entry_tipo.get()
    }

    resultado = modificar_persona(id_modificar, nuevos_datos)
    if resultado:
        messagebox.showinfo("Modificación", f"Datos de {id_modificar} actualizados correctamente.")
    else:
        messagebox.showerror("Modificación", "ID no encontrado.")

def eliminar():
    id_eliminar = entry_busqueda.get()
    resultado = eliminar_persona(id_eliminar)
    if resultado:
        messagebox.showinfo("Eliminación", f"{id_eliminar} ha sido eliminado del sistema.")
        limpiar_campos()
    else:
        messagebox.showerror("Eliminación", "ID no encontrado.")

def limpiar_campos():
    for campo in campos:
        campo.delete(0, tk.END)
    entry_busqueda.delete(0, tk.END)

# --- Interfaz gráfica ---

ventana = tk.Tk()
ventana.title("Gestión de Personas - SYMPHONY")
ventana.geometry("600x650")

tk.Label(ventana, text="Buscar/modificar por ID:").pack()
entry_busqueda = tk.Entry(ventana, width=40)
entry_busqueda.pack(pady=5)

etiquetas = [
    "Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido",
    "Correo Electrónico", "Fecha de Nacimiento", "Identificación",
    "Dirección", "Número Celular", "Tipo de Persona"
]

campos = []

for texto in etiquetas:
    tk.Label(ventana, text=texto + ":").pack()
    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=2)
    campos.append(entrada)

(entry_primer_nombre, entry_segundo_nombre, entry_primer_apellido, entry_segundo_apellido,
 entry_email, entry_fecha, entry_id, entry_direccion, entry_celular, entry_tipo) = campos

# Botones funcionales
tk.Button(ventana, text="Registrar nueva persona", command=registrar).pack(pady=10)
tk.Button(ventana, text="Consultar persona", command=consultar).pack(pady=5)
tk.Button(ventana, text="Modificar persona", command=modificar).pack(pady=5)
tk.Button(ventana, text="Eliminar persona", command=eliminar).pack(pady=5)

ventana.mainloop()