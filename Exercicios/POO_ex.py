#! /usr/bin/python3
# -*- coding:utf-8 -*-

class Carro:

    """classe que representa um carro"""

    def __init__(self):
        self.rodas = 4
        self.portas = 2
        self.motor = True
        self.vidros = 2
        self.status = "Desligado"   

    def ligar(self):
        if self.status == "Ligado" or self.rodas == None or self.portas == None or self.vidros == None:
            print("Nao e possivel ligar o carro")
        else:
            self.status = "Ligado"
            print("Carro ligado")

    def desligar(self):
        if self.status == "Ligado":
            self.status = "Desligado"
            print("Carro Desligado")
        else:
            print("Carro ja se encontra desligado")

    def frear(self):
        if self.status == "Ligado":
            print("Carro Freando")
        else:
            print("Impossivel frear, carro se encontra desligado")

    def acelerar(self):
        if self.status == "Ligado":
            print("Carro Acelerando")
        else:
            print("Impossivel acelerar, carro se encontra desligado")


montana = Carro()


montana.frear()
montana.acelerar()
montana.ligar()
montana.acelerar()
montana.frear()
montana.desligar()