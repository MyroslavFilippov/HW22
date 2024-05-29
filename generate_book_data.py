import csv
import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_book_records(num_records):
    records = []
    for i in range(1, num_records + 1):
        category_id = random.randint(1, 10)
        author = generate_random_string(8)
        title = generate_random_string(12)
        year = random.randint(1900, 2023)
        records.append((i, category_id, author, title, year))
    return records

def main():
    num_records = 1000000
    file_name = 'books5.csv'

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'category_id', 'author', 'title', 'year'])
        for record in generate_book_records(num_records):
            writer.writerow(record)

if __name__ == "__main__":
    main()
