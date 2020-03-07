#!/usr/bin/python3
# -*- coding: utf-8 -*-

n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))

if n1 > n2:
    print(f"O {n1} e maior que o {n2}")
elif n2 > n1:
    print(f"O {n2} e maior que o {n1}")
else:
    print("Os numeros sao iguais")