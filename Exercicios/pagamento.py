#!/usr/bin/python3
# -*- Coding: utf-8 -*-


vh = float(input("Valor da hora: "))
ht = float(input("Quantidade de horas trabalhadas: "))
sb = vh * ht

print(f"Salario Bruto: ({vh} * {ht}): R$ {sb}")

if (sb >= 1901 and sb <= 2800):
    ir = sb * 0.07
    sdct = sb * 0.03
    fgts = sb * 0.11 
    sl = sb - (sdct + ir)
    td = sdct + ir
    print("(-) IR (7%): R$ {0:.2f}".format(ir))
    print("(-) Sindicato (3%): R$ {0:.2f}".format(sdct))
    print("FGTS (11%): R$ {0:.2f}".format(fgts))
    print("Total de descontos: {0:.2f}".format(td))
    print("Salario Liquido: R$ {0:.2f}".format(sl))
elif (sb >= 2801 and sb <= 3700):
    ir = sb * 0.15
    sdct = sb * 0.03
    fgts = sb * 0.11 
    sl = sb - (sdct + ir)
    td = sdct + ir
    print("(-) IR (15%): R$ {0:.2f}".format(ir))
    print("(-) Sindicato (3%): R$ {0:.2f}".format(sdct))
    print("FGTS (11%): R$ {0:.2f}".format(fgts))
    print("Total de descontos: {0:.2f}".format(td))
    print("Salario Liquido: R$ {0:.2f}".format(sl))
elif (sb > 3700 and sb < 4600):
    ir = sb * 0.22
    sdct = sb * 0.03
    fgts = sb * 0.11 
    sl = sb - (sdct + ir)
    td = sdct + ir
    print("(-) IR (22%): R$ {0:.2f}".format(ir))
    print("(-) Sindicato (3%): R$ {0:.2f}".format(sdct))
    print("FGTS (11%): R$ {0:.2f}".format(fgts))
    print("Total de descontos: {0:.2f}".format(td))
    print("Salario Liquido: R$ {0:.2f}".format(sl))
elif (sb >= 4600):
    ir = sb * 0.27
    sdct = sb * 0.03
    fgts = sb * 0.11 
    sl = sb - (sdct + ir)
    td = sdct + ir
    print("(-) IR (27%): R$ {0:.2f}".format(ir))
    print("(-) Sindicato (3%): R$ {0:.2f}".format(sdct))
    print("FGTS (11%): R$ {0:.2f}".format(fgts))
    print("Total de descontos: {0:.2f}".format(td))
    print("Salario Liquido: R$ {0:.2f}".format(sl))
else:
    sdct = sb * 0.03
    fgts = sb * 0.11 
    sl = sb - sdct
    td = sdct
    print("(-) IR (Isento): R$ 0.00")
    print("(-) Sindicato (3%): R$ {0:.2f}".format(sdct))
    print("FGTS (11%): R$ {0:.2f}".format(fgts))
    print("Total de descontos: {0:.2f}".format(td))
    print("Salario Liquido: R$ {0:.2f}".format(sl))