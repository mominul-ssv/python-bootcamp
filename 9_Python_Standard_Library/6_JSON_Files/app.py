import json
from pathlib import Path

from nbformat import read

# Creating JSON object
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

# Converting JSON object to data string
# 'json.dumps()' will give us a movies data formatted as json
data = json.dumps(movies)

# Printing JSON object to the console
print(data)

# Writing JSON data to a file
Path("movies.json").write_text(data)

# Reading JSON data
# 'json.loads()' will give us an arrays of dictionaries
readData = Path("movies.json").read_text()
readMovies = json.loads(data)

# Printing dictionary to the console
print(readMovies)
print(readMovies[0])
print(readMovies[0]["title"])
