from src import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class User(db.Model):

    __tablename__ =  "Users"

    id: Mapped[int] =  mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    password: Mapped[str] =  mapped_column(String(256), nullable=False)


