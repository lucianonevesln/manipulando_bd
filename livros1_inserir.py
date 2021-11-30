# Importanto as ferramentas necessárias:
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Criando a conexão com o banco de dados:
engine = create_engine('sqlite:///livros.db')

# Algoritmo para incluir novo livro:
def inserirNovoLivro (nomeLivro, autorLivro):
    with engine.connect() as con:
        inserirLivro = "INSERT INTO livros (nome, autor) VALUES (:nomeLivro, :autorLivro)"
        con.execute(inserirLivro, nomeLivro=nomeLivro, autorLivro=autorLivro)

# Chamando função para inserir novo livro:
inserirNovoLivro(nomeLivro= input("Digite o nome do livro: "), autorLivro= input("Digite o nome do autor: "))