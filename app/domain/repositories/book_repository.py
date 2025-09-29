from typing import List, Optional
from app.domain.entities.book_entity import BookEntity

class BookRepository:
    def get_all(self) -> List[BookEntity]:
        raise NotImplementedError

    def get_by_id(self, book_id: int) -> Optional[BookEntity]:
        raise NotImplementedError

    def create(self, book: BookEntity) -> BookEntity:
        raise NotImplementedError

    def update(self, book_id: int, book: BookEntity) -> Optional[BookEntity]:
        raise NotImplementedError

    def delete(self, book_id: int) -> bool:
        raise NotImplementedError
### revisar