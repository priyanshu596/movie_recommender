# recommender_core.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel  # use memory-efficient kernel
import difflib

# Load datasets
movies = pd.read_csv('movies.csv')
tags = pd.read_csv('tags.csv')

# Clean and merge
tags['tag'] = tags['tag'].fillna('').astype(str)
tags_grouped = tags.groupby('movieId')['tag'].apply(lambda x: " ".join(x)).reset_index()
movie_data = pd.merge(movies, tags_grouped, on='movieId', how='left')

movie_data['tag'] = movie_data['tag'].fillna('')
movie_data['genres'] = movie_data['genres'].fillna('')
movie_data['content'] = movie_data['genres'] + ' ' + movie_data['tag']

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movie_data['content']).astype('float32')  # use float32 for efficiency

# Index mapping for fast lookup
indices = pd.Series(movie_data.index, index=movie_data['title'].str.lower()).drop_duplicates()

# Recommendation function using linear_kernel (on-demand similarity computation)
def get_recommendations(title, tfidf_matrix=tfidf_matrix, movie_data=movie_data, indices=indices):
    title = title.lower().strip()
    all_titles = movie_data['title'].str.lower().tolist()
    closest_matches = difflib.get_close_matches(title, all_titles, n=1, cutoff=0.6)

    if not closest_matches:
        return "Movie not found. Please check the name."

    matched_title = closest_matches[0]
    idx = indices[matched_title]

    # Compute similarity of just one movie with all others (no full matrix)
    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # top 5 excluding the movie itself

    movie_indices = [i[0] for i in sim_scores]
    return movie_data['title'].iloc[movie_indices].tolist()

# Optional: test it directly
if __name__ == "__main__":
    # Example usage
    query = input("Enter a movie title: ")
    recommendations = get_recommendations(query)
    print("\nTop 5 recommendations:")
    if isinstance(recommendations, list):
        for movie in recommendations:
            print("-", movie)
    else:
        print(recommendations)
