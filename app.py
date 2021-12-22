from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm
import json
from collections import defaultdict
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST': 
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		d = {}
		for ent in doc.ents:
			d.update({ent.label_: ent.text})

	return render_template("index.html",results=d)

if __name__ == '__main__':
	app.run(debug=True)