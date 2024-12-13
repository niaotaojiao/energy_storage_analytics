import requests
import json

def test_prediction():
    # API endpoint
    url = 'http://localhost:8080/predict'
    
    # 測試數據
    test_data = {
        'series': [1.0, 2.0, 3.0, 4.0, 5.0],
        'horizon': 3
    }
    
    # 發送請求
    try:
        response = requests.post(
            url,
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        # 印出結果
        print('Response:', json.dumps(response.json(), indent=2))
        
    except requests.exceptions.RequestException as e:
        print('Error:', str(e))

if __name__ == '__main__':
    test_prediction()