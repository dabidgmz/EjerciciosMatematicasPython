import tkinter as tk
from tkinter import ttk, messagebox
from metodos import Metodos

class Runge:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Runge Kutta")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
        self.root.config(bg="black")  

        self.frame_entrada = tk.LabelFrame(self.root, text="Insertar datos", padx=10, pady=10, bg="black", fg="purple")
        self.frame_entrada.pack(padx=10, pady=5, fill="x")

        labels = ["x0:", "y0:", "h:", "xf:", "f(x, y):"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.frame_entrada, text=label, font=("Arial", 10), bg="black", fg="purple").grid(row=0, column=i*2, sticky="w", pady=3, padx=5)
            entry = tk.Entry(self.frame_entrada, font=("Arial", 10), width=15)
            entry.grid(row=0, column=i*2+1, pady=3, padx=5)
            self.entries[label] = entry
        
        self.boton_calcular = tk.Button(self.frame_entrada, text="=", font=("Arial", 10, "bold"), bg="#4CAF50", fg="black", command=self.calcular)
        self.boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.boton_limpiar = tk.Button(self.frame_entrada, text="Clean", font=("Arial", 10, "bold"), bg="#FF0000", fg="black", command=self.limpiar_entradas)
        self.boton_limpiar.grid(row=1, column=2, columnspan=1, pady=10)

        self.frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10, bg="black", fg="purple")
        self.frame_resultados.pack(padx=10, pady=5, fill="both", expand=True)

        self.tabla_frame = tk.Frame(self.frame_resultados, bg="black")
        self.tabla_frame.pack(fill="both", expand=True)

        self.tabla_resultados = ttk.Treeview(self.tabla_frame, columns=("n", "Xn", "Yn", "K1", "K2","K3","K4", "Yn+1"), show="headings", height=8)
        
        
        style = ttk.Style()
        style.configure("Treeview", 
                        background="white", 
                        foreground="black", 
                        font=("Arial", 10), 
                        rowheight=25)
        style.map("Treeview", background=[("selected", "#4CAF50")])

        for col in self.tabla_resultados["columns"]:
            self.tabla_resultados.heading(col, text=col, anchor="w")
            self.tabla_resultados.column(col, anchor="w", width=85)

        self.tabla_resultados.pack(side="left", fill="both", expand=True)

        self.scroll_y = ttk.Scrollbar(self.tabla_frame, orient="vertical", command=self.tabla_resultados.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.tabla_resultados.configure(yscrollcommand=self.scroll_y.set)

        self.root.mainloop()            

    def calcular(self):
        x0 = float(self.entries["x0:"].get())
        y0 = float(self.entries["y0:"].get())
        h = float(self.entries["h:"].get())
        xf = float(self.entries["xf:"].get())
        fxy = self.entries["f(x, y):"].get()

        resultados = Metodos.runge_kutta(x0, y0, h, xf, fxy)

        for row in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(row)
        
        for resultado in resultados:
            self.tabla_resultados.insert("", "end", values=(resultado["n"], resultado["Xn"], resultado["Yn"], resultado["K1"], resultado["K2"], resultado["K3"], resultado["K4"], resultado["Yn+1"]))
    
    def limpiar_entradas(self):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)

        for row in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(row)
        
        self.entries["x0:"].focus()
