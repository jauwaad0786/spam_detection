# 📧 Spam Detection System

A machine learning-based web app that detects whether a given message is **Spam** or **Not Spam**. The app is built using Python, trained with two models (Naive Bayes and Logistic Regression), and deployed with **Streamlit**.

## 🚀 Features

- 📝 Input any text message
- 🔍 Predicts if it's **Spam** or **Ham**
- ⚖️ Uses Logistic Regression and Naive Bayes models
- 📊 Trained on a labeled SMS dataset
- 🖥️ Interactive Streamlit UI

## 🧠 Models Used

- Logistic Regression (`logistic_model.pkl`)
- Naive Bayes (`naive_bayes_model.pkl`)

## 🧪 Technologies

- Python
- scikit-learn
- pandas, numpy
- Streamlit
- pickle

## 📁 Project Structure

```
spam_detection/
├── app.py # Streamlit frontend
├── spam.ipynb # Jupyter notebook with model training
├── logistic_model.pkl # Trained Logistic Regression model
├── naive_bayes_model.pkl # Trained Naive Bayes model
├── dataset link # Dataset reference
└── README.md
```

## 📂 Dataset Used

The dataset used for this project contains SMS messages labeled as "spam" or "ham".  
🔗 [Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

## ▶️ How to Run the App

1. **Clone the repo:**
```bash
git clone https://github.com/jauwaad0786/spam_detection.git
cd spam_detection
## 2.Install dependencies:
pip install -r requirements.txt

### 3.Run the app:
streamlit run app.py

Output Example
Input: Congratulations! You've won a $1000 Walmart gift card. Click here to claim.
✅ Prediction: Spam

Input: Let's meet at 6 PM today.
✅ Prediction: Ham

👨‍💻 Author
Jauwaad Bin Irshad
📧 jauwaad0786@gmail.com
🔗 GitHub Profile

🛠️ Future Improvements
Add more ML models like SVM, XGBoost

Improve UI/UX

Add confusion matrix & evaluation reports

📄 License
This project is open-source and available for educational use.

