#! /usr/bin/python3
# -*- coding: utf-8 -*-

# class Servidor():

#     def __init__(self):
#         self.cpu = None
#         self.memoria = None
#         self.disco = None
#         self.hostname = None
#     def adicionaProcessador(self, novo_proc):
#         self.cpu = novo_proc

#     def removeProcessador(self):
#         self.cpu = None
    
#     def adicionaDisco(self, hd):
#         self.disco = hd
    
#     def aumentaMemoria(self, men):
#         if self.memoria == None:
#             self.memoria = men
#         else:
#             self.memoria += men

#     def alterarHostname(self, host):
#         if self.memoria == None or self.cpu == None or self.disco == None:
#             print('Máquina não encontrada')
#         else:
#             self.hostname = host
#             print(f'Nova máquina: {host}')

# dns = Servidor()

# dns.adicionaProcessador('Intel Xeon')
# dns.aumentaMemoria(4096)
# dns.adicionaDisco('1 TB')

# dns.alterarHostname('Servidor_WEB')


# class Automovel():

#     def __init__(self, cor, pneu, marca, motor):
#         self.cor = cor
#         self.pneu = pneu
#         self.marca = marca
#         self.motor = motor
    

# carro = Automovel('prata', 4, 'Fiat 147', 'V8')



# print(carro.motor)


class Personagem():
    """Classe que representa um personagem de RPG"""
    def __init__(self):
        self.nome="teste"