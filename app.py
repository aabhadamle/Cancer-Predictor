from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['radius']),
            float(request.form['texture']),
            float(request.form['perimeter']),
            float(request.form['area'])
        ]
        prediction = model.predict([features])[0]
        result = "Malignant" if prediction == 0 else "Benign"
        return render_template("index.html", prediction_text=f"Prediction: {result}")
    except:
        return render_template("index.html", prediction_text="Please enter valid numeric values.")

if __name__ == "__main__":
    app.run(debug=True)
