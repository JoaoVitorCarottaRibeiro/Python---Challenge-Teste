# criando a classe Track, que será usada para desenhar a pista e deixar o projeto mais "vivo"

from dataclasses import dataclass

@dataclass(frozen= True)
class Track:
    comprimento: float