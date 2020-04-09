#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request
from validate_email import validate_email
from postal.parser import parse_address

import socket ,os ,  json

app = Flask(__name__)


@app.route ('/')
def home():
    return parse_address('The Book Club 100-106 Leonard St Shoreditch London EC2A 4RH, United Kingdom')

@app.route ('/file')
def file_read():
	str = open('requirements.txt', 'r').read()
	return str
	
@app.route ('/env')
def ambiente():
		data = []
		new_data = [{'ENGINE': os.environ.get('ENGINE')}] 
		data.append(new_data)
		new_data = [{'DATABASE_NAME': os.environ.get('DATABASE_NAME')}] 
		data.append(new_data)
		new_data = [{'DATABASE_USER': os.environ.get('DATABASE_USER')}] 
		data.append(new_data)
		new_data = [{'DATABASE_PASSWORD': os.environ.get('DATABASE_PASSWORD')}]
		data.append(new_data)
		new_data = [{'DATABASE_HOST': os.environ.get('DATABASE_HOST')}] 
		data.append(new_data)
		new_data = [{'DATABASE_PORT': os.environ.get('DATABASE_PORT')}] 
		data.append(new_data)
		
		return (jsonify(data))

	
@app.route ('/mail/<string:mail>')
def valida_mail(mail):
	if   validate_email(mail) == True:
		x =  [{ 'name': mail , 'status': 'OK', 'server': socket.gethostname()}]
		return jsonify(x)
	y =  [{ 'name': mail , 'status': 'ERROR', 'server': socket.gethostname()}]
	return jsonify(y)

@app.route ('/json', methods=['POST'])
def valida_mail_json():
	request_data = request.get_json()
	mail = request_data['mail']
	if   validate_email(mail) == True:
		x =  [{ 'name': mail , 'status': 'OK', 'server': socket.gethostname()}]
		return jsonify(x)
	y =  [{ 'name': mail , 'status': 'ERROR', 'server': socket.gethostname()}]
	return jsonify(y)

	

if __name__ == "__main__":
    app.run (host="0.0.0.0", port= 8080)
