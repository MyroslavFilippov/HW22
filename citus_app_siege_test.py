from flask import Flask, request, jsonify
import psycopg2
import random
import string

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'example_db',
    'user': 'example_user',
    'password': 'example_password',
    'host': 'citus_coordinator',
    'port': 5433  # Updated to the new port
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
    cur.execute('SELECT * FROM books LIMIT 10;')  # Limit to 10 for testing
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(books)


@app.route('/books', methods=['POST'])
def add_book():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()

    category_id = random.randint(1, 10)
    author = generate_random_string(8)
    title = generate_random_string(12)
    year = random.randint(1900, 2023)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (category_id, author, title, year) VALUES (%s, %s, %s, %s)',
                (category_id, author, title, year))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(
        {'status': 'success', 'category_id': category_id, 'author': author, 'title': title, 'year': year}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
