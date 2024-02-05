'''
@dev This file is same as app.py but used for deployment only
'''
import pickle
import numpy as np
import pandas as pd

from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging

application = Flask(__name__)
app = application
# Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    '''
    @dev This function handles the prediction for input data
    '''
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        
        logging.info("Received data from web page")
        pred_data_frame = data.get_data_as_data_frame()
        logging.info("Input data is converted to dataframe")        
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_data_frame)

        logging.info("Publishing result")
        return render_template('home.html', results = results[0])

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)
