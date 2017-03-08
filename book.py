import codecs
import json
import urllib.request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    ISBN = db.Column('ISBN', db.Integer, primary_key=True, unique=True)
    title = db.Column('title', db.String(length=256))
    cover = db.Column('cover', db.String(length=256))
    publish_date = db.Column('publish_date', db.String(length=256))
    number_of_pages = db.Column('number_of_pages', db.String(length=256))
    authors = db.Column('authors', db.String(length=256))
    publishers = db.Column('publishers', db.String(length=256))

    def print(self):
        print(self.data)

    def __init__(self, ISBN):
        db.create_all()
        self.ISBN = ISBN
        url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + str(self.ISBN) + "&jscmd=data&format=json"
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        self.data = {}
        for k1, v1 in data.items():
            self.data = data[k1]

        if self.data is not None:
            if 'title' in self.data:
                self.title = self.data['title']
            if 'authors' in self.data:
                self.authors = self.data['authors'][0]['name']
                if len(self.data['authors']) > 1:
                    for author in range(len(self.data['authors'])):
                        self.authors += (", " + self.data['authors'][author]['name'])
            if 'cover' in self.data:
                self.cover = self.data['cover']['medium']
            if 'publish_date' in self.data:
                self.publish_date = self.data['publish_date']
            if 'number_of_pages' in self.data:
                self.number_of_pages = self.data['number_of_pages']
            if 'subjects' in self.data:
                self.tags = []
                for tag in range(len(self.data['subjects'])):
                    self.tags.append(self.data['subjects'][tag]['name'])
            if 'publishers' in self.data:
                self.publishers = self.data['publishers'][0]['name']
                if len(self.data['publishers']) > 1:
                    for publisher in range(len(self.data['publishers'])):
                        self.publishers += (", " + self.data['publishers'][publisher]['name'])
