from sqlalchemy import delete
from core import user_table, engine

nome = input("Digite seu nome: ")

conexao=engine.connect()
d = delete(user_table).where(user_table.c.nome==nome)
resultado = conexao.execute(d)
print(f"Quantidade de linhas afetadas: {resultado.rowcount}")
