from flask import Flask, request, send_file, jsonify, make_response
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
	
	# TODO: store the log in file
	print(process.stdout)
	print(process.stderr)

	# return the img url
	domain = request.host_url + '/image?imagename=' + filename
	response = make_response(jsonify({'imageurl': domain}), 200)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["content-type"] = "application/json; charset=utf8"
	return response


# serve the image
@app.route('/image', methods=['GET'])
def getImage():
	imagename = request.args.get('imagename')
	response = make_response(send_file('../' + imagename, mimetype='image/png'), 200)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["content-type"] = "image/png"
	return response


# mock the api for testing
@app.route('/mock', methods=['GET'])
def mock():
	# return the img url
	mockUrl = "https://rabbit-web-screenshoter.herokuapp.com//image?imagename=images/carmen_w.k_1586728086020.png"
	time.sleep(5)
	response = make_response(jsonify({'imageurl': mockUrl}), 200)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["content-type"] = "application/json; charset=utf8"
	return response

# TODO: store the images in db and support the delete method
# request to delete the image
# @app.route('/delete', methods=['GET'])
# def deleteImage():
# 	imagename = request.args.get('imagename')
# 	# delete the image 
# 	return send_file('../' + imagename, mimetype='image/png')