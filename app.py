from models.db import db
from models.superhero import Superhero
from controllers.SuperheroController import routes
from flask import Flask
import os
app = Flask(__name__, template_folder='views')
routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(dir, 'models/games.sqlite3')

    
if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=8000, debug=True)
