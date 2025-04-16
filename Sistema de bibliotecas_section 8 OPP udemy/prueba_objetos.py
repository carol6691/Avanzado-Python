from biblioteca import Biblioteca
from libro import Libro
mi_biblioteca = Biblioteca ('almassora')

#agregar libros
libro1 = Libro('la casa', 'carolina lliberos', 'terror')
libro2 = Libro('el pie', 'miguel gil', 'western')
libro3 = Libro('el raton', 'carmen req', 'amor')
libro4 = Libro('la mesa', 'aaron llib', 'historia')
libro5 = Libro('el sensor', 'lucia mont', 'drama')
libro6 = Libro('el sensor2', 'lucia mont', 'drama')
mi_biblioteca.agregar(libro1)
mi_biblioteca.agregar(libro2)
mi_biblioteca.agregar(libro3)
mi_biblioteca.agregar(libro4)
mi_biblioteca.agregar(libro5)
mi_biblioteca.agregar(libro6)

#buscar por autor
mi_biblioteca.buscar_por_autor('lucia mont')

#buscar por genero
mi_biblioteca.buscar_por_genero('drama')

#mostrar todos los libros
mi_biblioteca.mostrar_todos_libros()