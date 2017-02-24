import codecs
import json
import urllib.request


class Book:
    def build(self):
        url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + str(self.ISBN) + "&jscmd=data&format=json"
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        for k1, v1 in data.items():
            return data[k1]

    def print(self):
        url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + str(self.ISBN) + "&jscmd=data&format=json"
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        for k1, v1 in data.items():
            print(k1)
            for k2, v2 in data[k1].items():
                print(k2, " :: ", v2)
        print(data)

    def __init__(self, ISBN):
        self.ISBN = ISBN
        self.data = self.build()
        if self.data is not None:
            self.title = self.data['title']
            self.authors = []
            for author in range(len(self.data['authors'])):
                self.authors.append(self.data['authors'][author]['name'])
            self.cover = self.data['cover']['medium']
            self.publish_date = self.data['publish_date']
            self.number_of_pages = self.data['number_of_pages']
            self.tags = []
            for tag in range(len(self.data['subjects'])):
                self.tags.append(self.data['subjects'][tag]['name'])
            self.publishers = []
            for publisher in range(len(self.data['publishers'])):
                self.publishers.append(self.data['publishers'][publisher]['name'])
