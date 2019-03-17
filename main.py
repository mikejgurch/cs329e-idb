# -----------------------------------------
# main.py
# creating first flask application
# -----------------------------------------
#
#

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
    return render_template('html/index.html')


@app.route('/books/')
def books():
    return render_template('html/books.html')


@app.route('/authors/')
def authors():
    return render_template('html/authors.html')


@app.route('/publishers/')
def publishers():
    return render_template('html/publishers.html')


@app.route('/about/')
def about():
    return render_template('html/about.html')


# all routes belowe this -----!!!!!!
# change when we get html files
# books
"""
@app.route('/books/HPSorcererStone')
def HPSorcererStone():
    return render_template('html/HPSorcererStone.html')

@app.route('/books/book2/')
def publishers():
    return render_template('html/book2.html')

@app.route('/books/book3/')
def publishers():
    return render_template('html/book3.html')

# authors
@app.route('/authors/JKRowling')
def JKRowling():
    return render_template('html/JKRowling.html')

@app.route('/authors/author2')
def publishers():
    return render_template('html/author2.html')

@app.route('/authors/author3/')
def publishers():
    return render_template('html/author3.html')

# publishers
@app.route('/publishers/Pottermore')
def Pottermore():
    return render_template('html/Pottermore.html')

@app.route('/publishers/publisher2/')
def publishers():
    return render_template('html/publisher2.html')

@app.route('/publishers/publisher3/')
def publishers():
    return render_template('html/publisher3.html')
"""

# if main.py is run directly, i.e., as the main module, it will be assigned the value main
# and if it's main go ahead and run the application.
# if this application is imported, then the __name__ is no longer __main__ and
# the code, app.run(), will not be executed

if __name__ == "__main__":
    app.run()
# -----------------------------------------
# end of main.py
# -----------------------------------------
