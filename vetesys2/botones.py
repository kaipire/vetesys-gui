import os, sys
sys.path.append(os.getcwd()) # agregamos el directorio padre al path para que import busque tambien alli
os.chdir('..') # vamos al directorio padre
from tkinter import *
import getpass
import bd
text_font1 = ("Ubuntu", 10, "bold")

class BotonesCliente(Frame):
    '''     Clase que contiene botones que lo utilizaran los abms para la
       interaccion entre el sistema y el usuario. '''
    def __init__(self, root, abm_name):
        super().__init__(master = root)
        self.pack(side = 'top', pady = 0, padx = 0, ipadx = 0, anchor = 'nw')
        self.crear_widgets(nombre = abm_name)


    def crear_widgets(self, nombre):
        '''    Funcion que crea los botones a ser utilizados, ordenados en un panel. '''
        # panel de relleno
        self.panel0 = Frame(master = self)
        self.panel0.pack(ipady = 0, ipadx = 0)

        self.panel1 = Frame(master = self)
        self.panel1.pack(ipady = 0, ipadx = 0)
        # nombre del abm
        self.abm_name = Label(master = self.panel0, text = nombre, font = text_font1, bd = 15)
        self.abm_name.pack()

        ancho = 0 # ancho de los label´s
        largo_btn = 15 # largo de los label´s
        
        #panel
        self.panel2 = Frame(master = self,bd = 10, relief = GROOVE)
        self.panel2.pack(side = 'left', padx = 30, ipady = 0, ipadx = 0)

        #boton Listar
        self.btn_listar = Button(master = self.panel2, text = 'Listar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.listar )
        self.btn_listar.grid(row = 1, column = 0, sticky = 'nw', padx = 0)

        # boton registrar
        self.btn_agregar = Button(master = self.panel2, text = 'Registrar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.registrar)
        self.btn_agregar.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

        # boton buscar
        self.btn_buscar = Button(master = self.panel2, text = 'Buscar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.buscar)
        self.btn_buscar.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

        # boton editar
        self.btnEditar = Button(master = self.panel2, text = 'Modificar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.modificar)
        self.btnEditar.grid(row = 4, column = 0, sticky = 'nw', padx = 0)

        # boton borrar
        self.btn_borrar = Button(master = self.panel2, text = 'Eliminar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.borrar)
        self.btn_borrar.grid(row = 5, column = 0, sticky = 'nw', padx = 0)

        # boton add mascota
        self.btn_agregar = Button(master = self.panel2, text = 'Agregar Mascota', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.agregar)
        self.btn_agregar.grid(row = 6, column = 0, sticky = 'nw', padx = 0)

        # boton salir
        self.btn_salir = Button(master = self.panel2, text = 'Salir', font = text_font1, bg = 'pink',width = largo_btn,
        bd = 5, relief = RAISED,
        command = self.master.destroy)
        self.btn_salir.grid(row = 7, column = 0, sticky = 'nw', padx = 0)
        def activar_estado(self):
            print("no implementado")

class BotonesMascota(Frame):

    def __init__(self, root, abm_name):
        super().__init__(master = root)
        self.pack(side = 'top', pady = 0, padx = 0, ipadx = 0, anchor = 'nw')
        self.crear_widgets(nombre = abm_name)

    def crear_widgets(self, nombre):
        '''    Funcion que crea los botones a ser utilizados, ordenados en un panel. '''
        # panel de relleno
        self.panel0 = Frame(master = self)
        self.panel0.pack(ipady = 0, ipadx = 0)

        self.panel1 = Frame(master = self)
        self.panel1.pack(ipady = 0, ipadx = 0)
        # nombre del abm
        self.abm_name = Label(master = self.panel0, text = nombre, font = text_font1, bd = 15)
        self.abm_name.pack()

        ancho = 0 # ancho de los label´s
        largo_btn = 15 # largo de los label´s

        #panel
        self.panel2 = Frame(master = self,bd = 10, relief = GROOVE)
        self.panel2.pack(side = 'left', padx = 30, ipady = 0, ipadx = 0)

        #boton Listar
        self.btn_listar = Button(master = self.panel2, text = 'Listar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.listar )
        self.btn_listar.grid(row = 1, column = 0, sticky = 'nw', padx = 0)


        # boton mofificar
        self.btn_editar = Button(master = self.panel2, text = 'Modificar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.modificar)
        self.btn_editar.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

        # boton borrar
        self.btn_borrar = Button(master = self.panel2, text = 'Eliminar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.borrar)
        self.btn_borrar.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

        # boton mostrar historial
        self.btn_historial = Button(master = self.panel2, text = 'Historial', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.historial)
        self.btn_historial.grid(row = 4, column = 0, sticky = 'nw', padx = 0)

        # boton add servicio
        self.btn_servicio = Button(master = self.panel2, text = 'Servicios', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.servicio)
        self.btn_servicio.grid(row = 5, column = 0, sticky = 'nw', padx = 0)


        # boton salir
        self.btnSalir = Button(master = self.panel2, text = 'Salir', font = text_font1, bg = 'pink', width = largo_btn,
        bd = 5, relief = RAISED,
        command = self.master.destroy)
        self.btnSalir.grid(row = 6, column = 0, sticky = 'nw', padx = 0)

    def buscar(self):
            pass




class BotonesInsumos(Frame):
    '''     Clase que contiene botones que lo utilizaran los abms para la
       interaccion entre el sistema y el usuario. '''
    def __init__(self, root, abm_name):
        super().__init__(master = root)
        self.pack(side = 'top', pady = 0, padx = 0, ipadx = 0, anchor = 'nw')
        self.crear_widgets(nombre = abm_name)


    def crear_widgets(self, nombre):
        '''    Funcion que crea los botones a ser utilizados, ordenados en un panel. '''
        # panel de relleno
        self.panel0 = Frame(master = self)
        self.panel0.pack(ipady = 0, ipadx = 0)

        self.panel1 = Frame(master = self)
        self.panel1.pack(ipady = 0, ipadx = 0)
        # nombre del abm
        self.abm_name = Label(master = self.panel0, text = nombre, font = text_font1, bd = 15)
        self.abm_name.pack()

        ancho = 0 # ancho de los label´s
        largo_btn = 15 # largo de los label´s
        
        #panel
        self.panel2 = Frame(master = self,bd = 10, relief = GROOVE)
        self.panel2.pack(side = 'left', padx = 30, ipady = 0, ipadx = 0)

        #boton Listar
        self.btn_listar = Button(master = self.panel2, text = 'Listar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.listar )
        self.btn_listar.grid(row = 1, column = 0, sticky = 'nw', padx = 0)

        # boton registrar
        self.btn_agregar = Button(master = self.panel2, text = 'Registrar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,

        bd = 5, relief = RAISED, command = self.registrar)
        self.btn_agregar.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

        # boton buscar
        self.btn_buscar = Button(master = self.panel2, text = 'Buscar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.buscar)
        self.btn_buscar.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

        # boton modificar
        self.btn_editar = Button(master = self.panel2, text = 'Modificar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.modificar)
        self.btn_editar.grid(row = 4, column = 0, sticky = 'nw', padx = 0)

        # boton borrar
        self.btn_borrar = Button(master = self.panel2, text = 'Eliminar', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.borrar)
        self.btn_borrar.grid(row = 5, column = 0, sticky = 'nw', padx = 0)

        # boton vender
        self.btn_vender = Button(master = self.panel2, text = 'Venta', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.venta)
        self.btn_vender.grid(row = 6, column = 0, sticky = 'nw', padx = 0)


        # boton salir
        self.btn_salir = Button(master = self.panel2, text = 'Salir', font = text_font1, bg = 'pink',width = largo_btn,
        bd = 5, relief = RAISED,
        command = self.master.destroy)
        self.btn_salir.grid(row = 7, column = 0, sticky = 'nw', padx = 0)
        def activar_estado(self):
            print("no implementado")
