Título do Projeto:
Sistema de Apostas com Simulação de Corrida

Introdução:
Este projeto consiste em um sistema de apostas no qual os usuários podem apostar em uma corrida simulada. O sistema utiliza scripts em Python para simular o comportamento dos competidores (carros) em uma pista. As corridas são geradas com base em parâmetros como velocidade e motivação de cada corredor, e os resultados determinam os ganhos ou perdas dos apostadores.

Objetivos:
Permitir que os usuários façam apostas em corridas simuladas.
Simular corridas com base em parâmetros como velocidade e motivação dos corredores.
Oferecer probabilidades e odds ajustadas com base nas características dos competidores.
Mostrar o resultado da corrida e calcular as apostas vencedoras.
Componentes do Sistema:
Racers: Competidores na corrida, cada um com um nome, velocidade e um intervalo de motivação.
Track: Pista de corrida, definida pelo comprimento da pista.
Race: Gerencia a corrida, controlando os corredores e o progresso da corrida na pista.
Sistema de Apostas: Funções que calculam odds, registram apostas, e ajustam os saldos de acordo com os resultados.
Fluxo de Operação:
Entrada de Apostas: O usuário escolhe em qual corredor deseja apostar e insere o valor da aposta.
Simulação da Corrida: A corrida é simulada com base na velocidade e motivação de cada corredor. A motivação é calculada aleatoriamente em um intervalo predefinido.
Cálculo de Odds e Resultados: O sistema calcula as odds com base nas probabilidades ajustadas e mostra o vencedor.
Pagamento: O saldo do usuário é atualizado de acordo com o resultado da aposta.

----------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de Blocos Básico: Sistema de Apostas de Corrida

- Entrada do Usuário

O usuário insere:
Injetar dinheiro para aposta
Corredor escolhido
Valor da aposta
Validação da Aposta

O sistema verifica se o usuário tem saldo suficiente para realizar a aposta.
Se o saldo for insuficiente, exibe uma mensagem de erro.
Se o saldo for suficiente, a aposta é registrada.

- Simulação da Corrida

Ao entrar no arquivo, vá ao terminal e digite "python corrida.py" para iniciar a corrida.

A corrida é iniciada com os seguintes componentes:
Racers: Corredores com suas respectivas velocidades e níveis de motivação.
Track: Pista de corrida com um comprimento definido.
Cálculo de Motivação: A motivação de cada corredor é calculada aleatoriamente dentro de um intervalo predefinido.
O sistema atualiza as posições dos corredores ao longo da pista até que todos tenham completado o percurso.

- Determinação do Resultado

O sistema verifica qual corredor chegou primeiro.
Exibe o resultado da corrida (ordem de chegada dos corredores).

- Cálculo de Ganhos/Perdas

Se o corredor apostado for o vencedor:
O sistema calcula o valor ganho com base na odd do corredor.
Atualiza o saldo do usuário com o valor ganho.
Se o corredor apostado não for o vencedor:
O sistema subtrai o valor apostado do saldo do usuário.

- Exibição do Saldo

O sistema exibe o saldo atualizado do usuário.

- Encerramento da Sessão

O usuário pode escolher entre:
Fazer uma nova aposta
Verificar o saldo
Sacar seus ganhos ou valores em sua conta

- Encerrar o sistema

Arthur Bueno de Oliveira - RM558396
--------------------------------------
Diego Eleuterio Fadul da Costa - RM557218
--------------------------------------------
João Vitor Carotta Ribeiro - RM555187
--------------------------------------
Victor Magdaleno Marcos - RM556729
------------------------------------
