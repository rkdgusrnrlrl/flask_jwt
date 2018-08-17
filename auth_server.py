from flask import Flask, jsonify
import jwt
import datetime

app = Flask(__name__)
secret_key = "pycon"

@app.route("/")
def index():
    return "Hello"

@app.route("/get_token")
def get_token():
    # db 작업
    issuer = "token_maker"
    subject ="localhost:5002/v1"
    date_time_obj = datetime.datetime
    exp_time = date_time_obj.timestamp(date_time_obj.utcnow() + datetime.timedelta(hours=24))
    scope = ['v1', 'v2']
    payload = {
        "sub" : subject,
        "iss" : issuer,
        "exp" : int(exp_time),
        "scope" : scope
    }
    token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")

    return jsonify({
        "access_token" : token.decode("utf-8")
    }), 201

@app.route("/admin_login")
def admin_login():
    issuer = "token_maker"
    subject = "localhost:5002/v1"
    date_time_obj = datetime.datetime
    exp_time = date_time_obj.timestamp(date_time_obj.utcnow() + datetime.timedelta(hours=24))
    scope = ['v1', 'v2', "v3"]
    payload = {
        "sub": subject,
        "iss": issuer,
        "exp": int(exp_time),
        "scope": scope
    }
    token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")

    return jsonify({
        "access_token": token.decode("utf-8")
    }), 201


app.run(port=5001)