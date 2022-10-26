import sqlite3

conn = sqlite3.connect("url.sqlite")

sql_query = "CREATE TABLE url (id integer PRIMARY KEY, original VARCHAR(255) NOT NULL, shortened VARCHAR(255) NOT NULL)"

cursor.execute(sql_query)
