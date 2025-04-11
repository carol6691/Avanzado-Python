class Snack:
    contadorsnacks = 0
    def __init__(self, nombre='', precio=0.0):
        Snack.contadorsnacks += 1
        self.id = Snack.contadorsnacks
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return (f"snack: id: {self.id}, nombre: {self.nombre},"
                f" precio: {self.precio}")
    def escribir_snack_en_archivo(self):
        return f'{self.id}, {self.nombre}, {self.precio}'

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'
    def __init__(self):
        self.lista_snacks = []
        #revisar si existe archivo sancks
        #si ya existe, obtenemos los snacks del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.lista_snacks = self.obtener_snacks()
        # si no existe, cargamos sncaks iniciales
        else:
            self.cargar_snacks_iniciales()
    def cargar_snacks_iniciales(self):
        #creamos lista snacks iniciales
        snacks_iniciales = [
            Snack('mars', 2),
            Snack ('kitkat', 3)
        ]
        #anadimos la lista de snacks iniciales a la lista de snacks
        self.lista_snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                #para cada snack, anadirlo en el archivo usando el metodo 'escribir_snack_en_archivo'
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack_en_archivo}')
        except Exception as e:
            print(f"error: {e}")
    def agregar_snacks(self, snack):
        self.lista_snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print(f'')
        for snack in self.lista_snacks:
            print(snack)

    def get_snacks(self):
        return self.lista_snacks

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    #1, 'mars', 2
                    #2, 'kitkat', 3
                    #desempaquetamos tupla
                    id_snack, nombre, precio = linea.strip().strip(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'error: {e}')
        return snacks

class MaquinaSnacks:
    def __init__(self,):
        #variable de la clase ServicioSnacks
        self.servicio_snacks = ServicioSnacks
        #lista para almacenar los productos que vendamos
        self.productos = []

    def maquina_snacks(self):
        salir = False
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                #
                salir = self.ejecutar_opciones()
            except Exception as e:
                print(f'error: {e}')
    def mostrar_menu(self):
        print(f'menu'
              f'1. comprar snack'
              f'2. mostrar ticket'
              f'3. agregar nuevo snack'
              f'4. mostrar inventario snacks'
              f'5. salir')
        return int(input("introduce una opcion(1-5): "))
    def ejecutar_opciones(self, opcion):
        if opcion == 1:
            self.comprar_snacks()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion ==3:
            self.agregar_snacks()
        elif opcion ==4:
            self. servicio_snacks. mostrar_snacks()
        elif opcion ==5:
            print("saliendo")
            return True
        else:
            print(f"error: {opcion}")
        return False

    def comprar_snacks(self):
        id_snack = int("que snack quieres comprar?(id):")
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id.snack), None)
        if snack:
            self.productos.append(snack)
            print(f"snack encontrado: {snack}")
        else:
            print("snack no encontrado")

    def mostrar_ticket(self):
        if not self.productos:
            print("no hay snacks en el ticket")
            return
        total = sum(snack.precio for snack in self.productos)
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")
        print(f"{total}")

    def agregar_snacks(self):
        nombre = input("introduce nombre del snack: ")
        precio = input("introduce precio del snack: ")
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snacks(nuevo_snack)
        print("snack agregado correctamente")

if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()