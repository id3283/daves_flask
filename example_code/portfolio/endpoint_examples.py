from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/positions', methods=['GET'])
def get_positions():
    l = []
    l.append( ('AAPL', 10, 150, 1500) )
    l.append( ('GOOGL', 5, 2800, 14000) )
    return jsonify(l)



if __name__ == '__main__':
    # initialize_database()
    app.run()
