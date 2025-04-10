# numero = int(input("introduce el numero de canciones: "))
# for i in range(numero):
#     cancion = input("introduce cancion a agregar: ")
#     lista.append(cancion)
# lista.sort()
# lista = []
# for cancion in lista:
#     print(cancion)
# print(lista)
# numero = int(input("introduce el numero de calificaciones: "))
# lista = []
# for i in range(numero):
#     calificacion = float(input(f"introduce la calificacion[{i}]: "))
#     lista.append(calificacion)
# total = sum(lista)
# promedio = total/numero
# print(f"los resultados son:\n"
#       f"nota total: {total}\n"
#       f"nota promedio: {promedio}")
# tupla = (1, 2, 3)
# id1, id2, id3 = tupla
# print(id1, id2)
# print(id3)
# productos = [("a", "b", 1), ("c", "d", 2), ('e', 'f', 3)]
# preciototal = 0
# for producto in productos:
#     id1, id2, precio = producto
#     preciototal = preciototal + precio
# print(preciototal)
# miset = {1, 3, 2}
# mitupla = (1, 3, 2)
# milista = [1, 3, 2]
# print (miset, mitupla, milista)
# conjunto = {"a@gmail.com", "b@gmail.com"}
# suscriptor = input("introduce tu email: ")
# if suscriptor in conjunto:
#     print("ya esta en la lista")
#     decision = input("eliminar?(si/no)")
#     if decision == "si":
#         conjunto.remove (suscriptor)
# else:
#     conjunto.add(suscriptor)
#     print("suscriptor anadido a la lista")
# print(conjunto)
# for suscriptor in conjunto:
#     print(suscriptor)
# setvacio = set()
# numero = int(input("introduce numero de suscriptores: "))
# for i in range(numero):
#     suscriptor = input("introduce tu email: ")
#     if suscriptor in setvacio:
#         print("ya esta en la lista")
#         eliminar = input("quieres eliminar de la lista?(si/no)")
#         if eliminar == "si":
#             setvacio.remove(suscriptor)
#             print(f"el email{suscriptor} ha sido eliminado")
#     else:
#         setvacio.add(suscriptor)
#     print(f"se ha suscrito el siguiente email: {suscriptor}")
# for suscriptor in setvacio:
#      print(suscriptor)
# persona = {"nombre": 1,
#            "edad": 30,
#            "ciudad": "spain"}
# print(persona)
# print(persona["nombre"])
# print(persona["edad"])
# print(persona["ciudad"])
# persona["profesion"] = "ingeniero"
# print(persona)
# for clave, valor in persona.items():
#      print (f"clave: {clave}, valor: {valor}")
#contactos = {'nombre': 'carolina', 'telefono': 123, 'email': 'a@gmail.com', 'direccion': 'botanic 31'}
# contactos = {
#     "carlos": {
#         'apellido': 'llib',
#         'telefono': "123"},
#     "juan":{
#         'apellido': 'luz',
#         'telefono': "456"}}
# print (contactos)
# print(contactos["carlos"])
# print(f": {contactos["carlos"]["apellido"]}")
# contactos["caro"] = {'apellido': 'lliberos',
#         'telefono': "789"}
# print (contactos)
# for diccionario1, diccionario2 in contactos.items():
#     print(f'''nombre: {diccionario1}
#     apllido: {diccionario2["apellido"]}
#     telefono: {diccionario2["telefono"]}
# ''')
# lista = [{'nombre': 'carolina', 'apellido': 'lliberos'},
#          {'nombre': 'miguel', 'apellido': 'gil'}]
# print(f"{lista[1].get("apellido")}")
# for index, persona in enumerate(lista):
#     print(f"persona:\n"
#           f"nombre: {persona.get("nombre")}\n"
#           f"apellido: {persona.get("apellido")}\n")
# for persona in lista:
#     print(f"persona:\n"
#           f"nombre: {persona["nombre"]}\n"
#           f"apellido: {persona["apellido"]}\n")
# listaejemplo = [
#     {
#         'id': '1',
#         'nombre': 'camisa',
#         'precio': '26',
#         'cantidad': '50'
#     },
#     {
#         'id': '1',
#         'nombre': 'pantalones',
#         'precio': '40',
#         'cantidad': '30'
#     }
# ]
# lista = []
# numero = int(input("indique numero de prodctos a agregar: "))
# for i in range(numero):
#     print(f"proporciona la siguiente info del producto numero {i}: ")
#     nombre = input("indique nombre: ")
#     precio = float(input("indique precio: "))
#     cantidad = int(input("indique cantidad: "))
#     producto = {'id': i, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
#     lista.append(producto)
# print(lista)
# buscar = int(input("introducir id del producto a buscar: "))
# for producto in lista:
#     if producto['id'] == buscar:
#         print("producto encontrado")
#         print(f"id: {producto['id']}\n"
#               f"nombre: {producto['nombre']}")
#         break
#     else:
#         print("producto not found")





