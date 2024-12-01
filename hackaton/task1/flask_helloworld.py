from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"




app.run(debug=False, port=8000, host='0.0.0.0')