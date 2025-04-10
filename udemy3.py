# contador = 1
# for contador in range(1, 6, 2):
#     print(contador)
#     contador += 1
# maximo = 5
# suma = 0
# numero = 1
# while numero <= maximo:
#     suma = suma + numero
#     numero += 1
#     print (f"sumar parcial: {suma}")
# print (f"la suma de 1 a 5 es: {suma}")
# while True:
#     opcion_1 = "crear cuenta"
#     opcion_2 = "eliminar cuenta"
#     opcion_3 = "salir"
#     print(f"Menu:\n"
#           f"1.{opcion_1}\n"
#           f"2.{opcion_2}\n"
#           f"3.{opcion_3}\n")
#     opcion = input("escoje una opcion: ")
#     if opcion == "1":
#         print("creando tu cuenta...")
#     elif opcion == "2":
#         print("eliminando tu cuenta...")
#     elif opcion == "3":
#         print("saliendo del sistema. hasta pronto...")
#         break
# saldo = 1000
# while True:
#     print(f"Menu:\n"
#                f"1. depositar\n"
#                f"2. retirar\n"
#                f"3. consultar saldo\n"
#                f"4. salir\n")
#     opcion = int(input("escoje una opcion: "))
#     if opcion == 1:
#         dinero = int(input("indica dinero a depositar: "))
#         saldo += dinero
#         print(f"tu saldo actual es: {saldo}")
#     elif opcion == 2:
#         dinero = int(input("indica dinero a retirar: "))
#         if dinero <= saldo:
#             saldo = saldo - dinero
#             print(f"tu saldo actual es: {saldo}")
#         else:
#             print("no se puede proceder")
#     elif opcion == 3:
#         print(f"tu saldo actual es: {saldo}")
#     elif opcion == 4:
#         print("saliendo")
#         break
#     else:
#         print("error")
# while True:
#     print(f"Menu:\n"
#         f"1. suma\n"
#         f"2. resta\n"
#         f"3. multiplicacion\n"
#         f"4. division\n"
#         f"5. salir\n")
#     opcion = int(input("escoje una opcion: "))
#     operando1 = float(input("introduce valor operando 1: "))
#     operando2 = float(input("introduce valor operando 2: "))
#     if opcion == 1:
#         suma = operando1 + operando2
#         print(f"la suma de {operando1}+{operando2} es: {suma:.2f}")
#     elif opcion == 2:
#         resta = operando1 - operando2
#         print(f"la resta de {operando1}-{operando2} es: {resta:.2f}")
#     elif opcion == 3:
#         multiplicacion = operando1 * operando2
#         print(f"la multiplicacion de {operando1}*{operando2} es: {multiplicacion:.2f}")
#     elif opcion == 4:
#         division = operando1 / operando2
#         print(f"la division de {operando1}/{operando2} es: {division:.2f}")
#     elif opcion == 5:
#         print("saliendo")
#         break
#     else:
#         print("error")
#option1:
# while True:
#     password = input("introduce una contrasena: ")
#     if len(password)<6:
#         print("password necesita tener 6 caracteres")
#     elif len(password)>=6:
#         print("passowrd correcto")
#         break
#     else:
#         print("error. reintroduce password")
#option2:
# password = input("introduce una contrasena: ")
# while len(password)<6:
#         print("password necesita tener 6 caracteres")
#         password = input("reintroduce una contrasena: ")
# print("contrasena correcta")
# import random
# aleatorio = random.randint(1, 10)
# contador = 0
# while contador<=10:
#     numero = int(input("introduce numero a adivinar: "))
#     contador += 1
#     if numero > aleatorio:
#         print("el numero indicado es demasiado alto")
#     elif numero < aleatorio:
#         print("el numero escrito es demasiado pequeno")
#     elif numero == aleatorio:
#         print(f"el numero escrito: {numero} es identico al aleatorio: {aleatorio}")
#         print(f"el numero de intentos es: {contador}")
#     else:
#         print("error")
#from UDEMY import mensaje
# mensaje = input("introduce mensaje: ")
# repeticiones = int(input("introduce numero de repeticiones: "))
# for i in range(0, repeticiones):
#     print(i)
#     print(mensaje)
# filas = int(input("introduce numero de filas: "))
# for fila in range(1, filas + 1):
#     espacio = " " * (filas - fila)
#     asterisco = "*" * (2 * fila - 1)
#     print(f"{espacio}{asterisco}")








