import json
from models import db, Book, Author, Publisher


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def get_info(oneBook, str, detail):
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
        bookItem = oneBook['google_id']
        bookNum += 1
        bookDict[bookItem] = bookNum
        for oneAuthor in oneBook["authors"]:
            authorItem = oneAuthor["name"]
            if (authorItem not in authorDict.keys()):
                authorNum += 1
                authorDict[authorItem] = authorNum

        for onePublisher in oneBook["publishers"]:
            publisherItem = onePublisher["name"]
            if (publisherItem not in publisherDict.keys()):
                publisherNum += 1
                publisherDict[publisherItem] = publisherNum
    return authorDict, publisherDict, bookDict


def create_books(authorDict, publisherDict, bookDict):
    book = load_json('books.json')
    for oneBook in book:
        author = get_info(oneBook, "authors", "name")
        authorNum = authorDict[author]
        publisher = get_info(oneBook, "publishers", "name")
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

        db.session.add(newBook)
        db.session.commit()


def create_authors(authorDict, publisherDict, bookDict):
    book = load_json('books.json')
    authorslist = []
    for oneBook in book:
        for oneAuthor in oneBook['authors']:
            author = get_info(oneBook, "authors", "name")
            authorNum = authorDict[author]
            title = oneBook['title']
            if author not in authorslist:
                authorslist.append(author)
                authorNum = authorDict[author]
                publisher = get_info(oneBook, "publishers", "name")
                publisherNum = publisherDict[publisher]
                google_id = oneBook['google_id']
                bookNum = bookDict[google_id]

                born = oneAuthor.get('born')
                died = oneAuthor.get('died')
                nationality = oneAuthor.get('nationality')
                education = oneAuthor.get('education')
                alma_mater = oneAuthor.get('alma_mater')
                wikipedia_url = oneAuthor.get('wikipedia_url')
                image_url = oneAuthor.get('image_url')
                description = oneAuthor.get('description')

                newAuthor = Author(bookNum=bookNum, title=title, authorNum=authorNum, publisherNum=publisherNum, author=author, publisher=publisher, born=born, died=died,
                                   nationality=nationality, education=education, alma_mater=alma_mater, wikipedia_url=wikipedia_url, image_url=image_url, description=description)

                db.session.add(newAuthor)
                db.session.commit()


def create_publishers(authorDict, publisherDict, bookDict):
    book = load_json('books.json')
    publishersList = []
    for oneBook in book:
        for onePublisher in oneBook['publishers']:
            title = oneBook['title']
            publishersdict = oneBook['publishers']
            publisher = get_info(oneBook, "publishers", "name")
            if publisher not in publishersList:
                publishersList.append(publisher)
                publisherNum = publisherDict[publisher]
                author = get_info(oneBook, "authors", "name")
                authorNum = authorDict[author]
                google_id = oneBook['google_id']
                bookNum = bookDict[google_id]

                parent_company = onePublisher.get('parent company')
                owner = onePublisher.get('owner')
                founded = onePublisher.get('founded')
                location = onePublisher.get('location')
                website = onePublisher.get('website')
                wikipedia_url = onePublisher.get('wikipedia_url')
                image_url = onePublisher.get('image_url')
                description = onePublisher.get('description')

                newPublisher = Publisher(bookNum=bookNum, title=title, authorNum=authorNum, publisherNum=publisherNum, publisher=publisher, parent_company=parent_company, owner=owner,
                                         location=location, founded=founded, author=author, wikipedia_url=wikipedia_url, description=description, website=website, image_url=image_url)

                db.session.add(newPublisher)
                db.session.commit()


authorDict, publisherDict, bookDict = create_dictionaries()
create_books(authorDict, publisherDict, bookDict)
create_authors(authorDict, publisherDict, bookDict)
create_publishers(authorDict, publisherDict, bookDict)
# end of create_db.py
