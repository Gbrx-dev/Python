import json
import os
from abc import ABC

class AbstractCrud(ABC):
    def detalhar(self):
        data = self.__dict__.copy()
        if "arquivo" in data:
            del data["arquivo"]
        return data

    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        self.__gravarArquivo(lista)

    def alterar(self, item): 
        lista = self.consultar()
        lista[item] = self.detalhar()
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        self.__gravarArquivo(lista)

    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file: 
            json.dump(lista, file, indent=4)
        print('Operação realizada com sucesso')

    @classmethod
    def excluir(cls, item):
        lista = cls.consultar()
        del lista[item] 
         
        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
        print('Operação realizada com sucesso')


    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()
        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    @classmethod
    def consultar(cls, item=None):
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file)
                if item is not None:
                    return lista[item]
                return lista
        except Exception:
            return []
