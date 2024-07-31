from flask import Flask, g
import sqlite3

app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
    return g.db


@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
    return str(rows)


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        print('tearting down db')
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
