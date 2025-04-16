from monitor import Monitor
from dispositivo_entrada import Raton, Teclado

class Computadora:
    contador_computadores = 0
    def __init__(self, nombre):
        Computadora.contador_computadores += 1
        self.id_computadora = Computadora.contador_computadores
        self.nombre = nombre
        self.monitor = Monitor(marca, tamano)
        self.raton = Raton ()
        self.teclado = Teclado()
    def __str__(self):
        return (f'Detalles del monitor: ID = {self.id_computadora},'
                f'nombre = {self.nombre},\n'
                f'monitor = {self.monitor},\n'
                f'raton = {self.raton},\n'
                f'teclado = {self.teclado},\n'
                f'\n'
                f'Numero total de monitores = {Monitor.contador_monitores}')