# class Persona:
#     contador = 0
#     def __init__(self, nombre, apellido):
#         Persona.contador += 1
#         self.id = Persona.contador
#         self.nombre = nombre
#         self.apellido = apellido
#     def mostrar(self):
#         print(f"detalles son:\n"
#               f"id: {self.id}, nombre: {self.nombre}, apellido: {self.apellido}")
# if __name__ == '__main__':
#     persona1 = Persona('gerardo', 'perez')
#     persona1.mostrar()
#     persona2 = Persona('daniel', 'sanchez')
#     persona2.mostrar()
#     print(f"contador: {Persona.contador}")

# class Persona:
#     contador = 0
#     def __init__(self, nombre, apellido):
#         Persona.contador +=1
#         self.id = self.contador
#         self.nombre = nombre
#         self.apellido = apellido
#     def __str__(self):
#         return f'id{self.id}, nombre: {self.nombre}, apellido: {self.apellido}'
#     @staticmethod
#     def get_contador():
#         print('metodo estatico')
#         return Persona.contador
#     @classmethod
#     def get_contador(cls):
#         print('metodo clase')
#         return cls.contador
# if __name__ == '__main__':
#     persona1 = Persona('gerardo', 'perez')
#     print(persona1.__str__())
#     print(Persona.contador)
#     print(Persona.get_contador())






















