from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html', name="je moeder")

@app.route('/search', methods=['GET'])
def search():
    search_id = request.args.get('id') # Haal het ID op uit de querystring van het verzoek
    # Voer de zoekopdracht uit en krijg de resultaten terug (dummy resultaten hier)
    results = [{'id': 1}, {'id': 2}]  # Dummy resultaten, vervang dit door echte zoeklogica
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
