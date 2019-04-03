import json
from models import db, Book


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def parse_info(oneBook, str, detail):
    info = oneBook[str][0]
    return info[detail]


def create_dictionaries():
    book = load_json('books.json')
    authorDict = {}
    publisherDict = {}
    bookDict = {}
    bookNum = 0
    authorNum = 0
    publisherNum = 0
    for oneBook in book:
        author_entry = parse_info(oneBook, "authors", "name")
        publisher_entry = parse_info(oneBook, "publishers", "name")
        book_entry = oneBook['google_id']
        bookNum += 1
        bookDict[book_entry] = bookNum
        if (author_entry not in authorDict.keys()):
            authorNum += 1
            authorDict[author_entry] = authorNum
        if (publisher_entry not in publisherDict.keys()):
            publisherNum += 1
            publisherDict[publisher_entry] = publisherNum
    return authorDict, publisherDict, bookDict


def create_books(authorDict, publisherDict, bookDict):
    book = load_json('books.json')
    for oneBook in book:
        author = parse_info(oneBook, "authors", "name")
        authorNum = authorDict[author]
        publisher = parse_info(oneBook, "publishers", "name")
        publisherNum = publisherDict[publisher]
        title = oneBook['title']
        google_id = oneBook['google_id']
        bookNum = bookDict[google_id]

        subtitle = oneBook.get('subtitle')
        publication_date = oneBook.get('publication_date')
        isbn = oneBook.get('isbn')
        image_url = oneBook.get('image_url')
        description = oneBook.get('description')

        newBook = Book(bookNum=bookNum, authorNum=authorNum, publisherNum=publisherNum, title=title, subtitle=subtitle, author=author,
                       publisher=publisher, publication_date=publication_date, isbn=isbn, google_id=google_id, image_url=image_url, description=description)
        # After I create the book, I can then add it to my session.
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()


authorDict, publisherDict, bookDict = create_dictionaries()
create_books(authorDict, publisherDict, bookDict)
# end of create_db.py
