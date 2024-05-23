
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load the trained model during startup
# model_path = os.path.join(app.static, 'decision_tree_model.joblib')
# model_filename = 'decision_tree_model.joblib'
# model_path = os.path.join('/home/naufalputra/mysite/static/', model_filename)
# model_path = 'decision_tree_model.joblib'
model = joblib.load('decision_tree_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get form data
#         firstMeanEDA = request.form['firstMeanEDA']
#         midMeanEDA = request.form['midMeanEDA']
#         lastMeanEDA = request.form['lastMeanEDA']
#         MeanRR = request.form['MeanRR']
#         MeanHR = request.form['MeanHR']
#         MinHR = request.form['MinHR']
#         MaxHR = request.form['MaxHR']
#         SDNN = request.form['SDNN']
#         RMSSD = request.form['RMSSD']
#         NNx = request.form['NNx']
#         pNNx = request.form['pNNx']
#         PowerVLF = request.form['PowerVLF']
#         PowerLF = request.form['PowerLF']
#         PowerHF = request.form['PowerHF']
#         PowerTotal = request.form['PowerTotal']
#         LFHF = request.form['LF/HF']
#         PeakVLF = request.form['PeakVLF']
#         PeakLF = request.form['PeakLF']
#         PeakHF = request.form['PeakHF']
#         FractionLF = request.form['FractionLF']
#         FractionHF = request.form['FractionHF']

#         # Create a numpy array with the form data
#         input_data = np.array([[
#             float(firstMeanEDA),
#             float(midMeanEDA),
#             float(lastMeanEDA),
#             float(MeanRR),
#             float(MeanHR),
#             float(MinHR),
#             float(MaxHR),
#             float(SDNN),
#             float(RMSSD),
#             float(NNx),
#             float(pNNx),
#             float(PowerVLF),
#             float(PowerLF),
#             float(PowerHF),
#             float(PowerTotal),
#             float(LFHF),
#             float(PeakVLF),
#             float(PeakLF),
#             float(PeakHF),
#             float(FractionLF),
#             float(FractionHF)
#         ]])

#         # Make prediction using the loaded model
#         prediction = model.predict(input_data)

#         # Display the result
#         return render_template('result.html', prediction=prediction)

#     # Render the form template for GET requests
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
