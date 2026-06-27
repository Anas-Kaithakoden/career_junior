from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = (
    "postgresql+psycopg://postgres:password@localhost:5432/blog_db"
)

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine)


# DATABASE_URL: Tells SQLAlchemy where the database is.
# create_engine(...): Creates an Engine that manages connections.
# Base: Registers ORM models. It tells SQLAlchemy which classes represent tables
# sessionmaker(...): A factory that creates Session objects when you need them. Tracks Python objects and coordinates work with the database.

"""Create Python object
        ↓
Tell Session about it
        ↓
Session tracks changes
        ↓
commit()
        ↓
SQLAlchemy generates SQL
        ↓
Engine gets a connection
        ↓
psycopg sends SQL
        ↓
PostgreSQL executes SQl """