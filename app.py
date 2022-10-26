from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify("<p>Hello World</p>")

@app.route('/random', methods=['POST'])
def randomise():
    original_url = request.form['url']
    shortened_url = random_string():

