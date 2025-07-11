from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/credit_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['age'], data['income'], data['loanAmount']]).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    return jsonify({'default': prediction})

if __name__ == '__main__':
    app.run(port=5000)
