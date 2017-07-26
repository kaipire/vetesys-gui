from abc import ABCMeta, abstractmethod
from persistent import Persistent
from i18n import msg
import util
from persistent import Persistent

class Modulo(metaclass=ABCMeta):
    def __init__(self, titulo_menu='**** MENU ****'):
        self.__titulo_menu = titulo_menu
        self.__terminar_ejecucion = False

    def get_terminar_ejecucion(self):
        return self.__terminar_ejecucion
        
    def set_terminar_ejecucion(self, terminar_ejecucion):
        self.__terminar_ejecucion = terminar_ejecucion
                        
    def get_titulo_menu(self):
        return self.__titulo_menu
                    
    def set_titulo_menu(self, titulo_menu):
        self.__titulo_menu = titulo_menu
 
    @abstractmethod    
    def get_menu_dict(self):
        pass 
        
    def pausa(self):
       util.pausa(msg('presionar.enter.continuar'))   
        
    def mostrar_menu(self):

        print(self.get_titulo_menu())
        for key  in self.get_menu_dict().keys(): 
            menu = self.get_menu_dict().get(key)
            print(key, menu.get_titulo())

        print("")
   
    def iniciar(self):

        self.set_terminar_ejecucion(False)
        cant_menu = len(self.get_menu_dict())
        while (not self.get_terminar_ejecucion()):
            util.limpiar_pantalla()
            self.mostrar_menu()
            opcion = util.leer_entero(msg('ingresar.opcion'), min_value=1, max_value=cant_menu) 
            menu_seleccionado = self.get_menu_dict()[opcion]
            menu_seleccionado.ejecutar_funcion()

        
########################################################################
class Menu():
    def __init__(self, titulo, funcion):
        self.__titulo = titulo
        self.__funcion = funcion
        
    def get_titulo(self):
        return self.__titulo
        
    def set_titulo(self, titulo):
        self.__titulo = titulo
                    
    def get_funcion(self):
        return self.__funcion
        
    def set_funcion(self, funcion):
        self.__funcion = funcion
        
    def ejecutar_funcion(self):
        self.__funcion()

######################################################
class Persona(Persistent):
    def __init__(self, cedula, nombre, direccion):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__direccion = direccion
#setters & getters
    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion


##########ciente#########################
class Cliente(Persona):
    def __init__(self, contacto, mascotas, **kwargs):
        super().__init__(**kwargs)
        self.__contacto = contacto
        self.__mascotas = mascotas
#setters and getters

    def get_contacto(self):
        return self.__contacto

    def set_contacto(self, contacto):
        self.__contacto = contacto

    def get_mascotas(self):
        return self.__mascotas

    def set_mascotas(self, mascotas):
        self.__mascotas = mascotas

    def __str__(self):
        return ("Cedula: " + self.get_cedula() + "\n" + 
            "Cliente: " + self.get_nombre() + "\n" +
            "Direccion: " + self.get_direccion() + "\n" +
            "Contacto: " + self.get_contacto() + "\n")


############cliente######################################################33
class Mascota(Persistent):
    def __init__(self, identificador, nombre, edad, peso, sexo, especie, raza):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__sexo = sexo
        self.__especie = especie
        self.__raza = raza
        self.__servicio = None 


#setters & getters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_servicio(self):
        return self.__servicio

    def set_servicio(self, servicio):
        self.__servicio = servicio

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def get_identificador(self):
        return self.__identificador

    def set_identificador(self, identificador):
        self.__identificador = identificador

    def __str__(self):
        return ("ID: " + self.get_identificador() + "\n" + 
            "Mascota: " + self.get_nombre() + "\n" +
            "Edad: " + self.get_edad() + "\n" +
            "Peso: " + self.get_peso() + "\n" +
            "Sexo: " + self.get_sexo() + "\n" +
            "Especie: " + self.get_especie() + "\n" +
            "Raza: " + self.get_raza() + "\n")
    

################################################33
class Servicio(Persistent):
    def __init__(self, fecha):
        self.__fecha = fecha

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def __str__(self):
        return ("Fecha del servicio: " + str(self.get_fecha()))


