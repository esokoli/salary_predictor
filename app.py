from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
import os
from joblib import load

app = Flask(__name__)

model = load("SalaryModel.pkl")

@app.post('/prediction')
def makecalc():
    data = request.get_json()
    prediction = model.predict([[data]])
    prediction = prediction.tolist()
    return f'With {data} years of experience, our model predicts you earn {"${:,.2f}".format(round(prediction[0]))} a year.'


if __name__ == '__main__':
   app.run(host='0.0.0.0')