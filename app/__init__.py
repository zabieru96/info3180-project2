from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = "fdcf3m3o(H*DNEDAIODNke*@@#NJEDed3"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin@localhost/web_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

from app import views
