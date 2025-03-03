import tkinter as tk
from tkinter import ttk, messagebox
from metodos import Metodos

class Euler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Euler Mejorado")
        self.root.geometry("750x450") 
        self.root.resizable(False, False)

        self.color_fondo = "#000000"  
        self.color_texto = "#800080"  
        self.color_boton_calcular = "#00FF00" 
        self.color_boton_limpiar = "#FF0000"  
        self.color_boton_texto = "#000000"  
        self.color_entrada = "#424242"  
        self.color_entrada_texto = "#FFFFFF" 

        self.root.configure(bg=self.color_fondo)

        self.frame_entrada = tk.Frame(self.root, bg=self.color_fondo)
        self.frame_entrada.pack(pady=10)

        self.frame_entrada = tk.LabelFrame(self.root, text="Insertar datos ", padx=10, pady=10, bg=self.color_fondo, fg=self.color_texto)
        self.frame_entrada.pack(padx=10, pady=5, fill="x")
        self.label_descripcion = tk.Label(
            self.root, 
            text="x0: Valor inicial de x | y0: Valor inicial de y | h: Tamaño del paso | "
                "xf: Valor final de x | f(x, y): Función diferencial",
            font=("Arial", 9), 
            bg=self.color_fondo, 
            fg=self.color_texto,
            wraplength=700, 
            justify="left"
        )
        self.label_descripcion.pack(padx=10, pady=5)
        labels = ["x0:", "y0:", "h:", "xf:", "f(x, y):"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10), bg=self.color_fondo, fg=self.color_texto).pack(side="left", padx=5)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=10, bg=self.color_entrada, fg=self.color_entrada_texto, insertbackground=self.color_texto)
            entry.pack(side="left", padx=5)
            self.entries[label] = entry



        self.boton_calcular = tk.Button(self.root, text="=", font=("Arial", 10, "bold"), bg=self.color_boton_calcular, fg=self.color_boton_texto, command=self.calcular)
        self.boton_calcular.pack(pady=5)

        self.boton_limpiar = tk.Button(self.root, text="Clean", font=("Arial", 10, "bold"), bg=self.color_boton_limpiar, fg=self.color_boton_texto, command=self.limpiar_entradas)
        self.boton_limpiar.pack(pady=5)

        self.boton_limpiar = tk.Button(self.root, text="Menu", font=("Arial", 10, "bold"), bg=self.color_boton_limpiar, fg=self.color_boton_texto, command=self.volver_menu_principal)
        self.boton_limpiar.pack(pady=5)

        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10, bg=self.color_fondo, fg=self.color_texto)
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        self.tabla_frame = tk.Frame(self.frame_resultados, bg=self.color_fondo)
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Yn", "(Yn+1)*", "Xn+1", "Yn+1"), show="headings", height=8)

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
            x0 = float(self.entries["x0:"].get())
            y0 = float(self.entries["y0:"].get())
            h = float(self.entries["h:"].get())
            xf = float(self.entries["xf:"].get())
            fxy = self.entries["f(x, y):"].get()

            if h <= 0:
                messagebox.showerror("Error", "El paso h debe ser mayor que 0.")
                return

            if x0 >= xf:
                messagebox.showerror("Error", "x0 debe ser menor que xf.")
                return

            resultados = Metodos.euler_mejorado(x0, y0, h, xf, fxy)

            for row in self.tabla_resultados.get_children():
                self.tabla_resultados.delete(row)

            for resultado in resultados:
                self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Yn"], resultado["(Yn+1)*"], resultado["Xn+1"], resultado["Yn+1"]))

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def limpiar_entradas(self):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)

        for row in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(row)
        
        self.entries["x0:"].focus()

    def volver_menu_principal(self):        
            self.root.withdraw()
            self.root.quit()  
            import menu  
            menu_app = menu.Menu()  
            menu_app.run()