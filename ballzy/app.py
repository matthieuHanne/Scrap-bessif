
from flask import Flask
from flask import request 
import ic05_new_db

app = Flask(__name__)

@app.route('/')
def init():
    return 'server start!'

@app.route('/scrap', methods=['POST'])
def scrap():
    keywords = request.form['keywords'].split()
    for word in keywords:
        print word   
        # recherche(word)
    return 'test:)'
if __name__ == '__main__':
    app.run()
