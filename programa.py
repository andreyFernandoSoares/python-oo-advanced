class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano

    def like(self):
        return self.__like    
    
    def dar_like(self):
        self.__like += 1
    
    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano(self):
        return self.__ano

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def __str__(self):
        return "{} - {}".format(self.__nome, self.__ano)