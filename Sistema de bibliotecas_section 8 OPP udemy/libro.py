class Libro():
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    def get_titulo(self):
        return self._titulo
    def set_titulo(self, titulo):
        self._titulo = titulo
    @property
    def autor(self):
        return self._autor
    # def get_autor(self):
    #     return self._autor
    def set_autor(self, autor):
        self._autor = autor
    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero = genero
