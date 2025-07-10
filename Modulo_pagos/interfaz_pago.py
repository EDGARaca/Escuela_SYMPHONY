import tkinter as tk
from tkinter import messagebox
from pago import Pago

def registrar_pago():
    try:
        pago_id = entry_id.get()
        tipo = combo_tipo.get()
        monto = float(entry_monto.get())
        fecha = entry_fecha.get()
        metodo = combo_metodo.get()
        pagador_id = entry_pagador_id.get()
        nombre_pagador = entry_nombre_pagador.get()

        nuevo_pago = Pago(pago_id, tipo, monto, fecha, metodo, pagador_id, nombre_pagador)
        recibo = nuevo_pago.generar_recibo()
        messagebox.showinfo("Pago registrado", recibo)

    except ValueError as ve:
        messagebox.showerror("Error de validación", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

ventana = tk.Tk()
ventana.title("Registro de Pagos")
ventana.geometry("500x450")

# ID de pago
tk.Label(ventana, text="ID del pago:").pack()
entry_id = tk.Entry(ventana, width=40)
entry_id.pack()

# Tipo de pago
tk.Label(ventana, text="Tipo de pago:").pack()
combo_tipo = tk.StringVar()
tk.OptionMenu(ventana, combo_tipo, "obligacion_escuela", "nomina", "mensualidad", "inscripcion").pack()
combo_tipo.set("mensualidad")

# Monto
tk.Label(ventana, text="Monto (COP):").pack()
entry_monto = tk.Entry(ventana, width=40)
entry_monto.pack() 

# Fecha
tk.Label(ventana, text="Fecha (YYYY-MM-DD):").pack()
entry_fecha = tk.Entry(ventana, width=40)
entry_fecha.pack()

# Método de pago
tk.Label(ventana, text="Método de pago:").pack()
combo_metodo = tk.StringVar()
tk.OptionMenu(ventana, combo_metodo, "Efectivo", "Tarjeta de crédito o débito", "Nequi", "PayPal").pack()
combo_metodo.set("Efectivo")

# ID del pagador
tk.Label(ventana, text="ID del pagador:").pack()
entry_pagador_id = tk.Entry(ventana, width=40)
entry_pagador_id.pack()

# Nombre del pagador
tk.Label(ventana, text="Nombre del pagador:").pack()
entry_nombre_pagador = tk.Entry(ventana, width=40)
entry_nombre_pagador.pack()

# Botón
tk.Button(ventana, text="Registrar pago", command=registrar_pago).pack(pady=15)

ventana.mainloop()