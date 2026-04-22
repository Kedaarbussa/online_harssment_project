import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# -------------------------------
# Load the trained model + vectorizer
# -------------------------------
with open("cyberbullying_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# -------------------------------
# Define prediction function
# -------------------------------
def predict_cyberbullying(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    return prediction

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Cyberbullying Detector", page_icon="🧠", layout="centered")

st.title("🧠 Cyberbullying Detection App")
st.write("Type any social media comment or message below and see if it’s cyberbullying or not.")

user_input = st.text_area("💬 Enter a comment:", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a comment first.")
    else:
        pred = predict_cyberbullying(user_input)
        if pred == 1:
            st.error("🚨 Cyberbullying detected! 😡")
        else:
            st.success("✅ Not Cyberbullying 🙂")
