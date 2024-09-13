from flask import Flask, request, jsonify, abort, render_template
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserController():
    def init_app(app):
        @app.before_request
        def check_auth():
            routes = ["login", "register", "home"]
            if request.endpoint in routes request.path.startswith("/stastic"):
                return
            if "user_id" not in session
                return redirect(url_for("login"))
            
        @app.route("/my_heroes", methods=["GET"])
        def my_heroes():
            heroes = User.query.filter_by(username='hero_master').first()

    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            user = User.query.filter_by(username = email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.username
                render_template("home")
        return render_template("forms/login.html")

    @app.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "POST":
            email = request.form["email"]
            password=  request.form["password"]
            user = User.query.filter_by(username = email).first()
            if user:
                return redirect(url_for("login"))
            else:
                hashed_password = generate_password_hash(password, method="scrypt")
                new_user = User(username=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("login"))
        return render_template("forms/register.html")

    @app.route("/logout", methods=["POST", "GET"])
    def logout():
        session.clear()
        return redirect(url_for("home"))