# Cryptarch Microservice

Flask web service that performs symmetric encryption and decryption of UTF-8 strings. 

## Setup

First setup a python virtual environment

`python3 -m venv venv`

And then activate that environment

`. venv/bin/activate`

Install Flask in the activated environment

`pip install Flask`

## Running

Set environment variable

`FLASK_APP=cryptarch`

And run Flask

`flask run`

This will start the server at `http://127.0.0.1:5000`

## Requests

Requests can be made by sending a POST request with application/x-www-form-urlencoded form data with a message field. For example:

`curl -i -X POST -d "message=hello world\!" localhost:5000/encrypt`

`curl -i -X POST -F "message=gAAAAABi33I8Z0TSDx1LACt-UV5AssLtG_49gBJiPejmOFVH9HPyzI-DIgwI4RYQ7epoJSVsXTFTJrfODc-yplBHDUOMM2Wdyw==" localhost:5000/decrypt`

The response data of the POST request is the encrypted or decrypted text
