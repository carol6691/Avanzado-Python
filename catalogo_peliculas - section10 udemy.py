import os


class Pelicula:
    def __init__(self, nombre, director, ano):
        self.nombre = nombre
        self.director = director
        self.ano = ano
    def __str__(self):
        return f'Nombre: {self.nombre}, Director: {self.director}, Ano: {self.ano}'
    def escribir_pelicula_en_archivo(self):
        return f'{self.nombre}, {self.director}, {self.ano}\n'
class Servicio_Peliculas:
    NOMBRE_ARCHIVO = 'peliculas.txt'
    #def __init__(self):
        #self.nombre_archivo = 'peliculas.txt'
    def agregar_pelicula(self, pelicula):
        with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.escribir_pelicula_en_archivo()}')
        print(f'pelicula anadida: {pelicula}')
    def mostrar_peliculas(self):
        with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
            print(archivo.read())
    def eliminar_peliculas(self):
        with open(self.NOMBRE_ARCHIVO, 'w') as archivo:
            pass
        #os.remove(self.NOMBRE_ARCHIVO)
        print('Catalogo eliminado')

class AppCatalogoPeliculas:
    def __init__(self):
        #creamos un objeto
        self.servicio_peliculas = Servicio_Peliculas
    def menu(self):

        while True:
            try:
                print('''**** catalogo de peliculas ****
                1. agregar pelicula
                2. mostrar peliculas
                3. eliminar catalaogo completo
                4. salir
                ''')
                opcion = int(input('introduce una opcion (1-4): '))
                if opcion == 1:
                    nombre = str(input("introduce titulo de la pelicula: "))
                    director = str(input("introduce director de la pelicula: "))
                    ano = int(input("introduce ano de la pelicula: "))
                    nueva_pelicula = Pelicula(nombre, director, ano)
                    self.servicio_peliculas.agregar_pelicula(nueva_pelicula)
                elif opcion ==2:
                    self.servicio_peliculas.mostrar_peliculas()
                elif opcion ==3:
                    self.servicio_peliculas.eliminar_peliculas()
                elif opcion ==4:
                    print('saliendo')
                    break
                else:
                    print('opcion no valida')
            except Exception as e:
                print(f'error details: {e}')
if __name__ == '__main__':
    app1 = AppCatalogoPeliculas()
    app1.menu()


