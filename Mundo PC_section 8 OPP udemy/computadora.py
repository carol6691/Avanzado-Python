from monitor import Monitor
from raton import Raton
from teclado import Teclado

class Computadora:
    contador_computadores = 0

    def __init__(self, nombre, monitor, raton, teclado):
        Computadora.contador_computadores += 1
        self.id_computadora = Computadora.contador_computadores
        self.nombre = nombre
        self.monitor = monitor
        self.raton = raton
        self.teclado = teclado

    def __str__(self):
        return (f'Detalles del monitor: ID = {self.id_computadora},'
                f'  nombre = {self.nombre}\n'
                f'  monitor = {self.monitor}\n'
                f'  raton = {self.raton}\n'
                f'  teclado = {self.teclado}\n'
                f'Numero total de monitores = {Monitor.contador_monitores}')

#creacion de objetos
# if __name__ == '__main__':
#     teclado1 = Teclado ('hpteclado', 'usbteclado')
#     raton1 = Raton ('microsoftraton', 'usbraton')
#     monitor1 = Monitor('xiaomi', '50pulgadas')
#
#     computadora1 = Computadora('carolina', monitor1, raton1, teclado1)
#     print(computadora1)