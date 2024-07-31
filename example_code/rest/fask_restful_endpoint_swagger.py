from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='My API',
          description='A simple demonstration of a Flask REST API with Swagger',
          doc='/swagger/')

ns = api.namespace('books', description='Books operations')

book_model = api.model('Book', {
    'id': fields.Integer(readonly=True, description='The book unique identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author'),
})

# Sample data
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]
book_id_counter = 3

@ns.route('/')
class BookList(Resource):
    @ns.doc('list_books')
    @ns.marshal_list_with(book_model)
    def get(self):
        """List all books"""
        return books

    @ns.doc('create_book')
    @ns.expect(book_model)
    @ns.marshal_with(book_model, code=201)
    def post(self):
        """Create a new book"""
        global book_id_counter
        new_book = api.payload
        new_book['id'] = book_id_counter
        books.append(new_book)
        book_id_counter += 1
        return new_book, 201


@ns.route('/<int:id>')
@ns.response(404, 'Book not found')
@ns.param('id', 'The book identifier')
class Book(Resource):
    @ns.doc('get_book')
    @ns.marshal_with(book_model)
    def get(self, id):
        '''Fetch a book given its identifier'''
        book = next((book for book in books if book['id'] == id), None)
        if book:
            return book
        api.abort(404)

    @ns.doc('delete_book')
    @ns.response(204, 'Book deleted')
    def delete(self, id):
        """Delete a book given its identifier"""
        global books
        books = [book for book in books if book['id'] != id]
        return '', 204

    @ns.doc('update_book')
    @ns.expect(book_model)
    @ns.marshal_with(book_model)
    def put(self, id):
        """Update a book given its identifier"""
        book = next((book for book in books if book['id'] == id), None)
        if book:
            data = api.payload
            book.update(data)
            return book
        api.abort(404)


if __name__ == '__main__':
    app.run(debug=True)
