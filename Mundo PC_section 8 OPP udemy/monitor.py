class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano
    def __str__(self):
        return (f'Detalles del monitor: ID = {self.id_monitor},'
                f' marca = {self.marca}, tamano = {self.tamano}.'
                f'Numero total de monitores = {Monitor.contador_monitores}')