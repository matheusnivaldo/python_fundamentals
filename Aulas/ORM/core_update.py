from sqlalchemy import update
from core import user_table, engine

conexao = engine.connect()

antigo_nome = input("Digite o antigo nome: ")
novo_nome = input("Digite o novo nome: ")
atualizar = update(user_table).where(user_table.c.nome == antigo_nome)
atualizar = atualizar.values(nome=novo_nome)
resultado = conexao.execute(atualizar)
print(resultado.rowcount)

