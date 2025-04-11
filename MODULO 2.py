# lista = [1, 2, 3]
# iterador = iter(lista)
# print(f"el valor es: {next(iterador)}")
# print(f"el valor es: {next(iterador)}")
# for i in range(10, 0, -1):
#     print(i)
# nums = range(10)
# list_of = list(nums)
# print(list_of)
# def suma(a, b):
#     """hola"""
#     print(a+b)
# suma(1,1)
# import re
# pattern = "Hola"
# text = "Hola mi amiga Carolina, Hola"
# replacement = "Adiós"
# nuevo_texto = re.sub(pattern, replacement, text)
# print(nuevo_texto)
# nuevo_texto = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
# print(nuevo_texto)
from UDEMY import nombre


# #crear un archivo
# nombre_archivo = "miarchivo.txt"
#
# #abrir el archivo en modo escritura
# with open(nombre_archivo, 'w') as archivo:
#     archivo.write('como estas?\n')
#     archivo.write("muy bien")
#
# print(f"se ha creado el archivo: {nombre_archivo}")

# nombre_archivo = "miarchivo.txt"
# try:
#     with open(nombre_archivo, 'x') as archivo:
#         archivo.write("hola")
#         archivo.write("\nadios")
#     print("archivo creado")
# except FileExistsError as e:
#     print("ya existe")
#     print(f"detalles del error: {e}")

# nombre_archivo = "miarchivo.txt"
# with open(nombre_archivo, 'w') as archivo:
#     archivo.write("fff")
#     archivo.write("\nadios")
# print(f"{nombre_archivo}")

# nombre_archivo = "miarchivo.txt"
# #leer un archivo
# with open(nombre_archivo, 'r') as archivo:
#     print(archivo.read())

# nombre_archivo = "miarchivo.txt"
# with open(nombre_archivo, 'a') as archivo:
#     archivo.write('linea adicional usando append\n')
#     archivo.write('segunda linea adicional\n')
# print(f"se ha anadido info al siguiente archivo: {nombre_archivo}")
