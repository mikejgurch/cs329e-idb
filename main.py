# -----------------------------------------
# main.py
# creating first flask application
# -----------------------------------------
#
#

from flask import Flask, render_template, request
from models import app, db, Book
from create_db import db, Book, create_books, Author, create_authors, Publisher, create_publishers
from sqlalchemy import desc, asc, func
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books/')
def books():
    books = db.session.query(Book).all()
    return render_template('books.html', books=books)

# app route to sort books in desc order


@app.route('/books_desc/')
def books_desc():
    books = db.session.query(Book).order_by(desc(Book.title)).all()
    return render_template('books.html', books=books)

# app route to sort books in asc order


@app.route('/books_asc/')
def books_asc():
    books = db.session.query(Book).order_by(asc(Book.title)).all()
    return render_template('books.html', books=books)


@app.route('/authors/')
def authors():
    authors = db.session.query(Author).distinct(Author.author)
    return render_template('authors.html', authors=authors)

# app route to sort authors in desc order


@app.route('/authors_desc/')
def authors_desc():
    authors = db.session.query(Author).order_by(desc(Author.author)).distinct(Author.author)
    return render_template('authors.html', authors=authors)

# app route to sort authors in asc order


@app.route('/authors_asc/')
def authors_asc():
    authors = db.session.query(Author).order_by(asc(Author.author)).distinct(Author.author)
    return render_template('authors.html', authors=authors)


@app.route('/publishers/')
def publishers():
    publishers = db.session.query(Publisher).distinct(Publisher.publisher)
    return render_template('publishers.html', publishers=publishers)

# app route to sort publishers in desc order


@app.route('/publishers_desc/')
def publishers_desc():
    publishers = db.session.query(Publisher).order_by(
        desc(Publisher.publisher)).distinct(Publisher.publisher)
    return render_template('publishers.html', publishers=publishers)

# app route to sort publishers in asc order


@app.route('/searchBooks/')
def search_books():
    #books = db.session.query.filter(Note.message.like("%harry potter%")).all()
    # sample input, once linked to front end change harry potter to approriate variable
    books = db.session.query.filter(Book.title.like("%harry potter%"))


@app.route('/dummy2/')
def dummy2():
    return render_template('dummy2.html')

@app.route('/searchBar/', methods=['GET', 'POST'])
def search_bar():
    user_search = request.form['user_search']
    search_in = str(user_search).lower()
    #authors = db.session.query(Author).all()
    authorResults = []
    results = db.session.query(Author).filter(func.lower(Author.author).like("%" + search_in + "%")).from_self()
    b_results = db.session.query(Book).filter(func.lower(Book.title).like("%" + search_in + "%")).from_self()
    p_results = db.session.query(Publisher).filter(func.lower(Publisher.publisher).like("%" + search_in + "%")).from_self()
    for i in results:
        authorResults.append(i)

    for i in b_results:
        authorResults.append(i)

    for i in p_results:
        authorResults.append(i)

    #authorResults.append(results)
    return render_template('dummy2.html', authors=authors, authorResults=authorResults)

# # prototype
# @app.route('/searchPublishers/', methods=['GET', 'POST'])
# def search_publishers():

#     user_search = request.form['user_search']
#     #publishers = db.session.query.filter(Publisher.publisher.like("%" + user_search + "%")).all()
#     publishers = db.session.query(user_search).all()#.filter(Publisher.publisher.like("%" + user_search + "%")).all()
#     return render_template('dummy.html', publishers=publishers)


@app.route('/dummy/')
def dummy():
    return render_template('dummy.html')


@app.route('/search/', methods=['GET', 'POST'])
def search_all():
    # if "Ok" in request.form.values():
    user_search = request.form['user_search']
    #publishers = db.session.query.filter(Publisher.publisher.like("%" + user_search + "%")).all()
    books = db.session.query(Book).all()
    authors = db.session.query(Author).all()
    publishers = db.session.query(Publisher).all()

    bookResults = []
    for i in books:
        if str(user_search).lower() in str(i.title).lower():
            bookResults.append(i)
        # results.append(db.session.query(user_search).all())#.filter(Publisher.publisher.like("%" + user_search + "%")).all()
    return render_template('dummy.html', books=books, bookResults=bookResults)


@app.route('/publishers_asc/')
def publishers_asc():
    publishers = db.session.query(Publisher).order_by(
        asc(Publisher.publisher)).distinct(Publisher.publisher)
    return render_template('publishers.html', publishers=publishers)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/terms/')
