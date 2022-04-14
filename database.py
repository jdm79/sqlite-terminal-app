from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("data.db")

connection.row_factory = sqlite3.Row # this means sqlite3 gets rows instead of tuples

def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);"
            )

def add_entry(entry_content, entry_date):
    with connection:
         connection.execute(
             "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
             )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor