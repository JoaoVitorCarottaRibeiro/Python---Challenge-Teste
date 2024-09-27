from typing import Callable
from time import sleep

from .racer import CalcMotivation
from . import RacerStep, Track

# Criação da classe Race, que irá receber os corredores, a pista e o cálculo da motivação.
class Race:
    def __init__(self,
                 racers: list[RacerStep],
                 track: Track,
                 calculo_motivation: CalcMotivation):
        self.__racers = racers
        self.__track = track
        self.__calculo_motivation = calculo_motivation

    # def feita para dar movimento aos carrinhos e ver se algum ja terminou a corrida.

    def _running(self) -> bool:
        return any( not racer.finished for racer in self.__racers)
    
    #  Retornando a ordem com o sorted e printando a pontuação de cada corredor. Ordenando também o lambda de acordo com os steps (passos).

    def _print_score(self):
        sorted_by_steps = sorted(self.__racers, key= lambda r: r.steps)

        for position, racer in enumerate(sorted_by_steps, 1):
            print(f"{position}° colocado: {racer.name}")

    # função que começa a a corrida, renderiza também a pista no terminal, mostra a quantidade de km rodado por piloto e printa no final a pontuação.

    def start(self):
        for racer in self.__racers:
            racer.render(self.__track)

        print()    

        while self._running():
            sleep(.2) 
            for racer in self.__racers:
                distance = racer.passo(self.__calculo_motivation, self.__track)
                if distance != 0:
                    print(f'{racer.name} percorreu {distance:.2f} km na pista!')

            for racer in self.__racers:
                racer.render(self.__track)
            print()

        print()
        self._print_score()        