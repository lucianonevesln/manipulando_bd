# Importanto as ferramentas necessárias:
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Criando a conexão com o banco de dados:
engine = create_engine('sqlite:///livros.db')

# Criando tabela:
with engine.connect() as con:
    create_sql = """
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMERY KEY,
        nome TEXT NOT NULL,
        autor TEXT NOT NULL
    )
    """
    rs = con.execute(create_sql)