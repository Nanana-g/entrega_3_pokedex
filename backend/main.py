from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import requests

from modelo import create_tables, get_db, FavoritePokemon
from esquema import FavoritePokemonCreate, FavoritePokemon

app = FastAPI()

# Permitir CORS para el frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas al iniciar
create_tables()

# Endpoint para obtener pokémon de la PokeAPI (API externa)
@app.get("/api/pokemon/")
def get_pokemon_list(limit: int = 20, offset: int = 0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al obtener datos de PokeAPI")
    return response.json()

# Endpoint para obtener detalles de un pokémon específico
@app.get("/api/pokemon/{pokemon_name}")
def get_pokemon_detail(pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    return response.json()

# Endpoint para listar favoritos (API propia)
@app.get("/api/favorites/", response_model=list[FavoritePokemon])
def list_favorites(db: Session = Depends(get_db)):
    return db.query(FavoritePokemon).all()

# Endpoint para crear un favorito (API propia)
@app.post("/api/favorites/", response_model=FavoritePokemon)
def create_favorite(fav: FavoritePokemonCreate, db: Session = Depends(get_db)):
    db_fav = FavoritePokemon(**fav.dict())
    db.add(db_fav)
    db.commit()
    db.refresh(db_fav)
    return db_fav