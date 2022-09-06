from msilib.schema import Class
from multiprocessing import connection
from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'
app = Flask(__name__)

def open_connect():
    getattr(g.'_connection') = None
    return getattr(connection)
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')



