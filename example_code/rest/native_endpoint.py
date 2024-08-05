from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]


# Get all books
@app.route('/books/', methods=['GET'])
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):

    # CLASS: is this the best way to fetch a book by ID?
    book = next((book for book in books if book['id'] == book_id), None)

    return jsonify(book) if book else ('', 404)


# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201


# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return ('', 404)


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True)
