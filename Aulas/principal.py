#! /usr/bin/python3
# -*- coding: utf-8 -*-
import operacoes
import os
import sys
# import datetime

# print("Codigo Principal")

# nome = input(str("Digite seu nome: "))
# sobrenome = input(str("Digite seu sobrenome: "))

# operacoes.name(nome,sobrenome)

# datetime

# print("Codigo Principal")

# site = input(str("Digite um site: "))
# operacoes.ping(site)

print(os.system(f"ping {sys.argv[1]}"))