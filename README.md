## 🩺 Breast Cancer Prediction using Flask API

A simple Flask-based web app to predict whether a breast tumor is malignant or benign using a trained machine learning model based on the Breast Cancer Wisconsin dataset.

### 🚀 Deployment

This application is deployed using **Render**, a cloud platform for hosting web services.

🔗 **Live App:** [https://breast-cancer-predictor-s97m.onrender.com/](https://breast-cancer-predictor-s97m.onrender.com/)


### 🔍 Features

User-friendly web interface

Takes 4 key diagnostic features as input

Predicts tumor as Benign or Malignant

Built with Flask & Scikit-learn

Clean UI with image and styled layout

### ⚙️ How to Run the App

1️⃣ Clone the Repository

`git clone https://github.com/your-username/breast-cancer-predictor.git`

`cd breast-cancer-predictor`

2️⃣ Install Dependencies

`pip install -r requirements.txt`

OR install manually:

`pip install flask scikit-learn`

3️⃣ Train the Model (if not already)

`python model_builder.py`

This will generate model.pkl.

4️⃣ Run the Web App

`python app.py`

Open your browser and visit:
📍 http://127.0.0.1:5000/

### ✍️ Sample Inputs to Try

Feature	Value

Mean Radius	17.99

Mean Texture	10.38

Mean Perimeter	122.8

Mean Area	1001.0

### 🧠 Tech Stack

Python

Flask

scikit-learn

HTML, CSS (custom styling)

### ✅ Future Improvements

Add confidence score for predictions

Upload CSV for batch predictions

Deploy on Render
