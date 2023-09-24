from views.interface.Secundaria import ViewSecundaria
from controllers.Lista import listaPersonas
import tkinter as tk
from tkinter import messagebox


class ViewMostrar(ViewSecundaria):

    def __init__(self, root:tk.Tk, viewAnterior:tk.Tk):
        super().__init__(root, viewAnterior)
        self.root.geometry("350x350")
        self.root.title("Mostrar Personas")

        lblTitulo = tk.Label(self.root, text="Listado")
        lblTitulo.grid(row=0, column=1, pady=10)

        self.initResultados()
        self.initBotones()
        self.actualizar()

    # Componentes: Botones
    def initBotones(self):
        btnRegresar = tk.Button(self.root, text="Regresar", command=self.regresar)
        btnRegresar.grid(row=9, column=1,padx=1, pady=5)

    def initResultados(self):
        self.crearLabel("Lista: ", 5,1,5,1)
        self.txtLista = tk.Listbox(self.root, width=50)

        scrollbarY = tk.Scrollbar(self.root, orient='vertical', command=self.txtLista.yview)
        scrollbarY.grid(row=6, column=2, sticky=tk.NS)
        self.txtLista['yscrollcommand'] = scrollbarY.set

        scrollbarX = tk.Scrollbar(self.root, orient='horizontal', command=self.txtLista.xview)
        scrollbarX.grid(row=7, column=1, sticky=tk.NSEW)
        self.txtLista['xscrollcommand'] = scrollbarX.set

        self.txtLista.grid(row=6, column=1, padx=1, pady=5)

    def actualizar(self):
        if len(listaPersonas)<1:
            messagebox.showerror("Error", "Lista de Personas vacía")
            return
        
        self.txtLista.delete(0, tk.END)
        for persona in listaPersonas:
            self.txtLista.insert("end", persona.toString())