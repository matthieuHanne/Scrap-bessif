
from flask import Flask
from flask import request 
import scrap_bessif_launcher
import json

app = Flask(__name__)

@app.route('/')
def init():
    return 'server start!'

@app.route('/scrap', methods=['POST'])
def scrap():
	keywords = request.form['keywords'].split()
	export_config = request.form['export_config'].split()
	mail_addr= request.form['mail_to']
	databases = request.form['databases'].split() 
	scrap_bessif_launcher.Scrap(mail_addr,export_config,keywords,databases)
	return 'test:)'

@app.route('/export', methods=['POST'])
def export():
	export_config = request.form['export_config'].split()
	return json.dumps(scrap_bessif_launcher.GetGlobalDatabase(export_config,1))

@app.route('/number', methods=['POST'])
def getnumber():
	keywords = request.form['keywords'].split()
	return json.dumps(scrap_bessif_launcher.GetNumber(keywords))

@app.route('/keyword', methods=['GET'])
def GetKeyword():
	return json.dumps(scrap_bessif_launcher.GetKeywordsFromGlobalDatabase())
	 
if __name__ == '__main__':
    app.run()
