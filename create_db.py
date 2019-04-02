# beginning of create_db.py
import json
from models import app, db, Book

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_books():
    book = load_json('books.json')
    for oneBook in range(len(book)):
        title = book[oneBook]['title']
        g_id = book[oneBook]['google_id']

        newBook = Book(title = title, g_id = g_id)

        # After I create the book, I can then add it to my session.
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()

create_books()
# end of create_db.py
