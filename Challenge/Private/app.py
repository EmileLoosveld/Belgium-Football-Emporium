from flask import Flask, render_template, request, jsonify, session
import sqlite3
import os
import uuid

app = Flask(__name__, static_folder='assets/images')
app.secret_key = os.urandom(24)


SQLFILE = 'db/init.sql'


## Create table per user
def init_user_db():
    user_db_file = f"user_{session['id']}.db"
    if not os.path.exists(user_db_file):
        conn = sqlite3.connect(user_db_file)
        with app.open_resource(SQLFILE, mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

# DB query to search items
def DBSearchItems(query, args=()):
    print(args[0])
    if args[0].strip() == '7':
        # Do not show this item
        hidden_data = [(7, "Vlag", "Vlag om te supporteren voor de nationale ploeg van België", 20, "7.png")]
        return hidden_data
    else:
        conn = sqlite3.connect(f"user_{session['id']}.db")
        cursor = conn.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        conn.close()
        return rows

# DB query to update the description from items as Admin!
def DBUpdateDescription(product_id, new_description):
    conn = sqlite3.connect(f"user_{session['id']}.db")
    cursor = conn.cursor()

    # TODO check if this is safe!
    query = "UPDATE items SET description = '" + new_description + "' WHERE id = " + str(product_id)
    cursor.executescript(query)
    conn.commit()
    conn.close()


## DEFAULT ROUTES TO THE PAGES

@app.route('/admin')
def admin():
    if 'id' not in session:
        session['id'] = str(uuid.uuid4())
        init_user_db()  # Initialize the user's database

    return render_template('admin.html')

@app.route('/')
def homepage():
    if 'id' not in session:
        session['id'] = str(uuid.uuid4())
        init_user_db()  # Initialize the user's database

    return render_template('homepage.html')


# Search request to GET the products
@app.route('/search', methods=['GET'])
def search():
    search_id = request.args.get('id')
    results = DBSearchItems("SELECT * FROM items WHERE id = ?", (search_id,))
    # Format the results
    formatted_results = [{'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'image': row[4]} for row in results]
    return jsonify(formatted_results)

# API call to edit the post as admin!
@app.route('/edit', methods=['POST'])
def edit_description():

    # Check if user is admin
    if request.cookies.get('role') != 'admin':
        return jsonify(message="Unauthorized access!"), 401


    data = request.json
    product_id = data.get('id')
    new_description = data.get('description')
    if not product_id or not new_description:
        return jsonify(message="Product ID and new description are required."), 400
    try:
        DBUpdateDescription(product_id, new_description)
        return jsonify(message="Description updated successfully."), 200
    except Exception as e:
        return jsonify(message=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
