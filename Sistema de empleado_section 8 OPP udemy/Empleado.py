class Empleado:
    contador = 0
    def __init__(self, nombre, departamento):
        Empleado.contador += 1
        self.numero_empleado = Empleado.contador
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
            return (f'numero empleado: {self.numero_empleado}, '
                    f'nombre: {self.nombre}, depart: {self.departamento}')

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador