from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

print(f"Conectando ao banco de dados PostgreSQL em {DB_HOST}:{DB_PORT} como usuário {DB_USER}")
# Codifica caracteres especiais na password
DB_PASS_ENC = quote_plus(DB_PASS)

# URL de conexão PostgreSQL para Windows (TCP/IP)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS_ENC}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria engine e sessão
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
