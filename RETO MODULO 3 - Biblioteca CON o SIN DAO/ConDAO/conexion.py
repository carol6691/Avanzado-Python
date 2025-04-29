from mysql.connector import pooling
from mysql.connector import pooling

class Conexion:
    DATABASE = 'biblioteca_db'
    USERNAME = 'root'
    PASSWORD = ''
    DB_PORT = '3306'
    HOST = 'localhost' #tambien podemos poner la IP 127.0.0.1
    POOL_SIZE = 10 #creamos 10 objetos en el pool
    POOL_NAME = 'biblioteca_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            #creamos el pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    database = cls.DATABASE,
                    username = cls.USERNAME,
                    password = cls.PASSWORD,
                    port = cls.DB_PORT,
                    host = cls.HOST
                )
                return cls.pool
            except Exception as e:
                print(f'error details: {e}')
        else: # si el pool ya existe, lo ejecutamos
            return cls.pool

    @classmethod
    def crear_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def quitar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    pool1 = Conexion.obtener_pool()
    print(pool1)
    conexion1 = Conexion.crear_conexion()
    print(conexion1)
    Conexion.quitar_conexion(conexion1)
    print('la conexion se ha quitado')

