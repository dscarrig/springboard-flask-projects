from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_request():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(add(a, b))

@app.route("/sub")
def sub_request():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a, b))

@app.route("/mult")
def mult_request():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a, b))

@app.route("/div")
def div_request():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a, b))

@app.route("/math/<operator>")
def math_request(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    if operator == "add":
        return str(add(a, b))

    if operator == "sub":
        return str(sub(a, b))

    if operator == "mult":
        return str(mult(a, b))

    if operator == "div":
        return str(div(a, b))

    return "Not an operator"

