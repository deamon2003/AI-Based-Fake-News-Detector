from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load datasets
def load_datasets():
    datasets = []
    files = ['dataset/fake_or_real_news.csv', 'dataset/fake_news_dataset.csv', 'dataset/Fake.csv', 'dataset/True.csv']
    for file in files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            datasets.append(df)
    return datasets

# Preprocess and combine datasets
def preprocess_data(datasets):
    combined_data = []
    for df in datasets:
        if 'title' in df.columns and 'text' in df.columns and 'label' in df.columns:
            df['combined'] = df['title'] + ' ' + df['text']
            combined_data.append(df[['combined', 'label']])
        elif 'text' in df.columns and 'label' in df.columns:
            combined_data.append(df[['text', 'label']].rename(columns={'text': 'combined'}))
    if combined_data:
        full_df = pd.concat(combined_data, ignore_index=True)
        full_df['label'] = full_df['label'].str.lower().map({'fake': 0, 'real': 1, 'true': 1, 'false': 0})
        full_df = full_df.dropna()
        return full_df
    return pd.DataFrame()

# Train model
def train_model():
    datasets = load_datasets()
    data = preprocess_data(datasets)
    if data.empty:
        print("No data loaded")
        return None, None

    X = data['combined']
    y = data['label']

    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X_tfidf = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy}")

    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    return model, vectorizer

# Load model if exists, else train
if os.path.exists('model.pkl') and os.path.exists('vectorizer.pkl'):
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    # Load dataset texts for validation
    datasets = load_datasets()
    data = preprocess_data(datasets)
    dataset_texts = set()
    for df in datasets:
        if 'text' in df.columns:
            dataset_texts.update(df['text'].str.lower().str.strip())
else:
    model, vectorizer = train_model()
    # After training, load dataset texts
    datasets = load_datasets()
    data = preprocess_data(datasets)
    dataset_texts = set()
    for df in datasets:
        if 'text' in df.columns:
            dataset_texts.update(df['text'].str.lower().str.strip())

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Check if the input text is in the dataset
    input_text_lower = text.lower().strip()
    if input_text_lower not in dataset_texts:
        return jsonify({
            'prediction': 'Unrecorded',
            'confidence': 0.0,
            'probabilities': {'fake': 0.0, 'real': 0.0}
        })

    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)[0]
    probability = model.predict_proba(text_tfidf)[0]

    result = {
        'prediction': 'real' if prediction == 1 else 'fake',
        'confidence': float(max(probability)),
        'probabilities': {'fake': float(probability[0]), 'real': float(probability[1])}
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
