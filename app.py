#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request,socket
from validate_email import validate_email

app = Flask(__name__)

@app.route ('/')
def home():
    return "Ingrese email: <./mail/someone@server.com> "
	

@app.route ('/mail/<string:mail>')
def valida_mail(mail):
	if   validate_email(mail) == True:
		x =  [{ 'name': mail , 'status': 'OK'}]
		return jsonify(x)
	y =  [{ 'name': mail , 'status': 'ERROR'}]
	return jsonify(y)

@app.route ('/json', methods=['POST'])
def valida_mail_json():
	request_data = request.get_json()
	mail = request_data['mail']
	if   validate_email(mail) == True:
		x =  [{ 'name': mail , 'status': 'OK', 'server': socket.gethosname()}]
		return jsonify(x)
	y =  [{ 'name': mail , 'status': 'ERROR', 'server': socket.gethosname()}}]
	return jsonify(y)


if __name__ == "__main__":
    app.run (host="0.0.0.0", port= 8080)
