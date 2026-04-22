# Cyberbullying Detector

This is a small Streamlit app that loads a pretrained scikit-learn model and TF-IDF vectorizer and predicts whether a comment is cyberbullying.

Quick start (Windows PowerShell):

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

Notes:
- The project expects `cyberbullying_model.pkl` and `tfidf_vectorizer.pkl` to be present in the project root (they are in this repo).
- If your PowerShell execution policy prevents activation, run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` (requires admin rights).
- If you want me to try running the install + start the app now from this environment, tell me and I'll run the commands for you.
