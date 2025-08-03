# 🧠 NSAP AI Eligibility Prediction System

This project uses machine learning and IBM Cloud Watsonx.ai to predict the most suitable National Social Assistance Programme (NSAP) scheme for a citizen, based on demographic data. It aims to support researchers, government officials, and citizens in identifying benefit eligibility more efficiently.

---

## 🚀 Project Overview

- **Problem**: Manual NSAP scheme matching is time-consuming and error-prone
- **Solution**: An AI-powered ML model that automates eligibility prediction
- **Tools**: IBM Cloud, Watsonx.ai Studio, Random Forest Classifier, Python
- **Data**: District-wise NSAP beneficiary data from government open datasets

---

## 🛠️ Technologies Used

- IBM Watsonx.ai Studio
- IBM Watsonx AI Runtime
- IBM Cloud Object Storage
- IBM Granite Foundation Model
- Python, Pandas, Scikit-learn, Matplotlib

---

## 📊 Features

- Predicts NSAP scheme eligibility from input data
- Automates scheme selection based on demographic features
- Provides model evaluation metrics (accuracy, confusion matrix, feature importance)
- Fully deployed using IBM Cloud

---

## 👨‍💻 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/nsap-ai-project.git
   cd nsap-ai-project
2. Install dependencies:
   pip install -r requirements.txt

3. Run the notebook in IBM Watsonx.ai (recommended)

4.Or test API with:
  import requests

# Add your deployment API details here
📈 Model Performance
Accuracy: ~88%
Model: Random Forest Classifier
Input Features: Gender-wise count, caste group, Aadhaar, mobile availability, etc.

🧠 Future Scope
Chatbot integration using Watsonx Assistant
Multi-language and state-wise model versions
Mobile app for field-level beneficiary prediction

📜 IBM Credentials
IBM Cloud Account: Active
IBM Services Used: Watsonx Studio, Watsonx Runtime, Granite, COS

Output:
<img width="1582" height="398" alt="Screenshot 2025-08-04 at 2 26 39 AM" src="https://github.com/user-attachments/assets/ed43da6e-2b6a-40bf-8283-5c7d263aebd3" />

<img width="1116" height="597" alt="Screenshot 2025-08-04 at 2 06 20 AM" src="https://github.com/user-attachments/assets/589d3a11-1166-4fd9-bbcb-5e9b79e9cd7f" />

