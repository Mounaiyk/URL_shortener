import random
import string
import sqlite3

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('url.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

# printing lowercase
def random_string(id):
    letters = string.ascii_lowercase
    str1 = "".join(random.choice(letters) for i in range(10))
    str2 = []
    str2.append(str1)
    print(f'{str1}-----------------------------------------------------------------------------------------------------------------------------')
    conn = db_connection()
    cursor = conn.execute(f'SELECT * FROM url WHERE shortened = (?)', str2)
    # cursor = conn.execute(f'SELECT * FROM url WHERE id = {id};')
    # return cursor.fetchone()
    if cursor.fetchone() == None:
        return str1
    else:
        random_string()

def insert_urls(original_url, shortened_url):
    conn = db_connection()
    cursor = conn.execute(f'INSERT INTO url (original, shortened) VALUES ({original_url}, {shortened_url})')
