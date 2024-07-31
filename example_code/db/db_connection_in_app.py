from flask import Flask
import sqlite3
import atexit

app = Flask(__name__)
db_connection = None


def connect_db():
    """Function to connect to the database"""
    return sqlite3.connect('database.db')


@app.before_request # Run before EVERY request, but cheap
def initialize_db():
    """Function to initialize the database connection if it hasn't been initialized"""
    global db_connection
    if db_connection is None:
        db_connection = connect_db()


@app.route('/')
def index():
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
    return str(rows)


def close_db():
    """Function to close the database connection when the application shuts down"""
    global db_connection
    if db_connection:
        db_connection.close()


atexit.register(close_db)

if __name__ == '__main__':
    app.run(debug=True)
