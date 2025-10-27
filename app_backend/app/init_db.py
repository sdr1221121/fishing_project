from app.database import Base, engine
from app.models import vessel  # garante que os modelos são importados

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
