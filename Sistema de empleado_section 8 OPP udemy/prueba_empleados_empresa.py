from Empresa import Empresa
from Empleado import Empleado

def menu():
    empresa1 = Empresa('endesa')
    while True:
        try:
            print("opciones a elegir:\n"
                  "1. Contratar empleado\n"
                  "2. Consultar numero empleados por departamento\n"
                  "3. Consultar numero total de empleados\n"
                  "4. Salir")
            opcion = int(input("introduce opcion elegida: "))
            if opcion == 1:
                nombre = input("introduce nombre del empleado: ")
                departamento = input("introduce departamento del empleado: ")
                empresa1.contratar_empleado(nombre, departamento)
            elif opcion == 2:
                departamento = input("introduce departamento a consultar: ")
                empresa1.obtener_numero_empleados_por_departamento(departamento)
            elif opcion == 3:
                print(Empleado.obtener_total_empleados())
                empresa1.obtener_detalles_empleados()
            elif opcion == 4:
                print("saliendo")
                break
            else:
                print("error")
        except Exception as e:
            print(f'error: {e}')
if __name__ == "__main__":
    menu()