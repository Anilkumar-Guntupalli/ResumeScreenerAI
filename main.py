from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess_text
from load_data import load_resumes

def get_top_matches(job_description, resumes, filenames, top_n=5):
    all_texts = [preprocess_text(job_description)] + [preprocess_text(resume) for resume in resumes]

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(all_texts)

    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    top_indices = similarities.argsort()[::-1][:top_n]

    top_matches = [(filenames[i], similarities[i]) for i in top_indices]
    return top_matches
