from functools import reduce


#acc1: codigo accesorio
#b1: codigo balanceado
#m1: codigo medicamento
#p1: codigo producto aseo

dic_cantidad = {'acc1' : 10, 'b1' : 15, 'm1':20, 'p1':5}
dic_precio = {'acc1': 10000, 'b1':15000, 'm1':20000, 'p1':5000}

cantidad = int(input("CANTIDAD: "))
codigo = input("CODIGO PRODUCTO: ")

# son funciones anonimas de la programacion funcional
disminuir = lambda x, y: x - y
calculo = lambda x , y : x * y

for cod in dic_cantidad.keys():
    if cod == codigo:
        dic_cantidad[cod] = disminuir(dic_cantidad[cod] , cantidad) 
        total_pagar = calculo(dic_precio[cod], cantidad)

print("las cantidad actualizada: ",dic_cantidad[cod])
print("El total a pagar es: ", total_pagar)
