from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def dummy_api():
    return jsonify(data="This is a dummy API!")

if __name__ == "__main__":
    app.run()