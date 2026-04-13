# 🚦 Smart Traffic Congestion Detection System

## 📌 Project Overview
This project presents an AI-based smart traffic system that detects vehicles using a trained YOLOv8 model and estimates congestion levels using a weighted density-based approach. Based on congestion, it dynamically simulates traffic signal control with timing.

---

##  Features

* Vehicle detection using YOLOv8
* Congestion estimation (Low / Medium / High)
* Smart traffic signal (Green / Yellow / Red)
* Real-time image-based analysis via Streamlit interface

---

## Project Structure

smart_traffic_system/
│
├── model/
│   └── best.pt
├── app.py
├── utils.py
├── requirements.txt
└── README.md

## ⚙️ How to Run the Project

### Step 1: Clone Repository

```
git clone <repo-link>
cd smart_traffic_system


### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Add Model

Place your trained model file:
model/best.pt

### Step 4: Run Application
streamlit run app.py
---


