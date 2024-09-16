from flask import Flask
import os
from models.db import db
from models.user import User
from models.anime import Anime
from controllers.UserController import UserController
from controllers import routes
    
app = Flask(__name__, template_folder='views')

UserController.init_app(app)
routes.init_app(app)

app.config["SECRET_KEY"] = "secretnotthatsecret"
app.config["PERMANENT_SESSIONLIFETIME"] = 3600

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(dir, 'models/db.sqlite3')

    
if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
        User.seed_user()
        Anime.seed_animes()
    app.run(host='localhost', port=4000, debug=True)
