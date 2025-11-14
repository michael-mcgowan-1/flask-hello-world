from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Michael McGowan in 3308'


@app.route('/db_test/')
def db_test():
    conn = psycopg2.connect("postgresql://mimc5172_flask_hello_database_user:ysYGiRVYygPQ2C7szDG6d67p7jHq2PbY@dpg-d4b8kendiees73adp6j0-a/mimc5172_flask_hello_database")
    conn.close()
    return "Database Connection Successful"