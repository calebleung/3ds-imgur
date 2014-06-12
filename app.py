import requests
import datetime
import time
import os
from flask import Flask, jsonify, make_response, render_template, request
from pyimgur import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './tmp'
imgur = pyimgur('a117ab112c7028e', 'c81cbe29785a240082659f8f0b462e9343362e13')

@app.route('/', methods=['GET', 'POST'])
def indexPage():
	if request.method == 'POST':
		try:
			file = request.files['image']
			filename = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) )
			file.save(filename)
		except KeyError as e:
			return render_template('index.html', error = e)

		return render_template('index.html', URLs = imgurLinks, Lower = imgurLower)
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host = "127.0.0.1", port=7301)
