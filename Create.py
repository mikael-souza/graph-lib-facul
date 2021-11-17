import sqlite3 as conector

conexao = conector.connect("dev-base.db")

cursor = conexao.cursor()

# sql_query = '''SELECT nome, matricula FROM Aluno'''


sql_query = '''CREATE TABLE pessoa(
                                cpf INTEGER NOT NULL,
                                nome TEXT NOT NULL,
                                nascimento DATE NOT NULL,
                                oculos BOOLEAN NOT NULL,
                                PRIMARY KEY (cpf)
                                );'''



cursor.execute(sql_query)

alunos = cursor.fetchall()

for nome, matricula in alunos:
    print(nome, matricula)