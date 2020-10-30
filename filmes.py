from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao
    
    @property
    def duracao(self):
        return self.__duracao
    
    def __str__(self):
        return "{} - {} : {}".format(self.nome, self.ano, self.__duracao)