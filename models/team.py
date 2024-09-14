from .db import db
from sqlalchemy.orm import relationship

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    superhero_id = db.Column(db.Integer)    
    
    user = relationship('User', back_populates='teams')
    superhero = relationship('Superhero', back_populates='teams')

