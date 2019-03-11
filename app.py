#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request
from validate_email import validate_email
import socket ,os ,  json

app = Flask(__name__)


@app.route ('/')
def home():
	!yum list installed
    return "Ingrese email: <./mail/someone@server.com> "

	
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

	
@app.route ('/DB_VAR')
def DB_VAR():
	import pyodbc
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + os.environ.get('DATABASE_HOST') + ','+ os.environ.get('DATABASE_PORT') + ';DATABASE=' + os.environ.get('DATABASE_NAME') + ';UID=' + os.environ.get('DATABASE_USER') + ';PWD=' + os.environ.get('DATABASE_PASSWORD') + '')
	cursor = cnxn.cursor()
	cursor.execute("SELECT TOP 100 [de_direccion], de_verificado   FROM [Staging].[dbo].[st_cob_cl_dir_electronica_bkp]")
	data = []
	
	for row in cursor.fetchall():
		if ( validate_email(row.de_direccion) == True): 
			   is_valid = 'S'
		else:
			   is_valid = 'N'            
		
		new_data = [{'mail': row.de_direccion , 'status': is_valid, 'server': socket.gethostname()}]
		data.append(new_data)
		
	
	return (jsonify(data))
	
	

@app.route ('/DB_PLANO')
def DB_PLANO():
	import pyodbc
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESAMSSQL22,1148;DATABASE=DWC;UID=DTSDESA;PWD=*Paspa2')
	cursor = cnxn.cursor()
	cursor.execute("SELECT TOP 100 [de_direccion], de_verificado   FROM [Staging].[dbo].[st_cob_cl_dir_electronica_bkp]")
	data = []
	
	for row in cursor.fetchall():
		if ( validate_email(row.de_direccion) == True): 
			   is_valid = 'S'
		else:
			   is_valid = 'N'            
		
		new_data = [{'mail': row.de_direccion , 'status': is_valid, 'server': socket.gethostname()}]
		data.append(new_data)
		
	
	return (jsonify(data))
	

if __name__ == "__main__":
    app.run (host="0.0.0.0", port= 8080)
