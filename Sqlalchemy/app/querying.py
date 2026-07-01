
from sqlalchemy import String, Text, ForeignKey, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(200), nullable=False)

    content: Mapped[str] = mapped_column(Text)

    email: Mapped[str] = mapped_column(
    String(255),
    unique=True
    )

    published: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )


# And and Or 
stmt = (
    select(User)
    .where(
        User.name == "Anas",
        User.email == "anas@gmail.com"
    )
)

from sqlalchemy import or_

stmt = (
    select(User)
    .where(
        or_(
            User.name == "Anas",
            User.name == "Ali"
        )
    )
)

# Order By
stmt = (
    select(Post)
    .where(Post.published == True)
    .order_by(Post.id.desc())
)

# Limit and Offset
stmt = (
    select(Post)
    .limit(10)
    .offset(20)
)

# inner Join, left join

stmt = (
    select(User.name, Post.title)
    .join(Post)
)

            # results = session.execute(stmt).all()

stmt = (
    select(User.name, Post.title)
    .outerjoin(Post)
)

# Aggregation

from sqlalchemy import func

stmt = select(func.count(Post.id))

            # count = session.scalar(stmt)

# GROUP BY

stmt = (
    select(
        User.name,
        func.count(Post.id)
    )
    .join(Post)
    .group_by(User.name)
)

            # results = session.execute(stmt).all()


# HAVING

stmt = (
    select(
        User.name,
        func.count(Post.id)
    )
    .join(Post)
    .group_by(User.name)
    .having(func.count(Post.id) > 5)
)