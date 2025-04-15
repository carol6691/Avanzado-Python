import os
import re

class Contacto:
    def __init__(self, nombre = None, telefono = None, email = None):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def __str__(self):
        return (f'detalles del contacto:'
              f' nombre: {self.nombre}\n'
              f'telefono: {self.telefono}\n'
              f'email: {self.email}\n')
    def escribir_contacto_en_archivo(self):
        return f'{self.nombre}, {self.telefono}, {self.email}'
class GestionContactos:
    NOMBRE_ARCHIVO = 'contactos.txt'

    def __init__(self):
        self.lista_de_contactos = []
        self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(',')
                    nombre, telefono, email = datos
                    contacto = Contacto(nombre, telefono, email)
                    self.lista_de_contactos.append(contacto)
    def guardar_contactos(self):
        with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
            for contacto in self.lista_de_contactos:
                archivo.write(contacto.escribir_contacto_en_archivo()) # o
                # o archivo.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n")

    # funcion reguladora usando metodo de clase o estatico
    @staticmethod
    def validar_email(email):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        match = re.match(patron, email)
        return match

    def agregar_contacto(self, nombre = None, telefono = None, email = None):
        try:
            # lo ideal seria poner todos los inputs en la seccion de 'if opcion == 1, elif...'
            nombre = input("introduce nombre: ")
            telefono = int(input("introduce telefono: "))
            email = input("introduce email: ")
            if not nombre or not telefono or not email:
                print("campo en blanco. rellena todos los campos")
                return
            if not self.validar_email(email):
                print("email no valido")
                return

            nuevo_contacto = Contacto(nombre, telefono, email)
            self.lista_de_contactos.append(nuevo_contacto)
            self.guardar_contactos()
            print(f'contacto anadido: {nuevo_contacto}')

        except Exception as e:
            print(f'error details: {e}\n'
              f'Introduce de nuevo')

    def mostrar_contactos(self):
        for contacto in self.lista_de_contactos:
            print(contacto)
        else:
            print("contacto no encontrado")
    def buscar_contacto(self):
        nombre = input("introduce nombre: ")

        for contacto in self.lista_de_contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(contacto)
            else:
                print("no encontrado")

    def eliminar_contacto(self):
        nombre = input("introduce nombre: ")
        for contacto in self.lista_de_contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.lista_de_contactos.remove(contacto)
                print("contacto eliminado")
            else:
                print("no encontrado y no eliminado")
def menu():
    gestion = GestionContactos()
    while True:
        print('''--- Sistema de gestion de contactos ---
                1. agregar contacto
                2. mostrar todos los contactos
                3. buscar un contacto
                4. eliminar un contacto
                5. salir''')

        opcion = int(input("introduce una opcion (1-5): "))

        if opcion == 1:
            gestion.agregar_contacto()
        elif opcion == 2:
            gestion.mostrar_contactos()
        elif opcion == 3:
            gestion.buscar_contacto()
        elif opcion == 4:
           gestion. eliminar_contacto()
        elif opcion == 5:
            print("saliendo")
            break
        else:
            print("Error. Vuelve a introducir una opcion de 1 a 5: ")
if __name__ == '__main__':
    menu()
