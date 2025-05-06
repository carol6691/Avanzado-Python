#segunda version modificando el bucle while

from cliente import Cliente
from cliente_dao import ClienteDAO

opcion = None
while opcion !=5:
    print('''*** App Zon Fit ***
    Opciones:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar datos de cliente
    4. Eliminar cliente
    5. Salir
    ''')
    opcion = int(input('Introduce una opcion (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.listar_cliente()
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre = str(input('Introduce nombre: '))
        apellido = str(input('Introduce apellido: '))
        membresia = int(input('Introduce membresia: '))
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_insertados = ClienteDAO.agregar_cliente(nuevo_cliente)
        print(f'clientes insertados: {clientes_insertados}')
    elif opcion == 3:
        nombre = str(input('Introduce nombre: '))
        apellido = str(input('Introduce apellido: '))
        membresia = int(input('Introduce membresia: '))
        id = int(input('Introduce id: '))
        cliente_updated = Cliente(id=id, nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_updated = ClienteDAO.actualizar_cliente(cliente_updated)
        print(f'clientes actualizados: {clientes_updated}')
    elif opcion == 4:
        id = int(input('Introduce id: '))
        cliente_eliminado = Cliente(id=id)
        clientes_eliminado = ClienteDAO.eliminar_cliente(cliente_eliminado)
        print(f'clientes eliminados: {clientes_eliminado}')
else:
    print('Saliendo...')
