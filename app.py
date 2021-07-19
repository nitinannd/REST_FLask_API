from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is first flask API"

app.run(port=5000)