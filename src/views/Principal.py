import tkinter as tk
from views.personas.Agregar import ViewAgregar
from views.personas.Mostrar import ViewMostrar

class ViewPrincipal:

    def __init__(self, root:tk.Tk):
        #Configurando la ventana
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.finalizarPrograma)

        self.root.title("Ventana Principal")
        self.root.geometry("200x200")

        # Configurando widgets
        self.crearLabel(texto="Conferencia", pady=10)

        btnFormulario = tk.Button(self.root, text="Ir a Formulario", command=self.abrirFormulario)
        btnFormulario.grid(row=1, column=0, pady=10)

        btnMostrar = tk.Button(self.root, text="Ver agregados", command=self.abrirMostrar)
        btnMostrar.grid(row=2, column=0, pady=10)


    def abrirFormulario(self):
        self.root.withdraw()
        rootSecundario = tk.Toplevel(self.root)
        ViewAgregar(rootSecundario, self)


    def abrirMostrar(self):
        self.root.withdraw()
        rootSecundario = tk.Toplevel(self.root)
        ViewMostrar(rootSecundario, self)
        

    def crearLabel(self, texto="", fila=0, columna=0, padx=0, pady=0):
        lblTitulo = tk.Label(self.root, text=texto)
        lblTitulo.grid(row=fila, column=columna, padx=padx, pady=pady)

    def finalizarPrograma(self):
        self.root.destroy()