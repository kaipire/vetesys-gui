#ejecutar el archivo app_vete.py

#en la parte superior de la ventana principal tenemos el menu principal que se dividen 2 partes principales, los servicios clinicos(necesario registrar el cliente y sus respectivas mascotas), y la venta de insumos(accesorios para mascotas, productos de aseo, medicamentos y balanceados), no se registran las ventas de estos, pero si se actualizan las cantidades disponible de cada insumo

#Menu Cliente:
*Listar: nos muestra los datos de nuestros cliente guardados en la base de datos
*Registrar: nos presenta un formulario a llenar con los datos del cliente y sus respectivas mascotas



IMPORTANTE: a la hora de registrar un cliente, al darle clic en el boton "Cargar" estamos agregando una mascota en la lista del cliente y en la base de datos(independienmente del cliente) y nos permite seguir cargando mascotas,  al darle clic en el boton "Guardar", guardamos los datos del cliente con su lista de mascotas y finaliza el registro, por eso, cada vez que vamos a registrar un cliente primero tenermos que darle clic en "Cargar" y luego en "Guardar"




*Buscar: Busca el cliente en la base de datos por cedula, si lo encuentra, retorna sus datos y la lista de sus mascotas
*Modificar: busca el cliente que queremos eliminar en la base de datos, si lo encuentra retorna un formulario con los datos actuales, podemos borrar el campo que queremos cambiar y cargar el dato actualizado y darle clic en "Guardar" para que los cambios hagan efecto.
*Eliminar:borra de la base de datos al cliente cuya cedula coincida con que el solicitamos
*Agregar Mascota: permite el registro de una nueva mascota y añadirlo a la lista de un cliente ya existente en la base de datos


#Menu Mascota
*Listar: nos muestra una lista de todas las mascotas registradas de la veterinaria
*Modificar: permite actualizar datos de la mascota, (Idem Modificar Cliente)
*Eliminar: Borra todos los datos de una mascota de la base de datos y de la lista de su respectivo cliente
*Historial: sería al equivalente de "Buscar Cliente" pero con el agregado de que muestra el historial de servicios brindados a una mascota, el cual buscamos por su ID asignada
*Servicios: cada mascota posee una lista de servicios solicitados(Historial), con esta opcion vamos registrando esos servicios y agregandolos al historial de la mascota, ingresamos el ID de la mascota, y si se encuenta en la base de datos, nos muestra un submenu de servicio a solicitar(Consulta, Vacunacion, *Aseo), dependiendo del tipo de servicio veremos en pantalla un formulario a completar, al darle clic en guardar estaremos agregando el servicio al historial de la mascota.


*OBS: el Boton Aseo(Servicio Aseo) no fue implementado aun.


#Menu Insumos(Accesorios,Balanceados,Medicamentos,Productos de Aseo):
*Listar: nos muestra una lista de los insumos disponibles, podemos ver el precio, la cantidad disponible y su respectivo codigo(importante para realizar busqueda)
*Registrar: nos permite agregar un nuevo insumo en nuestra base de datos
*Buscar: nos permite buscar un insumo en especifico por codigo
*Modificar: nos permite actualizar cualquier dato del insumo
*Eliminar: borra el registro del insumo de nuestra base de datos
*Venta: la funcion principal del menu de insumos, ingresando el codigo del insumo y la cantidad solicita, nos calcula el precio a cobrar al interesado y actualiza automaticamente las existencias de dicho insumo

#Boton Salir: finaliza el programa

OBS: La base de datos utilizada es el ZODB, los datos cargados son de prueba y por tanto podrian llegar a ser incoherentes pero la logica del negocio funciona, es decir que con datos correctos igual funcionaria.

CORRECCIONES
*al registrar un servicio ya muestra a que mascota lo vamos a ser y el nombre de su dueño
*se implemento el servicio aseo
*el historial no imprime esteticamente bien(imprime en cualquier parte)pero imprime los datos corretos
*se corrigio el servicio de ventas de insumos
