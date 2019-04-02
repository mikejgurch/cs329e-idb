# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5434/bookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'

    title = db.Column(db.String(80), nullable = False)
    google_id = db.Column(db.String(80), primary_key = True)
    isbn = db.Column(db.String(80), nullable = True)
    subtitle = db.Column(db.String(80), nullable = True)
    description = db.Column(db.String(4000), nullable = True)
    image_url = db.Column(db.String(80), nullable = True)
    publication_date = db.Column(db.String(80), nullable=True)
    publisher = db.Column(db.PickleType())
    author = db.Column(db.PickleType())

db.drop_all()
db.create_all()
# End of models.py 

