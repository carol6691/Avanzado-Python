from computadora import Computadora

class Orden:
    contador_ordenes = 0

    def __init__(self, lista_computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.lista_computadoras = lista_computadoras

    def __str__(self):
        #usamos una cadena str para anadir las computadoras juntas en el orden
        lista_computadoras_str = ''
        for computadora in self.lista_computadoras:
            #dos formas de unir todos los string de computadora en uno solo (mejor la segunda forma con join)
            #lista_computadoras_str += '\n' + computadora.__str__()
            lista_computadoras_str = '\n'.join(str(computadora))

        return (f'ID del orden: {self.id_orden}\n'
            f'Numero de ordenes total: {Orden.contador_ordenes}\n'
            f'Detalles de todos los ordenes:\n'
            f'Orden numero {self.id_orden}\n'
            f'Detalles: {lista_computadoras_str}')

    def agregar_computadora(self, computadora):
        self.lista_computadoras.append(computadora)
        return (f'computadora agregada numero {self.id_orden} con los siguientes detalles:\n'
                f'{computadora}')
