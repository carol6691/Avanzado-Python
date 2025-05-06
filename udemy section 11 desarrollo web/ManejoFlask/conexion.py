from mysql.connector import pooling
from mysql.connector import pooling


class Conexion:
    DATABASE = 'zona'
    USERNAME = 'root'
    PASSWORD = ''
    DB_PORT = '3306'
    HOST = 'localhost' #podemos poner la IP 127.0.0.1
    POOL_SIZE = 5 #creamos 5 objetos en el pool
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #si el pool no existe, se crea
            try:
                cls.pool = pooling.MySQLConnectionPool( 
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Exception as e:
                print(f'error details: {e}')
        else:
            return cls.pool #si ya existe, se ejecuta

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = Conexion.obtener_conexion()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print('se ha liberado conexion1')




        # cursopython_db = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password='admin',
        #     database='cursopython_db'
        # )
        # cursor = cursopython_db.cursor()