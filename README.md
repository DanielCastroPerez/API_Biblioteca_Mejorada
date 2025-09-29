# 📚 API Biblioteca Mejorada

Esta API fue desarrollada con **FastAPI** siguiendo principios de **Clean Architecture**, con el objetivo de gestionar una biblioteca digital. Permite realizar operaciones CRUD sobre los libros almacenados en la base de datos.

## 🚀 Características

- Obtener la lista completa de libros.
- Consultar información detallada de un libro por su ID.
- Crear nuevos registros de libros.
- Actualizar información existente.
- Eliminar libros de la base de datos.
- Arquitectura organizada en capas (entidades, casos de uso, repositorios, controladores).
- Integración con **MySQL** como motor de base de datos.
- Incluye un archivo `seed_data.py` para inicializar datos de prueba.

## 🛠️ Tecnologías utilizadas

- **Python 3.11+**
- **FastAPI** (framework principal)
- **Uvicorn** (servidor ASGI)
- **SQLAlchemy** (ORM para conexión a MySQL)
- **Pydantic** (validación de datos)
- **MySQL** (base de datos)

## 📌 Endpoints principales

- `GET /libros` → Lista todos los libros.
- `GET /libros/{id}` → Obtiene un libro por ID.
- `POST /libros` → Crea un nuevo libro.
- `PUT /libros/{id}` → Actualiza un libro existente.
- `DELETE /libros/{id}` → Elimina un libro.

## ▶️ Ejecución local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python -m uvicorn app.main:app --reload
