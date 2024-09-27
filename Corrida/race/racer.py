from dataclasses import dataclass
from typing import Callable
from .track import Track

CalcMotivation = Callable[[float, float], float]

# Decorator usado para dar funcionalidades especiais as funções. Usamos ela de maneira congelada para que não fosse modificada nenhuma alteração.

@dataclass(frozen= True)
class Racer:
    name: str
    speed: float
    motivation: tuple[float, float]

    def initial(self):
        return f"{self.name[0]}"

# ----------------------------------------------------- #

# Definindo a classe RacerStep para pegar o nome do corredor, sua posição, se ele terminou ou não a corrida e o número de steps.

class RacerStep:
    def __init__(self, racer: Racer):
        self.__racer = racer
        self.__position = 0
        self.__finished = False
        self.__steps = 0

    # Calculando o intervaldo da motivação e verificação de posição com base no comprimento da corrida

    def passo(self, calculo_motivation: CalcMotivation, track: Track) -> float:
        if self.__finished:
            return 0.0   # 0.0 é o retorno da distancia

        floor, ceil = self.__racer.motivation
        motivation = calculo_motivation(floor, ceil)
        distance = self.__racer.speed * motivation

        self.__position += distance
        self.__steps += 1

        if self.__position >= track.comprimento:
            self.__position = track.comprimento
            self.__finished = True

        return distance

    # Função para desenhar a pista no terminal por meio de "-" mutiplicando a quantidade de vezes que queremos. Depois, pegamos a posição e dividimos pelo comprimento da pista.

    def render(self, track: Track):
        to_render = ['-'] * 100
        distance = self.__position / track.comprimento
        index = int(distance * 100) - 1

        if index < 0:
            index = 0

        to_render[index] = self.__racer.initial()
        print(''.join(to_render))

    # Tornando o membro finished privado com o __ antes

    # Usando o @property (built-in decorator) para dar funções especiais a estes self´s.

    @property
    def finished(self):
        return self.__finished
    
    @property
    def steps(self):
        return self.__steps

    @property
    def name(self):
        return self.__racer.name