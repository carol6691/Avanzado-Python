
class Cliente:

    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    def __str__(self):
        return(f'Datos del cliente: {self.id}, {self.nombre},'
              f' {self.apellido}, {self.membresia}')
if __name__ == '__main__':
    cliente1 = Cliente(1, 'Carmen', 'Requesens', 10)
    print(cliente1)