from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import sklearn
import pickle

# Creating flask app
app = Flask(__name__)

# --- MODEL LOADING ---
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=['POST'])
def predict():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorous'])
    k = int(request.form['Potassium'])
    temperature = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    features_list = [N, P, k, temperature, humidity, ph, rainfall]
    single_pred = np.array(features_list).reshape(1, -1)
    single_pred_scaled = scaler.transform(single_pred)
    prediction = model.predict(single_pred_scaled)

    crop_dict = {1:"rice", 2:"maize", 3:"chickpea", 4:"kidneybeans", 5:"pigeonpeas", 6:"mothbeans", 7:"mungbean", 8:"blackgram", 9:"lentil", 10:"pomegranate", 11:"banana", 12:"mango", 13:"grapes", 14:"watermelon", 15:"muskmelon", 16:"apple", 17:"orange", 18:"papaya", 19:"coconut", 20:"cotton", 21:"jute", 22:"coffee"}
    
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is a best crop to be cultivated".format(crop)
    else:
        result = "Sorry, not able to recommend a proper crop for this environment"

    return render_template('index.html', result=result)

# Python main
if __name__ == "__main__":
    app.run(debug=True)