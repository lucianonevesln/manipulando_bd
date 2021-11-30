# Importanto as ferramentas necessárias:
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Criando a conexão com o banco de dados:
engine = create_engine('sqlite:///livros.db')

# Criando exceção:
class livroNaoExiste(Exception):
    pass

# Algoritmo para consultar livro:
def consultarLivro(nomeLivro):
    with engine.connect() as con:
        consulta = text ("""SELECT * FROM livros WHERE nome = :nomeLivro""")
        rs = con.execute(consulta, nomeLivro = nomeLivro)
        livro = rs.fetchone()
        if livro == None:
            raise livroNaoExiste
        return dict(livro)

# Retornando o valor da consulta:
print(consultarLivro(input("Digite o nome do livro: ")))