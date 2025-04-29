from tkinter.constants import INSERT
import mysql.connector
from libro import Libro

class GestionInventario:
    SELECCIONAR = 'SELECT * FROM libros ORDER BY id'
    INSERTAR = 'INSERT INTO libros(titulo, autor, isbn, precio, genero) VALUES(%s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE libros SET titulo=%s, autor=%s, isbn=%s, precio=%s, genero=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM libros WHERE id=%s'
    BUSCAR = 'SELECT * FROM libros WHERE id=%s'

    def __init__(self, database, user, password, host):
        self.config = {
            'database': 'biblioteca_db',
            'user': 'root',
            'password': '',
            'host': 'localhost'
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print('conectado')
        except Exception as e:
            print(f'error details: {e}')

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print('desconectado')

    def agregar_libro(self, libro):
        try:
            self.connect()
            cursor = self.connection.cursor()
            valores = (libro.titulo, libro.autor, libro.isbn, libro.precio, libro.genero)
            cursor.execute(GestionInventario.INSERTAR, valores)
            self.connection.commit()
            print(f'se ha agregado a la db el siguiente libro:{libro}')
            return cursor.rowcount
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            cursor.close()
            self.disconnect()

    def mostrar_libros(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(GestionInventario.SELECCIONAR)
            resultado = cursor.fetchall()
            for libro in resultado:
                print(libro)
            return cursor.rowcount
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            cursor.close()
            self.disconnect()

    def buscar_id(self, libro):
        try:
            self.connect()
            cursor = self.connection.cursor()
            valores = (libro.id,)
            cursor.execute(GestionInventario.BUSCAR, valores)
            resultado = cursor.fetchone()
            if resultado:
                print(f'''se ha encontrado el libro con id: {libro.id}
                                            Detalles: {resultado}''')
                return libro
            else:
                print('libro no encontrado')
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            cursor.close()
            self.disconnect()

    def actualizar_libro(self, libro):
        if self.buscar_id(libro) is None:
            print('libro no encontrado')
            return
        else:
            try:
                self.connect()
                cursor = self.connection.cursor()
                valores = (libro.id, libro.titulo, libro.autor, libro.isbn, libro.precio, libro.genero)
                cursor.execute(GestionInventario.ACTUALIZAR, valores)
                self.connection.commit()
                print(f'se ha actualizado el libro con ID: {libro.id}')
            except Exception as e:
                print(f'error details en READ: {e}')
            finally:
                cursor.close()
                self.disconnect()

    def eliminar_libro_id(self, libro):
        try:
            self.connect()
            cursor = self.connection.cursor()
            valores = (libro.id,)
            cursor.execute(GestionInventario.ELIMINAR, valores)
            self.connection.commit()
            print(f'se ha eliminado el libro con id: {libro.id}')
            return cursor.rowcount
        except Exception as e:
            print(f'error details en READ: {e}')
        finally:
            cursor.close()
            self.disconnect()



