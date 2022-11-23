import psycopg2
try:
    conn=psycopg2.connect(host = "localhost", port = "5438", database = "postgres", user="teste", password = "123456")
    print("conexão estabelecida")
except:
    print("FALHOU CONEXAO")
if conn is not None:
    cursor=conn.cursor()

    cursor.execute("CREATE TABLE teste (id serial PRIMARY KEY, nome VARCHAR(15), sobrenome VARCHAR(15));")
    print("TABELA CRIADA")
    conn.commit()
    cursor.close()
    conn.close()

