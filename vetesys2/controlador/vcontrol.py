from abc import ABCMeta, abstractmethod
import BTrees.OOBTree
import persistent, transaction
from bd import get_zodb_root, get_usuario
from i18n import msg
from modulo.vmodel import Cliente, Mascota, Insumo
import util


class ControladorAncestro:
    __metaclass__ = ABCMeta
    __diccionario_objetos = None
    
    def crear(self, objeto):
        if not objeto:
            raise Exception(msg("no se pudo guardar el registro"))

        self.validar_objeto(objeto)
        self.validar_insercion_registro(objeto)
        self.get_diccionario_objetos()[self.get_id_objeto(objeto)] = objeto
                                                                             
        transaction.commit()

    def borrar(self, objeto):
        if not objeto:		
            raise Exception(msg("registro nulo"))
        self.validar_eliminacion_registro(objeto)
        del self.get_diccionario_objetos()[self.get_id_objeto(objeto)]
        transaction.commit()

    def actualizar(self, objeto):
        self.validar_actualizacion_registro(objeto)
        self.get_diccionario_objetos()[self.get_id_objeto(objeto)] = objeto
        transaction.commit()
    
    '''metodo que crea el dicccionario con el nombre de la base de datos si no existe,o retorna el diccionario de la clase'''

    def get_diccionario_objetos(self):
        if not self.__diccionario_objetos:
		#cada clase va a tener su propio diccionario
            nombre_diccionario = self.__class__.__name__
            if not hasattr(get_zodb_root(), nombre_diccionario):
			#creo un atributo para root, cuyo nombre es el nombre de la clase
                setattr(get_zodb_root(), nombre_diccionario,  BTrees.OOBTree.BTree())
			
            self.__diccionario_objetos = getattr(get_zodb_root(), nombre_diccionario)
        return self.__diccionario_objetos

    ''' retorna los valores de cada clave del diccionario'''
    def get_lista_objetos(self):
        return self.get_diccionario_objetos().values() 

    @abstractmethod
    def validar_objeto(self, objeto):
        pass

    @abstractmethod
    def validar_eliminacion_registro(self, objeto):
        pass
	
    @abstractmethod
    def validar_actualizacion_registro(self, objeto):
        pass

    @abstractmethod
    def validar_insercion_registro(self, objeto):
        pass

    @abstractmethod
    def get_id_objeto(self, objeto):
        pass

    @abstractmethod
    def buscar_cod(self, identificador):
        pass

########################################################################
class PersonaControlador(ControladorAncestro):

    def get_id_objeto(self, persona):
        return persona.get_cedula()
    '''no sea crea el persona si hay valores nulos'''
    def validar_objeto(self, persona):        
        if not persona.get_nombre() or len(persona.get_nombre().strip())==0:
            raise Exception(msg("cargar.nombre.persona"))

        if not persona.get_cedula() or len(persona.get_cedula().strip()) == 0:
            raise Exception(msg("cargar.cedula.persona")) 

        if not persona.get_direccion() or len(persona.get_direccion().strip()) == 0:
            raise Exception(msg("cargar.direccion.persona")) 

    '''valida que ya exista esa cedula'''
    def validar_insercion_registro(self,persona):
        if persona.get_cedula() in self.get_diccionario_objetos().keys() :
                raise Exception(msg("abm.persona.existe")) 

    '''valida de que exista la persona a actualizar '''
    def validar_actualizacion_registro(self, persona):
        if not persona.get_cedula() in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.persona.error.actualizar")) 

    '''valida que exista la persona a eliminar'''
    def validar_eliminacion_registro(self, persona):
        if not persona.get_cedula() in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.persona.error.eliminar")) 

    ''' busca la cedula en las claves y retorna el objeto'''
    def buscar_cod(self, cedula):
        for ced in self.get_diccionario_objetos().keys():
            if ced == cedula:
                return self.get_diccionario_objetos()[ced]
        return None


########################################################################
class MascotaControlador(ControladorAncestro):

    def get_id_objeto(self, mascota):
        return mascota.get_identificador()
    '''no sea crea el mascota si hay valores nulos'''
    def validar_objeto(self, mascota):

        if not mascota.get_identificador() or len(mascota.get_identificador().strip())==0:
            raise Exception(msg("cargar.mascota.id"))

        if not mascota.get_edad():	
            raise Exception(msg("cargar.mascota.edad"))

        if not mascota.get_peso(): #or len(mascota.get_peso()) == 0:
            raise Exception(msg("cargar.mascota.peso"))

        if not mascota.get_sexo() or len(mascota.get_sexo()) == 0:
            raise Exception(msg("cargar.mascota.sexo")) 

        if not mascota.get_especie() or len(mascota.get_especie()) == 0:
            raise Exception(msg("cargar.mascota.especie"))

        if not mascota.get_raza() or len(mascota.get_raza()) == 0:
            raise Exception(msg("cargar.mascota.raza"))

    '''valida que ya exista esa cedula'''
    def validar_insercion_registro(self, mascota):
        if mascota.get_identificador() in self.get_diccionario_objetos().keys() :
                raise Exception(msg("abm.mascota.existe"))

    '''valida de que exista el cliente a actualizar '''
    def validar_actualizacion_registro(self, mascota):
        if not mascota.get_identificador() in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.mascota.error.actualizar"))

    '''valida que exista el cliente a eliminar'''
    def validar_eliminacion_registro(self, mascota):
        if not mascota.get_identificador()in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.mascota.error.eliminar"))

    ''' busca el ruc en las claves y retorna el objeto'''
    def buscar_cod(self, ide):
        for iden in self.get_diccionario_objetos().keys():
            if iden == ide:
                return self.get_diccionario_objetos()[ide]
        return None


########################################################################
class InsumoControlador(ControladorAncestro):

    def get_id_objeto(self, insumo):
        return insumo.get_codigo()
    '''no sea crea el insumo si hay valores nulos'''
    def validar_objeto(self, insumo):
        if not insumo.get_codigo() or len(insumo.get_codigo().strip())==0:
            raise Exception(msg("cargar.insumo.codigo")) 

        if not insumo.get_fecha_de_caducidad():	
            raise Exception(msg("cargar.insumo.fecha"))

        if not insumo.get_existencia(): #or len(insumo.get_existencia())==0:
            raise Exception(msg("cargar.insumo.existencia"))

        if not insumo.get_marca():	
            raise Exception(msg("cargar.insumo.marca"))

        if not insumo.get_nombre():
            raise Exception(msg("cargar.insumo.nombre")) 


    '''valida que ya exista ese expediente'''
    def validar_insercion_registro(self,insumo):
        if insumo.get_codigo() in self.get_diccionario_objetos().keys() :
                raise Exception(msg("abm.insumo.existe"))

    '''valida de que exista el empleado a actualizar '''
    def validar_actualizacion_registro(self, insumo):
        if not insumo.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.insumo.actualizar"))

    '''valida que exista el empleado a elminar'''
    def validar_eliminacion_registro(self, insumo):
        if not insumo.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception(msg("abm.insumo.eliminar"))


    def buscar_cod(self, codigo):
        for nro in self.get_diccionario_objetos().keys():
            if nro == codigo:
                return self.get_diccionario_objetos()[nro]
        return None

######## InsumosControlador ####################################

class MedicamentoControlador(InsumoControlador):
    pass

class BalanceadoControlador(InsumoControlador):
    pass

class ProductoAseoControlador(InsumoControlador):
    pass

class AccesorioControlador(InsumoControlador):
    pass

