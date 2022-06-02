import sqlite3
import json
from pathlib import Path

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)

    # The following code will print tuples in the console
    # for row in cursor:
    #     print(row)

    # This following code will give us a list of tuples
    # The code above must be commented out because if we iterate over a cursor, it will reach at the end of the list
    movies = cursor.fetchall()
    print(movies)
