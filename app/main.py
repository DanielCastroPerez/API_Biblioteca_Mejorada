from fastapi import FastAPI
from app.core.database import Base, engine
from app.presentation import book_routes

# Crear tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Biblioteca API", version="1.0")

# Incluir rutas
app.include_router(book_routes.router)
