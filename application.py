from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return "<h5>Data Analytics From Group Wizards at Work...</h5>"