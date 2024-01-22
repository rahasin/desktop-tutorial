# This function creates a connection to the SQLite database 'APclinics.db'
import sqlite3

def create_connection():
    # Establish a connection to the SQLite database
    connection = sqlite3.connect('APclinics.db')
    return connection
