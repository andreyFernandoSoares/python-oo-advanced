from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas
    
    @property
    def temporadas(self):
        return self.__temporadas
    
    def __str__(self):
        return "{} - {} : {}".format(self.nome, self.ano, self.__temporadas)
