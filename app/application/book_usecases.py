from typing import List, Optional
from app.domain.entities.book_entity import BookEntity
from app.domain.repositories.book_repository import BookRepository

class BookUseCases:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_books(self) -> List[BookEntity]:
        return self.repository.get_all()

    def get_book(self, book_id: int) -> Optional[BookEntity]:
        return self.repository.get_by_id(book_id)

    def create_book(self, book: BookEntity) -> BookEntity:
        return self.repository.create(book)

    def update_book(self, book_id: int, book: BookEntity) -> Optional[BookEntity]:
        return self.repository.update(book_id, book)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete(book_id)


### revisar