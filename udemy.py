nombre = "carolina"
edad = 30
mensaje = "hola, me llamo {} y tengo {} anos".format(nombre, edad)
#print (mensaje)
#
nombre = input ("Introduce tu nombre: ")
apellido = input ("Introduce tu apellido: ")
ano_nacimiento = input("Introduce tu ano de nacimiento: ")
nombresliced = nombre[0:2]
nombreslicedmayus = nombresliced.upper()
apellidosliced = apellido[0:2]
apellidoslicedmayus = apellidosliced.upper()
ano_nacimientosliced = ano_nacimiento[2:4]
import random
num4digitosaleatorio = random.randint(1000, 9999)
IDunico =f"{nombresliced}{apellidosliced}{ano_nacimientosliced}{num4digitosaleatorio}"
print (f"El ID es el siguiente: {IDunico}")
