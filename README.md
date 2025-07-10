MOVIE RECOMMENDER SYSTEM (Flask)


DESCRIPTION:
------------
This is a content-based movie recommender system that suggests similar movies
based on genres and tags. It uses TF-IDF vectorization and cosine similarity 
to find the most relevant matches. A simple web interface is built using Flask.

--------------------------------------------------


PROJECT STRUCTURE:
------------------

movie_recommender/
  movies.csv              - Movie metadata (MovieLens)
  tags.csv                - User-generated tags (MovieLens)
  recommender_core.py     - Core logic for recommendation
  app.py                  - Flask web application
  templates/
    index.html            - HTML page for user interface
  README.txt              - This file




--------------------------------------------------

FEATURES:
---------
- Content-based filtering using genres and tags.
- Memory-efficient similarity calculation using linear_kernel.
- Fuzzy matching to handle typos or close matches in titles.
- Clean web interface using Flask.

--------------------------------------------------

REQUIREMENTS:
-------------
To install the required Python libraries, run:

    pip install flask pandas scikit-learn

--------------------------------------------------

HOW TO RUN:
-----------
1. Make sure you have 'movies.csv' and 'tags.csv' in the same directory.
   These files can be downloaded from: https://grouplens.org/datasets/movielens/

2. Run the Flask app:

    python app.py

3. Open your browser and go to:

    http://127.0.0.1:5000

--------------------------------------------------

USAGE EXAMPLE:
--------------
Input:
    Toy Story

Output:
     Toy Story 2
     A Bug's Life
     Monsters, Inc.
     Shrek
     Finding Nemo


--------------------------------------------------

NOTES:
------
- TF-IDF is limited to 5000 max features to reduce memory usage.
- `linear_kernel` is used instead of `cosine_similarity` for performance.
- The system only recommends based on the input movie's tags + genres.

--------------------------------------------------

AUTHOR:
-------
Priyanshu Singh

--------------------------------------------------

LICENSE:
--------
MIT License – You are free to use and modify.
