# -----------------------------------------
# main.py
# creating first flask application
# -----------------------------------------
#
#

from flask import Flask, render_template
from create_db import app, db, Book, create_books

#app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book2/')
def book():
    books = db.session.query(Book).all()
    return render_template('book2.html', books = books)

@app.route('/about/')
def about():
    return render_template('about.html')

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
