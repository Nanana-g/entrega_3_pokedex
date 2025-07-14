from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class FavoritePokemon(Base):
    __tablename__ = "favorite_pokemon"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    pokemon_id = Column(Integer, nullable=False)
    trainer_name = Column(String(100), nullable=False)
    reason = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./database/pokemon.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()