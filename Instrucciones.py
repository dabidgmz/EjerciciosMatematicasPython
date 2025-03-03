import tkinter as tk
from tkinter import ttk

class Instrucciones:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Instrucciones")
        self.root.geometry("500x400")
        self.root.configure(bg="#1E1E1E")

        label = tk.Label(self.root, text="Instrucciones", font=("Arial", 18, "bold"), bg="#1E1E1E", fg="#A97DFF")
        label.pack(pady=10)

        # Frame para el texto y el scroll
        frame_texto = tk.Frame(self.root, bg="#1E1E1E")
        frame_texto.pack(pady=5, padx=10, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_texto)
        scrollbar.pack(side="right", fill="y")

        self.texto_info = tk.Text(frame_texto, font=("Arial", 12), bg="#282828", fg="white", wrap="word",
                                  yscrollcommand=scrollbar.set, padx=10, pady=10, relief="flat", height=12)
        self.texto_info.pack(expand=True, fill="both")
        scrollbar.config(command=self.texto_info.yview)

        info = """
        !Atencion para iniciar el proyecto debes tener isntalado
         pip install sympy
         pip install matplotlib
         pip install tkinter

        ➤ Calculadora Matemática:
        despues de decomprimir el folder EjericiosMatematicosPython
        debe ejecutar el archivo main.py para iniciar la aplicacion
        y mostrar la interfaz grafica del menu
        
        ➤ Euler Mejorado:
          - x0: Valor inicial de x
          - y0: Valor inicial de y
          - h: Tamaño del paso
          - xf: Valor final de x
          - f(x, y): Función diferencial
          - Multiplicar con "*", elevar con "**"
          - Ejemplo de Multiplicacion: 2*x*y (es igual a 2xy)
          - Ejemplo de Exponenciación: x**2 (es igual a x²)

        ➤ Runge-Kutta:
          - x0: Valor inicial de x
          - y0: Valor inicial de y
          - h: Tamaño del paso
          - xf: Valor final de x
          - f(x, y): Función diferencial
          - Ejemplo de Multiplicacion: 2*x*y (es igual a 2xy)
          - Ejemplo de Exponenciación: x**2 (es igual a x²)

        ➤ Newton-Raphson:
          - x1: Valor inicial de x
          - Precisión: Cantidad de decimales
          - fx: La función a evaluar
          - Ejemplo de Multiplicacion: 2*x*y (es igual a 2xy)
          - Ejemplo de Exponenciación: x**2 (es igual a x²)
        """

        self.texto_info.insert("1.0", info)
        self.texto_info.config(state="disabled")

        # Botón para volver al menú
        self.color_boton_menu = "#A97DFF"
        self.color_boton_texto = "black"
        self.boton_menu = tk.Button(self.root, text="Menú", font=("Arial", 12, "bold"),
                                    bg=self.color_boton_menu, fg=self.color_boton_texto,
                                    command=self.volver_menu_principal)
        self.boton_menu.pack(pady=10)

        self.root.mainloop()

    def volver_menu_principal(self):        
        self.root.withdraw()
        self.root.quit()
        import menu  
        menu_app = menu.Menu()  
        menu_app.run()

# Ejecutar la aplicación
if __name__ == "__main__":
    Instrucciones()
