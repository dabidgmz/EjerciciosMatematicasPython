import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, diff, lambdify

class Newton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Newton Raphson")
        self.root.geometry("650x450") 
        self.root.resizable(False, False)

        # Colores personalizados
        self.color_fondo = "#000000" 
        self.color_texto = "#800080"  
        self.color_boton_calcular = "#4CAF50" 
        self.color_boton_limpiar = "#FF0000"  
        self.color_entrada = "#424242"  
        self.color_entrada_texto = "#FFFFFF"  

        self.root.configure(bg=self.color_fondo)

        self.frame_entrada = tk.LabelFrame(self.root, text="Insertar Datos", padx=10, pady=10, bg=self.color_fondo, fg=self.color_texto)
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        self.entries = {}
        labels = ["x1:", "Precisión (decimales):", "fx:"]

        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10), bg=self.color_fondo, fg=self.color_texto).grid(row=0, column=i*2, sticky="w", pady=3, padx=5)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=15, bg=self.color_entrada, fg=self.color_entrada_texto)
            entry.grid(row=0, column=i*2+1, pady=3, padx=5)
            self.entries[label] = entry


        self.frame_botones = tk.Frame(self.frame_entrada, bg=self.color_fondo)
        self.frame_botones.grid(row=1, column=0, columnspan=5, pady=10)

        self.boton_calcular = tk.Button(self.frame_botones, text="=", font=("Arial", 10, "bold"), bg=self.color_boton_calcular, fg="black", command=self.calcular)
        self.boton_calcular.grid(row=0, column=0, padx=5)

        self.boton_limpiar = tk.Button(self.frame_botones, text="Clean", font=("Arial", 10, "bold"), bg=self.color_boton_limpiar, fg="black", command=self.limpiar_entradas)
        self.boton_limpiar.grid(row=0, column=1, padx=5)

        self.boton_volver = tk.Button(self.frame_botones, text="Menú", font=("Arial", 10, "bold"), bg=self.color_boton_limpiar, fg="black", command=self.volver_menu_principal)
        self.boton_volver.grid(row=0, column=2, padx=5)

        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10, bg=self.color_fondo, fg=self.color_texto)
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        self.tabla_frame = tk.Frame(self.frame_resultados, bg=self.color_fondo)
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Xn+1"), show="headings", height=8)

        for col in self.tabla_resultados["columns"]:
            self.tabla_resultados.heading(col, text=col)
            self.tabla_resultados.column(col, anchor="w", width=85)

        self.tabla_resultados.pack(side="left", fill="both", expand=True)

        self.scroll_y = ttk.Scrollbar(self.tabla_frame, orient="vertical", command=self.tabla_resultados.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.tabla_resultados.configure(yscrollcommand=self.scroll_y.set)

        self.root.mainloop()

    def calcular(self):
        try:
            x1 = float(self.entries["x1:"].get())             
            Precision = int(self.entries["Precisión (decimales):"].get())
            fx = self.entries["fx:"].get()

            resultados = self.newthon_raphson(x1, fx, Precision)

            for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)

            for resultado in resultados:
                self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Xn+1"]))
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def limpiar_entradas(self):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)

        for row in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(row)
        
        self.entries["x1:"].focus()

    def volver_menu_principal(self):        
        self.root.withdraw()
        self.root.quit()  
        import menu  
        menu_app = menu.Menu()  
        menu_app.run()

    def newthon_raphson(self, x1, fx, precision):
        x = symbols('x')
        f_expr = fx
        f_prime_expr = diff(f_expr, x)

        f = lambdify(x, f_expr)
        f_prime = lambdify(x, f_prime_expr)

        x_n = x1
        resultado = []

        max_iteraciones = 1000
        iteraciones = 0

        while iteraciones < max_iteraciones:
            f_xn = f(x_n)
            f_prime_xn = f_prime(x_n)

            if f_prime_xn == 0:
                return resultado
            x_next = x_n - f_xn / f_prime_xn

            resultado.append({
                "n": len(resultado),
                "Xn": round(x_n, precision),
                "Xn+1": round(x_next, precision)
            })

            if abs(x_next - x_n) < 10**(-precision):
                return resultado

            x_n = x_next
            iteraciones += 1

        messagebox.showwarning("Advertencia", "El método no ha convergido después de 1000 iteraciones.")
        return resultado
