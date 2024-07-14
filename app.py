from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained models from pickle files
with open('knn_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('logistic_model.pkl', 'rb') as f:
    logistic_model = pickle.load(f)

with open('naive_bayes_model.pkl', 'rb') as f:
    naive_bayes_model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.get_json()['email']
    vectorizer = TfidfVectorizer()
    email_tfidf = vectorizer.transform([email])
    
    knn_pred = knn_model.predict(email_tfidf)
    logistic_pred = logistic_model.predict(email_tfidf)
    naive_bayes_pred = naive_bayes_model.predict(email_tfidf)
    
    return jsonify({'knn': knn_pred[0], 'logistic': logistic_pred[0], 'naive_bayes': naive_bayes_pred[0]})

if __name__ == '__main__':
    app.run(debug=True)