import os
import sys
from datetime import datetime, date
import time

      
def limpiar_pantalla():
    '''Limpia la pantalla. Se tiene en cuenta si el OS es windows o linux'''
    os.system('cls' if os.name=='nt' else 'clear')


def validar_ruc(msg,obligatorio, default = ""):

    """ Funcion que obtiene una cadena
    parametros: msg = mensaje que aparecerá al usuario, obligatorio = valor booleano si es obligatorio o no"""
    while ( True ): 
        
        data = input(msg)
        data = data or default
        try:
            if not obligatorio:
                raise Exception("Debe ingresar valor!")
            elif data.count("-") > 1:
                raise Exception("Debe meter un numero de RUC valido!")
            elif es_numerico(data.replace("-","")):
                if int(data) < 0:
                    raise Exception("Se esperaba numero positivo")
                return data
            else:
               raise Exception("Se esperaba Ruc valido!")
        except Exception:
            print ("Se esperaba Ruc valido!")

def es_numerico(numero):
    numeros = "0123456789"
    numerico = True
    for caracter in numeros:
        if caracter not in numeros:
            numerico = False
    return numerico


def numerico(msg,obligatorio, default = ""):

    """ Funcion que obtiene una cadena
    parametros: msg = mensaje que aparecerá al usuario, obligatorio = valor booleano si es obligatorio o no"""
    while ( True ): 
        
        data = input(msg)
        data = data or default
        try:
            if not obligatorio:
                raise Exception("Debe ingresar valor!")
            elif es_numerico(data):
                if int(data) < 0:
                    raise Exception("Se esperaba numero positivo")
                data = int(data)
                return data
            else:
               raise Exception("Se esperaba número!")
        except Exception as e:
            print (e)

def es_numerico(numero):
    numeros = "0123456789"
    numerico = True
    for caracter in numeros:
        if caracter not in numeros:
            numerico = False
    return numerico



def leer_entero(msg, min_value, max_value, default=None):
    ''' (string, int, int) -> int
       Pide que se ingrese número. Solo se retorna resultado cuando se ingresa
       un valor válido.
       @Parámetros
          msg : mensaje que se muestra al usuario.
          min_value: el valor mínimo que usuario debe ingresar
          max_value: el valor máximo que usuario debe ingresar
       Ej:
          leer_numero('Ingrese un número entre 1 y 9', 1, 9)
    '''
    while ( True ): 
        cualquier_valor = input(msg)
        try:
            #tratamos de convertir en número entero
            number = int(cualquier_valor)
            #verificamos si número no esta fuera de rango
            if number < min_value or number > max_value:
                raise Exception("Número fuera de rango [el minimo valor = " + 
                str(min_value) + ", el maximo valor = " + str(max_value) + "]: ")
            #se retorna valor válido ingresado por el usuario
            return number
        except ValueError as e:
            print ("Se esperaba número!")
        except TypeError as e:
            print ("Se esperaba número!")
        except Exception as e:
            print (e)


def leer_cadena(msg, obligatorio, default=""):
    """ Funcion que obtiene una cadena
    parametros: msg = mensaje que aparecerá al usuario, obligatorio = valor booleano si es obligatorio o no"""
    while ( True ): 
        '''if default:
           msg = msg + default + chr(8) * len(default)'''

        data = input(msg)
        data = data or default
        try:
            if obligatorio and len(data.strip()) == 0:
                raise Exception("Debe ingresar valor!")
            #se retorna valor válido ingresado por el usuario
            return data
        except Exception as e:
            print (e)


def leer_fecha(msg, obligatorio, default=""):
    while ( True ): 
        try:
            data = input(msg)
            data = data or default.strftime('%d/%m/%Y')

            if obligatorio and len(data.strip()) == 0:
                raise Exception("Debe ingresar valor!")
 
            if not datetime.strptime(data, '%d/%m/%Y').date(): #<= date.today():
                raise Exception("Debe cargar una fecha valida!")

            return datetime.strptime(data, '%d/%m/%Y').date()
        except AttributeError as e:
            print("Debe cargar una fecha valida!")
        except Exception as e:
            print ("Debe ingresar valor con el formato '%d/%m/%Y'!")

def leer_hora(msg, obligatorio, default= None):
    while(True):
        data = input(msg)
        try:
            if obligatorio and len(data.strip()) == 0:
                raise Exception("Debe ingresar valor de hora hh:mm")

            return time.time.strptime(data, '%H:%M').mktime()
        except Exception as e:
                print(e)

def pausa(msg):
    input(msg)
