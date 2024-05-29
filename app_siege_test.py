from flask import Flask, request, jsonify
import psycopg2
import string
import random

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'example_db',
    'user': 'example_user',
    'password': 'example_password',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**db_params)
    return conn

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count(1) FROM books_wo_sharding;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    id = random.randint(1000000, 10000000)
    category_id = random.randint(1, 10)
    author = generate_random_string(8)
    title = generate_random_string(12)
    year = random.randint(1900, 2023)

    cur.execute('INSERT INTO books_wo_sharding (id, category_id, author, title, year) VALUES (%s, %s, %s, %s, %s);',
                (id, category_id, author, title, year))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)