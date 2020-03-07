# dada a lista

funcionarios = ['joao', 'maria', 'carlos', 'paula', 'mario', 'frodo']

# faça um programa que valide se o usuario é funcionario
# caso seja
# imprima acesso permitido
# caso não
# imprima acesso negado
# sendo que o funcionario frodo está bloqueado
# caso ele tente entrar será exibido um NameError com a seguinte mensagem
# Usuario bloqueado, ir direto pro RH

# print(20*'=')

# print("1. Fazer Login")
# print("2. Desbloquear Usuario")
# print("3. Bloquear Usuario")

# choice = input("Escolha a opcao desejada: ")
# print(20*'=')

while True:
    try:
        bloqueados = ['frodo']
        usuario = input("Digite seu usuario:")
        if usuario.lower() in funcionarios:
            if usuario.lower() in bloqueados:
                raise NameError('Usuario bloqueado, ir direto ao RH')
            else:
                print('Acesso permitido')
                break
        else:
                print ("Acesso Negado")
                continue
    except NameError as n:
        print(n)
        continue
