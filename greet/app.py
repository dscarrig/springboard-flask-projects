from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome_response():
    return "welcome"

@app.route("/welcome/back")
def welcome_back_response():
    return "welcome back"

@app.route("/welcome/home")
def welcome_home_response():
    return "welcome home"