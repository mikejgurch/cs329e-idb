from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DB_STRING", 'postgres://postgres:asd123@localhost:5432/bookdb')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    google_id = db.Column(db.String(), primary_key=True)
    bookNum = db.Column(db.Integer(), nullable=False)
    authorNum = db.Column(db.Integer(), nullable=False)
    author = db.Column(db.String(), nullable=True)
    publisherNum = db.Column(db.Integer(), nullable=False)
    publisher = db.Column(db.String(), nullable=True)
    title = db.Column(db.String(), nullable=True)
    subtitle = db.Column(db.String(), nullable=True)
    publication_date = db.Column(db.String(), nullable=True)
    isbn = db.Column(db.String(), nullable=True)
    image_url = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)


class Author(db.Model):
    __tablename__ = 'authors'
    title = db.Column(db.String(), nullable=True)
    bookNum = db.Column(db.Integer(), nullable=False)
    authorNum = db.Column(db.Integer(), primary_key=True)
    born = db.Column(db.String(), nullable=True)
    died = db.Column(db.String(), nullable=True)
    nationality = db.Column(db.String(), nullable=True)
    education = db.Column(db.String(), nullable=True)
    alma_mater = db.Column(db.String(), nullable=True)
    wikipedia_url = db.Column(db.String(), nullable=True)
    image_url = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)
    author = db.Column(db.String(), nullable=True)
    publisherNum = db.Column(db.Integer(), nullable=False)
    publisher = db.Column(db.String(), nullable=True)


class Publisher(db.Model):
    __tablename__ = 'publishers'
    title = db.Column(db.String(), nullable=True)
    bookNum = db.Column(db.Integer(), nullable=False)
    authorNum = db.Column(db.Integer(), nullable=False)
    author = db.Column(db.String(), nullable=True)
    publisherNum = db.Column(db.Integer(), primary_key=True)
    publisher = db.Column(db.String(), nullable=True)
    parent_company = db.Column(db.String(), nullable=True)
    owner = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    founded = db.Column(db.String(), nullable=True)
    wikipedia_url = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)
    website = db.Column(db.String(), nullable=True)
    image_url = db.Column(db.String(), nullable=True)


db.drop_all()
db.create_all()
