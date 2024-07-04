import sqlite3
import json
import uuid

connect = sqlite3.connect('instance/development.db')
cursor = connect.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS Country (
		id TEXT PRIMARY KEY,
		name TEXT NOT NULL,
		code TEXT NOT NULL
);
''')


with open('countries.json', 'r') as file:
    countries = json.load(file)

for country in countries:
    countries_id = str(uuid.uuid4())
    cursor.execute(
		"INSERT INTO countries (id, name, code) VALUES (?, ?, ?);",
  (countries_id, country['name'], country['code'])
  )

    connect.commit()
    cursor.close()
    connect.close()
