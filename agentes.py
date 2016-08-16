# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 08:20:04 2016

@author: carlos.ssantos
"""
import minoria
import random


class AgentePeriodico(minoria.Agent):
    """Agente que joga periodicamente a mesma 
    sequencia.
    """
    def __init__(self, history_length):
        super(AgentePeriodico, self).__init__( history_length, "Periodico")
        self.sequencia = [-1, -1, 1, -1, 1]
        self.indice = 0
        
    def get_bid(self):
        ind = self.indice
        bid = self.sequencia[ind]
        self.indice = (ind + 1) % len(self.sequencia)
        ### IMPORTANTE: é preciso atualizar o valor
        ### de self.last_bid antes de retornar
        self.last_bid = bid
        return bid


class AgenteAleatorio(minoria.Agent):
    """Agente que joga aleatoriamente
    """
    def __init__(self, history_length):
        super(AgenteAleatorio, self).__init__( history_length, "Aleatorio")
        
    def get_bid(self):
        bid = random.randint(0,1) *2 -1
        self.last_bid = bid
        return bid


class AgenteHistorico(minoria.Agent):
    """Agente que utiliza do historico para tomar decisoes
    """
    def __init__(self, history_length):
        super(AgenteHistorico, self).__init__( history_length, "Historico")
        
    def get_bid(self):
        estrategias = [self.majority, self.latest_bid, self.aleatorio]
        self.last_bid = random.choice(estrategias)()
        return self.last_bid

    def majority(self):
        """ Estrategia que verifica se houve mais compras ou vendas na historia,
        se houve mais vendas o agente compra e se houve mais vendes o agente compra.
        Se o numero for igual a decisao tomada e aleatoria
        """
        tmp = 0
        for i in self.history:
            tmp += i
        if tmp > 0: # mais pessoas compraram, entao temos que vender
            bid = -1
        if tmp < 0: # mais pessoas venderam, entao temos que comprar
            bid = 1
        if tmp == 0: # igual o numero de compra e venda -> jogue aleatoriamente
            bid = random.randint(0,1) *2 -1
        return bid
    
    def latest_bid(self):
        """ Estrategia que verifica o ultimo bid da historia e faz exatamente a mesma coisa """
        if self.history[-1] == -1:
            return -1
        else:
            return 1

    def aleatorio(self):
        """ Estrategia aleatoria """
        return random.randint(0,1) *2 -1
