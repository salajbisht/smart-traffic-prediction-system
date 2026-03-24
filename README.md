# 🚦 Smart Traffic Prediction System

A machine learning-based system that predicts traffic congestion and visualizes it using an interactive dashboard with graphs and maps.

---

## 📌 Overview

Traffic congestion is a major issue in urban areas.
This project uses **Machine Learning** to predict traffic volume based on historical data and displays insights through a **Streamlit dashboard**.

---

## ✨ Features

* 📈 24-hour traffic prediction graph
* 🗺 Traffic congestion heatmap
* 🎛 Interactive user inputs (day, month, temperature)
* 🤖 Machine learning-based predictions

---

## 🧠 Machine Learning Model

* Model Used: **Random Forest Regressor**
* Features:

  * Hour of the day
  * Day of the week
  * Month
  * Temperature

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Folium
* Matplotlib

---

## 📂 Project Structure

```
smart-traffic-prediction-system
│
├── dashboard/
│   └── app.py
│
├── src/
│   └── train_model.py
│
├── data/
│   └── traffic.csv
│
├── models/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/salajbisht/smart-traffic-prediction-system.git
cd smart-traffic-prediction-system
```

---

### 2. Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Train the model

```
python src/train_model.py
```

This will generate:

```
models/traffic_model.pkl
```

---

### 5. Run the dashboard

```
streamlit run dashboard/app.py
```

---

### 6. Open in browser

```
http://localhost:8501
```

---

## 📊 Dashboard Preview

*(Add screenshots here for better presentation)*

Example:

```
![Dashboard](images/dashboard.png)
```

---

## 🚀 Future Improvements

* Real-time traffic data integration
* Route optimization system
* Deep learning models (LSTM)
* Deployment on cloud

---

## 👨‍💻 Author

**Salaj Bisht**
GitHub: https://github.com/salajbisht

---

## ⭐ How to Use

1. Install dependencies
2. Train the model
3. Run the Streamlit app
4. Explore predictions and heatmap

---

## ⚠️ Note

The trained model file (`.pkl`) is not included in the repository due to size limits.
Run `train_model.py` to generate it locally.
