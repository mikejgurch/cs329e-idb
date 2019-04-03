# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DB_STRING", 'postgres://postgres:asd123@localhost:5434/bookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # to suppress a warning message
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    google_id = db.Column(db.String(), primary_key=True)
    bookNum = db.Column(db.String(), nullable=False)
    authorNum = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=True)
    publisherNum = db.Column(db.String(), nullable=False)
    publisher = db.Column(db.String(), nullable=True)
    title = db.Column(db.String(), nullable=True)
    subtitle = db.Column(db.String(), nullable=True)
    publication_date = db.Column(db.String(), nullable=True)
    isbn = db.Column(db.String(), nullable=True)
    image_url = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)


db.drop_all()
db.create_all()
# End of models.py
