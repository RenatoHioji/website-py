from .db import db
from werkzeug.security import generate_password_hash
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def seed_user():
        if not User.query.first():
            user = User(username="admin",  password=generate_password_hash("admin", method="scrypt"))
            db.session.add(user)
            db.session.commit()
            print("Usuários adicionado com sucesso")
        else:
            print("Usuários já existentes")
        