from dispositivo_entrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID del raton: {self.id_raton}; marca del raton: {self.marca},'
                f' tipo de entrada: {self.tipo_entrada}'
                f'Numero total de ratones: {Raton.contador_ratones}')

#creacion de objetos
#if __name__ == '__main__':
    # raton1 = Raton('nike', 'usb')
    # raton2 = Raton('adidas', 'usb2')
    # print(raton1)