from google.cloud import aiplatform

project_id = "867477975417"
location = "asia-east1"
endpoint_id = "3843175769123586048"

client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

endpoint_name = f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

instances = [
    {'prompt': 'What is Artificial Intelligence?'}
]

response = client.predict(endpoint=endpoint_name, instances=instances, timeout=500)
print(response)