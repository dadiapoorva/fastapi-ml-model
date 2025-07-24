import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="PASS/FAIL Predictor")

# Title and description
st.title("Student PASS/FAIL Predictor")
st.write("Enter the marks for 3 subjects to predict whether the student will pass or fail.")

# Input fields
mark1 = st.number_input("Subject 1 marks", min_value=0, max_value=100, value=50)
mark2 = st.number_input("Subject 2 marks", min_value=0, max_value=100, value=50)
mark3 = st.number_input("Subject 3 marks", min_value=0, max_value=100, value=50)

# Collect features
features = [mark1, mark2, mark3]

# Prediction logic
if st.button("Predict Result"):
    try:
        response = requests.post(
           "https://fastapi-ml-model-gu9t.onrender.com",
            json={"features": features}
        )
        if response.status_code == 200:
            result = response.json().get("prediction")
            if result == 1:
                st.success("✅ The student is predicted to *Pass*.")
            elif result == 0:
                st.error("❌ The student is predicted to *Fail*.")
            else:
                st.warning("⚠ Unexpected prediction value.")
        else:
            st.warning(f"⚠ Unexpected response from server (status code {response.status_code}).")
    except Exception as e:
        st.error(f"🚫 Error: {e}")