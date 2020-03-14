import psycopg2


try:
    conexao = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

    cursor = conexao.cursor()

    cursor.execute("insert into scripts(nome,conteudo) values('devops','projeto de python')")
    conexao.commit()
    print("Registro criado com sucesso")
    
except Exception as e:
    print("Erro: {}".format(e))    
    print("Fazendo rollback")    
    conexao.rollback()
finally:    
    print("Finalizando conexao com o banco de dados")    
    cursor.close()
    conexao.close()
    