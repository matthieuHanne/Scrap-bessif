
from flask import Flask
from flask import request 
import scrap_bessif_launcher

app = Flask(__name__)

@app.route('/')
def init():
    return 'server start!'

@app.route('/scrap', methods=['POST'])
def scrap():
    keywords = request.form['keywords'].split()
	export_config = request.form['export_config'].split()# inventeur / demandeur / classification_internationalle/ abregé_pour / mot_clef (k)
	mail_addr= request.form['mail_to']
	databases = request.form['databases'].split() # f pour espace.net.fr et w pour espace.net.world , faire comme pour export config 
    scrap_bessif_launcher.Scrap(mail_addr,export_config,keywords,databases)
    return 'test:)'
if __name__ == '__main__':
    app.run()
