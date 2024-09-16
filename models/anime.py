from .db import db
from werkzeug.security import generate_password_hash
class Anime(db.Model):
    __tablename__ = 'anime'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=True, nullable=False)
    ano = db.Column(db.String(255), nullable=True)
    imagem = db.Column(db.String(255), nullable=True)
    
    def __init__(self, nome, ano, imagem=None):
        self.nome = nome
        self.ano = ano
        self.imagem = imagem or ""

    def seed_animes():
        if not Anime.query.first():
            default_animes = [
                Anime(nome="Naruto", ano="2007", imagem="images/naruto.jpg"),
                Anime(nome="World End", ano="2017", imagem="images/worldend.jpg"),
                Anime(nome="Kaiju Nº 8", ano="2024", imagem="images/kaiju.jpg"),
                Anime(nome="Pokémon 2000 - Filme", ano="2024", imagem="images/kaiju.jpg"),
                Anime(nome="Kokoro Connect", ano="2012", imagem="images/kokoroconnect.jpg")
            ]
            db.session.bulk_save_objects(default_animes)
            db.session.commit()
            print("Animes adicionado com sucesso")
        else:
            print("Animes já existentes")


