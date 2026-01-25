# 🌱 SMART SEED QUALITY PREDICTION SYSTEM

A Machine Learning based web application that predicts **seed quality (Good / Bad)** using **physical and biological features**, built with **Random Forest Classifier** and deployed using **Streamlit**.

---

## 📌 Project Overview

Seed quality plays a vital role in agricultural productivity. Traditional seed testing methods are **time-consuming, costly, and labor-intensive**.

This project provides a **smart, fast, and automated solution** for predicting seed quality using **Machine Learning**, helping **farmers, seed industries, and agricultural researchers** make faster and more accurate decisions.

The system analyzes seed features like moisture, germination rate, purity, vigor index, fungal infestation, and more to classify seeds as **Good or Bad** with **high accuracy (~99%)**.

---

## 🚀 Key Features

- ✅ Machine Learning based prediction  
- 🌳 Random Forest Classifier  
- 📊 Feature Importance & Explainability  
- 🌐 Interactive Web UI using Streamlit  
- 📁 CSV Batch Prediction Support  
- 📈 Visualization of Results  
- ⚡ Fast & Accurate Prediction  

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Model Saving:** Joblib  
- **Web Framework:** Streamlit  
- **Visualization:** Matplotlib, Plotly  
- **Environment:** Anaconda (Conda)

---

## 📂 Project Structure

# 🌱 SMART SEED QUALITY PREDICTION SYSTEM

A Machine Learning based web application that predicts **seed quality (Good / Bad)** using **physical and biological features**, built with **Random Forest Classifier** and deployed using **Streamlit**.

---

## 📌 Project Overview

Seed quality plays a vital role in agricultural productivity. Traditional seed testing methods are **time-consuming, costly, and labor-intensive**.

This project provides a **smart, fast, and automated solution** for predicting seed quality using **Machine Learning**, helping **farmers, seed industries, and agricultural researchers** make faster and more accurate decisions.

The system analyzes seed features like moisture, germination rate, purity, vigor index, fungal infestation, and more to classify seeds as **Good or Bad** with **high accuracy (~99%)**.

---

## 🚀 Key Features

- ✅ Machine Learning based prediction  
- 🌳 Random Forest Classifier  
- 📊 Feature Importance & Explainability  
- 🌐 Interactive Web UI using Streamlit  
- 📁 CSV Batch Prediction Support  
- 📈 Visualization of Results  
- ⚡ Fast & Accurate Prediction  

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Model Saving:** Joblib  
- **Web Framework:** Streamlit  
- **Visualization:** Matplotlib, Plotly  
- **Environment:** Anaconda (Conda)

---

## 📂 Project Structure

smart_seed_quality_pridiction_system/
│
├── data/ # Dataset CSV files
├── src/ # Training scripts
├── app/ # Streamlit web app
├── models/ # Saved ML model (pipeline.pkl)
├── images/ # Diagrams and screenshots
├── requirements.txt # Required libraries
└── README.md # Project documentation

---

## 📊 Dataset Features

| Feature | Description |
|----------|--------------|
| Moisture (%) | Water content in seed |
| Germination (%) | Germination rate |
| Purity (%) | Seed purity |
| Vigor Index | Seed strength |
| Fungal Infestation (%) | Fungus infection |
| Discoloration (%) | Color change |
| Protein Content (%) | Protein percentage |
| Oil Content (%) | Oil percentage |
| Seed Age (days) | Age of seed |
| Seed Length (mm) | Physical length |
| Seed Width (mm) | Physical width |

**Target Variable:** `Quality → Good / Bad`

---

## 🤖 Machine Learning Model

- **Algorithm Used:** Random Forest Classifier  

### Why Random Forest?
- High Accuracy  
- Handles multiple features efficiently  
- Reduces overfitting  
- Provides feature importance (explainability)

---

## 📈 Model Performance

- **Accuracy:** ~99%  
- **Precision:** High  
- **Recall:** High  
- **F1-score:** High  

Evaluation Metrics Used:
- Confusion Matrix  
- Classification Report  
- ROC-AUC  

---

## 🌐 Streamlit Web Application

The web interface allows users to:

- 📥 Enter seed parameters  
- 🔘 Click predict button  
- 📊 View prediction result (Good / Bad)  
- 🧠 See explanation using feature importance  
- 📁 Upload CSV file for batch prediction  

---

## ▶️ How To Run This Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/VKittu/smart_seed_quality_pridiction_system.git
cd smart_seed_quality_pridiction_system

