#! /usr/bin/python3
# -*- Coding: utf-8 -*-

# Erros e excecoes

while True:
    try:
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Digite o segundo numero: "))
        print(f"Resultado: {x/y}")
        break
    except TypeError as e:
        print(e)
        print("Digite apenas numeros!")
        continue
    except ZeroDivisionError as z:
        print(z)
        print("Numero divido por!")
        continue
    
