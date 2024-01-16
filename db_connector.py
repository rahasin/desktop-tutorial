import sqlite3

def create_connection():
    connection = sqlite3.connect('APclinics.db')
    return connection
