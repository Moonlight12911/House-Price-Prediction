# 🏠 House Price Prediction using Machine Learning

An interactive Machine Learning web application that predicts residential house prices based on property features using a trained **Linear Regression** model.

---

## 🚀 Live Demo

[![Live Demo](https://img.shields.io/badge/Live-Demo-red?logo=streamlit)](https://house-price-prediction-12911.streamlit.app/)---

## 📖 Project Overview

This project predicts house prices by analysing various property features such as:

- 📐 Area (Square Feet)
- 🛏 Bedrooms
- 🚿 Bathrooms
- 🏢 Number of Stories
- 🚗 Parking Spaces
- 🛣 Main Road Access
- 🛋 Guest Room
- 🏠 Basement
- ♨ Hot Water Heating
- ❄ Air Conditioning
- 📍 Preferred Area
- 🪑 Furnishing Status

The prediction is generated instantly using a Machine Learning model trained on historical housing data.

---

## 📊 Dataset

The project uses a cleaned housing dataset named **Housing_Cleaned.csv** containing information about **530 residential properties**.

The dataset includes:

- Property Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Amenities
- Furnishing Status
- House Price (Target Variable)

During development the dataset was used to train the Machine Learning model.

After training, the model was saved as **model.pkl**.

> **Note:** The CSV file is used only for training and project statistics. During prediction, the application uses the trained model (`model.pkl`) instead of searching the CSV.

---

## 🤖 How Prediction Works

The prediction process follows these steps:

```text
Housing_Cleaned.csv
        │
        ▼
Model Training (Linear Regression)
        │
        ▼
model.pkl
        │
        ▼
Streamlit Application
        │
User enters house details
        │
        ▼
Predicted House Price
```

### Training Phase

- The housing dataset is cleaned and preprocessed.
- Linear Regression learns relationships between house features and their prices.
- The trained model is saved as `model.pkl`.

### Prediction Phase

When a user enters house details:

1. The application collects the property information.
2. The trained model (`model.pkl`) loads into memory.
3. The model calculates the estimated house price based on the learned relationships.
4. The predicted price is displayed instantly.

No retraining is performed during prediction.

---

## ✨ Features

- Machine Learning based house price prediction
- Interactive Streamlit interface
- Real-time prediction
- Clean and simple UI
- Estimated market price range
- Dataset statistics

---

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression

Model Performance:

- R² Score: **0.6609**
- Dataset Size: **530 Houses**
- Features Used: **12**

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Pickle

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── model.pkl
├── Housing_Cleaned.csv
├── requirements.txt
├── README.md
├── .gitignore
├── notebooks/
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move into the project folder:

```bash
cd House-Price-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 📸 Screenshots

_Add screenshots of the application here after deployment._

---

## 👨‍💻 Author

**Mukesh Kumhar**

BCA Student | Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and portfolio purposes.
