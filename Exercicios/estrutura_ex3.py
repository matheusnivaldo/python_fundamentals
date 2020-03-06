#!/usr/bin/python3
# -*- coding: utf-8 -*-

aluno = input("Digite seu nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))
media = float(n1+n2+n3+n4)/4

if media >= 7:
    print(f"Ola {aluno}, sua nota foi {media} e voce esta aprovado")
else:
    print(f"Ola {aluno}, sua nota foi {media} e voce esta reprovado")
