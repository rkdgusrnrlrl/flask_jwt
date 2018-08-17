from flask import Flask, jsonify, abort, request
import requests
import jwt
from functools import wraps

app = Flask(__name__)
secret_key = "pycon"

def jwt_token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not "Authorization" in request.headers:
            return jsonify({
                "msg" : "token is not given"
            }), 400

        token = request.headers["Authorization"]
        try:
            decode_token = jwt.decode(token, secret_key, algorithms="HS256")
            kwargs['decode_token'] = decode_token
        except:
            return jsonify({
                "msg" : "Invalid token given"
            }), 400


        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return "Hello"


@app.route("/login")
def login():
    response = requests.get("http://localhost:5001/get_token")
    json_dict = response.json()

    return json_dict["access_token"]


@app.route("/protected_service")
@jwt_token_required
def protected_service(**kwargs):

    return jsonify({
        "msg" : "jwt work well"
    })

@app.route("/v3/other_service")
@jwt_token_required
def other_scope_service(**kwargs):

    token = kwargs["decode_token"]
    if not "v3" in token["scope"]:
        return jsonify({
            "msg" : "you are not authorize"
        }), 401

    return jsonify({
        "msg" : "jwt work well"
    })


app.run()