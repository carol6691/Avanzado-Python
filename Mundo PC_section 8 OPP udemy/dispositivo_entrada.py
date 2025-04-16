class Dispositivo_Entrada:
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

class Raton():
    contador_ratones = []
    def __init__(self):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
    def __str__(self):
        return (f'ID del raton: {self.id_raton}\n'
                f'Numero de ratones: {Raton.contador_ratones}')

class Teclado():
    contador_teclados = []
    def __init__(self):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
    def __str__(self):
        return (f'ID del teclado: {self.id_teclado}\n'
                f'Numero de teclados: {Teclado.contador_teclados}')
