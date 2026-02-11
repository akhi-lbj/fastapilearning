
# 🤖 Machine Learning Model Serving with FastAPI & Streamlit

This module demonstrates how to serve a trained Machine Learning model using a FastAPI backend and a user-friendly Streamlit frontend. It specifically focuses on predicting **Insurance Premium Categories** based on user demographics and lifestyle data.

![Streamlit App Screenshot](Serving_MLModels_with_FastAPI/StreamLit_InsurancePremium_App.png)

## 📁 Project Structure (ML Serving)

The components are located in the `Serving_MLModels_with_FastAPI` directory:

- **`main.py`**: The FastAPI backend script. It loads the pickled ML model and provides a prediction endpoint.
- **`frontend.py`**: The Streamlit interface that allows users to input their data and receive predictions in real-time.
- **`model.pkl`**: The pre-trained scikit-learn model (v1.6.1).
- **`fastapi_ml_model.ipynb`**: The Jupyter Notebook used for data exploration, preprocessing, and model training.
- **`insurance.csv`**: The dataset used for training the model.

## 🛠️ Detailed Walkthrough

### 1. The FastAPI Backend (`main.py`)
The backend is responsible for the heavy lifting:
- **Model Loading**: Uses `pickle` to load the trained model into memory at startup.
- **Data Validation**: Uses Pydantic's `BaseModel` to ensure incoming data is formatted correctly.
- **Feature Engineering**: Calculates additional features like `BMI`, `City Tier`, `Age Group`, and `Lifestyle Risk` on-the-fly using `@computed_field`.
- **Prediction**: Converts validated data into a Pandas DataFrame and passes it to the model to get the premium category.

### 2. The Streamlit Frontend (`frontend.py`)
Streamlit provides a sleek UI for user interaction:
- **Input Widgets**: Uses `st.number_input`, `st.selectbox`, and `st.text_input` for intuitive data entry.
- **API Communication**: Uses the `requests` library to send a POST request to the FastAPI `/predict` endpoint.
- **Result Display**: Shows the predicted category (Low, Medium, or High) in a success banner if the API call is successful.

### 3. Model Compatibility
- **Scikit-Learn Versioning**: This project specifically uses `scikit-learn==1.6.1` to maintain compatibility with the pickled model file, avoiding common serialization errors.

## 🚀 How to Run

To run this specific module, follow these steps:

### 1. Install ML Dependencies
```bash
pip install pandas scikit-learn==1.6.1 streamlit requests
```

### 2. Start the FastAPI Server
Open a terminal and run:
```bash
uvicorn Serving_MLModels_with_FastAPI.main:app --reload
```

### 3. Start the Streamlit App
Open a **new** terminal and run:
```bash
streamlit run Serving_MLModels_with_FastAPI.frontend.py
```

Now, navigate to the URL provided by Streamlit (usually `http://localhost:8501`) to interact with the Insurance Premium Predictor!

