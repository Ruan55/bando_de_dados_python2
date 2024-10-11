from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class User(Base):
    # Definindo características da tabela
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    email = Column(String(250), unique=True)
    password = Column(String(250))

    # Definindo atributos da classe 
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

# Criando tabelas no banco de dados.
Base.metadata.create_all(bind=db)