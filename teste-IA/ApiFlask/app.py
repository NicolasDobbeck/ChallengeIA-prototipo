from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import re
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

df = pd.read_csv('BIKE DETAILS.csv')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

df['processed_name'] = df['name'].apply(preprocess_text)

tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')

def get_similar_bikes(bike_name, df=df, vectorizer=None):
    if vectorizer is None:
        vectorizer = TfidfVectorizer(ngram_range=(1, 2)) # Incluímos uni-gramas e bi-gramas
        vectorizer.fit(df['processed_name']) # Ajustamos o vetorizador com todos os nomes

    processed_name = preprocess_text(bike_name)

    input_vector = vectorizer.transform([processed_name])
    all_vectors = vectorizer.transform(df['processed_name'].tolist())

    cosine_sim_scores = cosine_similarity(input_vector, all_vectors)[0]
    similar_bikes_with_scores = sorted(enumerate(cosine_sim_scores), key=lambda x: x[1], reverse=True)

    similar_bikes = []
    seen_bikes = set()
    for i, score in similar_bikes_with_scores:
        name = df['name'].iloc[i]
        if name not in seen_bikes and score > 0:
            similar_bikes.append(name)
            seen_bikes.add(name)
            if len(similar_bikes) >= 10:
                break

    return similar_bikes

@app.route('/similar_bikes', methods=['POST'])
def similar_bikes_endpoint():
    data = request.get_json()
    if not data or 'bike_name' not in data:
        return jsonify({'error': 'Por favor, forneça o nome da moto no formato JSON: {"bike_name": "nome da moto"}'}), 400

    bike_name = data['bike_name']
    similar_bikes = get_similar_bikes(bike_name)
    return jsonify({'similar_bikes': similar_bikes})

if __name__ == '__main__':
    app.run(debug=True)