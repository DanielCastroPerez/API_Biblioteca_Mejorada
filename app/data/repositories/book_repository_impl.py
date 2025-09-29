from sqlalchemy.orm import Session
from typing import List, Optional
from app.domain.repositories.book_repository import BookRepository
from app.domain.entities.book_entity import BookEntity, AuthorEntity, ReviewEntity, CategoryEntity
from app.data.models.book_model import BookModel, AuthorModel, ReviewModel, CategoryModel

class BookRepositoryImpl(BookRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[BookEntity]:
        books = self.db.query(BookModel).all()
        return [self._map_to_entity(book) for book in books]

    def get_by_id(self, book_id: int) -> Optional[BookEntity]:
        book = self.db.query(BookModel).filter(BookModel.id == book_id).first()
        return self._map_to_entity(book) if book else None

    def create(self, book: BookEntity) -> BookEntity:
        # Crear autor si no existe
        autor = AuthorModel(nombre=book.autor.nombre, pais=book.autor.pais)
        self.db.add(autor)
        self.db.flush()  # para obtener el id

        # Crear libro
        book_model = BookModel(
            titulo=book.titulo,
            año=book.año,
            genero=book.genero,
            autor_id=autor.id
        )
        self.db.add(book_model)
        self.db.flush()

        # Agregar categorías
        for cat in book.categorias:
            category_model = CategoryModel(nombre=cat.nombre, libro_id=book_model.id)
            self.db.add(category_model)

        # Agregar reseñas
        for rev in book.reseñas:
            review_model = ReviewModel(
                usuario=rev.usuario,
                comentario=rev.comentario,
                calificacion=rev.calificacion,
                libro_id=book_model.id
            )
            self.db.add(review_model)

        self.db.commit()
        self.db.refresh(book_model)

        return self._map_to_entity(book_model)

    def update(self, book_id: int, book: BookEntity) -> Optional[BookEntity]:
        book_model = self.db.query(BookModel).filter(BookModel.id == book_id).first()
        if not book_model:
            return None

        book_model.titulo = book.titulo
        book_model.año = book.año
        book_model.genero = book.genero
        self.db.commit()
        self.db.refresh(book_model)
        return self._map_to_entity(book_model)

    def delete(self, book_id: int) -> bool:
        book = self.db.query(BookModel).filter(BookModel.id == book_id).first()
        if not book:
            return False
        self.db.delete(book)
        self.db.commit()
        return True

    def _map_to_entity(self, book_model: BookModel) -> BookEntity:
        return BookEntity(
            id=book_model.id,
            titulo=book_model.titulo,
            año=book_model.año,
            genero=book_model.genero,
            autor=AuthorEntity(
                id=book_model.autor.id,
                nombre=book_model.autor.nombre,
                pais=book_model.autor.pais
            ),
            categorias=[CategoryEntity(id=c.id, nombre=c.nombre) for c in book_model.categorias],
            reseñas=[
                ReviewEntity(
                    id=r.id,
                    usuario=r.usuario,
                    comentario=r.comentario,
                    calificacion=r.calificacion
                )
                for r in book_model.reseñas
            ]
        )
