from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# DATABASE_URL = (
#         f"mysql://{settings.db_user}:{settings.db_password}@"
#         f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
#     )

DATABASE_URL = (
        f"mysql://{settings.db_user}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    )


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
