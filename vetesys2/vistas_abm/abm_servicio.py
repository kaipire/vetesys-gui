import sys
sys.path.append("../")
from modulo.vmodel import Cliente, Modulo, Menu, Mascota, Aseo,Vacunacion, Consulta
from i18n import msg
from controlador.vcontrol import MascotaControlador
import util
import tkinter as tk 
from tkinter import *
text_font1 = ("Purisa", 10, "bold")

class AbmServicio(Frame):
    '''Clase que permite el registro de los tipos de servicio'''

    def __init__(self, root):
        super().__init__(root, ".:: MENU MASCOTA ::.")

    def crear_ventana(self):
        '''Metodo que crea una ventana donde se posicionaran todos los botones que ayudaran
           a la interaccion con el usuario.'''
        root = tk.Tk()
        root.title(".:: MENU SERVICIOS ::.")
        root.largo = 1000
        root.ancho = 500
        #LARGOxANCHO+X+Y
        root.geometry('%dx%d+360+100'%(root.largo, root.ancho))
        root.resizable(width=False, height=False)

        root.focus_force()
        return root

    def registrar(self):
        ''' Metodo que crea la ventana donde se mostrara el formulario para el registro'''
        self.registrar = Registrar(self.crear_ventana())

class RegistrarConsulta(Frame):
    ''' Clase que mostrara el formulario a ser llenado para el registro de consultas ''' 

    '''controlador de clase involucrada'''
    __controlador = MascotaControlador()

    '''define los entry y lbl a ser utilizados'''
    __titulo_lbl = None
    __diagnostico_lbl = None
    __diagnostico_entry = None 
    __tratamiento_lbl = None
    __tratamiento_entry = None
    __observacion_lbl = None
    __observacion_entry = None
    __fecha_lbl = None
    __fecha_entry = None
    __salir_btn = None
    __guardar_btn = None
    
    '''se define el panel principal'''
    def __init__(self, panel_master, id_mascota):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50, pady = 15)
        self.__panel_master = panel_master
        self.id_mascota = id_mascota
        self.lista_servicio = []
        self.inicializar()

    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('REGISTRAR CONSULTA'))
        self.get_titulo_lbl()
        self.get_diagnostico_lbl()
        self.get_diagnostico_entry()
        self.get_tratamiento_lbl()
        self.get_tratamiento_entry()
        self.get_observacion_lbl()
        self.get_observacion_entry()
        self.get_fecha_lbl()
        self.get_fecha_entry()
        self.get_salir_btn()
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self, text=" .:: REGISTRO DE CONSULTAS ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_diagnostico_lbl(self):
        if not self.__diagnostico_lbl:
            self.__diagnostico_lbl = tk.Label(master=self, text="Diagnostico: ", width=10)
            self.__diagnostico_lbl.grid(row=1, column=0)
        return self.__diagnostico_lbl
        
    def get_diagnostico_entry(self):
        if not self.__diagnostico_entry:
            self.__diagnostico_entry = tk.Entry(master=self, width=20)
            self.__diagnostico_entry.focus()
            self.__diagnostico_entry.grid(row=1, column=1)
        return self.__diagnostico_entry
        
    def get_tratamiento_lbl(self):
        if not self.__tratamiento_lbl:
            self.__tratamiento_lbl = tk.Label(master=self, text="Tratamiento: ", width=10)
            self.__tratamiento_lbl.grid(row=2, column=0)
        return self.__tratamiento_lbl
        
    def get_tratamiento_entry(self):
        if not self.__tratamiento_entry:
            self.__tratamiento_entry = tk.Entry(master=self, width=20)
            self.__tratamiento_entry.grid(row=2, column=1)
        return self.__tratamiento_entry        
             
    def get_observacion_lbl(self):
        if not self.__observacion_lbl:
            self.__observacion_lbl = tk.Label(master=self, text="Observacion: ", width=10)
            self.__observacion_lbl.grid(row=3, column=0)
        return self.__observacion_lbl
        
    def get_observacion_entry(self):
        if not self.__observacion_entry:
            self.__observacion_entry = tk.Entry(master=self, width=20)
            self.__observacion_entry.grid(row=3, column=1)
        return self.__observacion_entry 
        
    def get_fecha_lbl(self):
        if not self.__fecha_lbl:
            self.__fecha_lbl = tk.Label(master=self, text="Fecha: ", width=10)
            self.__fecha_lbl.grid(row=4, column=0)
        return self.__fecha_lbl
        
    def get_fecha_entry(self):
        if not self.__fecha_entry:
            self.__fecha_entry = tk.Entry(master=self, width=20)
            self.__fecha_entry.grid(row=4, column=1)
        return self.__fecha_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:  
            self.__guardar_btn = tk.Button(master=self, text="Guardar", bg = 'white', command=self.guardar_consulta) 
            self.__guardar_btn.grid(row=8, column=0)
        return self.__guardar_btn      

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=8, column=1)
        return self.__salir_btn

    def guardar_consulta(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        diagnostico = self.get_diagnostico_entry().get()
        tratamiento = self.get_tratamiento_entry().get()
        observacion = self.get_observacion_entry().get()
        fecha = self.get_fecha_entry().get()
       

        consulta = Consulta(diagnostico, tratamiento, observacion, fecha = fecha)
       
        self.lista_servicio.append(consulta)
        mascota = self.get_controlador().buscar_cod(self.id_mascota)
       
        if mascota.get_servicio():
            for i in mascota.get_servicio():
                self.lista_servicio.append(i)
       
        mascota.set_servicio(self.lista_servicio)
        self.get_controlador().actualizar(mascota)
        messagebox.showinfo("","Registro creado")
        self.cerrar()

    def cerrar(self):
        self.master.destroy()

    def get_controlador(self):
        return self.__controlador



class RegistrarVacuna(Frame):
    ''' Clase que mostrara el formulario a ser llenado para el registro de vacunacion ''' 
    __controlador = MascotaControlador()
    __titulo_lbl = None
    __vacuna_lbl = None
    __vacuna_entry = None 
    __dosis_lbl = None
    __dosis_entry = None
    __revacuna_lbl = None
    __revacuna_entry = None
    __observacion_lbl = None
    __observacion_entry = None
    __fecha_lbl = None
    __fecha_entry = None
    __salir_btn = None
    __guardar_btn = None
    
    def __init__(self, panel_master,id_mascota):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50, pady = 15)
        self.__panel_master = panel_master
        self.lista_servicio = []
        self.id_mascota = id_mascota
        self.inicializar()

    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('REGISTRAR VACUNACION'))
        self.get_titulo_lbl()
        self.get_vacuna_lbl()
        self.get_vacuna_entry()
        self.get_dosis_lbl()
        self.get_dosis_entry()
        self.get_revacuna_lbl()
        self.get_revacuna_entry()
        self.get_observacion_lbl()
        self.get_observacion_entry()
        self.get_fecha_lbl()
        self.get_fecha_entry()
        self.get_salir_btn()
        self.get_guardar_btn()


    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self, text=" .:: REGISTRO DE VACUNAS ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
                   
    def get_vacuna_lbl(self):
        if not self.__vacuna_lbl:
            self.__vacuna_lbl = tk.Label(master=self, text="Vacuna: ", width=10)
            self.__vacuna_lbl.grid(row=1, column=0)
        return self.__vacuna_lbl
        
    def get_vacuna_entry(self):
        if not self.__vacuna_entry:
            self.__vacuna_entry = tk.Entry(master=self, width=20)
            self.__vacuna_entry.focus()
            self.__vacuna_entry.grid(row=1, column=1)
        return self.__vacuna_entry
        
    def get_dosis_lbl(self):
        if not self.__dosis_lbl:
            self.__dosis_lbl = tk.Label(master=self, text="Dosis: ", width=10)
            self.__dosis_lbl.grid(row=2, column=0)
        return self.__dosis_lbl
        
    def get_dosis_entry(self):
        if not self.__dosis_entry:
            self.__dosis_entry = tk.Entry(master=self, width=20)
            self.__dosis_entry.grid(row=2, column=1)
        return self.__dosis_entry

    def get_revacuna_lbl(self):
        if not self.__revacuna_lbl:
            self.__revacuna_lbl = tk.Label(master=self, text="Revacuna: ", width=10)
            self.__revacuna_lbl.grid(row=3, column=0)
        return self.__revacuna_lbl
        
    def get_revacuna_entry(self):
        if not self.__revacuna_entry:
            self.__revacuna_entry = tk.Entry(master=self, width=20)
            self.__revacuna_entry.grid(row=3, column=1)
        return self.__revacuna_entry        
             
    def get_observacion_lbl(self):
        if not self.__observacion_lbl:
            self.__observacion_lbl = tk.Label(master=self, text="Observacion: ", width=10)
            self.__observacion_lbl.grid(row=4, column=0)
        return self.__observacion_lbl
        
    def get_observacion_entry(self):
        if not self.__observacion_entry:
            self.__observacion_entry = tk.Entry(master=self, width=20)
            self.__observacion_entry.grid(row=4, column=1)
        return self.__observacion_entry 
        
    def get_fecha_lbl(self):
        if not self.__fecha_lbl:
            self.__fecha_lbl = tk.Label(master=self, text="Fecha: ", width=10)
            self.__fecha_lbl.grid(row=5, column=0)
        return self.__fecha_lbl
        
    def get_fecha_entry(self):
        if not self.__fecha_entry:
            self.__fecha_entry = tk.Entry(master=self, width=20)
            self.__fecha_entry.grid(row=5, column=1)
        return self.__fecha_entry


    def get_guardar_btn(self):
        if not self.__guardar_btn:
            self.__guardar_btn = tk.Button(master=self, text="Guardar", bg = 'white', command=self.guardar_vacuna) 
            self.__guardar_btn.grid(row=6, column=0)
        return self.__guardar_btn      

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=6, column=1)
        return self.__salir_btn

    def guardar_vacuna(self):
        '''Metodo que instancia el objeto y llama al controlador para guardar los atributos. '''
        vacuna = self.get_vacuna_entry().get()
        dosis = self.get_dosis_entry().get()
        revacuna = self.get_revacuna_entry().get()
        observacion = self.get_observacion_entry().get()
        fecha = self.get_fecha_entry().get()

        vacuna = Vacunacion(vacuna, dosis, revacuna, observacion, fecha = fecha)
        self.lista_servicio.append(vacuna)
        mascota = self.get_controlador().buscar_cod(self.id_mascota)
       
        if mascota.get_servicio():
            for i in mascota.get_servicio():
                self.lista_servicio.append(i)
       
        mascota.set_servicio(self.lista_servicio)
        self.get_controlador().actualizar(mascota)
        messagebox.showinfo("","Registro creado")
        self.cerrar()

    def cerrar(self):
        self.master.destroy()

    def get_controlador(self):
        return self.__controlador

