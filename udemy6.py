# class Aritmetica:
#     def __init__(self, operando1=None, operando2=None):
#         self._operando1 = operando1
#         self._operando2 = operando2
#     def sumar(self):
#         resultado = self._operando1 + self._operando2
#         print(f"el resultado de la suma es: {resultado}")
#     def restar(self):
#         resultado = self._operando1 - self._operando2
#         print(f"el resultado de la suma es: {resultado}")
#     def get_operando1(self):
#         return self._operando1
#     def set_operando1(self, operando1):
#         self._operando1 = operando1
#     def get_operando2(self):
#         return self._operando2
#     def set_operando2(self, operando2):
#         self._operando2 = operando2
# if __name__ == '__main__':
#     aritmetica1 = Aritmetica(operando1 = 1, operando2 = 1)
#     aritmetica1.sumar()
#     aritmetica1.set_operando1(3)
#     aritmetica1.set_operando2(3)
#     print(f"el valor del operando1 es: {aritmetica1.get_operando1()}")
#     print(f"el valor del operando1 es: {aritmetica1.get_operando2()}")
#     aritmetica1.sumar()
#
#     print()
#     aritmetica2 = Aritmetica(2, 2)
#     aritmetica2.restar()
#     aritmetica2.set_operando1(5)
#     aritmetica2.set_operando2(4)
#     aritmetica2.restar()
from udemy import nombre


# class Coche:
#     def __init__(self, marca, modelo, color):
#         self._marca = marca
#         self._modelo = modelo
#         self.__color = color
#     def conducir(self):
#         print(f"marca: {self._marca}, modelo: {self._modelo}, color: {self.__color}")
#     def get_marca(self):
#         return self._marca
#     def set_marca(self, marca):
#         self._marca = marca
#     def get_modelo(self):
#         return self._modelo
#     def set_modelo(self, modelo):
#         self._modelo = modelo
#     def get__color(self):
#         return self.__color
#     def set__color(self, color):
#         self.__color = color
# coche1 = Coche('kia', 'niro', 'negro')
# coche1.conducir()
# coche1.set_marca('opel')
# coche1.set_modelo('corsa')
# coche1.set__color('rosa')
# coche1.conducir()
# coche1.marca = 'caro' # por el dinamismo de python
#                       # se ha creado un nuevo atributo llamado: marca con su valor: caro
# print(f"atributos coche1: {coche1.__dict__}") # el atributo marca solo sale usando __dict__













