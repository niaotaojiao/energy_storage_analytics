from pickle import load
import os
import logging

from darts.models import TCNModel

logging.basicConfig(level=logging.INFO)
cwd = os.path.abspath(os.path.dirname(__file__))

def load_model():
    given_path = "models"
    model_path = os.path.abspath(os.path.join(cwd, given_path))
    
    '''model = joblib.load(os.path.abspath(
        os.path.join(model_path,
                     'housing_price_model.joblib')))'''

    model = TCNModel.load(os.path.abspath(
        os.path.join(model_path,
                     'tcn_4k7y_0310.pt')))
    
    scaler = load(open(os.path.abspath(
        os.path.join(model_path, 'scaler.pkl')), 'rb'))

    
    return model, scaler

def formatting(prediction, scaler):
    """Round the prediction to the nearest integer."""
    predictions_inverse = scaler.inverse_transform(prediction)
    pred = predictions_inverse.values()
    return pred[:, 0].tolist()

def predict(instances):
    """Make predictions for a list of instances"""    
    model , scaler= load_model()    
    prediction = model.predict(n=instances)
    prediction = formatting(prediction, scaler)
        
    return prediction