import random

from race import Racer, Track, RacerStep, Race

# Def que calcula a motivação (demos o nome de motivação pelo fato dos carrinhos "crescerem" na corrida) da corrida, onde os números gerados pelo random tem que estar necessariamente entre os números 0.8 e 1.2, para que as probalbilidades finais sejam as esperadas

def calculo_motivation(floor: float, ceil: float) -> float:

    diferença = ceil - floor
    rand = random.random()

    motivacao = rand * diferença + floor

    return motivacao

# print(calculo_motivation(floor = 0.8, ceil = 1.2))

# r = Racer(name='Nick Cassidy', speed= 5, motivation=(0.8, 1.2))
# # print(r.name, r.speed, r.motivation)
# rs = RacerStep(r)
# t = Track(100)

# rs.render(t)

# while not rs.finished:
#     rs.passo(calculo_motivation, t)
#     rs.render(t)

# Inserindo a variável racers em uma lista, onde pegamos a classe Racer (corredor) e suas respectivas informações, como o nome, a velocidade e a motivação.

racers = [
    Racer('Nick Cassidy', 5, (0.8, 1.4)),
    Racer('Abraham', 7, (0.5, 1)),
    Racer('Lincon', 4, (1, 1.75))
]

# Realizando a inicialização da corrida.

track = Track(100)

race = Race([RacerStep(r) for r in racers ], track, calculo_motivation)

race.start()