import mysql.connector
from flask import Flask

def init_app(app: Flask):
    # MySQL Configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'form'

    # MySQL connection
    try:
        print("Trying to connect to MySQL...")
        conn = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        print("MySQL connection established.")
    except Exception as e:
        print("Connection error:")
        print(f"Error connecting to the database: {str(e)}")
        conn = None

    return conn
