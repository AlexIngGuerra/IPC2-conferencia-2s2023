from views.interface.Secundaria import ViewSecundaria
from models.Persona import Persona
from controllers.Lista import listaPersonas
import tkinter as tk
from tkinter import messagebox


class ViewAgregar(ViewSecundaria):

    def __init__(self, root:tk.Tk, viewAnterior:tk.Tk):
        super().__init__(root, viewAnterior)
        self.root.geometry("400x300")
        self.root.title("Formulario")

        lblTitulo = tk.Label(self.root, text="Formulario Persona")
        lblTitulo.grid(row=0, column=1, pady=10)

        self.initFormulario()
        self.initBotones()

    def initFormulario(self):
        # Creamos los labels para cada entry
        self.crearLabel("Carnet", 1, 0, 5, 1)
        self.crearLabel("Nombre", 2, 0, 5, 1)
        self.crearLabel("Apellido", 3, 0, 5, 1)

        #Crear los entrys
        self.entryCarnet = self.crearEntry(1, 1)
        self.entryNombre = self.crearEntry(2, 1)
        self.entryApellido = self.crearEntry(3, 1)

        btnAgregar = tk.Button(self.root, text="Agregar", command=self.agregarPersona)
        btnAgregar.grid(row=4, column=1, pady=5)

    def crearEntry(self, row, column):
        entry = tk.Entry(self.root, text="", width=50)
        entry.grid(row=row, column=column)
        return entry
    
    # Componentes: Botones
    def initBotones(self):
        btnRegresar = tk.Button(self.root, text="Regresar", command=self.regresar)
        btnRegresar.grid(row=9, column=1,padx=1, pady=5)

    def agregarPersona(self):
        persona = Persona(self.entryCarnet.get(), self.entryNombre.get(), self.entryApellido.get())
        listaPersonas.append(persona)

        # Limpiamos los entrys
        self.entryCarnet.delete(0, tk.END)
        self.entryNombre.delete(0, tk.END)
        self.entryApellido.delete(0, tk.END)

        messagebox.showinfo("Correcto", "Ingresado: "+persona.toString())


