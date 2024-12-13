from flask import Flask, jsonify
from google.cloud import aiplatform

app = Flask(__name__)

# Vertex AI Endpoint Details
project_id = "867477975417"
location = "asia-east1"
endpoint_id = "3843175769123586048"

# Initialize the PredictionServiceClient
client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

endpoint_name = f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Prepare the request payload
        instances = [
            {'timestamp': 15000}
        ]

        # Make the prediction request
        response = client.predict(endpoint=endpoint_name, instances=instances, timeout=500)

        # Format the response
        predictions = response.predictions
        predictions = [pred / 10 for pred in response.predictions]
        
        # make X-axis
        total_hours_in_month = 720
        m_values = [i / total_hours_in_month for i in range(len(predictions))]

        # Combine M values (X-axis) and predictions (Y-axis) into a series
        series = [{"Month": round(m_values[i], 4), "SOH (%)": predictions[i]} for i in range(len(predictions))]

        # Return the structured data
        return jsonify({'status': 'success', 'data': series})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
