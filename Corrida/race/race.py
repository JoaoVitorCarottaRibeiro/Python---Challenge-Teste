from typing import Callable
from time import sleep

from .racer import CalcMotivation
from . import RacerStep, Track


class Race:
    def __init__(self,
                 racers: list[RacerStep],
                 track: Track,
                 calculo_motivation: CalcMotivation):
        self.__racers = racers
        self.__track = track
        self.__calculo_motivation = calculo_motivation

    def _running(self) -> bool:
        return any( not racer.finished for racer in self.__racers)
    
    # Ordenando com o lambda de acordo com os steps (passos)

    def _print_score(self):
        sorted_by_steps = sorted(self.__racers, key= lambda r: r.steps)

        for position, racer in enumerate(sorted_by_steps, 1):
            print(f"{position}° colocado: {racer.name}")

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