from sqlalchemy import String, Text, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

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




# *Let's compare that to SQL.

# CREATE TABLE posts (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(200) NOT NULL,
#     content TEXT,
#     published BOOLEAN DEFAULT FALSE,
#     user_id INTEGER NOT NULL REFERENCES users(id)
# );



# *Exercises
# 1:
# CREATE TABLE comments (
#     id SERIAL PRIMARY KEY,
#     message TEXT NOT NULL,
#     user_id INTEGER REFERENCES users(id),
#     post_id INTEGER REFERENCES posts(id)
# );
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    message:Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
