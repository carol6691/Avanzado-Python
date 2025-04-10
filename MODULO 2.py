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
import re
pattern = "Hola"
text = "Hola mi amiga Carolina, Hola"
replacement = "Adiós"
nuevo_texto = re.sub(pattern, replacement, text)
print(nuevo_texto)
nuevo_texto = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(nuevo_texto)




