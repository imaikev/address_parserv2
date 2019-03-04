#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify
from validate_email import validate_email

app = Flask(__name__)


@app.route ('/mail')
def home():
    return "Ingrese email: <./mail/someone@server.com> "
	

@app.route ('/mail/<string:mail>')
def valida_mail(mail):
	if   validate_email(mail) == True:
		return  "Mail a validar: " + mail + ": OK"
	return 	"Mail a validar: " + mail + " - ERROR"

if __name__ == "__main__":
    app.run (host="0.0.0.0", port= 8080)