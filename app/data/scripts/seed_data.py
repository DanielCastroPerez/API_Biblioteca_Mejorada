from app.core.database import SessionLocal, Base, engine
from app.data.models.book_model import AuthorModel, BookModel, CategoryModel, ReviewModel

def seed():
    Base.metadata.drop_all(bind=engine)  # Limpia la BD (⚠️ borra todo)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # 📕 Libro 1: Clean Code
    autor1 = AuthorModel(nombre="Robert C. Martin", pais="Estados Unidos")
    libro1 = BookModel(titulo="Clean Code", año=2008, genero="Programación", autor=autor1)
    libro1.categorias = [
        CategoryModel(nombre="Desarrollo"),
        CategoryModel(nombre="Buenas prácticas")
    ]
    libro1.reseñas = [
        ReviewModel(usuario="Ana", comentario="Excelente libro para mejorar como programador.", calificacion=5),
        ReviewModel(usuario="Luis", comentario="Muy técnico, pero muy bueno.", calificacion=4)
    ]

    # 📗 Libro 2: El Señor de los Anillos
    autor2 = AuthorModel(nombre="J.R.R. Tolkien", pais="Reino Unido")
    libro2 = BookModel(titulo="El Señor de los Anillos", año=1954, genero="Fantasía", autor=autor2)
    libro2.categorias = [
        CategoryModel(nombre="Fantasía épica"),
        CategoryModel(nombre="Aventura")
    ]
    libro2.reseñas = [
        ReviewModel(usuario="Carlos", comentario="Un clásico que todo fan de la fantasía debe leer.", calificacion=5)
    ]

    # 📘 Libro 3: Don Quijote de la Mancha
    autor3 = AuthorModel(nombre="Miguel de Cervantes", pais="España")
    libro3 = BookModel(titulo="Don Quijote de la Mancha", año=1605, genero="Novela", autor=autor3)
    libro3.categorias = [CategoryModel(nombre="Clásico"), CategoryModel(nombre="Aventura")]
    libro3.reseñas = [
        ReviewModel(usuario="Pedro", comentario="Una obra maestra de la literatura universal.", calificacion=5)
    ]

    # 📙 Libro 4: Cien Años de Soledad
    autor4 = AuthorModel(nombre="Gabriel García Márquez", pais="Colombia")
    libro4 = BookModel(titulo="Cien Años de Soledad", año=1967, genero="Realismo mágico", autor=autor4)
    libro4.categorias = [CategoryModel(nombre="Literatura latinoamericana")]
    libro4.reseñas = [
        ReviewModel(usuario="María", comentario="Difícil al inicio pero fascinante.", calificacion=5)
    ]

    # 📕 Libro 5: La Odisea
    autor5 = AuthorModel(nombre="Homero", pais="Grecia")
    libro5 = BookModel(titulo="La Odisea", año=-800, genero="Épica", autor=autor5)
    libro5.categorias = [CategoryModel(nombre="Mitología"), CategoryModel(nombre="Aventura")]
    libro5.reseñas = [
        ReviewModel(usuario="Sofía", comentario="Un viaje épico y lleno de simbolismo.", calificacion=5)
    ]

    # 📗 Libro 6: Harry Potter y la Piedra Filosofal
    autor6 = AuthorModel(nombre="J.K. Rowling", pais="Reino Unido")
    libro6 = BookModel(titulo="Harry Potter y la Piedra Filosofal", año=1997, genero="Fantasía", autor=autor6)
    libro6.categorias = [CategoryModel(nombre="Juvenil"), CategoryModel(nombre="Fantasía mágica")]
    libro6.reseñas = [
        ReviewModel(usuario="Daniel", comentario="El inicio de una saga inolvidable.", calificacion=5),
        ReviewModel(usuario="Laura", comentario="Perfecto para jóvenes lectores.", calificacion=4)
    ]

    # 📘 Libro 7: El Principito
    autor7 = AuthorModel(nombre="Antoine de Saint-Exupéry", pais="Francia")
    libro7 = BookModel(titulo="El Principito", año=1943, genero="Fábula", autor=autor7)
    libro7.categorias = [CategoryModel(nombre="Clásico"), CategoryModel(nombre="Infantil")]
    libro7.reseñas = [
        ReviewModel(usuario="Julia", comentario="Un libro para todas las edades.", calificacion=5)
    ]

    # 📙 Libro 8: 1984
    autor8 = AuthorModel(nombre="George Orwell", pais="Reino Unido")
    libro8 = BookModel(titulo="1984", año=1949, genero="Distopía", autor=autor8)
    libro8.categorias = [CategoryModel(nombre="Política"), CategoryModel(nombre="Ficción social")]
    libro8.reseñas = [
        ReviewModel(usuario="Andrés", comentario="Una advertencia atemporal.", calificacion=5)
    ]

    # 📕 Libro 9: Crimen y Castigo
    autor9 = AuthorModel(nombre="Fiódor Dostoyevski", pais="Rusia")
    libro9 = BookModel(titulo="Crimen y Castigo", año=1866, genero="Novela psicológica", autor=autor9)
    libro9.categorias = [CategoryModel(nombre="Filosofía"), CategoryModel(nombre="Clásico ruso")]
    libro9.reseñas = [
        ReviewModel(usuario="Elena", comentario="Denso pero muy profundo.", calificacion=4)
    ]

    # Guardar todos
    db.add_all([libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9])
    db.commit()
    db.close()
    print("✅ 9 libros insertados correctamente.")

if __name__ == "__main__":
    seed()
