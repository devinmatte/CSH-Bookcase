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

    def print(self):
        print(self.data)

    def __init__(self, ISBN):
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
                self.authors = []
                for author in range(len(self.data['authors'])):
                    self.authors.append(self.data['authors'][author]['name'])
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
                self.publishers = []
                for publisher in range(len(self.data['publishers'])):
                    self.publishers.append(self.data['publishers'][publisher]['name'])
