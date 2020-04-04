from flask import Flask
from utils import (add, multiply)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/math/<int:num1>/<int:num2>", methods=['GET'])
def mathApi(num1, num2):
    addResult = add(num1, num2)
    multiplyResult = multiply(num1, num2)
    return {
        "add": addResult,
        "mutiply": multiplyResult
    }, 200

if __name__ == "__main__":
    app.run()