class RegistrarAseo(Frame):
    __controlador = MascotaControlador()
    __titulo_lbl = None
    __fecha_lbl = None
    __fecha_entry = None
    __salir_btn = None
    

    def __init__(self, panel_master,id_mascota):
        super().__init__(master=panel_master)
        self.pack(ipadx=50, ipady=50, pady = 15)
        self.__panel_master = panel_master
        self.lista_servicio = []
        self.id_mascota = id_mascota
        self.inicializar()

    def inicializar(self):
        ''' Metodo que hace la llamada a otros metodos para que se visualicen en pantalla'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title(msg('REGISTRAR ASEO'))
        self.get_titulo_lbl()
        self.get_fecha_lbl()
        self.get_fecha_entry()
        self.get_salir_btn()
        largo_btn = 20
        #boton banho
        self.btn_banho = Button(master = self, text = 'Banho', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.banho)
        self.btn_banho.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

        # boton peluqueria
        self.btn_peluqueria = Button(master = self, text = 'Peluqueria', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.peluqueria)
        self.btn_peluqueria.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

        # boton ambos
        self.btn_ambos = Button(master = self, text = 'Ambos', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
        bd = 5, relief = RAISED, command = self.ambos)
        self.btn_ambos.grid(row = 4, column = 0, sticky = 'nw', padx = 0)

    def get_titulo_lbl(self):
        '''crear etiqueta para mensaje titulo'''
        if not self.__titulo_lbl:
            self.__titulo_lbl = tk.Label(master=self, text=" .:: REGISTRO DE ASEOS ::. ",  font=text_font1, pady = 10)
            self.__titulo_lbl.grid(row=0, column=0, columnspan=2)
        return self.__titulo_lbl
        
    def get_fecha_lbl(self):
        if not self.__fecha_lbl:
            self.__fecha_lbl = tk.Label(master=self, text="Fecha: ", width=10)
            self.__fecha_lbl.grid(row=1, column=0)
        return self.__fecha_lbl
        
    def get_fecha_entry(self):
        if not self.__fecha_entry:
            self.__fecha_entry = tk.Entry(master=self, width=20)
            self.__fecha_entry.grid(row=1, column=1)
        return self.__fecha_entry
     

    def get_salir_btn(self):
        if not self.__salir_btn:
            self.__salir_btn = tk.Button(master=self, text="Salir", bg = 'white', command=self.master.destroy) 
            self.__salir_btn.grid(row=5, column=1)
        return self.__salir_btn
        
    '''#boton banho
    self.btn_banho = Button(master = self, text = 'Banho', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
    bd = 5, relief = RAISED, command = self.banho)
    self.btn_banho.grid(row = 2, column = 0, sticky = 'nw', padx = 0)

    # boton peluqueria
    self.btn_peluqueria = Button(master = self, text = 'Peluqueria', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
    bd = 5, relief = RAISED, command = self.peluqueria)
    self.btn_peluquera.grid(row = 3, column = 0, sticky = 'nw', padx = 0)

    # boton ambos
    self.btn_ambos = Button(master = self, text = 'Ambos', font = text_font1, bg = 'purple', fg = "white", width = largo_btn,
    bd = 5, relief = RAISED, command = self.ambos)
    self.btn_ambos.grid(row = 4, column = 0, sticky = 'nw', padx = 0)'''

    def banho(self):
        fecha = self.get_fecha_entry().get()
        aseo = Aseo("SI","NO", fecha = fecha)
        self.lista_servicio.append(aseo)
        mascota = self.get_controlador().buscar_cod(self.id_mascota)
       
        if mascota.get_servicio():
            for i in mascota.get_servicio():
                self.lista_servicio.append(i)
       
        mascota.set_servicio(self.lista_servicio)
        self.get_controlador().actualizar(mascota)
        messagebox.showinfo("","Registro creado")
        self.cerrar()

    def cerrar(self):
        self.master.destroy()
        
    def peluqueria(self):
        fecha = self.get_fecha_entry().get()
        aseo = Aseo("NO","SI",fecha = fecha)
        self.lista_servicio.append(aseo)
        mascota = self.get_controlador().buscar_cod(self.id_mascota)
       
        if mascota.get_servicio():
            for i in mascota.get_servicio():
                self.lista_servicio.append(i)
       
        mascota.set_servicio(self.lista_servicio)
        self.get_controlador().actualizar(mascota)
        messagebox.showinfo("","Registro creado")
        self.cerrar()
        
    def ambos(self):
        fecha = self.get_fecha_entry().get()
        aseo = Aseo("SI","SI", fecha = fecha)
        self.lista_servicio.append(aseo)
        mascota = self.get_controlador().buscar_cod(self.id_mascota)
       
        if mascota.get_servicio():
            for i in mascota.get_servicio():
                self.lista_servicio.append(i)
       
        mascota.set_servicio(self.lista_servicio)
        self.get_controlador().actualizar(mascota)
        messagebox.showinfo("","Registro creado")
        self.cerrar()
        

    def get_controlador(self):
        return self.__controlador


if __name__ == '__main__':
    root = tk.Tk()
    servicio = AbmServicio(root)
    root.mainloop()
