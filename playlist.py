class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def listagem(self):
        return self.__programas
    
    def __len__(self):
        return len(self.__programas)
    
    def __getitem__(self, item):
        return self.__programas[item]