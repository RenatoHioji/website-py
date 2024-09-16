from flask import render_template, request, redirect, url_for, session
from datetime import date
from models.anime import Anime
from models.db import db
def init_app(app):
        @app.before_request
        def check_auth():
            if request.path == '/' or request.path.startswith("/static"):
                return
            if "user_id" not in session:
                return redirect(url_for("login"))
        @app.route("/")  
        def home(): 
            animes = Anime.query.all()
            return render_template('index.html', animes = animes)
        
        @app.route("/addAnime", methods=['GET', 'POST'])
        def addAnime():
            animes_len = Anime.query.count()
            if request.method =="POST":
                if animes_len >= 6:
                    return render_template('addAnime.html', error = "Infelizmente não será possível adicionar novos animes na lista, pois a mesma está cheia!!!")
                nome = request.form.get("nome") if request.form.get("nome") else "Não possui nome"
                ano = request.form.get("ano") if request.form.get("ano") else "Não possui ano"

                anime = Anime(nome = nome, ano = ano, imagem="images/notfound.jpg")
                db.session.add(anime)
                db.session.commit()
                return redirect(url_for("home"))
            return render_template('addAnime.html')
    
        @app.route("/removeAnime", methods=['GET', 'POST'])
        def removeAnime():
            animes = Anime.query.all()
            if request.method =="POST":
                anime_id = request.form.get("anime_id")
                anime = Anime.query.get(anime_id)
                if anime:
                    print("Deletando")
                    db.session.delete(anime)
                    db.session.commit()
                    return redirect(url_for("home"))
                return render_template("removeAnime.html", error = "Não foi encontrando nenhum com esse id")
            return render_template("removeAnime.html", animes = animes)
        
        @app.route("/updateAnime", methods=['GET', 'POST'])
        def updateAnime():
            animes = Anime.query.all()
            if request.method =="POST":
                anime_id = request.form.get("anime_id")
                
                anime = Anime.query.get(anime_id)
                nome = request.form.get("nome") 
                ano = request.form.get("ano")
                print(ano)
                if not nome:
                    nome = anime.nome
                if not ano:
                    ano = anime.ano
                    
                anime.nome = nome
                anime.ano = ano
                db.session.commit()
                return redirect(url_for("home"))
            return render_template("updateAnime.html", animes = animes)