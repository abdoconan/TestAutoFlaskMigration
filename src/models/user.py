from src import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class User(db.Model):

    __tablename__ =  "Users"

    id: Mapped[int] =  mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    password: Mapped[str] =  mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=False)
    # mobile: Mapped[str] =  mapped_column(String(256))
    national_id: Mapped[str] = mapped_column(String(256))
    # another_column: Mapped[int] = mapped_column(Integer)
    # another_column_2: Mapped[int] = mapped_column(Integer)
    # another_column_3: Mapped[int] = mapped_column(Integer)

    # new_script_column: Mapped[int] = mapped_column(Integer)

    # new_column_main: Mapped[int] = mapped_column(Integer)


