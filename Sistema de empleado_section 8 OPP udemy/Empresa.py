from Empleado import Empleado
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_empleados = []

    def contratar_empleado(self, nombre, departamento):
        nuevo_empleado = Empleado(nombre,departamento)
        self.lista_empleados.append(nuevo_empleado)

    def obtener_numero_empleados_por_departamento(self, departamento):
        contador_empleados_pordepartamento = 0
        for empleado in self.lista_empleados:
            if empleado.departamento == departamento.strip():
                contador_empleados_pordepartamento += 1
                print(f"numero de empleados en depart: {departamento} es: {contador_empleados_pordepartamento}")
            else:
                print('depart no encontrado')
    def obtener_detalles_empleados(self):
        for empleado in self.lista_empleados:
            print (f'numero empleado: {empleado.numero_empleado}, '
                    f'nombre: {empleado.nombre}, depart: {empleado.departamento}')