import sqlite3

# Connect to db
connection = sqlite3.connect("zoo.db")

# test connection
print(connection.total_changes)

# to execute sql commands we need a cursor object
cursor = connection.cursor()

