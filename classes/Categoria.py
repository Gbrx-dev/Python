from classes.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):
    arquivo = 'db/categorias.json'

    def __init__(self, nome):
        self.arquivo = Categoria.arquivo
        self.nome = nome
