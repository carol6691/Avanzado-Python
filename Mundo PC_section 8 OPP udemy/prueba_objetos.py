##con join en Orden
from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
##crear computadoras
teclado1 = Teclado ('hpteclado', 'usbteclado')
raton1 = Raton ('microsoftraton', 'usbraton')
monitor1 = Monitor('xiaomi', '50pulgadas')
computadora1 = Computadora('carolina', monitor1, raton1, teclado1)
teclado2 = Teclado ('hpteclado2', 'usbteclado2')
raton2 = Raton ('microsoftraton2', 'usbraton2')
monitor2 = Monitor('xiaomi2', '50pulgadas2')
computadora2 = Computadora('carolina2', monitor2, raton2, teclado2)
#crear orden
lista_computadoras1 = [computadora1, computadora2]
orden1 = Orden(lista_computadoras1)
#crear una tercera computadora
teclado3 = Teclado ('hpteclado3', 'usbteclado3')
raton3 = Raton ('microsoftraton3', 'usbraton3')
monitor3 = Monitor('xiaomi3', '50pulgadas3')
computadora3 = Computadora('carolina3', monitor3, raton3, teclado3)
orden1.agregar_computadora(computadora3)
print(orden1)
lista_computadoras2 = [computadora3]
orden2 = Orden(lista_computadoras2)
print(orden2)

#sin join
from orden_sin_join import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
#if __name__ == '__main__':
#crear computadoras
teclado1 = Teclado ('hpteclado', 'usbteclado')
raton1 = Raton ('microsoftraton', 'usbraton')
monitor1 = Monitor('xiaomi', '50pulgadas')
computadora1 = Computadora('carolina', monitor1, raton1, teclado1)
teclado2 = Teclado ('hpteclado2', 'usbteclado2')
raton2 = Raton ('microsoftraton2', 'usbraton2')
monitor2 = Monitor('xiaomi2', '50pulgadas2')
computadora2 = Computadora('carolina2', monitor2, raton2, teclado2)
#crear orden
orden1 = Orden()
orden1.agregar_computadora(computadora1)
orden1.agregar_computadora(computadora2)
#crear una tercera computadora
teclado3 = Teclado ('hpteclado3', 'usbteclado3')
raton3 = Raton ('microsoftraton3', 'usbraton3')
monitor3 = Monitor('xiaomi3', '50pulgadas3')
computadora3 = Computadora('carolina3', monitor3, raton3, teclado3)
orden1.agregar_computadora(computadora3)
orden1.__str__()
