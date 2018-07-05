from flask import Flask
from http import HTTPStatus


app = Flask(__name__)


@app.route("/<string:num1>/<string:num2>")
def hello_world(num1, num2):
    try:
        return f"{int(num1) * int(num2)}", HTTPStatus.OK
    except:
        return "only int is accepted", HTTPStatus.BAD_REQUEST

app.run(host="localhost")
