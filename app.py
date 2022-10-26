from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

from controllers import random as r

app = Flask(__name__)
CORS(app)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('url.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def hello():
    return render_template("input.html")

@app.route('/random', methods=['POST'])
def randomise():
    original_url = request.get_json(force=True)
    print(f'{original_url["url"]}---------------------------------------------------------------------------------------------------------------')
    shortened_url = r.random_string()
    urls = [original_url['url'], shortened_url]
    r.insert_urls(urls)
    # return jsonify("https://url--reducer.herokuapp.com/" + shortened_url)
    print("http://localhost:5000/" + shortened_url)
    return jsonify("http://localhost:5000/" + shortened_url)

@app.route('/<str>')
def reroute(str):
    str_t = []
    str_t.append(str)
    conn = db_connection()
    cursor = conn.execute('SELECT original FROM url WHERE shortened = (?)', str_t)
    url = cursor.fetchone()[0]
    print(url)
    if url == None:
        print('redirecting to home')
        return redirect('/')
    else:
        url2 = url[7:]
        print(url2)
        print('redirecting to original')
        return redirect(f'http://{url2}')
    

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    path = environ.get("PATH_INFO")
    print(path)
    return err

if __name__ == "__main__":
    app.run(debug=True)




