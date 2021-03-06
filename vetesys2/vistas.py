import sys
sys.path.append("../") #referencia al directorio base
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from vistas_abm.abm_cliente import AbmCliente
from vistas_abm.abm_mascota import AbmMascota
from vistas_abm.abm_accesorio import AbmAccesorio
from vistas_abm.abm_balanceado import AbmBalanceado
from vistas_abm.abm_medicamento import AbmMedicamento
from vistas_abm.abm_producto_aseo import AbmProductoAseo
from vistas_abm.abm_servicio import  AbmServicio


class PanelPrincipal(tk.Frame):
    ''' 'Clase que crea el panel principal donde se visualizaran los menus que permitiran el 
         acceso a los distintos paneles de los abm´s'''
    __vista_actual = None
    def __init__(self,  panel_master):
        tk.Frame.__init__(self,  panel_master)            
        self.__panel_master =  panel_master   
        self.inicializar()
        self.pack()
        
    def inicializar(self):
        ''' Metodo que crea el menubar'''
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("Menu")   
        menubar = tk.Menu(self.__panel_master) #menu1
        self.__panel_master.config(menu=menubar)
        
        clinica_menu = tk.Menu(menubar)#menu3
        clinica_menu.add_command(label="Menu Cliente", command=self.mostrar_cliente)
        clinica_menu.add_command(label="Menu Mascota", command=self.mostrar_mascota)
        clinica_menu.add_separator()
        clinica_menu.add_command(label="Salir", command=self.salir)

        insumo_menu = tk.Menu(menubar) #menu2
        insumo_menu.add_command(label="Menu Accesorios", command=self.mostrar_accesorio)
        insumo_menu.add_command(label="Menu Balanceados", command=self.mostrar_balanceado)
        insumo_menu.add_command(label="Menu Medicamentos", command=self.mostrar_medicamento)
        insumo_menu.add_command(label="Menu Productos de Aseo", command=self.mostrar_producto)
        insumo_menu.add_separator()
        insumo_menu.add_command(label="Salir", command=self.salir)
        
        menubar.add_cascade(label="Servicio Clinico", menu=clinica_menu)
        menubar.add_cascade(label="Insumos", menu=insumo_menu)
        menubar.add_command(label="Menu Principal",command=self.volver)

        
    def salir(self):
        ''' Metodo para salir del sistema.'''
        self.quit()

    def volver(self):
        ''' Metodo que ayuda a volver al panel principal.'''
        if self.__vista_actual:
            self.__vista_actual.destroy()
            #panel_principal = PanelPrincipal(self)
        #root.mainloop()
        
    def limpiar(self):
        ''' Metodo que limpia el frame o panel actual.'''
        if self.__vista_actual:
            self.__vista_actual.destroy()

    def mostrar_cliente(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmCliente'''
        self.limpiar()
        form = AbmCliente(self.__panel_master)
        self.__vista_actual = form
                
    def mostrar_mascota(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmMascota'''
        self.limpiar()
        form = AbmMascota(self.__panel_master)
        self.__vista_actual = form

    def mostrar_accesorio(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmAccesorio'''
        self.limpiar()
        form = AbmAccesorio(self.__panel_master)
        self.__vista_actual = form

    def mostrar_balanceado(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmBalanceado'''
        self.limpiar()
        form = AbmBalanceado(self.__panel_master)
        self.__vista_actual = form

    def mostrar_medicamento(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmMedicamento'''
        self.limpiar()
        form = AbmMedicamento(self.__panel_master)
        self.__vista_actual = form

        
    def mostrar_producto(self):
        ''' Metodo que permite acceder a las funcionalidad del AbmProductoAseo'''
        self.limpiar()
        form = AbmProductoAseo(self.__panel_master)
        self.__vista_actual = form

