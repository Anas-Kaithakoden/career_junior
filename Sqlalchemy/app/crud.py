from sqlalchemy import create_engine, String,  Text, ForeignKey, Boolean, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, relationship

DATABASE_URL = (
    "postgresql+psycopg://postgres:password@localhost:5432/blog_db"
)

engine = create_engine(DATABASE_URL)



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)

Base.metadata.create_all(engine)


SessionLocal = sessionmaker(bind=engine)


with SessionLocal() as session:

    # CREATE
    user = User(name="Anas", email="anas@gmail.com")
    session.add(user)
    session.commit()

    # READ
    stmt = select(User)
    users = session.scalars(stmt).all()

    # UPDATE
    user.name = "Anas KK"
    session.commit()

    # DELETE
    session.delete(user)
    session.commit()



# *Exercise
# 1:
with SessionLocal() as session:
    user = User(name="Ali", email="ali@gmail.com")
    session.add(user)
    session.commit()

    stmt = select(User)
    users = session.scalars(stmt).all()

    stmt = select(User).where(User.id==1)
    user = session.scalar(stmt)
    user.name = "Ahmed"
    session.commit()

    stmt = select(User).where(User.id==5)
    user = session.scalar(stmt)
    session.delete(user)
    session.commit()