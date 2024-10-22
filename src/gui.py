import tkinter as tk
from tkinter import messagebox
from operaciones import mod_add, mod_subtract, mod_multiply, mod_divide, mod_power

class CalculadoraModular:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Modular")
        
        # Crear campos de entrada para las operaciones
        self.entrada_1 = tk.Entry(root)
        self.entrada_2 = tk.Entry(root)
        self.entrada_p = tk.Entry(root)
        
        self.entrada_1.grid(row=0, column=1, padx=10, pady=10)
        self.entrada_2.grid(row=1, column=1, padx=10, pady=10)
        self.entrada_p.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Valor 1:").grid(row=0, column=0)
        tk.Label(root, text="Valor 2:").grid(row=1, column=0)
        tk.Label(root, text="Modulo (p):").grid(row=2, column=0)
        
        # Crear botones para las operaciones
        tk.Button(root, text="Sumar", command=self.sumar).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Restar", command=self.restar).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(root, text="Multiplicar", command=self.multiplicar).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(root, text="Dividir", command=self.dividir).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(root, text="Potencia", command=self.potencia).grid(row=5, column=0, padx=10, pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado = tk.Label(root, text="Resultado: ")
        self.resultado.grid(row=6, column=0, columnspan=2)

    def obtener_entradas(self):
        try:
            valor1 = int(self.entrada_1.get())
            valor2 = int(self.entrada_2.get())
            p = int(self.entrada_p.get())
            return valor1, valor2, p
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
            return None, None, None

    def sumar(self):
        valor1, valor2, p = self.obtener_entradas()
        if valor1 is not None:
            resultado = mod_add(valor1, valor2, p)
            self.resultado.config(text=f"Resultado: {resultado}")

    def restar(self):
        valor1, valor2, p = self.obtener_entradas()
        if valor1 is not None:
            resultado = mod_subtract(valor1, valor2, p)
            self.resultado.config(text=f"Resultado: {resultado}")

    def multiplicar(self):
        valor1, valor2, p = self.obtener_entradas()
        if valor1 is not None:
            resultado = mod_multiply(valor1, valor2, p)
            self.resultado.config(text=f"Resultado: {resultado}")

    def dividir(self):
        valor1, valor2, p = self.obtener_entradas()
        if valor1 is not None:
            try:
                resultado = mod_divide(valor1, valor2, p)
                self.resultado.config(text=f"Resultado: {resultado}")
            except ValueError:
                messagebox.showerror("Error", "No se puede dividir por este valor en el módulo dado")
    
    def potencia(self):
        valor1, valor2, p = self.obtener_entradas()
        if valor1 is not None:
            resultado = mod_power(valor1, valor2, p)
            self.resultado.config(text=f"Resultado: {resultado}")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraModular(root)
    root.mainloop()