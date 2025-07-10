# app.py

from flask import Flask, render_template, request
from recommender_core import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    error = None

    if request.method == 'POST':
        movie_name = request.form.get('movie')
        if movie_name:
            results = get_recommendations(movie_name)
            if isinstance(results, list):
                recommendations = results
            else:
                error = results
        else:
            error = "Please enter a movie name."

    return render_template('index.html', recommendations=recommendations, error=error)

if __name__ == '__main__':
    app.run(debug=True)
