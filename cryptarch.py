from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
cryptarch = Fernet(key)

@app.post('/encrypt')
def encrypt():
    message = request.form.get("message")
    encrypted_message = cryptarch.encrypt(message.encode('UTF-8'))
    return encrypted_message

@app.post('/decrypt')
def decrypt():
    message = request.form.get("message")
    decrypted_message = cryptarch.decrypt(message.encode('UTF-8'))
    return decrypted_message
