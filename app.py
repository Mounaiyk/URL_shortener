from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

from controllers import random as r



if __name__ == '__main__':
  web_app = create_app()

  web_app.run(debug=False, port=get_port(), host='0.0.0.0')

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
    original_url = request.form["url"]
    shortened_url = r.random_string()
    urls = (original_url, shortened_url)
    r.insert_urls(urls)
    return jsonify(shortened_url)

@app.route('/<str>')
def reroute(str):
    str_t = []
    str_t.append(str)
    conn = db_connection()
    cursor = conn.execute('SELECT original FROM url WHERE shortened = (?)', str_t)
    url = cursor.fetchone()[0]
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

# define Flask app
def create_app():
  try:

    web_app = Flask(__name__)
    CORS(web_app)

    logging.info('Starting up..')

    return web_app

  except Exception as e:
    logging.exception(e)

# retrieve port
def get_port():
  return int(os.environ.get("PORT", 5000))

# start Flask app





