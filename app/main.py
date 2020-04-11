from flask import Flask, request, send_file
import subprocess
import time

app = Flask(__name__)

@app.route("/")
def home_view():
	return "<h1>Welcome to Rabbit Web ScreenShoter</h1>"

@app.route('/screenshot', methods=['GET'])
def screenshot():
	url = request.args.get('url')
	timestamp = int(time.time()*1000.0)
	filename = 'images/' + request.args.get('username') + '_' + str(timestamp) + '.png'
	process = subprocess.run('phantomjs app/generator.js ' + url + ' ' + filename, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	print(process.stdout)
	print(process.stderr)
	return send_file('../' + filename, mimetype='image/png')