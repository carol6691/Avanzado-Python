from computadora import Computadora

class Orden:
    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.lista_computadoras = []

    def __str__(self):
        for computadora in self.lista_computadoras:
            print (f'ID del orden: {self.id_orden}\n'
                f'Numero de ordenes total: {Orden.contador_ordenes}\n'
                f'Detalles de todos los ordenes:\n'
                f'Orden numero {self.id_orden}\n'
                f'Detalles: {computadora}')

    def agregar_computadora(self, computadora):
        self.lista_computadoras.append(computadora)
        return (f'computadora agregada numero {self.id_orden} con los siguientes detalles:\n'
                f'{computadora}')
