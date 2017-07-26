import sys
sys.path.append("../") #referencia al directorio base
import tkinter as tk
from vistas import PanelPrincipal
        

root = tk.Tk()

def login_listener():
    ''' Metodo que inicia el panel principal'''
    
    panel_principal = PanelPrincipal(root)

login_listener()
root.mainloop()
