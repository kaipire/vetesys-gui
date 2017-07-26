import sys
sys.path.append("../") #referencia al directorio base
import ZODB
import ZODB.FileStorage

__zodb_root = None
#__idioma = 'es'
__locale = None
__usuarios = {'admin':'root'}	


def get_zodb_root():
    global __zodb_root
    if not __zodb_root:
        db = ZODB.DB('data/db.fs')
        connection = db.open()
        __zodb_root  = connection.root
    return __zodb_root

def set_usuario(usuario):
	global __locale
	__locale = usuario

def get_usuario():
	
	return __locale

def logincompare(usu, contra):
	if usu in __usuarios.keys():
		if __usuarios[usu] == contra:
			global __locale
			__locale = usu
			return True
		else:
			return False
	else:
		return False

