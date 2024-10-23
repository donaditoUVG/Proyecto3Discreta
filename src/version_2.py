import tkinter as tk
from tkinter import messagebox

def calcular_expresion():
    try:
        # Obtener la expresión ingresada
        expresion = entrada_expresion.get()
        # Evaluar la expresión utilizando eval (con ^ sustituido por **)
        resultado = eval(expresion.replace("^", "**"))
        
        # Obtener el valor del módulo, si existe
        modulo_text = entrada_modulo.get()
        
        # Si el campo de módulo está vacío, no aplicamos el módulo
        if modulo_text:
            modulo = int(modulo_text)
            resultado_mod = resultado % modulo
            resultado_var.set(f"Resultado: {resultado} (mod {modulo} = {resultado_mod})")
        else:
            # Si no hay módulo, solo mostramos el resultado
            resultado_var.set(f"Resultado: {resultado}")
        
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida.")
    except Exception as e:
        messagebox.showerror("Error", f"Error en la expresión: {e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Expresiones con Módulo")

# Crear etiqueta y entrada para la expresión
tk.Label(ventana, text="Expresión:").grid(row=0, column=0, padx=10, pady=10)
entrada_expresion = tk.Entry(ventana, width=30)
entrada_expresion.grid(row=0, column=1, padx=10, pady=10)

# Crear etiqueta y entrada para el valor del módulo
tk.Label(ventana, text="Módulo (opcional):").grid(row=1, column=0, padx=10, pady=10)
entrada_modulo = tk.Entry(ventana, width=10)
entrada_modulo.grid(row=1, column=1, padx=10, pady=10)

# Crear botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_expresion)
boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Crear variable y etiqueta para mostrar el resultado
resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var).grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()