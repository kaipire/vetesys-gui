import sys
sys.path.append("../")
from i18n import msg
import util
from controlador.vcontrol import PersonaControlador, MascotaControlador
from modulo.vmodel import Cliente, Modulo, Menu, Mascota
from vistas_abm.abm_servicio import RegistrarConsulta,RegistrarVacuna, RegistrarAseo
import tkinter as tk 
from tkinter import *
from botones import BotonesMascota
text_font1 = ("Purisa", 10, "bold")
#from abm.abm_cliente import ModuloCliente


class AbmMascota(BotonesMascota):
    '''Clase que ayuda a la insercion, eliminacion y modificacion de los datos.'''

    def __init__(self, root):
        super().__init__(root, ".:: MENU MASCOTA ::.")

    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU MASCOTA ::.")
        root.largo = 1000
        root.ancho = 500
        #LARGOxANCHO+X+Y
        root.geometry('%dx%d+360+100'%(root.largo, root.ancho))
        root.resizable(width=False, height=False)

        root.focus_force()
        return root


    def listar(self):
        ''' Metodo que crea la ventana donde se mostrara la lista'''
        self.listar = Listar(self.crear_ventana())

    def modificar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para la modificacion del registro'''
        self.modificar = Modificar(self.crear_ventana())

    def borrar(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el objeto'''
        self.borrar = Borrar(self.crear_ventana())

    def historial(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el objeto'''
        self.historial = Historial(self.crear_ventana())

    def servicio(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el objeto'''
        self.servicio = Servicio(self.crear_ventana())

#Listar
class Listar(Frame):
    '''Clase donde se visualiza la lista.  '''
    __controlador = MascotaControlador()

    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text=' .:: LISTADO DE MASCOTAS ::.', font=text_font1)
        self.nombre_opcion.pack(pady = 10)        
        self.panel1 = Frame(master=self)
        self.panel1.pack(side='top')
        #largor de los label´s
        largo = 10 
        self.id = Label(master=self.panel1, text='ID', bg='purple', fg = 'white', width = largo,
                            justify='left', relief="ridge")
        self.id.pack(side='left')

        self.nombre = Label(master=self.panel1, text='NOMBRE', bg='purple', fg = 'white',width = largo,
                            justify='left', relief="ridge")
        self.nombre.pack(side='left')

        self.edad = Label(master=self.panel1, text='EDAD', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.edad.pack(side='left')

        self.peso = Label(master=self.panel1, text='PESO', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.peso.pack(side='left')

        self.sexo = Label(master=self.panel1, text='SEXO', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.sexo.pack(side='left')

        self.especie = Label(master=self.panel1, text='ESPECIE', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.especie.pack(side='left')

        self.raza = Label(master=self.panel1, text='RAZA', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.raza.pack(side='left')



        lista_mascotas = self.get_controlador().get_lista_objetos()

        for lista in lista_mascotas:
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

        self.panel2 = Frame(master=self)
        self.panel2.pack(side='top')
        self.atras_btn = Button(master = self.panel2, text='Salir', font=text_font1, bg = 'purple', fg = 'pink', command = self.master.destroy)
        self.atras_btn.pack(side = BOTTOM, padx=10, pady = 10)

    def get_controlador(self):
        ''' retorna el controlador a ser utilizado'''
        return self.__controlador

#Registrar
class Registrar(Frame):
    ''' Clase que mostrara el formulario a ser llenado para el registro del objeto ''' 
    __controlador = MascotaControlador()
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
    __expecie_lbl = None
    __especie_entry = None
    __salir_btn = None
    __guardar_btn = None
    
    
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50, pady = 15)
        self.__panel_master = panel_master
        self.inicializar()

    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('Mascotas'))
        self.get_titulo_lbl()
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
        self.get_salir_btn()
        self.get_guardar_btn()
        self.get_cargar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self, text=" .:: REGISTRO DE MASCOTAS ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_id_lbl(self):
        if not self.__id_lbl:
            self.__id_lbl = tk.Label(master=self, text="ID: ", width=10)
            self.__id_lbl.grid(row=1, column=0)
        return self.__id_lbl
        
    def get_id_entry(self):
        if not self.__id_entry:
            self.__id_entry = tk.Entry(master=self, width=20)
            self.__id_entry.focus()
            self.__id_entry.grid(row=1, column=1)
        return self.__id_entry
        
    def get_nombre_lbl(self):
        if not self.__nombre_lbl:
            self.__nombre_lbl = tk.Label(master=self, text="Nombre: ", width=10)
            self.__nombre_lbl.grid(row=2, column=0)
        return self.__nombre_lbl
        
    def get_nombre_entry(self):
        if not self.__nombre_entry:
            self.__nombre_entry = tk.Entry(master=self, width=20)
            self.__nombre_entry.grid(row=2, column=1)
        return self.__nombre_entry        
             
    def get_edad_lbl(self):
        if not self.__edad_lbl:
            self.__edad_lbl = tk.Label(master=self, text="Edad: ", width=10)
            self.__edad_lbl.grid(row=3, column=0)
        return self.__edad_lbl
        
    def get_edad_entry(self):
        if not self.__edad_entry:
            self.__edad_entry = tk.Entry(master=self, width=20)
            self.__edad_entry.grid(row=3, column=1)
        return self.__edad_entry 
        
    def get_peso_lbl(self):
        if not self.__peso_lbl:
            self.__peso_lbl = tk.Label(master=self, text="Peso: ", width=10)
            self.__peso_lbl.grid(row=4, column=0)
        return self.__peso_lbl
        
    def get_peso_entry(self):
        if not self.__peso_entry:
            self.__peso_entry = tk.Entry(master=self, width=20)
            self.__peso_entry.grid(row=4, column=1)
        return self.__peso_entry

    def get_sexo_lbl(self):
        if not self.__sexo_lbl:
            self.__sexo_lbl = tk.Label(master=self, text="Sexo: ", width=10)
            self.__sexo_lbl.grid(row=5, column=0)
        return self.__sexo_lbl
        
    def get_sexo_entry(self):
        if not self.__sexo_entry:
            self.__sexo_entry = tk.Entry(master=self, width=20)
            self.__sexo_entry.grid(row=5, column=1)
        return self.__sexo_entry

    def get_raza_lbl(self):
        if not self.__raza_lbl:
            self.__raza_lbl = tk.Label(master=self, text="Raza: ", width=10)
            self.__raza_lbl.grid(row=6, column=0)
        return self.__raza_lbl
        
    def get_raza_entry(self):
        if not self.__raza_entry:
            self.__raza_entry = tk.Entry(master=self, width=20)
            self.__raza_entry.grid(row=6, column=1)
        return self.__raza_entry

    def get_especie_lbl(self):
        if not self.__especie_lbl:
            self.__especie_lbl = tk.Label(master=self, text="Especie: ", width=10)
            self.__especie_lbl.grid(row=7, column=0)
        return self.__especie_lbl
        
    def get_especie_entry(self):
        if not self.__especie_entry:
            self.__especie_entry = tk.Entry(master=self, width=20)
            self.__especie_entry.grid(row=7, column=1)
        return self.__especie_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self, text="Guardar", bg = 'white', command=self.guardar_mascota) 
            self.__guardar_btn.grid(row=8, column=0)
        return self.__guardar_btn      

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=8, column=1)
        return self.__salir_btn

    def guardar_mascota(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        identificador = self.get_id_entry().get()
        nombre = self.get_nombre_entry().get()
        edad = self.get_edad_entry().get()
        peso = self.get_peso_entry().get()
        sexo = self.get_sexo_entry().get()
        raza = self.get_raza_entry().get()
        especie = self.get_especie_entry().get()

        mascota = Mascota(identificador, nombre, edad, peso, sexo, especie, raza)


        try:
            self.get_controlador().crear(mascota) 
            messagebox.showinfo("", "Registro Creado")
        except Exception as e:
            messagebox.showinfo("", e)

    def get_controlador(self):
        return self.__controlador

class Buscar(Frame):
    '''Clase que busca el objeto y retorna para su visualizacion en la pantalla. '''
    __controlador = MascotaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text='.:: BUSCAR MASCOTA ::.', font=text_font1)
        self.nombre_opcion.pack()
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta2 = Label(master=self.panel1, text='Ingrese el ID de la mascota:', font=text_font1)
        self.etiqueta2.pack(side='left', pady=10)
        self.id = Entry(master=self.panel1, width = 30)
        self.id.pack(side='left')
        self.id.focus_force()
        #boton buscar
        self.buscar_btn = Button(master=self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_mascota)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)


    def buscar_mascota(self):
        ''' Metodo que busca el objeto a traves del controlador y lo muestra en la pantalla.'''
        mascota = self.get_controlador().buscar_cod(self.id.get())
        if not mascota:
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
                  text='ID : {}'.format(mascota.get_identificador()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 1, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Nombre : {}'.format(mascota.get_nombre()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 2, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Edad: {}'.format(mascota.get_edad()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 3, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Peso: {}'.format(mascota.get_peso()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 4, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Sexo: {}'.format(mascota.get_sexo()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 5, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Raza: {}'.format(mascota.get_raza()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 6, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Especie: {}'.format(mascota.get_especie()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 7, column = 0, sticky = 'w')

            for lista in mascota.get_servicio():
                Label(master=panel2,
                      text='lista_servicio: {}'.format(lista.get_servicio()),
                      fg='blue3', anchor='nw', font=text_font1).grid(row = 8, column = 0, sticky = 'w')

    def get_controlador(self):
        return self.__controlador

class Modificar(Frame):
    '''Clase que muestra un formulario con los datos a modificar del objeto buscado.'''
    __controlador = MascotaControlador()
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
    
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta2 = Label(master=self.panel1, text='Ingrese el ID de la mascota:', font=text_font1)
        self.etiqueta2.pack(side='left', pady=10)
        self.id = Entry(master=self.panel1, width = 30)
        self.id.pack(side='left')
        self.id.focus_force()
        #boton buscar
        self.buscar_btn = Button(master = self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_mascota)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)
 
    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('abm.mascota.titulo.actualizar'))
        self.panel2 = Frame(master=self)
        self.panel2.pack(ipady=10, fill='x')
        self.get_titulo_lbl()
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
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para el titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self.panel2, text=" .:: MODIFICAR DATOS DE LA MASCOTA::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
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


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self.panel2, text="Guardar", bg = 'white', command=self.guardar_mascota) 
            self.__guardar_btn.grid(row=9, column=1)
        return self.__guardar_btn      
        
    def guardar_mascota(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        identificador = self.get_id_entry().get()
        nombre = self.get_nombre_entry().get()
        edad = self.get_edad_entry().get()
        peso = self.get_peso_entry().get()
        sexo = self.get_sexo_entry().get()
        raza = self.get_raza_entry().get()
        especie = self.get_especie_entry().get()

        mascota = Mascota(identificador, nombre, edad, peso, sexo, especie, raza)
        try:
            self.get_controlador().actualizar(mascota) 
            messagebox.showinfo("", "Registro Actualizado")
        except Exception as e:
            messagebox.showinfo("", e)

    def buscar_mascota(self):
        mascota = self.get_controlador().buscar_cod(self.id.get())
        if not mascota:
            messagebox.showinfo("", "Registro no existe")
        else:
            self.inicializar()
            # primero borramos lo que haya en los Entrys
            self.get_id_entry().delete(0, 'end')
            self.get_nombre_entry().delete(0, 'end')
            self.get_edad_entry().delete(0, 'end')
            self.get_peso_entry().delete(0, 'end')
            self.get_sexo_entry().delete(0, 'end')
            self.get_raza_entry().delete(0, 'end')
            self.get_especie_entry().delete(0, 'end')
            # insertamos
            self.get_id_entry().insert(0, mascota.get_identificador())
            self.get_nombre_entry().insert(0, mascota.get_nombre())
            self.get_edad_entry().insert(0, mascota.get_edad())
            self.get_peso_entry().insert(0, mascota.get_peso())
            self.get_sexo_entry().insert(0, mascota.get_sexo())
            self.get_raza_entry().insert(0, mascota.get_raza())
            self.get_especie_entry().insert(0, mascota.get_especie())
            
    def get_controlador(self):
        return self.__controlador



'''class Borrar(Frame):
    Clase que ayuda a la eliminacion del objeto buscado.
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
        Metoro que busca el objeto a traves del controlador por ID y lo elimina.
        cedula = self.cedula.get()
        cliente = self.get_controlador().buscar_cod(cedula)
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
       return self.__controlador2'''

class Borrar(Frame):
    ''' Clase que ayuda a la eliminacion del objeto buscado.'''
    __controlador = MascotaControlador()
    __controlador2 = PersonaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.__panel_master = panel_master
        self.pack()
        self.nombre_borrar = tk.Label(master=self, text='.:: BORRAR MASCOTA ::.', font=text_font1)
        self.nombre_borrar.pack()
        
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
           
        self.etiqueta = Label(master=self.panel1, text='Ingrese el numero de identificador:', font=text_font1)
        self.etiqueta.pack(side='left', pady=10)
        self.id = Entry(master=self.panel1,width=30)
        self.id.pack(side='left')
        self.id.focus_force()
        self.borrar_boton = Button(master=self.panel1, text='Borrar', font=text_font1, bg='white',command = self.borrar_mascota)
        self.borrar_boton.pack(side='left', padx=10)
        #boton atras
        self.atras_boton = tk.Button(master = self.panel1, text='Volver', font=text_font1,bg='white',command=self.master.destroy)
        self.atras_boton.pack(side ='left', padx=10) 

    def borrar_mascota(self):
        '''Metoro que busca el objeto a traves del controlador por ID y lo elimina. '''
        identificador = self.id.get()
        mascota = self.get_controlador().buscar_cod(identificador)
        clientes = self.get_controlador2().get_lista_objetos()

        if not mascota:
            messagebox.showinfo("", "Registro no existe")
        else:
            for cli in clientes:
                for mas in cli.get_mascotas():
                    if mas.get_identificador() == mascota.get_identificador():
                        cli.get_mascotas().remove(mas)
            try:
                self.get_controlador().borrar(mascota)
                messagebox.showinfo("",'Registro borrado con exito!')
            except Exception as e:
                messagebox.showinfo("",e)

    def get_controlador(self):
        return self.__controlador
  
    def get_controlador2(self):
        return self.__controlador2


class Servicio(Frame):
    __controlador = MascotaControlador()
    __controlador2 = PersonaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.grid(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text='.:: REGISTRAR SERVICIO ::.', font=text_font1)
        self.nombre_opcion.grid()
        self.panel_buscar = None
        self.panel = Frame(master=self)
        self.panel.grid(row = 0,column = 0)
        self.etiqueta = Label(master=self.panel, text='Ingrese ID de la mascota:', font=text_font1)
        self.etiqueta.grid(row = 0, column = 1)
        self.id = Entry(master=self.panel, width = 30)
        self.id.grid(row = 0, column = 2)
        self.id.focus_force()
        #boton buscar
        self.buscar_btn = Button(master=self.panel, text='Buscar', font=text_font1, bg = 'white', command = self.menu_servicio)
        self.buscar_btn.grid(row = 0, column = 3)
        #boton atras
        self.atras_btn = Button(master = self.panel, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.grid(row = 0, column = 4)
        self.lista_servicios = []
    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU MASCOTA ::.")
        root.largo = 1000
        root.ancho = 500
        #LARGOxANCHO+X+Y
        root.geometry('%dx%d+360+100'%(root.largo, root.ancho))
        root.resizable(width=False, height=False)

        root.focus_force()
        return root
    
    def menu_servicio(self):
        largo_btn = 20
        mascota = self.get_controlador().buscar_cod(self.id.get())
        lista_clientes = self.get_controlador2().get_lista_objetos()

                    
        if not mascota:
            messagebox.showinfo("", "Registro no existe")
        else:
            for cliente in lista_clientes:
                lista_mascotas = cliente.get_mascotas()
                for mas in lista_mascotas:
                    if mas.get_identificador() == mascota.get_identificador():
                        self.nombre = Label(master=self.panel, text='Cliente: {}'.format(cliente.get_nombre()), fg='black', font=text_font1)
                        self.nombre.grid(row=1,column=1)
        
            self.nombre = Label(master=self.panel, text='Nombre: {}'.format(mascota.get_nombre()), fg='black', font=text_font1)
            self.nombre.grid(row=2,column=1)
            self.edad = Label(master=self.panel, text='Edad: {}'.format(mascota.get_edad()), fg='black', font=text_font1)
            self.edad.grid(row=3,column=1)
            self.peso = Label(master=self.panel, text='Peso: {}'.format(mascota.get_peso()), fg='black', font=text_font1)
            self.peso.grid(row=4,column=1)
            self.sexo = Label(master=self.panel, text='Sexo: {}'.format(mascota.get_sexo()), fg='black', font=text_font1)
            self.sexo.grid(row=5,column=1)
            self.especie = Label(master=self.panel, text='Especie: {}'.format(mascota.get_especie()), fg='black', font=text_font1)
            self.especie.grid(row=6,column=1)
            self.raza = Label(master=self.panel, text='Raza: {}'.format(mascota.get_raza()), fg='black', font=text_font1)
            self.raza.grid(row=7,column=1)        
  
            #boton consulta
            self.btn_consulta = Button(master = self.panel, text = 'Consultas', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
            bd = 5, relief = RAISED, command = self.consulta)
            self.btn_consulta.grid(row = 1, column = 0, sticky = 'nw', padx = 0)

            # boton vacunacion
            self.btn_vacuna = Button(master = self.panel, text = 'Vacunacion', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
            bd = 5, relief = RAISED, command = self.vacuna)
            self.btn_vacuna.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

            # boton aseo
            self.btn_aseo = Button(master = self.panel, text = 'Aseo', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
            bd = 5, relief = RAISED, command = self.aseo)
            self.btn_aseo.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

    def consulta(self):
        RegistrarConsulta(self.crear_ventana(), self.id.get())

    def vacuna(self):
        RegistrarVacuna(self.crear_ventana(), self.id.get())

    def aseo(self):
        RegistrarAseo(self.crear_ventana(), self.id.get())

    def get_controlador(self):
        return self.__controlador
        
    def get_controlador2(self):
        return self.__controlador2


class Historial(Frame):
    __controlador = MascotaControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack()
        self.__panel_master = panel_master
        self.panel10 = Frame(master = self.__panel_master)
        self.panel10.pack()
        self.nombre_opcion = Label(master=self, text='.:: Historial Mascota ::.', font=text_font1)
        self.nombre_opcion.grid()
        self.panel_buscar = None
        self.panel = Frame(master=self.panel10)
        self.panel.grid(row = 0,column = 0)
        self.etiqueta = Label(master=self.panel10, text='Ingrese ID de la mascota:', font=text_font1)
        self.etiqueta.grid(row = 0, column = 1)
        self.id = Entry(master=self.panel10, width = 30)
        self.id.grid(row = 0, column = 2)
        self.id.focus_force()
        #boton buscar
        self.buscar_btn = Button(master=self.panel10, text='Buscar', font=text_font1, bg = 'white', command = self.historico)
        self.buscar_btn.grid(row = 0, column = 3)
        #boton atras
        self.atras_btn = Button(master = self.panel10, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.grid(row = 0, column = 4)

    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU MASCOTA ::.")
        root.largo = 2000
        root.ancho = 500
        #LARGOxANCHO+X+Y
        root.geometry('%dx%d+360+100'%(root.largo, root.ancho))
        root.resizable(width=False, height=False)

        root.focus_force()
        return root

    def historico(self):
        ident = self.id.get()
        mascota = self.get_controlador().buscar_cod(ident)
        if not mascota:
            messagebox.showinfo("","Mascota no existe")
        else:
            self.panel_aux = Frame(master=self.__panel_master)
            self.panel_aux.pack()
            largo = 10
            panel2 = Frame(master=self.panel_aux)
            panel2.grid(row=3,column=0)
            panel3 = Frame(master=self.panel_aux)
            panel3.grid(row=3,column=1)
            panel4 = Frame(master=self.panel_aux)
            panel4.grid(row=4,column=0,ipadx= 10)
            panel5 = Frame(master=self.panel_aux)
            panel5.grid(row=4,column=1)

            if not mascota.get_servicio():
                messagebox.showinfo("","Historial Vacio")
            else:
                '''se muestra en pantalla los datos de la mascota'''
                self.nombre = Label(master=self.panel10, text='Nombre: {}'.format(mascota.get_nombre()), fg='black', font=text_font1)
                self.nombre.grid(row=1,column=2)
                self.edad = Label(master=self.panel10, text='Edad: {}'.format(mascota.get_edad()), fg='black', font=text_font1)
                self.edad.grid(row=2,column=2)
                self.peso = Label(master=self.panel10, text='Peso: {}'.format(mascota.get_peso()), fg='black', font=text_font1)
                self.peso.grid(row=3,column=2)
                self.sexo = Label(master=self.panel10, text='Sexo: {}'.format(mascota.get_sexo()), fg='black', font=text_font1)
                self.sexo.grid(row=4,column=2)
                self.especie = Label(master=self.panel10, text='Especie: {}'.format(mascota.get_especie()), fg='black', font=text_font1)
                self.especie.grid(row=5,column=2)
                self.raza = Label(master=self.panel10, text='Raza: {}'.format(mascota.get_raza()), fg='black', font=text_font1)
                self.raza.grid(row=6,column=2)

                '''estos flags sirven para imprimir solo una vez la cabecera de la tabla de historial'''
                cont_consulta = 0
                cont_vacuna = 0

                '''se imprimen las tabla del historial'''
                for lista in mascota.get_servicio(): 
                    if lista.__class__.__name__ == "Consulta":
                        if cont_consulta == 0:
                            self.diagnostico = Label(master=panel2, text='Diagnostico',  bg='purple', fg = 'white', width = largo,
                            justify='left', relief="ridge")
                            self.diagnostico.pack(side='left')

                            self.tratamiento = Label(master=panel2, text='Tratamiento',  bg='purple', fg = 'white',width = largo,
                            justify='left', relief="ridge")
                            self.tratamiento.pack(side='left')

                            self.observacion = Label(master=panel2, text='Observacion',  bg='purple', fg = 'white',width = 20,
                              justify='left', relief="ridge")
                            self.observacion.pack(side='left')

                            self.fecha = Label(master=panel2, text='Fecha',  bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
                            self.fecha.pack(side='left')
                            cont_consulta +=1

                        self.panel = Frame(master=panel4)
                        self.panel.pack(side='top', ipadx=0)
                        Label(master=self.panel, text=lista.get_diagnostico(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_tratamiento(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_obs(),
                        relief="ridge", width=20, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_fecha(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        
                        panel = None
                    elif lista.__class__.__name__ == "Vacunacion":
                        if cont_vacuna == 0:
                            self.vacuna = Label(master=panel3, text='Vacuna', bg='purple', fg = 'white', width = largo,
                            justify='left', relief="ridge")
                            self.vacuna.pack(side='left')

                            self.dosis = Label(master=panel3, text='Dosis', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
                            self.dosis.pack(side='left')


                            self.revacuna = Label(master=panel3, text='Revacuna', bg='purple', fg = 'white',width = largo,
                            justify='left', relief="ridge")
                            self.revacuna.pack(side='left')
                            self.observacion = Label(master=panel3, text='Observacion', bg='purple', fg = 'white',width = 20,
                            justify='left', relief="ridge")
                            self.observacion.pack(side='left')

                            self.fecha = Label(master=panel3, text='Fecha', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
                            self.fecha.pack(side='left')
                            cont_vacuna +=1

                        self.panel = Frame(master=panel5)
                        self.panel.pack(side='top', ipadx=0)
                        Label(master=self.panel, text=lista.get_vacuna(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_dosis(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_revacuna(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_obs(),
                        relief="ridge", width=20, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_fecha(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        
                        panel = None
                        
                    elif lista.__class__.__name__ == "Aseo":
                        if cont_vacuna == 0:
                            self.vacuna = Label(master=panel3, text='Banho', bg='purple', fg = 'white', width = largo,
                            justify='left', relief="ridge")
                            self.vacuna.pack(side='left')

                            self.dosis = Label(master=panel3, text='Peluqueria', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
                            self.dosis.pack(side='left')


                            self.fecha = Label(master=panel3, text='Fecha', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
                            self.fecha.pack(side='left')
                            cont_vacuna +=1

                        self.panel = Frame(master=panel5)
                        self.panel.pack(side='top', ipadx=0)
                        Label(master=self.panel, text=lista.get_banho(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_peluqueria(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        Label(master=self.panel, text=lista.get_fecha(),
                        relief="ridge", width=largo, bg = 'pink').pack(side='left')
                        
                        panel = None

                          
    def get_controlador(self):
        return self.__controlador 

if __name__ == '__main__':
    root = tk.Tk()
    mascota = AbmMascota(root)
    root.mainloop() 
