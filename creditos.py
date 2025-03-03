import tkinter as tk 
class Creditos:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Créditos")
        self.root.geometry("450x300")
        self.root.configure(bg="#1E1E1E")

        label = tk.Label(self.root, text="Créditos", font=("Arial", 18, "bold"), bg="#1E1E1E", fg="#A97DFF")
        label.pack(pady=10)

        info = """
        Matricula: 22170035
        Nombre: David Gomez Herrera
        Carrera: ING. en Desarrollo y Gestión de Software
        Turno: Nocturno
        Grupo: 8º "C"
        """
        label_info = tk.Label(self.root, text=info, font=("Arial", 14), bg="#1E1E1E", fg="white", justify="left")
        label_info.pack(pady=10)

        self.color_boton_menu = "#A97DFF"
        self.color_boton_texto = "black"


        self.boton_menu = tk.Button(self.root, text="Menú", font=("Arial", 10, "bold"), bg=self.color_boton_menu, fg=self.color_boton_texto, command=self.volver_menu_principal)
        self.boton_menu.pack(pady=10)

        self.root.mainloop()

    def volver_menu_principal(self):        
        self.root.withdraw()
        self.root.quit()  
        import menu  
        menu_app = menu.Menu()  
        menu_app.run()
