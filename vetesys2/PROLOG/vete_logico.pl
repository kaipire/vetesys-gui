/*Programacion Logica de Sistema Veterinaria*/

/*Hechos sobre Personas */

/* Hechos: es_persona(X) X es una persona */
es_persona('1222333').
es_persona('3222111').

/*Hechos: es_nombre_de(X,Y)X es nombre de Y*/
es_nombre_de('Luis','1222333').
es_nombre_de('Victor','3222111').

/*Hecho: es direccion_de(X,Y) X es apellido de Y*/
es_direccion_de('Palma 123','1222333').
es_direccion_de('Mcal Lopez 312','3222111').

/*Hechos sobre Clientes*/

/*Hechos: es_contacto_de(X,Y) X es telefono de Y*/
es_contacto_de('944-000','1222333').
es_contacto_de('495-558','3222111').


/*Hechos:es_direccion_de(X,Y) X es la direccion de Y*/
es_mascota_de('Pelusa', '1222333').
es_mascota_de('Apolo', '1222333').
es_mascota_de('Pandora', '3222111').
es_mascota_de('Waldo', '3222111').

/* Regla: es_informacion_de_cliente(Cedula, Nombre, Direccion, Contacto, Mascotas) si */
es_informacion_de_propietario(Cedula, Nombre, Apellido, Contacto) :-
	es_nombre_de(Nombre, Cedula), es_direccion_de(Direccion, Cedula), es_contacto_de_propietario(Contacto, Cedula), son_mascotas_de(Mascotas, Cedula).

/*Hechos sobre Mascotas*/
es_mascota('1').
es_mascota('2').
es_mascota('3').
es_mascota('4').

/*Hechos: es_nombre_de(X,Y)X es nombre de Y*/
es_nombre_de('Pelusa','1').
es_nombre_de('Apolo','2').
es_nombre_de('Pandora','3').
es_nombre_de('Waldo','4').

/*Hechos: es_edad_de(X,Y)X es nombre de Y*/
es_edad_de('11','1').
es_edad_de('5','2').
es_edad_de('3','3').
es_edad_de('7','4').

/*Hechos: es_peso_de(X,Y)X es nombre de Y*/
es_peso_de('10','1').
es_peso_de('4','2').
es_peso_de('3','3').
es_peso_de('2','4').

/*Hechos: es_sexo_de(X,Y)X es nombre de Y*/
es_sexo_de('hembra','1').
es_sexo_de('macho','2').
es_sexo_de('hembra','3').
es_sexo_de('macho','4').

/*Hechos: es_especie_de(X,Y)X es nombre de Y*/
es_especie_de('canina','1').
es_especie_de('felina','2').
es_especie_de('felina','3').
es_especie_de('felina','4').

/*Hechos: es_raza_de(X,Y)X es nombre de Y*/
es_raza_de('mestiza','1').
es_raza_de('siames','2').
es_raza_de('bengala','3').
es_raza_de('ragdoll','4').

/* Regla: es_informacion_de_mascota(ID, Nombre, Edad, Peso, Sexo, Especie, Raza) si */
es_informacion_de_propietario(Cedula, Nombre, Apellido, Contacto) :-
	es_nombre_de(Nombre, ID), es_edad_de(Edad, ID), es_peso_de(Peso, ID), es_sexo_de(Sexo, ID), es_especie_de(Especie, ID), es_raza_de(Raza, ID) 
