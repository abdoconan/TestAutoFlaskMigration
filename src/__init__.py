from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


class Base(DeclarativeBase):
    pass


db =  SQLAlchemy(model_class=Base)

def create_app() -> Flask:
    app =  Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:P%40ssw0rd@localhost:5432/TestMigration'

    print("another changes")

    db.init_app(app)
    migration = Migrate(app, db)

    return app