def terms():
    return render_template('termsofuse.html')


@app.route('/privacy/')
def privacy():
    return render_template('privacypolicy.html')


@app.route('/bookInfo/<bookID>')
def bookInfo(bookID):
    book_id = str(bookID)
    books = db.session.query(Book).all()
    for i in books:
        if (book_id == str(i.bookNum)):
            bookList = [j for j in books if i.authorNum == j.authorNum]
            return render_template('bookInfo.html', books=books, bookList=bookList, i=i)


@app.route('/authorInfo/<authorID>')
def authorInfo(authorID):
    author_id = str(authorID)
    authors = db.session.query(Author).all()
    books = db.session.query(Book).all()
    for i in authors:
        if (author_id == str(i.authorNum)):
            bookList = [j for j in books if i.authorNum == j.authorNum]
            publishers = []
            publisherList = []
            for k in bookList:
                if k.publisher not in publishers:
                    publishers.append(k.publisher)
                    publisherList.append(k)
            return render_template('authorInfo.html', bookList=bookList, publisherList=publisherList, authors=authors, i=i)


@app.route('/publisherInfo/<publisherID>')
def publisherInfo(publisherID):
    publisher_id = str(publisherID)
    publishers = db.session.query(Publisher).all()
    books = db.session.query(Book).all()
    for i in publishers:
        if (publisher_id == str(i.publisherNum)):
            bookList = [j for j in books if i.publisherNum == j.publisherNum]
            authors = []
            authorList = []
            for k in bookList:
                if k.author not in authors:
                    authors.append(k.author)
                    authorList.append(k)
            return render_template('publisherInfo.html', bookList=bookList, authorList=authorList, publishers=publishers, i=i)


import subprocess


@app.route('/test')
def test():
    p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()
    output = err+out
    output = output.decode("utf-8")  # convert from byte type to string type

    return render_template('test.html', output=output)


if __name__ == "__main__":
    app.run()
# end of main3.py
'''
from flask import Flask, render_template

# create a flask object (flask needs an object to represent the application)
app = Flask(__name__)

# The route decorator '@app.route()' maps a function to a route on your website.
# decorators are used to map a function, index(), to a web page, / or
# i.e., when someone types in the home address of the web site,
# flask will run the function index()
# summary: type in a URL, flask check the URL, finds the associate function with it, runs the
# function, collect responses, and send back the results to the browser.


@app.route('/')
def index():
    return render_template('index.html')

'''
'''
@app.route('/books/')
def books():
    return render_template('books.html')
'''
'''
@app.route('/books/')
def books():
    return render_template('books.html')

@app.route('/authors/')
def authors():
    return render_template('authors.html')


@app.route('/publishers/')
def publishers():
    return render_template('publishers.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/terms/')
def terms():
    return render_template('termsofuse.html')

@app.route('/privacy/')
def privacy():
    return render_template('privacypolicy.html')

# all routes belowe this -----!!!!!!
# change when we get html files

# Books:

@app.route('/books/HPSorcererStone/')
def HPSorcererStone():
    return render_template('HPSorcererStone.html')

@app.route('/books/AnimalFarm/')
def AnimalFarm():
    return render_template('AnimalFarm.html')

@app.route('/books/ToKillaMockingBird/')
def TKMB():
    return render_template('TKMB.html')

# Authors:

@app.route('/authors/JKRowling')
def JKRowling():
    return render_template('JKRowling.html')

@app.route('/authors/GeorgeOrwell')
def GeorgeOrwell():
    return render_template('GeorgeOrwell.html')

@app.route('/authors/HarperLee/')
def HarperLee():
    return render_template('HarperLee.html')

# Publishers:

@app.route('/publishers/Pottermore')
def Pottermore():
    return render_template('Pottermore.html')

@app.route('/publishers/ScholasticCo/')
def ScholasticCo():
    return render_template('ScholasticCo.html')

@app.route('/publishers/HarperCollins/')
def HarperCollins():
    return render_template('HarperCollins.html')


# if main.py is run directly, i.e., as the main module, it will be assigned the value main
# and if it's main go ahead and run the application.
# if this application is imported, then the __name__ is no longer __main__ and
# the code, app.run(), will not be executed

if __name__ == "__main__":
    app.run()
'''
# -----------------------------------------
# end of main.py
# -----------------------------------------
