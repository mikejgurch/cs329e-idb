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
        google_id = book[oneBook]['google_id']
        title = book[oneBook]['title']
        image_url = book[oneBook]['image_url']

        try:
            publication_date = book[oneBook]['publication_date']
        except KeyError:
            publication_date = 'NULL'

        try:
            subtitle = book[oneBook]['subtitle']
        except KeyError:
            subtitle = 'NULL'

        try:
            isbn = book[oneBook]['isbn']
        except KeyError:
            isbn = 'NULL'

        try:
            description = book[oneBook]['description']
        except KeyError:
            description = 'NULL'

        for oneAuthor in book[oneBook]['authors']:
            author = oneAuthor['name']

        for onePublisher in book[oneBook]['publishers']:
            publisher = onePublisher['name']

        newBook = Book(google_id=google_id, title=title, subtitle=subtitle, author=author, publisher=publisher, isbn=isbn,
                       publication_date=publication_date, description=description,
                       image_url=image_url)


create_books()
# end of create_db.py
