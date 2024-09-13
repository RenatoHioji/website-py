from models.db import db
from models.superhero import Superhero
from controllers.SuperheroController import SuperheroController
from controllers.UserController import UserController
from flask import Flask
import os


app = Flask(__name__, template_folder='views')
SuperheroController.init_app(app)
UserController.init_app(app)
app.config["SECRET_KEY"] = "secretnotthatsecret"
app.config["PERMANENT_SESSIONLIFETIME"] = 3600

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(dir, 'models/db.sqlite3')

    
if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=8000, debug=True)
