# 🏥 Disease Prediction System  

This is a **Streamlit web application** that predicts diseases based on user symptoms.  
It also provides **guidelines** such as precautions, specialists, hospital requirements, diet, exercise, and medicines in **both English and Hindi**, powered by **Google Gemini AI**.  

---

## 🚀 Features  
- ✅ User can select symptoms via checkboxes.  
- ✅ Predicts the most probable disease.  
- ✅ Provides a **treatment guide** (precautions, medicines, etc.) using Gemini AI.  
- ✅ Outputs results in **English & Hindi** for both villagers and city users.  
- ✅ Easy-to-use **web interface** with Streamlit.  

---

## 🛠️ Tech Stack  
- **Python 3.13**  
- **Streamlit** – for the user interface  
- **Scikit-learn** – for training ML model  
- **Pickle** – for saving & loading trained model  
- **Google Gemini AI API** – for medical advice generation  

---

## 📂 Project Structure  
Hospital/
│-- medical.py # Main Streamlit app
│-- model.pkl # Trained ML model
│-- training_data.csv # Dataset
│-- requirements.txt # Python dependencies
│-- README.md # Project documentation

---

## ⚙️ Installation & Setup  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Kuwarjibetha/Hospital.git
   cd Hospital


2. Create virtual environment (recommended):
     python3 -m venv .venv
     source .venv/bin/activate   # Mac/Linux
     .venv\Scripts\activate      # Windows

3. Install dependencies:
     pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run medical.py

##🎯 How to Use
#Select symptoms by ticking checkboxes.
   Click on Predict to get the disease name.
   Get a short guideline (English & Hindi) with precautions, medicines, diet, etc.
