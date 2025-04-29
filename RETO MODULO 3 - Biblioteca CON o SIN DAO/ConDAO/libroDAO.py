from conexion import Conexion
from libro import Libro

class LibroDAO:
    READ = 'SELECT * FROM libros'
    CREATE = 'INSERT INTO libros(titulo, autor, isbn, precio, genero) VALUES(%s, %s, %s, %s, %s) '
    UPDATE ='UPDATE libros SET titulo=%s, autor=%s, isbn=%s, precio=%s, genero=%s WHERE id=%s'
    DELETE ='DELETE FROM libros WHERE id=%s'

    @classmethod
    def mostrar_libros(cls):
        conexion = None
        try:
            conexion = Conexion.crear_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.READ)
            libros = cursor.fetchall()
            for libro in libros:
                print(libro)
            return libros
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.quitar_conexion(conexion)

    @classmethod
    def agregar_libro(cls, libro):
        conexion = None
        try:
            conexion = Conexion.crear_conexion()
            cursor = conexion.cursor()
            valores = (libro.titulo, libro.autor, libro.isbn, libro.precio, libro.genero)
            cursor.execute(cls.CREATE, valores)
            conexion.commit()
            print(f'Libro anadido a la DB')
            return cursor.rowcount
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.quitar_conexion(conexion)

    @classmethod
    def actualizar_libro(cls, libro):
        conexion = None
        try:
            conexion = Conexion.crear_conexion()
            cursor = conexion.cursor()
            valores = (libro.titulo, libro.autor, libro.isbn, libro.precio, libro.genero, libro.id)
            cursor.execute(cls.UPDATE, valores)
            conexion.commit()
            print(f'Libro ha sido actualizado')
            return cursor.rowcount
        except Exception as e:
            print(f'error details en UPDATE: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.quitar_conexion(conexion)

    @classmethod
    def eliminar_libro(cls, libro):
        conexion = None
        try:
            conexion = Conexion.crear_conexion()
            cursor = conexion.cursor()
            valores = (libro.id,)
            cursor.execute(cls.DELETE, valores)
            conexion.commit()
            print(f'Libro ha sido eliminado')
            return cursor.rowcount
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.quitar_conexion(conexion)

if __name__ == '__main__':
    #AGREGAR LIBRO
    libro1 = Libro(titulo='Solo en casa', autor='carolina lliberos', isbn=123, precio=10, genero='terror')
    libro2 = Libro(titulo='masia', autor='miguel gil', isbn=456, precio=5, genero='aventura')
    libros_agregados = LibroDAO.agregar_libro(libro1)
    libros_agregados = LibroDAO.agregar_libro(libro2)
    # print(libros_agregados)
    # #update libros
    # libro1_updated = Libro(titulo='el anillo', autor='pepita bueno', isbn=123, precio=10, genero='terror', id=1)
    # libros_updated = LibroDAO.actualizar_libro(libro1_updated)
    # print(libros_updated)
    #eliminar libros
    # libro_eliminado = Libro(id=2)
    # libros_eliminados = LibroDAO.eliminar_libro(libro_eliminado)
    # print(libros_eliminados)

    #mostrar libros
    print(LibroDAO.mostrar_libros())