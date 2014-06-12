import requests
import datetime
import time
import os
import pyimgur
from flask import Flask, jsonify, make_response, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './tmp'
imgur = pyimgur.Imgur('CLIENT ID')

@app.route('/', methods=['GET', 'POST'])
def indexPage():
	if request.method == 'POST':
		try:
			file = request.files['image']
			filename = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) )
			file.save(filename)
		except KeyError as e:
			return render_template('index.html', error = e)

		try:
			imgurResults = imgur.upload_image(filename)
			imgurLinks = imgurResults.link.encode('ascii')
			imgurLower = imgurLinks.split('imgur.com/')[1].lower()
		except (KeyError, TypeError):
			os.remove(filename)
			return render_template('index.html', error = True)

		os.remove(filename)

		return render_template('index.html', URLs = imgurLinks, Lower = imgurLower)
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host = "127.0.0.1", port=7300)
