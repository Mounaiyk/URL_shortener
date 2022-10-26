import sqlite3

conn = sqlite3.connect("url.sqlite")
cursor = conn.cursor()

sql_query = "CREATE TABLE url (id integer PRIMARY KEY, original VARCHAR(255) NOT NULL, shortened VARCHAR(255) NOT NULL)"

cursor.execute(sql_query)

sql_query2 = f'INSERT INTO url (original, shortened) VALUES ("https://www.getfutureproof.co.uk/", "fixbqxzloq")'

cursor.execute(sql_query2)
conn.commit()
