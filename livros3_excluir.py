# Importanto as ferramentas necessárias:
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Criando a conexão com o banco de dados:
engine = create_engine('sqlite:///livros.db')

# Algoritmo para excluir livro:
def excluirLivro(nomeLivro):
    with engine.connect() as con:
        delete = "DELETE FROM livros WHERE nome = :nomeLivro"
        con.execute(delete, nomeLivro = nomeLivro)

# Chamando função para excluir o livro:
excluirLivro(input("Digite o nome do livro que será excluído: "))