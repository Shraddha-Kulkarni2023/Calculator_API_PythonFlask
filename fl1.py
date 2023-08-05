from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
   return "Hi"

@app.route("/add/<int:a>/<int:b>",methods=['GET'])
def add1(a,b):
    return jsonify(a + b)

@app.route("/sub/<int:a>/<int:b>",methods=['GET'])
def sub1(a,b):
    return jsonify(a - b)

@app.route("/mult/<int:a>/<int:b>",methods=['GET'])
def mult1(a,b):
    return jsonify(a * b)

@app.route("/div/<int:a>/<int:b>",methods=['GET'])
def div1(a,b):
    return jsonify(a/b)


if __name__ == "__main__":
    app.run(debug = True)
