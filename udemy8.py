# #sin usar comprehension
# numeros = range(1, 10+1)
# numeros_pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         numeros_pares.append(numero)
# print(f'numeros pares: {numeros_pares}')
# #con list comprehension
# numeros = range(1, 10+1)
# numeros_pares2 = [numero for numero in numeros if numero % 2 == 0]
# print(numeros_pares2)
#funcion zip
# nombres = ['juan', 'maria', 'pedro']
# edades = [20, 30, 40]
# ciudades = ['madrid', 'valencia','huesca']
# personas = zip(nombres, edades, ciudades)
# print(personas)
# for persona in personas:
#     print(persona)
# #funcion split
# cadena = 'Hola Mundo'
# palabras = cadena.split()
# print(palabras)
# #find
# cadena = 'Hola Mundo'
# posicion = cadena.find('Mundo')
# print(posicion)
# #replace
# cadena = 'Hola Mundo'
# nueva_cadena = cadena.replace('Mundo', 'Amigo')
# print(nueva_cadena)
#multiplicar la cadena
# cadena = 'Hola Mundo'
# multiplicar = cadena*3
# print(multiplicar)
# #funcion strip
# cadena = '           Hola Mundo'
# cadena_limpia = cadena.strip()
# print(cadena)
# print(cadena_limpia)
# cadena = '...................Hola Mundo'
# cadena_limpia = cadena.strip('.')
# print(cadena)
# print(cadena_limpia)
#funcion sin lambda
# def cuadrado(x):
#     return x**2
# print(cuadrado(5))
# #funcion lambda (anonima)
# cuadrado_lambda = lambda x: x**2
# print(cuadrado_lambda(5))
# cuadrado_lambda = lambda x, y: x**2+y
# print(cuadrado_lambda(5, 1))
#con map y lambda: obtener el ^2 de cada valor de la lista
# numeros = [1, 2, 3, 4, 5]
# cuadrado = list(map(lambda x: x**2, numeros))
# print(cuadrado)
# #con filter y lambda: filtrar elementos pares
# numeros = [1, 2, 3, 4, 5]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)
# #con reduce y lambda
# from functools import reduce
# numeros = [1, 2, 3, 4, 5]
# suma_acumulativa = reduce(lambda x, y: x+y, numeros)
# print(suma_acumulativa)
# #sorted
# nombres = ['juan', 'pedro','aaron']
# nueva_lista_ordenada = sorted(nombres)
# print(nueva_lista_ordenada)
# #ordenar diccionario usando sorted y lambda
# nombres = [
#     {'nombre': 'juan', 'salario': 1},
#     {'nombre': 'aaron', 'salario': 2},
#     {'nombre': 'carmen', 'salario': 3}
# ]
# nueva_lista_ordenados_salario = sorted(nombres, key=lambda x:x['salario'], reverse=True)
# print(nueva_lista_ordenados_salario)
# #generadores
# def generador(maximo):
#     contador = 0
#     while contador < maximo:
#         yield contador
#         contador +=1
# #creamos un generador
# var_generador = generador(5)
# #iteramos sobre el generador
# for valor in var_generador:
#     print(valor)
# #expresiones generadoras
# generador = (x*2 for x in range(10)if x % 2 ==0)
# for cuadrado_pares in generador:
#     print(cuadrado_pares)
# #funcion a decorar
# def saludar(nombre):
#     print(f'hola {nombre}')
# saludar('carolina')
# #decorador
# def decorador(funcion):
#     def wrapper(*args, **kwargs):
#         print('antes de llamar la funcion saludar')
#         resultado = funcion(*args, **kwargs) #llammaos a la funcion
#         print('despues de llamar a la funcion saludar')
#         return resultado
#     return wrapper
#
# @decorador
# def saludar(nombre):
#     print(f'hola {nombre}')
# saludar('carolina')
# #funcion sum
# lista = [1, 2, 3, 4, 5]
# resultado = sum(lista)
# print(resultado)
# #dando un valor inicial
# resultado = sum(lista, 5)
# print(resultado)
# #funcion next
# lista = [1, 2, 3, 4, 5]
# iterador = iter(lista)
# resultado = next(iterador)
# print(resultado)
# resultado = next(iterador)
# print(resultado)
from logging import exception
def dividir (numerador, denominador):
    try:
        if denominador == 0:
            raise Exception('el denominador es zero')
        resultado = numerador / denominador
        print(resultado)
    except Exception as e:
        print(f'el error detail es: {e}')
    else:
        print('solo se ejecuta si no hay exception')
    finally:
        print('siempre se ejecuta aunque haya o no exception')
dividir(0,'hola')



