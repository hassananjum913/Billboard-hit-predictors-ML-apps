# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:33:07 2021

@author: Anjum
"""

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
file = './Model/ML_Model1.pkl'
model = pickle.load(open(file, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    # final_features = [np.array(float_features)]
    prediction = model.predict([float_features])

    if prediction == 0:
        output1 = 'Not Hit'
        return render_template('index.html', prediction_text1='It is  {}'.format(output1))
    else:
        output2 = 'Hit'
        return render_template('index.html', prediction_text2='It is  {}'.format(output2))

    



if __name__ == "__main__":
    app.run(debug=True)