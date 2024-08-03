import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the data
vi_data_df = pd.read_csv("./vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

def corr_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    
    # Calculate correlation
    query_array = query_embedded.toarray().flatten()
    context_array = context_embedded.toarray()
    
    # Calculate correlation coefficients manually
    corr_scores = []
    for doc_vector in context_array:
        correlation = np.corrcoef(query_array, doc_vector)[0, 1]
        corr_scores.append(correlation)
    
    corr_scores = np.array(corr_scores)
    
    # Get top k correlation score and index its
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results

# Use the first question as an example
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
correlation_score = results[1]['corr_score']

print(f"Correlation score: {correlation_score:.2f}")

# Check which option matches the result
options = [0.20, 0.21, 0.22, 0.23]
closest_option = min(options, key=lambda x: abs(x - correlation_score))
print(f"Closest option: {closest_option:.2f}")

# Answer: B