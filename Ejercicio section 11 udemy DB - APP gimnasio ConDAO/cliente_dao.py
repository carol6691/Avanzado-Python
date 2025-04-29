from cliente import Cliente
from conexion import Conexion
import mysql.connector

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM clientes ORDER BY id'
    INSERTAR = 'INSERT INTO clientes(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM clientes WHERE id=%s'

    @classmethod
    def listar_cliente(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #DAO no solo lee la tabla, sino que por cada registro crea un objeto
            # vamos a guardar cada registro en una lista
            # mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'error details: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def agregar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()  # guardar los cambios en la db
            print('se ha agregado a la db')
            return cursor.rowcount
        except Exception as e:
            print(f'error details: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()  # guardar los cambios en la db
            print('se ha modificado en la db')
            return cursor.rowcount
        except Exception as e:
            print(f'error details: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()  # guardar los cambios en la db
            print('se ha eliminado en la db')
            return cursor.rowcount
        except Exception as e:
            print(f'error details: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    # insertar clientes
    # nuevo_cliente = Cliente(nombre='jose', apellido='sampedro', membresia='10')
    # clientes_insertados = ClienteDAO.agregar_cliente(nuevo_cliente)
    # print(f'clientes insertados: {clientes_insertados}')
    #actualizar cliente
    # cliente_updated = Cliente(nombre='lara', apellido='dibildos', membresia='34', id=4)
    # clientes_updated = ClienteDAO.actualizar_cliente(cliente_updated)
    # print(f'clientes actualiados: {clientes_updated}')
    #eliminar cliente
    cliente_eliminado = Cliente(id=5,)
    clientes_eliminado = ClienteDAO.eliminar_cliente(cliente_eliminado)
    print(f'clientes actualiados: {clientes_eliminado}')

    # mostrar clientes
    clientes = ClienteDAO.listar_cliente()
    for cliente in clientes:
        print(cliente)




