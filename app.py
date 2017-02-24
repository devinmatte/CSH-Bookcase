from flask import Flask
from flask import render_template

from book import Book

app = Flask(__name__)


@app.route('/')
def main():
    books = {Book(9780130125071), Book(9780980200447), Book(9780980200448)}
    return render_template('index.html', books=books)


@app.route('/elements')
def elements():
    return render_template('elements.html')


if __name__ == "__main__":
    app.run()
