from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Sample data
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]


class BookList(Resource):
    def get(self):
        return books

    def post(self):
        new_book = request.get_json()
        books.append(new_book)
        return (new_book, 201)


class Book(Resource):
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        return book if book else ('', 404)

    def put(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book:
            data = request.get_json()
            book.update(data)
            return book
        return ('', 404)

    def delete(self, book_id):
        global books
        books = [book for book in books if book['id'] != book_id]
        return ('', 204)


api.add_resource(BookList, '/books/')
api.add_resource(Book, '/books/<int:book_id>/')

if __name__ == '__main__':
    app.run(debug=True)
