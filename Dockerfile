FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

RUN pip install flask 

COPY app.py /opt/

RUN git clone https://github.com/openvenues/libpostal

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
