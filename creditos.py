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
        Nombre: 22170035
        Carrera: ING. en Desarrollo y Gestión de Software
        Turno: Nocturno
        Grupo: 8º "C"
        """
        label_info = tk.Label(self.root, text=info, font=("Arial", 14), bg="#1E1E1E", fg="white", justify="left")
        label_info.pack(pady=10)
        self.root.mainloop()

