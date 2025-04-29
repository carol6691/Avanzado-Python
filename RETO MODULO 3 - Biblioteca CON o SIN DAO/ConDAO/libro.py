
class Libro:
    def __init__(self, id=None, titulo=None, autor=None, isbn=None, precio=None, genero=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio
        self.genero = genero

    def __str__(self):
        return (f'ID: {self.id}, Titulo: {self.titulo}, '
                f'Autor: {self.autor}, ISBN: {self.isbn}, '
                f'Precio: {self.precio}, Genero: {self.genero}')

if __name__ == '__main__':
    libro1 = Libro(1, 'LibroA', 'Carolina', 123, 5, 'terror')
    print(libro1)