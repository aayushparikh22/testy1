from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Aayush Parikh - 1BM20IS004"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
