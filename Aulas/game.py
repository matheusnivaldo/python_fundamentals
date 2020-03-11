#! /usr/bin/python3
# -*- coding:utf-8 -*-

from random import randint

class Personagem():
    """classe que representa um personagem de um jogo de RPG"""
    def __init__(self, nome, xp=0, nivel=1):
        """Inicializando as propriedades de um personagem"""
        self.nome = nome
        self.hp = 100
        self.mp = 100
        self.xp = xp
        self.nivel = nivel
    
    def subirNivel(self):
        if self.xp > 99:
            self.nivel += 1
            self.xp = 0
            self.hp = 100
            self.hp = (self.hp * (0.10 * self.nivel))
            print('Você subiu de nível!')

    def mataMostro(self, hp_monstro=100):
        self.poderMonstro = randint(1,100)
        if self.poderMonstro > 50:
            self.hp -= 20
            print(f"Poder do monstro: {self.poderMonstro}")
            print(f'Você tomou dano! \n{self.nome}:{self.hp}')
        else:
            self.hp_monstro = hp_monstro - 40
            print(f"Poder do monstro: {self.poderMonstro}")
            print(f'Você deu um dano! \n{self.nome}:{self.hp}')
            print(f'Monstro: {self.hp_monstro}')
            if self.hp_monstro <= 0:
                self.xp += 10
                self.hp_monstro = 100
                subirNivel()

class Mago(Personagem):

    def ataque(self):
        print("Ataque do THOR")
        p2 = Mago("Thora")
        p2.mataMostro()

p2 = Mago("Thora")
p2.ataque()
