#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys



# def name(nome,sobrenome):
#     print(f"Nome: {nome}\nSobrenome: {sobrenome}.")

# def ping(site):
#         print(os.system(f"ping {site}"))


#!/usr/bin/python3
# # def soma(x, y):
# #     print(x + y)

# # def subtracao(z, p):
# #     print(z - p)

# # Faça uma função que peça um nome e um sobrenome separadamente
# # e imprima Nome: <nome> Sobrenome: <Sobrenome>
# # usar essa funçao em principal

# # def nomecompleto(nome, sobrenome):
# #     return f'Nome: {nome} Sobrenome: {sobrenome}'


# # def documentos(rg, cpf):
# #     return f'RG: {rg} CPF: {cpf}'

# import sys
# import os

# print(sys.argv[0])

# # Faça um program que leia o primeiro parametro passado e faça um ping
# # deve ser um site

# os.system(f'ping {argv[1]}')

# print(os.system(f'ping {sys.argv[1]}'))





# lista = [1, 2, 3, 4]
# for i in range(len(lista)):
#     print(i)



# for i in range(len(sys.argv)):
#     if i == 0:
#         print(f'Função: {sys.argv[0]}')
#     else:
#         print(f'{i}. argumento: {sys.argv[i]}')

import datetime

# print(datetime.timedelta(7))

# print(datetime.time(14,0,0))

var = datetime.datetime(2020, 1, 9)
var_fmt = var.strftime('%d/%m/%Y')


print(var_fmt)  