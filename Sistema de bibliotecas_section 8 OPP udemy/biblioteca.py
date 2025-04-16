from libro import Libro
class Biblioteca():
    def __init__(self, nombrebiblio):
        self._nombre = nombrebiblio
        self._listadelibros = []

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombrebiblio):
        self._nombre = nombrebiblio
    def get_listadelibros(self):
        return self._listadelibros

    def agregar(self, libro):
        #libro = Libro(Libro.get_titulo, Libro.get_autor, Libro.get_genero)
        self._listadelibros.append(libro)
        print(f'el siguiente libro ha sido anadido:{self.mostrar_libro(libro)}')

    def buscar_por_autor(self, autor):
        for libro in self._listadelibros:
            if libro.autor == autor:
                print(f'{self.mostrar_libro(libro)}')
        else:
            print("autor no encontrado")

    def buscar_por_genero(self, genero):
        for libro in self._listadelibros:
            if libro.get_genero() == genero:
                print(f'{self.mostrar_libro(libro)}')
        else:
            print("genero no encontrado")

    def mostrar_todos_libros(self):
        for libro in self.get_listadelibros():
            print(f'titulo: {libro.get_titulo()}, autor: {libro.autor}, genero: {libro.get_genero()}')

    def mostrar_libro(self, libro):
            return f'titulo: {libro.get_titulo()}, autor: {libro.autor}, genero: {libro.get_genero()}'
