from typing import List, Optional
from pydantic import BaseModel

class AuthorEntity(BaseModel):
    id: Optional[int]
    nombre: str
    pais: str

class ReviewEntity(BaseModel):
    id: Optional[int]
    usuario: str
    comentario: str
    calificacion: int

class CategoryEntity(BaseModel):
    id: Optional[int]
    nombre: str

class BookEntity(BaseModel):
    id: Optional[int]
    titulo: str
    año: int
    genero: str
    autor: AuthorEntity
    categorias: List[CategoryEntity] = []
    reseñas: List[ReviewEntity] = []
