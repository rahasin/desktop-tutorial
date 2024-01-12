# db_connector
import pymysql.cursors

def create_connection():
    connection = pymysql.connect(host = 'localhost', user = 'root', password = 'APterm3r@r@8304', database = 'APclinics')
    return connection