from series import Serie
from filmes import Filme
from playlist import Playlist

vingadores = Filme("Avengers - Inifinity War", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmp = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

playlist_fim_de_semana = Playlist("Fim de semana", [vingadores, atlanta, tmp, demolidor])

print(playlist_fim_de_semana.nome+"\n")
print("Tamanho da lista: {} \n".format(len(playlist_fim_de_semana)))

for programa in playlist_fim_de_semana:
    print(programa)

