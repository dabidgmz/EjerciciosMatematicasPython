import tkinter as tk
from euler import Euler
from newton import Newton
from runge import Runge
from creditos import Creditos
from Instrucciones import Instrucciones
class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menú Principal")
        self.root.geometry("450x500")  
        self.root.configure(bg="#1E1E1E") 

        label = tk.Label(self.root, text="Calculadora Matematica", font=("Arial", 18, "bold"), 
                         bg="#1E1E1E", fg="#A97DFF")  
        label.pack(pady=20)

        self.crear_boton("Euler Mejorado", self.abrir_euler_mejorado, "#6A0DAD", "#A97DFF")
        self.crear_boton("Runge Kutta", self.abrir_runge_kulta, "#6A0DAD", "#A97DFF")
        self.crear_boton("Newton Raphson", self.abrir_newton_raphson, "#6A0DAD", "#A97DFF")
        self.crear_boton("Créditos", self.abrir_creditos, "#6A0DAD", "#A97DFF")
        self.crear_boton("Instrucciones", self.abrir_instrucciones, "#6A0DAD", "#A97DFF")

    def crear_boton(self, texto, comando, color_base, color_hover):
        btn = tk.Button(self.root, text=texto, font=("Arial", 14, "bold"), bg=color_base, fg="black",
                        activebackground=color_hover, activeforeground="black", bd=0, padx=10, pady=10,
                        width=25, relief="flat", cursor="hand2", borderwidth=5)
        btn.pack(pady=12)
        btn.bind("<Enter>", lambda e: btn.config(bg=color_hover))  
        btn.bind("<Leave>", lambda e: btn.config(bg=color_base))  
        btn.config(command=comando)

    def abrir_euler_mejorado(self):      
        self.root.destroy()                  
        Euler()

    def abrir_runge_kulta(self):
        self.root.destroy()
        Runge()

    def abrir_newton_raphson(self):
        self.root.destroy()
        Newton()

    def abrir_creditos(self):
        self.root.destroy()
        Creditos()

    def abrir_instrucciones(self):
        self.root.destroy()
        Instrucciones()

    def run(self):
        self.root.mainloop()


