import sys
sys.path.append("../") #referencia al directorio base
from controlador.vcontrol import ProductoAseoControlador
from modulo.vmodel import ProductoAseo
from modulo.vmodel import Modulo, Menu
from i18n import msg
import util
import tkinter as tk 
from tkinter import *
from botones import BotonesInsumos
text_font1 = ("Purisa", 10, "bold")

class AbmProductoAseo(BotonesInsumos):
    '''Clase que ayuda a la insercion, eliminacion y modificacion de los datos.'''

    def __init__(self, root):
        super().__init__(root, ".:: MENU PRODUCTO ASEO ::.")

    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU PRODUCTO ASEO ::.")
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

    def registrar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para el registro'''
        self.registrar = Registrar(self.crear_ventana())

    def buscar(self):
        ''' Metodo que crea la ventana donde se buscara el objeto'''
        self.buscar = Buscar(self.crear_ventana())

    def modificar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para la modificacion del registro'''
        self.modificar = Modificar(self.crear_ventana())

    def borrar(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el objeto'''
        self.borrar = Borrar(self.crear_ventana())

    def venta(self):
        ''' Metodo que crea la ventana donde se permitira eliminar el objeto'''
        self.venta = Venta(self.crear_ventana())

#Listar
class Listar(Frame):
    '''Clase donde se visualiza la lista.  '''
    __controlador = ProductoAseoControlador()

    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text=' .:: LISTA DE PRODUCTOS DE ASEO ::.', font=text_font1)
        self.nombre_opcion.pack(pady = 10)        
        self.panel1 = Frame(master=self)
        self.panel1.pack(side='top')
        #largor de los label´s
        largo = 10 
        self.codigo = Label(master=self.panel1, text='CODIGO',bg='purple', fg = 'white', width = largo,
                            justify='left', relief="ridge")
        self.codigo.pack(side='left')

        self.nombre = Label(master=self.panel1, text='NOMBRE', bg='purple', fg = 'white',width = 20,
                            justify='left', relief="ridge")
        self.nombre.pack(side='left')

        self.marca = Label(master=self.panel1, text='MARCA', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.marca.pack(side='left')

        self.descripcion = Label(master=self.panel1, text='DESCRIPCION', bg='purple', fg = 'white',width = 40,
                              justify='left', relief="ridge")
        self.descripcion.pack(side='left')

        self.fecha_caducidad = Label(master=self.panel1, text='VENCIMIENTO', bg='purple', fg = 'white',width = 20,
                              justify='left', relief="ridge")
        self.fecha_caducidad.pack(side='left')

        self.precio = Label(master=self.panel1, text='PRECIO', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.precio.pack(side='left')

        self.existencia = Label(master=self.panel1, text='EXISTENCIAS', bg='purple', fg = 'white',width = largo,
                              justify='left', relief="ridge")
        self.existencia.pack(side='left')



        lista_productos = self.get_controlador().get_lista_objetos()

        for lista in lista_productos:
            self.panel = Frame(master=self)
            self.panel.pack(side='top', ipadx=0)
            Label(master=self.panel, text=lista.get_codigo(),
                  relief="ridge", width=largo, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_nombre(),
                  relief="ridge", width=20, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_marca(),
                  relief="ridge", width=largo, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_descripcion(),
                  relief="ridge", width=40, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_fecha_de_caducidad(),
                  relief="ridge", width=20, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_precio(),
                  relief="ridge", width=largo, bg = 'pink').pack(side='left')
            Label(master=self.panel, text=lista.get_existencia(),
                  relief="ridge", width=largo, bg = 'pink').pack(side='left')

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
    __controlador = ProductoAseoControlador()
    __titulo_lbl = None
    __codigo_lbl = None
    __codigo_entry = None 
    __nombre_lbl = None
    __nombre_entry = None
    __marca_lbl = None
    __marca_entry = None
    __descripcion_lbl = None
    __descripcion_entry = None
    __fecha_caducidad_lbl = None
    __fecha_caducidad_entry = None
    __precio_lbl = None
    __precio_entry = None
    __existencia_lbl = None
    __existencia_entry = None
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
        self.__panel_master.title(msg('abm.cliente.apoderado.menu.titulo'))
        self.get_titulo_lbl()
        self.get_codigo_lbl()
        self.get_codigo_entry()
        self.get_nombre_lbl()
        self.get_nombre_entry()
        self.get_marca_lbl()
        self.get_marca_entry()
        self.get_descripcion_lbl()
        self.get_descripcion_entry()
        self.get_fecha_caducidad_lbl()
        self.get_fecha_caducidad_entry()
        self.get_precio_lbl()
        self.get_precio_entry()
        self.get_existencia_lbl()
        self.get_existencia_entry()
        self.get_salir_btn()
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self, text=" .:: REGISTRO DE PRODUCTOS DE ASEO ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_codigo_lbl(self):
        if not self.__codigo_lbl:
            self.__codigo_lbl = tk.Label(master=self, text="Codigo: ", width=10)
            self.__codigo_lbl.grid(row=1, column=0)
        return self.__codigo_lbl
        
    def get_codigo_entry(self):
        if not self.__codigo_entry:
            self.__codigo_entry = tk.Entry(master=self, width=20)
            self.__codigo_entry.focus()
            self.__codigo_entry.grid(row=1, column=1)
        return self.__codigo_entry
        
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
             
    def get_marca_lbl(self):
        if not self.__marca_lbl:
            self.__marca_lbl = tk.Label(master=self, text="Marca: ", width=10)
            self.__marca_lbl.grid(row=3, column=0)
        return self.__marca_lbl
        
    def get_marca_entry(self):
        if not self.__marca_entry:
            self.__marca_entry = tk.Entry(master=self, width=20)
            self.__marca_entry.grid(row=3, column=1)
        return self.__marca_entry 
        
    def get_descripcion_lbl(self):
        if not self.__descripcion_lbl:
            self.__descripcion_lbl = tk.Label(master=self, text="Descripcion: ", width=10)
            self.__descripcion_lbl.grid(row=4, column=0)
        return self.__descripcion_lbl
        
    def get_descripcion_entry(self):
        if not self.__descripcion_entry:
            self.__descripcion_entry = tk.Entry(master=self, width=20)
            self.__descripcion_entry.grid(row=4, column=1)
        return self.__descripcion_entry

    def get_fecha_caducidad_lbl(self):
        if not self.__fecha_caducidad_lbl:
            self.__fecha_caducidad_lbl = tk.Label(master=self, text="Fecha de caducidad: ", width=10)
            self.__fecha_caducidad_lbl.grid(row=5, column=0)
        return self.__fecha_caducidad_lbl
        
    def get_fecha_caducidad_entry(self):
        if not self.__fecha_caducidad_entry:
            self.__fecha_caducidad_entry = tk.Entry(master=self, width=20)
            self.__fecha_caducidad_entry.grid(row=5, column=1)
        return self.__fecha_caducidad_entry

    def get_precio_lbl(self):
        if not self.__precio_lbl:
            self.__precio_lbl = tk.Label(master=self, text="Precio: ", width=10)
            self.__precio_lbl.grid(row=6, column=0)
        return self.__precio_lbl
        
    def get_precio_entry(self):
        if not self.__precio_entry:
            self.__precio_entry = tk.Entry(master=self, width=20)
            self.__precio_entry.grid(row=6, column=1)
        return self.__precio_entry

    def get_existencia_lbl(self):
        if not self.__existencia_lbl:
            self.__existencia_lbl = tk.Label(master=self, text="Existencia: ", width=10)
            self.__existencia_lbl.grid(row=7, column=0)
        return self.__existencia_lbl
        
    def get_existencia_entry(self):
        if not self.__existencia_entry:
            self.__existencia_entry = tk.Entry(master=self, width=20)
            self.__existencia_entry.grid(row=7, column=1)
        return self.__existencia_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self, text="Guardar", bg = 'white', command=self.guardar_producto) 
            self.__guardar_btn.grid(row=8, column=0)
        return self.__guardar_btn      

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=8, column=1)
        return self.__salir_btn

    def guardar_producto(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        codigo = self.get_codigo_entry().get()
        nombre = self.get_nombre_entry().get()
        marca = self.get_marca_entry().get()
        descripcion = self.get_descripcion_entry().get()
        fecha_caducidad = self.get_fecha_caducidad_entry().get()
        precio = self.get_precio_entry().get()
        existencia = self.get_existencia_entry().get()

        producto = ProductoAseo(codigo=codigo, nombre=nombre, marca=marca, descripcion=descripcion, fecha_de_caducidad=fecha_caducidad, precio=precio, existencia=existencia)


        try:
            self.get_controlador().crear(producto) 
            messagebox.showinfo("", "Registro Creado")
        except Exception as e:
            messagebox.showinfo("", e)

    def get_controlador(self):
        return self.__controlador

class Buscar(Frame):
    '''Clase que busca el objeto y retorna para su visualizacion en la pantalla. '''
    __controlador = ProductoAseoControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.nombre_opcion = Label(master=self, text='.:: BUSCAR PRODUCTO DE ASEO ::.', font=text_font1)
        self.nombre_opcion.pack()
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta2 = Label(master=self.panel1, text='Ingrese el codigo del Producto:', font=text_font1)
        self.etiqueta2.pack(side='left', pady=10)
        self.codigo = Entry(master=self.panel1, width = 30)
        self.codigo.pack(side='left')
        self.codigo.focus_force()
        #boton buscar
        self.buscar_btn = Button(master=self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_producto)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)


    def buscar_producto(self):
        ''' Metodo que busca el objeto a traves del controlador y lo muestra en la pantalla.'''
        producto = self.get_controlador().buscar_cod(self.codigo.get())
        if not producto:
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
                  text='Codigo : {}'.format(producto.get_codigo()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 1, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Nombre : {}'.format(producto.get_nombre()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 2, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Marca: {}'.format(producto.get_marca()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 3, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Descripcion: {}'.format(producto.get_descripcion()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 4, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Fecha de Caducidad: {}'.format(producto.get_fecha_de_caducidad()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 5, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Precio: {}'.format(producto.get_precio()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 6, column = 0, sticky = 'w')
            Label(master=panel2,
                  text='Existencia: {}'.format(producto.get_existencia()),
                  fg='blue3', anchor='nw', font=text_font1).grid(row = 7, column = 0, sticky = 'w')

    def get_controlador(self):
        return self.__controlador

class Modificar(Frame):
    '''Clase que muestra un formulario con los datos a modificar del objeto buscado.'''
    __controlador = ProductoAseoControlador()
    __titulo_lbl = None
    __codigo_lbl = None
    __codigo_entry = None 
    __nombre_lbl = None
    __nombre_entry = None
    __marca_lbl = None
    __marca_entry = None
    __descripcion_lbl = None
    __descripcion_entry = None
    __fecha_caducidad_lbl = None
    __fecha_caducidad_entry = None
    __precio_lbl = None
    __precio_entry = None
    __existencia_lbl = None
    __existencia_entry = None
    __guardar_btn = None
    
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50)
        self.__panel_master = panel_master
        self.panel_buscar = None
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
        self.etiqueta = Label(master=self.panel1, text='Ingrese el codigo del Producto:', font=text_font1)
        self.etiqueta.pack(side='left', pady=10)
        self.codigo = Entry(master=self.panel1, width = 30)
        self.codigo.pack(side='left')
        self.codigo.focus_force()
        #boton buscar
        self.buscar_btn = Button(master = self.panel1, text='Buscar', font=text_font1, bg = 'white', command = self.buscar_producto)
        self.buscar_btn.pack(side='left', padx=10)
        #boton atras
        self.atras_btn = Button(master = self.panel1, text='Volver', font=text_font1, bg = 'white', command = self.master.destroy)
        self.atras_btn.pack(side ='left', padx=10)
 
    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('abm.cliente.apoderado.menu.titulo'))
        self.panel2 = Frame(master=self)
        self.panel2.pack(ipady=10, fill='x')
        self.get_titulo_lbl()
        self.get_codigo_lbl()
        self.get_codigo_entry()
        self.get_nombre_lbl()
        self.get_nombre_entry()
        self.get_marca_lbl()
        self.get_marca_entry()
        self.get_descripcion_lbl()
        self.get_descripcion_entry()
        self.get_fecha_caducidad_lbl()
        self.get_fecha_caducidad_entry()
        self.get_precio_lbl()
        self.get_precio_entry()
        self.get_existencia_lbl()
        self.get_existencia_entry()
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para el titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self.panel2, text=" .:: MODIFICAR DATOS DE UN PRODUCTO::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_codigo_lbl(self):
        if not self.__codigo_lbl:
            self.__codigo_lbl = tk.Label(master=self.panel2, text="Codigo: ", width=10)
            self.__codigo_lbl.grid(row=1, column=0)
        return self.__codigo_lbl
        
    def get_codigo_entry(self):
        if not self.__codigo_entry:
            self.__codigo_entry = tk.Entry(master=self.panel2, width=20)
            self.__codigo_entry.focus()
            self.__codigo_entry.grid(row=1, column=1)
        return self.__codigo_entry
        
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
             
    def get_marca_lbl(self):
        if not self.__marca_lbl:
            self.__marca_lbl = tk.Label(master=self.panel2, text="Marca: ", width=10)
            self.__marca_lbl.grid(row=3, column=0)
        return self.__marca_lbl
        
    def get_marca_entry(self):
        if not self.__marca_entry:
            self.__marca_entry = tk.Entry(master=self.panel2, width=20)
            self.__marca_entry.grid(row=3, column=1)
        return self.__marca_entry 
        
    def get_descripcion_lbl(self):
        if not self.__descripcion_lbl:
            self.__descripcion_lbl = tk.Label(master=self.panel2, text="Descripcion: ", width=10)
            self.__descripcion_lbl.grid(row=4, column=0)
        return self.__descripcion_lbl
        
    def get_descripcion_entry(self):
        if not self.__descripcion_entry:
            self.__descripcion_entry = tk.Entry(master=self.panel2, width=20)
            self.__descripcion_entry.grid(row=4, column=1)
        return self.__descripcion_entry

    def get_fecha_caducidad_lbl(self):
        if not self.__fecha_caducidad_lbl:
            self.__fecha_caducidad_lbl = tk.Label(master=self.panel2, text="fecha de caducidad: ", width=10)
            self.__fecha_caducidad_lbl.grid(row=5, column=0)
        return self.__fecha_caducidad_lbl
        
    def get_fecha_caducidad_entry(self):
        if not self.__fecha_caducidad_entry:
            self.__fecha_caducidad_entry = tk.Entry(master=self.panel2, width=20)
            self.__fecha_caducidad_entry.grid(row=5, column=1)
        return self.__fecha_caducidad_entry

    def get_precio_lbl(self):
        if not self.__precio_lbl:
            self.__precio_lbl = tk.Label(master=self.panel2, text="Precio: ", width=10)
            self.__precio_lbl.grid(row=6, column=0)
        return self.__precio_lbl
        
    def get_precio_entry(self):
        if not self.__precio_entry:
            self.__precio_entry = tk.Entry(master=self.panel2, width=20)
            self.__precio_entry.grid(row=6, column=1)
        return self.__precio_entry

    def get_existencia_lbl(self):
        if not self.__existencia_lbl:
            self.__existencia_lbl = tk.Label(master=self.panel2, text="Existencia: ", width=10)
            self.__existencia_lbl.grid(row=7, column=0)
        return self.__existencia_lbl
        
    def get_existencia_entry(self):
        if not self.__existencia_entry:
            self.__existencia_entry = tk.Entry(master=self.panel2, width=20)
            self.__existencia_entry.grid(row=7, column=1)
        return self.__existencia_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self.panel2, text="Guardar", bg = 'white', command=self.guardar_producto) 
            self.__guardar_btn.grid(row=9, column=1)
        return self.__guardar_btn      
        
    def guardar_producto(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        codigo = self.get_codigo_entry().get()
        nombre = self.get_nombre_entry().get()
        marca = self.get_marca_entry().get()
        descripcion = self.get_descripcion_entry().get()
        fecha_caducidad = self.get_fecha_caducidad_entry().get()
        precio = self.get_precio_entry().get()
        existencia = self.get_existencia_entry().get()

        producto = ProductoAseo(codigo=codigo, nombre=nombre, marca=marca, descripcion=descripcion, fecha_de_caducidad=fecha_caducidad, precio=precio, existencia=existencia)
        try:
            self.get_controlador().actualizar(producto) 
            messagebox.showinfo("", "Registro Actualizado")
        except Exception as e:
            messagebox.showinfo("", e)

    def buscar_producto(self):
        producto = self.get_controlador().buscar_cod(self.codigo.get())
        if not producto:
            messagebox.showinfo("", "Registro no existe")
        else:
            self.inicializar()
            # primero borramos lo que haya en los Entrys
            self.get_codigo_entry().delete(0, 'end')
            self.get_nombre_entry().delete(0, 'end')
            self.get_marca_entry().delete(0, 'end')
            self.get_descripcion_entry().delete(0, 'end')
            self.get_fecha_caducidad_entry().delete(0, 'end')
            self.get_precio_entry().delete(0, 'end')
            self.get_existencia_entry().delete(0, 'end')
            # insertamos
            self.get_codigo_entry().insert(0, producto.get_codigo())
            self.get_nombre_entry().insert(0, producto.get_nombre())
            self.get_marca_entry().insert(0, producto.get_marca())
            self.get_descripcion_entry().insert(0, producto.get_descripcion())
            self.get_fecha_caducidad_entry().insert(0, producto.get_fecha_de_caducidad())
            self.get_precio_entry().insert(0, producto.get_precio())
            self.get_existencia_entry().insert(0, producto.get_existencia())
            
    def get_controlador(self):
        return self.__controlador



class Borrar(Frame):
    ''' Clase que ayuda a la eliminacion del objeto buscado.'''
    __controlador = ProductoAseoControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.__panel_master = panel_master
        self.pack()
        self.nombre_borrar = tk.Label(master=self, text='.:: BORRAR PRODUCTO ::.', font=text_font1)
        self.nombre_borrar.pack()
        
        self.panel1 = Frame(master=self)
        self.panel1.pack(ipady=10, fill='x')
           
        self.etiqueta = Label(master=self.panel1, text='Ingrese el ID del insumo:', font=text_font1)
        self.etiqueta.pack(side='left', pady=10)
        self.codigo = Entry(master=self.panel1,width=30)
        self.codigo.pack(side='left')
        self.codigo.focus_force()
        self.borrar_boton = Button(master=self.panel1, text='Borrar', font=text_font1, bg='white',command = self.borrar_producto)
        self.borrar_boton.pack(side='left', padx=10)
        #boton atras
        self.atras_boton = tk.Button(master = self.panel1, text='Volver', font=text_font1,bg='white',command=self.master.destroy)
        self.atras_boton.pack(side ='left', padx=10) 

    def borrar_producto(self):
        '''Metoro que busca el objeto a traves del controlador por ID y lo elimina. '''
        codigo = self.codigo.get()
        producto = self.get_controlador().buscar_cod(codigo)
        try:
            self.get_controlador().borrar(producto)
            messagebox.showinfo("",'Registro borrado con exito!')
        except Exception as e:
            messagebox.showinfo("",e)

    def get_controlador(self):
        return self.__controlador

class Venta(Frame):
    __controlador = ProductoAseoControlador()
    def __init__(self, panel_master):
        super().__init__(master=panel_master)
        self.__panel_master = panel_master
        self.grid(row = 0, column = 0)
        self.nombre_borrar = tk.Label(master=self, text='.:: VENTA DE PRODUCTOS ::.', font=text_font1)
        self.nombre_borrar.grid()        
        self.panel1 = Frame(master=self)
        self.panel1.grid(row = 1, column = 0)
        self.etiqueta = Label(master=self.panel1, text='Ingrese el codigo del producto:', font=text_font1)
        self.etiqueta.grid(row = 0, column = 1)
        self.codigo = Entry(master=self.panel1,width=30)
        self.codigo.grid(row = 0, column = 2)
        self.codigo.focus_force()
        self.etiqueta2 = Label(master=self.panel1, text='Unidades:', font=text_font1)
        self.etiqueta2.grid(row = 1, column = 1)
        self.cantidad = Entry(master=self.panel1,width=30)
        self.cantidad.grid(row = 1, column = 2)
        self.cantidad.focus_force()
        self.vender_boton = Button(master=self.panel1, text='Vender', font=text_font1, bg='white',command = self.vender_producto)
        self.vender_boton.grid(row = 2, column = 1)
        #boton atras
        self.atras_boton = tk.Button(master = self.panel1, text='Volver', font=text_font1,bg='white',command=self.master.destroy)
        self.atras_boton.grid(row = 2, column = 2) 

    def vender_producto(self):
        producto = self.get_controlador().buscar_cod(self.codigo.get())
        cantidad = int(self.cantidad.get())
        if not producto:
            messagebox.showinfo("", "Registro no existe")
        elif int(producto.get_existencia()) <= 0:
            messagebox.showinfo("", "producto agotado")
        elif cantidad > int(producto.get_existencia()):
            messagebox.showinfo("", "Supera el stock")
        else:
            costo = cantidad * int(producto.get_precio())
            messagebox.showinfo("Total a cobrar:  ", str(costo) + " gs")
            disminuir = int(producto.get_existencia()) - cantidad
            producto.set_existencia(disminuir)
            self.get_controlador().actualizar(producto)

    def get_controlador(self):
        return self.__controlador

if __name__ == '__main__':
    root = tk.Tk()
    producto = AbmProductoAseo(root)
    root.mainloop()
