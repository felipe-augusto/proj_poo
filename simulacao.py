# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 08:44:19 2016

@author: carlos.ssantos
"""

import minoria
import agentes
from matplotlib import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

HISTORY_LENGTH = 5
NUM_AGENTS = 41
NUM_ROUNDS = 50

jogo = minoria.Game(HISTORY_LENGTH)
for i in range(NUM_AGENTS):
    jogo.add_agent(agentes.AgenteHistorico(HISTORY_LENGTH))
for i in range(NUM_ROUNDS):
    jogo.play_round()
    # mostra a volatilidade e o preco medio
    print jogo.volatility(), jogo.mean_price()

for agent in jogo.agents:
	print agent.total_score()

pl.plot(jogo.prices)
pl.xlabel('tempo')
pl.ylabel('preco')
# pl.title('Variação de preco, agente periodico')
pl.show()

