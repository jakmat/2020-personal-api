from flask import Flask, request, jsonify
from main import perform_observation
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test')
def test_api():
    return jsonify(data="This is a test")

@app.route('/celestial-objects', methods=['POST'])
def planets_all():
    object = request.args.get('object')
    timestamp = request.args.get('timestamp')
    # observable = perform_observation(object, timestamp)
    # observation = jsonify(observable)
    # print(observation)
    return observation
    observation=[object, timestamp]
    return jsonify(data=observation)

if __name__ == "__main__":
    app.run()
