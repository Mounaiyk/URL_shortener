from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

from controllers import random as r

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template("input.html")

@app.route('/random', methods=['POST'])
def randomise():
    print(request.form)
    # return r.search(request.form["url"])
    # original_url = request.form["url"]
    # shortened_url = r.random_string()
    # r.insert_urls(original_url, shortened_url)
    # return jsonify(shortened_url)
    return r.random_string(request.form["url"])
