# class Animal:
#     def hacer_sonido(self):
#         print("hace sonido")
# class Perro(Animal):
#     def hacer_sonido(self):
#         print("ladra")
# class Gato(Animal):
#     def hacer_sonido(self):
#         print("arana")
# animal1 = Animal()
# animal1.hacer_sonido()
# perro1 = Perro()
# perro1.hacer_sonido()
# gato1 = Gato()
# gato1.hacer_sonido()
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f'''
        nombre: {self.nombre}
        apellido: {self.apellido}
        del padre: {super.__str__(self)}'''
persona1 = Persona ("carolina", "lliberos")
print(persona1.__str__())




