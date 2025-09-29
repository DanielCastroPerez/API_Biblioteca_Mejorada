from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    pais = Column(String(100), nullable=False)

    libros = relationship("BookModel", back_populates="autor")


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    año = Column(Integer, nullable=False)
    genero = Column(String(100), nullable=False)

    autor_id = Column(Integer, ForeignKey("authors.id"))
    autor = relationship("AuthorModel", back_populates="libros")

    categorias = relationship("CategoryModel", back_populates="libro")
    reseñas = relationship("ReviewModel", back_populates="libro")


class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    libro_id = Column(Integer, ForeignKey("books.id"))
    libro = relationship("BookModel", back_populates="categorias")


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(100), nullable=False)
    comentario = Column(String(300), nullable=False)
    calificacion = Column(Integer, nullable=False)

    libro_id = Column(Integer, ForeignKey("books.id"))
    libro = relationship("BookModel", back_populates="reseñas")
