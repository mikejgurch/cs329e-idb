#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
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

@app.route('/book/')
def book():
    return render_template('html/book.html')

@app.route('/authors/')
def authors():
    return render_template('html/authors.html')

@app.route('/publishers/')
def publishers():
    return render_template('html/publishers.html')

# if main.py is run directly, i.e., as the main module, it will be assigned the value main
# and if it's main go ahead and run the application.
# if this application is imported, then the __name__ is no longer __main__ and
# the code, app.run(), will not be executed

if __name__ == "__main__":
    app.run()
#----------------------------------------
# end of main.py
#-----------------------------------------

