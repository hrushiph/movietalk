from flask import Flask
application = Flask(__name__)

@application.route('/home')
def home():
    return "<h5>Data Analytics From Group.</h5>"