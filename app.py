#Application config file
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved model
with open('sales_forecast_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict_sales():
    """
    Expects JSON input with all feature values.
    Example:
    {
      "Store_id": 1,
      "Store_Type": 0,
      "Location_Type": 2,
      "Region_Code": 1,
      "Holiday": 0,
      "Discount": 1,
      "#Order": 25,
      "year": 2019,
      "month": 5,
      "day_of_week": 2,
      "is_weekend": 0,
      "lag_1": 5000,
      "lag_7": 4800,
      "rolling_mean_7": 5150,
      "rolling_std_7": 320
    }
    """
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'predicted_sales': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
