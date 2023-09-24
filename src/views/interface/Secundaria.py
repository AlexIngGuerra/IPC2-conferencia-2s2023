import tkinter as tk
from views.Config import raiz

class ViewSecundaria:

    def __init__(self, root:tk.Tk, viewAnterior:tk.Tk):
        # Configuraciones generales
        self.root = root
        self.viewAnterior = viewAnterior
        self.root.protocol("WM_DELETE_WINDOW", self.finalizarPrograma)

    # Funcion para crear un label
    def crearLabel(self, texto="", fila=0, columna=0, padx=0, pady=0):
        lblTitulo = tk.Label(self.root, text=texto)
        lblTitulo.grid(row=fila, column=columna, padx=padx, pady=pady)

    # Funcion para finalizar el programa al cerrar ventana
    def finalizarPrograma(self):
        raiz.destroy()

    # Funcion regresar a ventana anterior
    def regresar(self):
        self.root.destroy()
        self.viewAnterior.root.deiconify()