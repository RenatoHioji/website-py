from flask_sqlalchemy import SQLAlchemy
from .db import db


class Superhero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    moral = db.Column(db.String(100), nullable=True)
    history = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Superhero {self.name}>'