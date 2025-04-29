from libroDAO import LibroDAO
from libro import Libro
from conexion import Conexion

def menu():
    opcion = 0
    while opcion<5:
        print('''Menu
        1. Agregar libros
        2. Mostrar libros
        3. Actualizar libro
        4. Eliminar libro
        5. Salir''')
        opcion = int(input("Introduce una opcion(1-5): "))
        try:
            if opcion == 1:
                titulo = str(input("Introduce el titulo: "))
                autor = str(input("Introduce el autor/a: "))
                isbn = int(input("Introduce el isbn: "))
                precio = float(input("Introduce el precio: "))
                genero = str(input("Introduce el genero: "))
                nuevo_libro = Libro(titulo, autor, isbn, precio, genero)
                libros_agregados = LibroDAO.agregar_libro(nuevo_libro)
                print(libros_agregados)
            elif opcion == 2:
                LibroDAO.mostrar_libros()
            elif opcion == 3:
                id_updated = int(input("Introduce el ID: "))
                titulo_updated = str(input("Introduce el titulo: "))
                autor_updated = str(input("Introduce el autor/a: "))
                isbn_updated = int(input("Introduce el isbn: "))
                precio_updated = float(input("Introduce el precio: "))
                genero_updated = str(input("Introduce el genero: "))
                libro_updated = Libro(id_updated, titulo_updated, autor_updated, isbn_updated,
                                      precio_updated, genero_updated)
                libros_updated = LibroDAO.actualizar_libro(libro_updated)
                print(libros_updated)
            elif opcion == 4:
                id_deleted = int(input("Introduce el ID: "))
                libro_deleted = Libro(id_deleted)
                libros_deleted = LibroDAO.eliminar_libro(libro_deleted)
                print(libros_deleted)
        except Exception as e:
            print(f'error details: {e}')
    else:
        print('Saliendo...')

if __name__ == '__main__':
    menu()