####################################################
class Consulta(Servicio):
    def __init__(self, diagnostico, tratamiento, obs, **kwargs):
        super().__init__(**kwargs)        
        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento
        self.__obs = obs

    def get_diagnostico(self):
        return self.__diagnostico

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def get_tratamiento(self):
        return self.__tratamiento

    def set_tratamiento(self, tratamiento):
        self.__tratamiento = tratamiento

    def get_obs(self):
        return self.__obs

    def set_obs(self, obs):
        self.__obs = obs

    def __str__(self):
        return ("CONSULTA\n" + super().__str__() + "\n" +
                "Diagnostico: " + self.__diagnostico + "\n" +
                "Tratamiento: " + self.__tratamiento + "\n" + 
                "Observaciones: " + self.__obs)


###############################################################333
class Vacunacion(Servicio):
    def __init__(self, vacuna, dosis, revacuna, obs, **kwargs):
        super().__init__(**kwargs)
        self.__vacuna = vacuna
        self.__dosis = dosis
        self.__revacuna = revacuna
        self.__obs = obs

    def get_vacuna(self):
        return self.__vacuna

    def set_vacuna(self, vacuna):
        self.__vacuna = vacuna

    def get_dosis(self):
        return self.__dosis

    def set_dosis(self, dosis):
        self.__dosis = dosis

    def get_revacuna(self):
        return self.__revacuna

    def set_revacuna(self, revacuna):
        self.__revacuna = revacuna

    def get_obs(self):
        return self.__obs

    def set_obs(self, obs):
        self.__obs = obs

    def __str__(self):
        return ("VACUNACION\n" + super().__str__() + "\n" + 
               "Vacuna: " + self.__vacuna + "\n" + 
               "Dosis: " + self.__dosis + "\n" + 
               "Fecha de Revacunacion: " + str(self.__revacuna) + "\n" +
               "Observaciones: " + self.__obs)

###################################################################
class Aseo(Servicio):
    def __init__(self, banho, peluqueria, **kwargs):
        super().__init__(**kwargs)
        self.__banho = banho
        self.__peluqueria = peluqueria

    def get_banho(self):
        return self.__banho

    def set_banho(self, banho):
        self.__banho = banho

    def get_peluqueria(self):
        return self.__peluqueria

    def set_peluqueria(self, peluqueria):
        self.__peluqueria = peluqueria

    def __str__(self):
        
        return ("ASEO\n" + super().__str__() + "\n" +
               "Baño: " + self.__banho + "\n" +
               "Peluqueria: " + self.__peluqueria)


###########################################33
class Insumo(Persistent):
    def __init__(self, codigo, nombre, marca, descripcion, fecha_de_caducidad, precio, existencia):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__marca = marca
        self.__descripcion = descripcion
        self.__fecha_de_caducidad = fecha_de_caducidad
        self.__precio = precio
        self.__existencia = existencia

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo
      
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_existencia(self):
        return self.__existencia

    def set_existencia(self, existencia):
        self.__existencia = existencia

    def get_fecha_de_caducidad(self):
        return self.__fecha_de_caducidad

    def set_fecha_de_caducidad(self, fecha_de_caducidad):
        self.__fecha_de_caducidad = fecha_de_caducidad

    def __str__(self):
        return ("COD: " + self.get_codigo() + "\n" + 
               "Accesorio: " + self.get_nombre() + "\n" +
               "Marca: " +  self.get_marca() + "\n" + 
               "Descripcion: " + self.get_descripcion() + "\n" +
               "Fecha de Caducidad: " + str(self.get_fecha_de_caducidad()) + "\n" + 
               "Precio: " + str(self.get_precio()) + "\n" +
               "Existencias: " + str(self.get_existencia()))

################################################
class Medicamento(Insumo):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)

#################################################
class Balanceado(Insumo):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)

####################################################
class ProductoAseo(Insumo):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)

################################################
class Accesorio(Insumo):
    def __init__(self, **kwarg):
        super().__init__(**kwarg)


