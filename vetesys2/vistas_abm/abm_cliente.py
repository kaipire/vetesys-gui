import sys
sys.path.append("../") #referencia al directorio base
from i18n import msg
import util
from controlador.vcontrol import PersonaControlador,MascotaControlador
from modulo.vmodel import Cliente, Mascota
from botones import BotonesCliente
from vistas_abm.abm_mascota import AbmMascota

import tkinter as tk 
from tkinter import *
text_font1 = ("Purisa", 10, "bold")

class AbmCliente(BotonesCliente):
    '''Clase que ayuda a la insercion, eliminacion y modificacion de los datos.'''

    def __init__(self, root):
        super().__init__(root, ".:: MENU CLIENTE ::.")

    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU CLIENTE ::.")
        root.largo = 1000
        root.ancho = 500
        #LARGOxANCHO+X+Y
        root.geometry('%dx%d+360+100'%(root.largo, root.ancho))
        root.resizable(width=False, height=False)
        root.focus_force()
        return root


    def listar(self):
        ''' Metodo que crea la ventana donde se mostrara la lista de cliente'''
        self.listar = Listar(self.crear_ventana())

    def registrar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para el registro de clientes y mascotas'''
        self.registrar = Registrar(self.crear_ventana())

    def buscar(self):
        ''' Metodo que crea la ventana donde se buscara el cliente'''
        self.buscar = Buscar(self.crear_ventana())

    def modificar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para la modificacion del registro'''
        self.modificar = Modificar(self.crear_ventana())

    def borrar(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el cliente'''
        self.borrar = Borrar(self.crear_ventana())

    def agregar(self):
        ''' Metodo que crea la ventana donde se permitira agregar una mascota el cliente'''
        self.agregar = Agregar(self.crear_ventana())    


#Listar
class Listar(Frame):
    '''Clase donde se visualiza la lista.  '''
    __controlador = PersonaControlador()

    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text=' .:: LISTADO DE CLIENTES ::.', font=text_font1)
        self.nombre_opcion.pack(pady = 10)        
        self.panel1 = Frame(master=self)
        self.panel1.pack(side='top')
        #largor de los label´s
        largo = 10

        '''cabecera de la tabla donde se muesta la lista'''
        self.cedula = Label(master=self.panel1, text='CEDULA', bg='purple', fg = 'white', width = 10,
                            justify='left', relief="ridge")
        self.cedula.pack(side='left')

        self.nombre = Label(master=self.panel1, text='NOMBRE COMPLETO', bg='purple', fg = 'white',width = 40,
                            justify='left', relief="ridge")
        self.nombre.pack(side='left')

        self.direccion = Label(master=self.panel1, text='DIRECCION', bg='purple', fg = 'white',width = 40,
                              justify='left', relief="ridge")
        self.direccion.pack(side='left')

        self.contacto = Label(master=self.panel1, text='CONTACTO', bg='purple', fg = 'white',width = 10,
                              justify='left', relief="ridge")
        self.contacto.pack(side='left')

        lista_clientes = self.get_controlador().get_lista_objetos()

        '''lista que recorre la lista de clientes y los muestra en pantalla'''
        for lista in lista_clientes:
            self.panel = Frame(master=self)
            self.panel.pack(side='top', ipadx=0)
            Label(master=self.panel, text=lista.get_cedula(),
                  relief="ridge", width=10, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_nombre(),
                  relief="ridge", width=40, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_direccion(),
                  relief="ridge", width=40, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_contacto(),
                  relief="ridge", width=10, bg = 'pink').pack(side='left')
            
            panel = None

        self.panel2 = Frame(master=self)
        self.panel2.pack(side='top')
        self.atras_btn = Button(master = self.panel2, text='Salir', font=text_font1, bg = 'purple', fg = 'pink',command = self.master.destroy)
        self.atras_btn.pack(side = BOTTOM, padx=10, pady = 10)

    def get_controlador(self):
        ''' retorna el controlador a ser utilizado'''
        return self.__controlador

#Registrar
class Registrar(Frame):
    ''' Clase que mostrara el formulario a ser llenado para el registro del objeto '''

    __controlador = PersonaControlador()
    __controlador2 = MascotaControlador()

    '''se declara los entry y lbl necesario para el correspondiente formulario'''
################ formulario cliente ########################
    __titulo_lbl = None
    __cedula_lbl = None
    __cedula_entry = None 
    __nombre_lbl = None
    __nombre_entry = None
    __direccion_lbl = None
    __direccion_entry = None
    __contacto_lbl = None
    __contacto_entry = None
    __titulo_lbl = None
    __salir_btn = None
    __guardar_btn = None
################ formulario mascota ########################
    __titulo2_lbl = None
    __id_lbl = None
    __id_entry = None 
    __nombre2_lbl = None
    __nombre2_entry = None
    __edad_lbl = None
    __edad_entry = None
    __peso_lbl = None
    __peso_entry = None
    __sexo_lbl = None
    __sexo_entry = None
    __raza_lbl = None
    __raza_entry = None
    __especie_lbl = None
    __especie_entry = None
    __cargar_btn = None
##########################################################################    
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50, pady = 15)
        self.__panel_master = panel_master
        self.panel1 = Frame(master = self)
        self.panel1.grid(row = 0, column = 0)
        self.panel_limpiar = None        
        self.lista_mascotas = []        
        self.inicializar()

        
##################### inicializar formulario cliente ##############################
    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('abm.cliente.titulo.registrar'))

        self.get_titulo_lbl()
        self.get_cedula_lbl()
        self.get_cedula_entry()
        self.get_nombre_lbl()
        self.get_nombre_entry()
        self.get_direccion_lbl()
        self.get_direccion_entry()
        self.get_contacto_lbl()
        self.get_contacto_entry()
        self.inicializar2()

#################### inicializar formulario mascota #########################
    def inicializar2(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        if self.panel_limpiar:
            self.get_id_entry().delete(0, 'end')
            self.get_nombre2_entry().delete(0, 'end')
            self.get_edad_entry().delete(0, 'end')
            self.get_peso_entry().delete(0, 'end')
            self.get_sexo_entry().delete(0, 'end')
            self.get_raza_entry().delete(0, 'end')
            self.get_especie_entry().delete(0, 'end')
            
        
        self.panel2 = Frame(master = self, bd = 10)
        self.panel2.grid(row = 2, column = 0)
        self.get_titulo2_lbl()
        self.get_id_lbl()
        self.get_id_entry()
        self.get_nombre2_lbl()
        self.get_nombre2_entry()
        self.get_edad_lbl()
        self.get_edad_entry()
        self.get_peso_lbl()
        self.get_peso_entry()
        self.get_sexo_lbl()
        self.get_sexo_entry()
        self.get_raza_lbl()
        self.get_raza_entry()
        self.get_especie_lbl()
        self.get_especie_entry()
        self.get_salir_btn()
        self.get_guardar_btn()
        self.get_cargar_btn()

################## PANEL CLIENTE ######################
    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self.panel1, text=" .:: REGISTRO DE CLIENTES ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_cedula_lbl(self):
        if not self.__cedula_lbl:
            self.__cedula_lbl = tk.Label(master=self.panel1, text="Cedula: ", width=10)
            self.__cedula_lbl.grid(row=1, column=0)
        return self.__cedula_lbl
        
    def get_cedula_entry(self):
        if not self.__cedula_entry:
            self.__cedula_entry = tk.Entry(master=self.panel1, width=20)
            self.__cedula_entry.focus()
            self.__cedula_entry.grid(row=1, column=1)
        return self.__cedula_entry
        
    def get_nombre_lbl(self):
        if not self.__nombre_lbl:
            self.__nombre_lbl = tk.Label(master=self.panel1, text="Nombre: ", width=10)
            self.__nombre_lbl.grid(row=2, column=0)
        return self.__nombre_lbl
        
    def get_nombre_entry(self):
        if not self.__nombre_entry:
            self.__nombre_entry = tk.Entry(master=self.panel1, width=20)
            self.__nombre_entry.grid(row=2, column=1)
        return self.__nombre_entry        
             
    def get_direccion_lbl(self):
        if not self.__direccion_lbl:
            self.__direccion_lbl = tk.Label(master=self.panel1, text="Direccion: ", width=10)
            self.__direccion_lbl.grid(row=3, column=0)
        return self.__direccion_lbl
        
    def get_direccion_entry(self):
        if not self.__direccion_entry:
            self.__direccion_entry = tk.Entry(master=self.panel1, width=20)
            self.__direccion_entry.grid(row=3, column=1)
        return self.__direccion_entry 
        
    def get_contacto_lbl(self):
        if not self.__contacto_lbl:
            self.__contacto_lbl = tk.Label(master=self.panel1, text="contacto: ", width=10)
            self.__contacto_lbl.grid(row=4, column=0)
        return self.__contacto_lbl
        
    def get_contacto_entry(self):
        if not self.__contacto_entry:
            self.__contacto_entry = tk.Entry(master=self.panel1, width=20)
            self.__contacto_entry.grid(row=4, column=1)
        return self.__contacto_entry
 


############################## funciones #################################################3
    def guardar_cliente(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        cedula = self.get_cedula_entry().get()
        nombre = self.get_nombre_entry().get()
        direccion = self.get_direccion_entry().get()
        contacto = self.get_contacto_entry().get()
        cliente = Cliente(contacto, self.lista_mascotas, cedula = cedula, nombre = nombre, direccion = direccion)

        try:
            self.get_controlador().crear(cliente) 
            messagebox.showinfo("", "Registro Creado")
        except Exception as e:
            messagebox.showinfo("", e)

    def cargar_mascota(self):
        '''Metodo que cargar la mascota en la lista del cliente y guardar mascota en la bd'''
        identificador = self.get_id_entry().get()
        nombre = self.get_nombre2_entry().get()
        edad = self.get_edad_entry().get()
        peso = self.get_peso_entry().get()
        sexo = self.get_sexo_entry().get()
        raza = self.get_raza_entry().get()
        especie = self.get_especie_entry().get()
        mascota = Mascota(identificador, nombre, edad, peso, sexo, especie, raza)
        #self.lista_mascotas.append(mascota)
        try:
            self.get_controlador2().crear(mascota)
            self.lista_mascotas.append(mascota) 
            messagebox.showinfo("", "Registro Creado")
        except Exception as e:
            messagebox.showinfo("", e)
        self.panel_limpiar = self.panel2
        self.inicializar2()

############################ PANEL MASCOTA ######################################

    def get_titulo2_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo2_lbl:
            self.__titulo2_lbl = tk.Label(master=self.panel2, text=" .:: REGISTRO DE MASCOTAS ::. ",  font=text_font1, pady = 10)
            self.__titulo2_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo2_lbl
                   
    def get_id_lbl(self):
        if not self.__id_lbl:
            self.__id_lbl = tk.Label(master=self.panel2, text="ID: ", width=10)
            self.__id_lbl.grid(row=1, column=0)
        return self.__id_lbl
        
    def get_id_entry(self):
        if not self.__id_entry:
            self.__id_entry = tk.Entry(master=self.panel2, width=20)
            self.__id_entry.focus()
            self.__id_entry.grid(row=1, column=1)
        return self.__id_entry
           
    def get_nombre2_lbl(self):
        if not self.__nombre2_lbl:
            self.__nombre2_lbl = tk.Label(master=self.panel2, text="Nombre: ", width=10)
            self.__nombre2_lbl.grid(row=2, column=0)
        return self.__nombre2_lbl
        
    def get_nombre2_entry(self):
        if not self.__nombre2_entry:
            self.__nombre2_entry = tk.Entry(master=self.panel2, width=20)
            self.__nombre2_entry.grid(row=2, column=1)
        return self.__nombre2_entry        
             
    def get_edad_lbl(self):
        if not self.__edad_lbl:
            self.__edad_lbl = tk.Label(master=self.panel2, text="Edad: ", width=10)
            self.__edad_lbl.grid(row=3, column=0)
        return self.__edad_lbl
        
    def get_edad_entry(self):
        if not self.__edad_entry:
            self.__edad_entry = tk.Entry(master=self.panel2, width=20)
            self.__edad_entry.grid(row=3, column=1)
        return self.__edad_entry 
        
    def get_peso_lbl(self):
        if not self.__peso_lbl:
            self.__peso_lbl = tk.Label(master=self.panel2, text="Peso: ", width=10)
            self.__peso_lbl.grid(row=4, column=0)
        return self.__peso_lbl
        
    def get_peso_entry(self):
        if not self.__peso_entry:
            self.__peso_entry = tk.Entry(master=self.panel2, width=20)
            self.__peso_entry.grid(row=4, column=1)
        return self.__peso_entry

    def get_sexo_lbl(self):
        if not self.__sexo_lbl:
            self.__sexo_lbl = tk.Label(master=self.panel2, text="Sexo: ", width=10)
            self.__sexo_lbl.grid(row=5, column=0)
        return self.__sexo_lbl
        
    def get_sexo_entry(self):
        if not self.__sexo_entry:
            self.__sexo_entry = tk.Entry(master=self.panel2, width=20)
            self.__sexo_entry.grid(row=5, column=1)
        return self.__sexo_entry

    def get_raza_lbl(self):
        if not self.__raza_lbl:
            self.__raza_lbl = tk.Label(master=self.panel2, text="Raza: ", width=10)
            self.__raza_lbl.grid(row=6, column=0)
        return self.__raza_lbl
        
    def get_raza_entry(self):
        if not self.__raza_entry:
            self.__raza_entry = tk.Entry(master=self.panel2, width=20)
            self.__raza_entry.grid(row=6, column=1)
        return self.__raza_entry

    def get_especie_lbl(self):
        if not self.__especie_lbl:
            self.__especie_lbl = tk.Label(master=self.panel2, text="Especie: ", width=10)
            self.__especie_lbl.grid(row=7, column=0)
        return self.__especie_lbl
        
    def get_especie_entry(self):
        if not self.__especie_entry:
            self.__especie_entry = tk.Entry(master=self.panel2, width=20)
            self.__especie_entry.grid(row=7, column=1)
        return self.__especie_entry

    def get_cargar_btn(self):
        if not self.__cargar_btn:
            self.__cargar_btn = tk.Button(master=self.panel2, text="Cargar", bg = 'white', command=self.cargar_mascota) 
            self.__cargar_btn.grid(row=8, column=0)
        return self.__cargar_btn


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self.panel2, text="Guardar", bg = 'white', command=self.guardar_cliente) 
            self.__guardar_btn.grid(row=8, column=1)
        return self.__guardar_btn      

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self.panel2, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=8, column=2)
        return self.__salir_btn
################################################################################################### 
    '''controlador cliente'''
    def get_controlador(self):
        return self.__controlador

    '''controlador mascota'''
    def get_controlador2(self):
        return self.__controlador2


class Buscar(Frame):
    '''Clase que busca el objeto y retorna para su visualizacion en la pantalla. '''
    __controlador = PersonaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text='.:: BUSCAR CLIENTE ::.', font=text_font1)
        self.nombre_opcion.pack()
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta2 = Label(master=self.panel1, text='Ingrese el numero de cedula:', font=text_font1)
        self.etiqueta2.pack(side='left', pady=10)
        self.cedula = Entry(master=self.panel1, width = 30)
        self.cedula.pack(side='left')
        self.cedula.focus_force()
        #boton buscar
        self.buscar_btn = Button(master=self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_cliente)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)


    def buscar_cliente(self):
        ''' Metodo que busca el objeto a traves del controlador y lo muestra en la pantalla.'''
        cliente = self.get_controlador().buscar_cod(self.cedula.get())
        if not cliente:
            messagebox.showinfo("", "Registro no existe")
        else:
            if self.panel_buscar:
                self.panel_buscar.destroy()
                self.panel_buscar = None
            panel1 = Frame(master=self)
            panel1.pack(side='left', ipadx=5, fill='y')
            self.panel_buscar = panel1
            panel2 = Frame(master=panel1)
            panel2.pack(side='top', ipadx=10)

            Label(master=panel2,
                  text='Cedula : {}'.format(cliente.get_cedula()),
                  fg='black', anchor='nw', font=text_font1).grid(row = 1, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Nombre : {}'.format(cliente.get_nombre()),
                  fg='black', anchor='nw', font=text_font1).grid(row = 2, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Direccion: {}'.format(cliente.get_direccion()),
                  fg='black', anchor='nw', font=text_font1).grid(row = 3, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Contacto: {}'.format(cliente.get_contacto()),
                  fg='black', anchor='nw', font=text_font1).grid(row = 4, column = 0, sticky = 'w')
            largo = 10 
            self.panel_aux = Frame(master = self)
            self.panel_aux.pack(side = 'top')

            self.id = Label(master=self.panel_aux, text='ID', bg = 'purple', fg = "white", width = largo,
                            justify='left', relief="ridge")
            self.id.pack(side='left')

            self.nombre = Label(master=self.panel_aux, text='NOMBRE', bg = 'purple', fg = "white",width = largo,
                            justify='left', relief="ridge")
            self.nombre.pack(side='left')

            self.edad = Label(master=self.panel_aux, text='EDAD', bg = 'purple', fg = "white",width = largo,
                              justify='left', relief="ridge")
            self.edad.pack(side='left')

            self.peso = Label(master=self.panel_aux, text='PESO', bg = 'purple', fg = "white",width = largo,
                              justify='left', relief="ridge")
            self.peso.pack(side='left')

            self.sexo = Label(master=self.panel_aux, text='SEXO', bg = 'purple', fg = "white",width = largo,
                              justify='left', relief="ridge")
            self.sexo.pack(side='left')

            self.especie = Label(master=self.panel_aux, text='ESPECIE', bg = 'purple', fg = "white",width = largo,
                              justify='left', relief="ridge")
            self.especie.pack(side='left')

            self.raza = Label(master=self.panel_aux, text='RAZA', bg = 'purple', fg = "white",width = largo,
                              justify='left', relief="ridge")
            self.raza.pack(side='left')

            for lista in cliente.get_mascotas():
                self.panel = Frame(master=self)
                self.panel.pack(side='top', ipadx=0)
                Label(master=self.panel, text=lista.get_identificador(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_nombre(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_edad(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_peso(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_sexo(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_raza(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')
                Label(master=self.panel, text=lista.get_especie(),
                      relief="ridge", width=largo, bg = 'pink').pack(side='left')

            panel = None


    def get_controlador(self):
        return self.__controlador

class Modificar(Frame):
    '''Clase que muestra un formulario con los datos a modificar del objeto buscado.'''
    __controlador = PersonaControlador()
    __titulo_lbl = None
    __cedula_lbl = None
    __cedula_entry = None 
    __nombre_lbl = None
    __nombre_entry = None
    __direccion_lbl = None
    __direccion_entry = None
    __contacto_lbl = None
    __contacto_entry = None
    __guardar_btn = None
    
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta2 = Label(master=self.panel1, text='Ingrese el numero de cedula:', font=text_font1)
        self.etiqueta2.pack(side='left', pady=10)
        self.cedula = Entry(master=self.panel1, width = 30)
        self.cedula.pack(side='left')
        self.cedula.focus_force()
        #boton buscar
        self.buscar_btn = Button(master = self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_cliente)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)
 
    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('abm.cliente.titulo.actualizar'))
        self.panel2 = Frame(master=self)
        self.panel2.pack(ipady=10, fill='x')
        self.get_titulo_lbl()
        self.get_cedula_lbl()
        self.get_cedula_entry()
        self.get_nombre_lbl()
        self.get_nombre_entry()
        self.get_direccion_lbl()
        self.get_direccion_entry()
        self.get_contacto_lbl()
        self.get_contacto_entry()
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para el titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self.panel2, text=" .:: MODIFICAR DATOS DEL CLIENTE::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_cedula_lbl(self):
        if not self.__cedula_lbl:
            self.__cedula_lbl = tk.Label(master=self.panel2, text="Cedula: ", width=10)
            self.__cedula_lbl.grid(row=1, column=0)
        return self.__cedula_lbl
        
    def get_cedula_entry(self):
        if not self.__cedula_entry:
            self.__cedula_entry = tk.Entry(master=self.panel2, width=20)
            self.__cedula_entry.focus()
            self.__cedula_entry.grid(row=1, column=1)
        return self.__cedula_entry
        
    def get_nombre_lbl(self):
        if not self.__nombre_lbl:
            self.__nombre_lbl = tk.Label(master=self.panel2, text="Nombre: ", width=10)
            self.__nombre_lbl.grid(row=2, column=0)
        return self.__nombre_lbl
        
    def get_nombre_entry(self):
        if not self.__nombre_entry:
            self.__nombre_entry = tk.Entry(master=self.panel2, width=20)
            self.__nombre_entry.grid(row=2, column=1)
        return self.__nombre_entry        
             
    def get_direccion_lbl(self):
        if not self.__direccion_lbl:
            self.__direccion_lbl = tk.Label(master=self.panel2, text="Direccion: ", width=10)
            self.__direccion_lbl.grid(row=5, column=0)
        return self.__direccion_lbl
        
    def get_direccion_entry(self):
        if not self.__direccion_entry:
            self.__direccion_entry = tk.Entry(master=self.panel2, width=20)
            self.__direccion_entry.grid(row=5, column=1)
        return self.__direccion_entry 
        
    def get_contacto_lbl(self):
        if not self.__contacto_lbl:
            self.__contacto_lbl = tk.Label(master=self.panel2, text="contacto: ", width=10)
            self.__contacto_lbl.grid(row=4, column=0)
        return self.__contacto_lbl
        
    def get_contacto_entry(self):
        if not self.__contacto_entry:
            self.__contacto_entry = tk.Entry(master=self.panel2, width=20)
            self.__contacto_entry.grid(row=4, column=1)
        return self.__contacto_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self.panel2, text="Guardar", bg = 'white', command=self.guardar_cliente) 
            self.__guardar_btn.grid(row=9, column=1)
        return self.__guardar_btn      
        
    def guardar_cliente(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        cliente = self.get_controlador().buscar_cod(self.cedula.get())
        cedula = self.get_cedula_entry().get()
        nombre = self.get_nombre_entry().get()
        direccion = self.get_direccion_entry().get()
        contacto = self.get_contacto_entry().get()
        aux = self.get_controlador().buscar_cod(cedula)
        mascotas = aux.get_mascotas()
        cliente = Cliente(contacto, mascotas,cedula=cedula,nombre=nombre,direccion=direccion)
        try:
            self.get_controlador().actualizar(cliente) 
            messagebox.showinfo("", "Registro Actualizado")
        except Exception as e:
            messagebox.showinfo("", e)

    def buscar_cliente(self):
        cliente = self.get_controlador().buscar_cod(self.cedula.get())
        if not cliente:
            messagebox.showinfo("", "Registro no existe")
        else:
            self.inicializar()
            # primero borramos lo que haya en los Entrys
            self.get_cedula_entry().delete(0, 'end')
            self.get_nombre_entry().delete(0, 'end')
            self.get_direccion_entry().delete(0, 'end')
            self.get_contacto_entry().delete(0, 'end')
            # insertamos
            self.get_cedula_entry().insert(0, cliente.get_cedula())
            self.get_nombre_entry().insert(0, cliente.get_nombre())
            self.get_direccion_entry().insert(0, cliente.get_direccion())
            self.get_contacto_entry().insert(0, cliente.get_contacto())
            
    def get_controlador(self):
        return self.__controlador



class Borrar(Frame):
    ''' Clase que ayuda a la eliminacion del objeto buscado.'''
    __controlador = PersonaControlador()
    __controlador2 = MascotaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.__panel_master = panel_master
        self.pack()
        self.nombre_borrar = tk.Label(master=self, text='.:: BORRAR CLIENTE ::.', font=text_font1)
        self.nombre_borrar.pack()
        
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
           
        self.etiqueta = Label(master=self.panel1, text='Ingrese el numero de cédula:', font=text_font1)
        self.etiqueta.pack(side='left', pady=10)
        self.cedula = Entry(master=self.panel1,width=30)
        self.cedula.pack(side='left')
        self.cedula.focus_force()
        self.borrar_boton = Button(master=self.panel1, text='Borrar', font=text_font1, bg='white',command = self.borrar_cliente)
        self.borrar_boton.pack(side='left', padx=10)
        #boton atras
        self.atras_boton = tk.Button(master = self.panel1, text='Volver', font=text_font1,bg='white',command=self.master.destroy)
        self.atras_boton.pack(side ='left', padx=10) 

    def borrar_cliente(self):
        '''Metodo que busca el objeto a traves del controlador por ID y lo elimina. '''
        cedula = self.cedula.get()
        cliente = self.get_controlador().buscar_cod(cedula)
        #self.get_controlador().borrar(cliente)
        if not cliente:
            messagebox.showinfo("", "Registro no existe")
        else:
            try:
                for mascota in cliente.get_mascotas():
                    self.get_controlador2().borrar(mascota)
                self.get_controlador().borrar(cliente)
                messagebox.showinfo("",'Registro borrado con exito!')
            except Exception as e:
                messagebox.showinfo("",e)

    def get_controlador(self):
        return self.__controlador

    def get_controlador2(self):
       return self.__controlador2

class Agregar(Frame):
    '''Esta clase sirve para agregar mascotas a la lista de cliente'''

    '''se define entry y lbl necesario para el panel'''
    __titulo_lbl = None
    __id_lbl = None
    __id_entry = None 
    __nombre_lbl = None
    __nombre_entry = None
    __edad_lbl = None
    __edad_entry = None
    __peso_lbl = None
    __peso_entry = None
    __sexo_lbl = None
    __sexo_entry = None
    __raza_lbl = None
    __raza_entry = None
    __especie_lbl = None
    __especie_entry = None
    __guardar_btn = None
    __agregar_btn = None

    __controlador = PersonaControlador()
    __controlador2 = MascotaControlador()

    def __init__(self, panel_master):
        '''se define el panel principal a utilizar'''
        super().__init__(master=panel_master)
        self.__panel_master = panel_master
        self.grid(row = 0, column = 0)
        self.lista_mascotas = []
        self.nombre_borrar = tk.Label(master=self, text='.:: AGREGAR MASCOTA ::.', font=text_font1)
        self.nombre_borrar.grid()        
        self.panel = Frame(master=self)
        self.panel.grid(row = 1, column = 0)
        self.etiqueta = Label(master=self.panel, text='Ingrese cedula del cliente:', font=text_font1)
        self.etiqueta.grid(row = 1, column = 0)
        self.cedula = Entry(master=self.panel,width=30)
        self.cedula.grid(row = 1, column = 1)
        self.cedula.focus_force()
        self.buscar_boton = Button(master=self.panel, text='Buscar', font=text_font1, bg='white',command = self.buscar_cliente)
        self.buscar_boton.grid(row = 1, column = 2)
        #boton atras
        self.atras_boton = tk.Button(master = self.panel, text='Volver', font=text_font1,bg='white',command=self.master.destroy)
        self.atras_boton.grid(row = 1, column = 3)
     

    def inicializar(self):
        '''se inicializan los entry y lbl'''  
        self.get_id_lbl()
        self.get_id_entry()
        self.get_nombre_lbl()
        self.get_nombre_entry()
        self.get_edad_lbl()
        self.get_edad_entry()
        self.get_peso_lbl()
        self.get_peso_entry()
        self.get_sexo_lbl()
        self.get_sexo_entry()
        self.get_raza_lbl()
        self.get_raza_entry()
        self.get_especie_lbl()
        self.get_especie_entry()
        self.get_agregar_btn()

                   
    def get_id_lbl(self):
        if not self.__id_lbl:
            self.__id_lbl = tk.Label(master=self.panel, text="ID: ", width=10)
            self.__id_lbl.grid(row=2, column=0)
        return self.__id_lbl
        
    def get_id_entry(self):
        if not self.__id_entry:
            self.__id_entry = tk.Entry(master=self.panel, width=20)
            self.__id_entry.focus()
            self.__id_entry.grid(row=2, column=1)
        return self.__id_entry
           
    def get_nombre_lbl(self):
        if not self.__nombre_lbl:
            self.__nombre_lbl = tk.Label(master=self.panel, text="Nombre: ", width=10)
            self.__nombre_lbl.grid(row=3, column=0)
        return self.__nombre_lbl
        
    def get_nombre_entry(self):
        if not self.__nombre_entry:
            self.__nombre_entry = tk.Entry(master=self.panel, width=20)
            self.__nombre_entry.grid(row=3, column=1)
        return self.__nombre_entry        
             
    def get_edad_lbl(self):
        if not self.__edad_lbl:
            self.__edad_lbl = tk.Label(master=self.panel, text="Edad: ", width=10)
            self.__edad_lbl.grid(row=4, column=0)
        return self.__edad_lbl
        
    def get_edad_entry(self):
        if not self.__edad_entry:
            self.__edad_entry = tk.Entry(master=self.panel, width=20)
            self.__edad_entry.grid(row=4, column=1)
        return self.__edad_entry 
        
    def get_peso_lbl(self):
        if not self.__peso_lbl:
            self.__peso_lbl = tk.Label(master=self.panel, text="Peso: ", width=10)
            self.__peso_lbl.grid(row=5, column=0)
        return self.__peso_lbl
        
    def get_peso_entry(self):
        if not self.__peso_entry:
            self.__peso_entry = tk.Entry(master=self.panel, width=20)
            self.__peso_entry.grid(row=5, column=1)
        return self.__peso_entry

    def get_sexo_lbl(self):
        if not self.__sexo_lbl:
            self.__sexo_lbl = tk.Label(master=self.panel, text="Sexo: ", width=10)
            self.__sexo_lbl.grid(row=6, column=0)
        return self.__sexo_lbl
        
    def get_sexo_entry(self):
        if not self.__sexo_entry:
            self.__sexo_entry = tk.Entry(master=self.panel, width=20)
            self.__sexo_entry.grid(row=6, column=1)
        return self.__sexo_entry

    def get_raza_lbl(self):
        if not self.__raza_lbl:
            self.__raza_lbl = tk.Label(master=self.panel, text="Raza: ", width=10)
            self.__raza_lbl.grid(row=7, column=0)
        return self.__raza_lbl
        
    def get_raza_entry(self):
        if not self.__raza_entry:
            self.__raza_entry = tk.Entry(master=self.panel, width=20)
            self.__raza_entry.grid(row=7, column=1)
        return self.__raza_entry

    def get_especie_lbl(self):
        if not self.__especie_lbl:
            self.__especie_lbl = tk.Label(master=self.panel, text="Especie: ", width=10)
            self.__especie_lbl.grid(row=8, column=0)
        return self.__especie_lbl
        
    def get_especie_entry(self):
        if not self.__especie_entry:
            self.__especie_entry = tk.Entry(master=self.panel, width=20)
            self.__especie_entry.grid(row=8, column=1)
        return self.__especie_entry

    def get_agregar_btn(self):
        if not self.__agregar_btn:
            self.__agregar_btn = tk.Button(master=self.panel, text="Agregar", bg = 'white', command=self.agregar_mascota) 
            self.__agregar_btn.grid(row=9, column=1)
        return self.__agregar_btn

    def buscar_cliente(self):
        cedula = self.cedula.get()
        cliente = self.get_controlador().buscar_cod(cedula)
        if not cliente:
            messagebox.showinfo("", "Registro no existe")
        else:
            self.inicializar() 

    def agregar_mascota(self):
        cedula = self.cedula.get()
        cliente = self.get_controlador().buscar_cod(cedula)
        if not cliente:
            messagebox.showinfo("", "Registro no existe")
        else:
            '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
            identificador = self.get_id_entry().get()
            nombre = self.get_nombre_entry().get()
            edad = self.get_edad_entry().get()
            peso = self.get_peso_entry().get()
            sexo = self.get_sexo_entry().get()
            raza = self.get_raza_entry().get()
            especie = self.get_especie_entry().get()

            mascota = Mascota(identificador, nombre, edad, peso, sexo, especie, raza)
            self.lista_mascotas.append(mascota)
            for i in cliente.get_mascotas():
                self.lista_mascotas.append(i)
            
            cliente.set_mascotas(self.lista_mascotas)
            self.get_controlador().actualizar(cliente)
            try:
                self.get_controlador2().crear(mascota) 
                messagebox.showinfo("", "Registro Creado")
            except Exception as e:
                messagebox.showinfo("", e)

    '''controlador de la clase persona para el abmCliente'''
    def get_controlador(self):
        return self.__controlador

    '''controlador de la clase mascota'''
    def get_controlador2(self):
        return self.__controlador2



if __name__ == '__main__':
    root = tk.Tk()
    cliente = AbmCliente(root)
    root.mainloop() 
