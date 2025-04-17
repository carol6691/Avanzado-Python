from dispositivo_entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID del teclado: {self.id_teclado}; Marca del teclado: {self.marca};'
                f' Tipo de entrada del teclado: {self. tipo_entrada};'
                f'Numero total de teclados: {Teclado.contador_teclados}')

#creacion de objetos
#if __name__ == '__main__':
    # teclado1 = Teclado('hp', 'usb3')
    # print(teclado1)