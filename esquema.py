from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FavoritePokemonBase(BaseModel):
    name: str
    pokemon_id: int
    trainer_name: str
    reason: Optional[str] = None
    image_url: Optional[str] = None

class FavoritePokemonCreate(FavoritePokemonBase):
    pass

class FavoritePokemon(FavoritePokemonBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class PokemonExternal(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    base_experience: int
    sprites: dict
    types: list
    abilities: list