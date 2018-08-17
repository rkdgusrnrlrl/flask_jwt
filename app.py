import jwt
payload = {
    "msg" : "Hello World"
}
secret_key = "pycon"
al = "HS256"
token = jwt.encode(payload=payload, key=secret_key, algorithm=al)
print(token)

raw = jwt.decode(token, key=secret_key, algorithms=[al])
print(raw)