import logging
from flask import Flask, request, jsonify
import os
import opslib

# Set path for the model
cwd = os.path.abspath(os.path.dirname(__file__))
given_path = "models"
model_path = os.path.abspath(os.path.join(cwd, given_path))

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
logger = logging.getLogger(__name__) 

@app.route("/", methods=['GET'])
def home():
    html = "<h3>Model Serving</h3>"
    return html.format(format)

@app.route("/health")
def ialive():
    return jsonify({'status': 'ok'}), 200

@app.route("/predict", methods=['POST'])
def predict():
    request_data = request.get_json()
    instances = request_data["instances"]
    predictions = opslib.predict(instances)
    app.logger.info(f"predictions: {predictions}")
    
    return jsonify({"predictions": predictions})

app.run(host="0.0.0.0")