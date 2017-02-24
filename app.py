from flask import render_template

from book import *

app = Flask(__name__)


def add_book(ISBN):
    book = Book(ISBN)
    db.session.add(book)
    db.session.commit()


@app.route('/')
def main():
    books = Book.query.all()

    for book in books:
        book.__init__(book.ISBN)
    return render_template('index.html', books=books)


@app.route('/elements')
def elements():
    return render_template('elements.html')


if __name__ == "__main__":
    app.run()
