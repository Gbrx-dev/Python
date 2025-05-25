from classes.Produto import Produto
from classes.Categoria import Categoria

if __name__ == "__main__":
    Produto.listarTodos()

    produto = Produto('001', 'Mouse', 200, 65)
    produto.inserir()
    Produto.listarTodos()

    categoria = Categoria('Roupas')
    categoria.inserir()
