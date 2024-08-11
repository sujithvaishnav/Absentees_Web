from flask import Flask, request, send_from_directory, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('','index.html')

@app.route('/about')
def about():
    return send_from_directory('','about.html')

@app.route('/contact')
def contact():
    return send_from_directory('','contact.html')

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
