# def saludar():
#     print(f"Hola Carolina!")
# saludar()
# def sumar(a, b):
#     return (a + b)
# #from udemy4 import sumarD
# a = float(input("introduce numero A: "))
# b = float(input("introduce numero B: "))
# print(f"El resultado de la suma es: {sumar(a, b):.2f}")
# def persona ():
#     nombre, apellido, edad = 'a', 'b', 31
#     return nombre.upper(), apellido.upper(), edad
# print(persona())
# tupla = persona ('a', 'b', 1)
# print (f"nombre: {tupla[0]}, apellido: {tupla[1]}, edad: {tupla[2]}")
# nombre, apellido, edad = persona ('a', 'b', 1)
# print (f"nombre: {nombre}, apellido: {apellido}, edad: {edad}")
# def coordenadas():
#     x, y, z = 1, 2, 3
#     return x, y, z
# print(coordenadas())
# x, y, z = coordenadas()
# print(f"resultado es: x: {x}, y: {y}, z: {z}")
# def sumar(*args):
#     total = 0
#     for i in args:
#         total = sum(i)
#     return total
# print(sumar(1, 2, 3, 3))
# def imprimir(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# imprimir(apellido='lliberos',edad=30)
# def es_par(numero):
#     if numero % 2 ==0:
#         print("el numero es par")
#     else:
#         print("el numero es impar")
#
# minumero = float(input("introduce numero: "))
# es_par(minumero)
# def funcion_recursiva(numero):
#     # caso base:
#     if numero ==1:
#         print(numero)
#     # caso recursivo
#     else:
#         print(numero)
#         funcion_recursiva(numero-1)
# funcion_recursiva(5)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(2))
# inventario = [
#     {'id': 1,
#      'nombre': 'camisa',
#      'precio': '$25',
#      'cantidad': 50},
#     {'id': 2,
#      'nombre': 'pantalones',
#      'precio': '$40',
#      'cantidad': 30}
# ]
# def mostrar():
#     print(inventario)
#     for producto in inventario:
#         print(f"ID: {producto['id']}, nombre: {producto['nombre']},"
#           f" precio: {producto['precio']}, cantidad: {producto['cantidad']}")
# def agregar():
#     print("--- Agregar nuevo producto ---")
#     nuevoid = int(input("ID: "))
#     nuevonombre = int(input("Nombre: "))
#     nuevoprecio = int(input("Precio: "))
#     nuevocantidad = int(input("Cantidad: "))
#     producto = {'id': nuevoid, 'nombre': nuevonombre, 'precio': nuevoprecio,'cantidad': nuevocantidad}
#     inventario.append(producto)
#     print("Producto anadido al inventario")
# def buscar():
#     print("--- buscar product por ID ---")
#     buscarporid = int(input("ingrese el id del producto que desea buscar: "))
#     for producto in inventario:
#         if buscarporid == producto['id']:
#             print("producto encontrado")
#             print("informacion del producto encontrado: ")
#             print(f"ID: {producto['id']}, nombre: {producto['nombre']},"
#                   f" precio: {producto['precio']}, cantidad: {producto['cantidad']}")
#     print("producto no encontrado")
#
# if __name__ == '__main__':
#     while True:
#         print("--- MENU ---")
#         print("\t 1. Mostrar inventario")
#         print("\t 2. Agregar nuevo producto")
#         print("\t 3. Buscar producto por ID")
#         print("\t 4. Salir")
#         seleccion = int(input("Seleccione una opción (1-4): "))
#         if seleccion == 1:
#             mostrar()
#         elif seleccion == 2:
#             agregar()
#         elif seleccion == 3:
#             buscar()
#         elif seleccion == 4:
#             print("saliendo")
#             break
#         else:
#             print("error")
# lista = [
#     {'id': 1, 'nombre': 'mars', 'precio': '$1'},
#     {'id': 2, 'nombre': 'kitkat', 'precio': '$2'}
# ]
# listacomprados =[]
#
# def comprar():
#     buscarid = int(input("introduce id del snack: "))
#     for producto in lista:
#         if producto['id'] == buscarid:
#             print("producto encontrado")
#             productocomprado = producto
#             listacomprados.append(productocomprado)
#             print(f"ID: {producto['id']}, nombre: {producto['nombre']},"
#             f"precio: {producto['precio']}, cantidad: {producto['cantidad']}")
#     print("producto no encontrado")
#
# def mostrar (comprar):
#     print("--- venta final: ---")
#     for producto in lista:
#         print(f"ID: {producto['id']}, nombre: {producto['nombre']},"
#               f"precio: {producto['precio']}, cantidad: {producto['cantidad']}")
def suma(a, b):
    resultado = a+b
    print(f"el resultado de la suma es: {resultado}")
def resta(a, b):
    resultado = a - b
    print(f"el resultado de la suma es: {resultado}")
def multiplicacion(a, b):
    resultado = a * b
    print(f"el resultado de la suma es: {resultado}")
def division(a, b):
    resultado = a // b
    print(f"el resultado de la suma es: {resultado}")
while True:
    print("*** calculadora con funciones ***")
    print("operaciones que puedes realizar: ")
    print('''
     1. Suma
     2. Resta
     3. Multiplicacion
     4. Division
     5. Salir''')
    opcion = int(input("introduce una opcion (1-5): "))
    if 1<= opcion <=4:
        a = float(input("introduce el valor 1: "))
        b = float(input("introduce el valor 2: "))
        if opcion == 1:
            suma(a, b)
        elif opcion == 2:
            resta(a, b)
        elif opcion == 3:
            multiplicacion(a, b)
        elif opcion == 4:
            division(a, b)
    elif opcion == 5:
        print("Saliendo")
        break
    else:
        print("Error")









