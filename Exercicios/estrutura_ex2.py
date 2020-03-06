#!/usr/bin/python3
# -*- coding: utf-8 -*-
# dado o dicionario:

dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}

# Imprima as seguintes informações:

# 1. Nome dos estados
# print(dados['estados']['mg']['nome'])
# print(dados['estados']['rj']['nome'])
# print(dados['estados']['sp']['nome'])


# # 2. Nome dos estados, quantidade de municipios e  população
# print(f"Estado: {dados['estados']['sp']['nome']}, \nQuantidade de municipios: {dados['estados']['sp']['municipios']}, \nPopulacao: {dados['estados']['sp']['populacao']}")
# print(f"Estado: {dados['estados']['rj']['nome']}, \nQuantidade de municipios: {dados['estados']['rj']['municipios']}, \nPopulacao: {dados['estados']['rj']['populacao']}")
# print(f"Estado: {dados['estados']['mg']['nome']}, \nQuantidade de municipios: {dados['estados']['mg']['municipios']}, \nPopulacao: {dados['estados']['mg']['populacao']}")

# for i in dados['estados'].keys():
#     print(30*'=')
#     print(f"Estado: {dados['estados'][i]['nome']}, \nQuantidade de municipios: {dados['estados'][i]['municipios']}, \nPopulacao: {dados['estados'][i]['populacao']}")
#     print(' ')
#     print(30*'=')
#     print(' ')