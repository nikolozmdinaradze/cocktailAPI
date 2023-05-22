import sqlite3
conn = sqlite3.connect("History.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE History

(id INTEGER PRIMARY KEY AUTOINCREMENT,
cocktail VARCHAR(50),
user VARCHAR(100),
date VARCHAR(50));''')
conn.close()