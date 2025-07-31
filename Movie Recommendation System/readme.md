# 🎬 Movie Recommendation System with Feedback Integration
<img width="1710" height="928" alt="Screenshot 2025-07-31 at 12 11 44 PM" src="https://github.com/user-attachments/assets/af6bcd28-e5c8-4f51-9dde-f0b506e55850" />

An AI-powered, content-based movie recommendation application developed using Python and Streamlit. This system enables users to receive personalized movie suggestions and submit feedback via an intuitive web interface.

---

## 📌 Project Overview

This application analyzes metadata from the TMDB 5000 dataset to generate accurate movie recommendations based on content similarity. In addition, it incorporates a feedback form to gather user insights, enhancing the system’s usability and future development.

---

## 🚀 Key Features

### 🔍 Intelligent Recommendations
- Suggests top 15 similar movies based on a selected title.
- Uses cosine similarity on processed textual features (genres, cast, director, keywords).
- Displays movie posters, genres, cast, and director information.

### 📝 Feedback Collection
- Allows users to submit their name, email, and feedback.
- Includes input validation for correct email formatting.
- Saves responses to an Excel file (`feedback.xlsx`) for future analysis.

---
### 🎥 Movie Recommender Interface
<img width="1708" height="451" alt="Screenshot 2025-07-31 at 12 13 26 PM" src="https://github.com/user-attachments/assets/2a3d5dcb-4811-40b4-ba4f-0a19343e10fe" />

### 🎥  Movie Recommendation 
<img width="635" height="877" alt="Screenshot 2025-07-31 at 12 18 00 PM" src="https://github.com/user-attachments/assets/3048e34c-2bbe-478d-8888-d85e2d6c11ad" />

### ✍️ Feedback Form (Successful Submission)
<img width="1706" height="940" alt="Screenshot 2025-07-31 at 12 00 55 PM" src="https://github.com/user-attachments/assets/dc32dc6a-8d9e-46c9-a04c-68d91cc3a828" />




---

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **Data Handling**: `pandas`, `numpy`, `openpyxl`
- **Modeling**: Cosine similarity (via `scikit-learn`)
- **Persistence**: `pickle` for model objects, `.xlsx` for feedback data

---                                                                                                                                            



├── app.py / Untitled1.ipynb # Main application logic
├── feedback.xlsx # Collected user feedback
├── movies.pkl # Processed movie metadata
├── movie_dict.pkl # Dictionary of movie titles and IDs
├── similarity.pkl # Precomputed similarity matrix
├── tmdb_5000_movies.csv # Raw movie metadata
├── tmdb_5000_credits.csv # Raw cast/crew metadata
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
└── screenshots/ # UI preview images



---
# ⚙️ Installation & Setup

## 1. Install Dependencies
   Run the following command to install all required Python packages:
   pip install -r requirements.txt

## 2. Launch the Application
   Start the Streamlit app using:
   streamlit run app.py

   Note: If you're working with the notebook version, open Untitled1.ipynb in Jupyter Notebook or convert it to a Python script for       production use.

## 📊 Dataset
   Source: TMDB 5000 Movie Dataset

## Files Used:
   tmdb_5000_movies.csv
   tmdb_5000_credits.csv

## 🧠 Recommendation Logic

The recommendation engine follows these steps:

Data Preprocessing: Load and merge movie and credit metadata.

Feature Extraction: Collect keywords, genres, cast, and director details.

Text Vectorization: Convert combined metadata into numeric vectors.

Similarity Calculation: Compute cosine similarity across all movie vectors.

Recommendation Output: Display the top similar movies to the user.

## ✅ Future Enhancements

🎞️ Integrate live poster and metadata using the TMDB API.

📧 Store feedback securely in Google Sheets, Firebase, or a SQL database.

🧪 Enhance recommendation accuracy with advanced NLP models (e.g., TF-IDF, BERT).

🌐 Deploy on platforms like Streamlit Cloud or Hugging Face Spaces for global access.


