# Import necessary libraries
from flask import Flask, render_template, request  # Flask core functions for web development
import pickle  # To load serialized Python objects (models/data)
import numpy as np  # For numerical operations, especially indexing

# Load the precomputed data from pickle files
popular_df = pickle.load(open('popular.pkl', 'rb'))  # Contains data of popular books
pt = pickle.load(open('pt.pkl', 'rb'))  # Pivot table or user-item matrix
books = pickle.load(open('books.pkl', 'rb'))  # Metadata of books
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))  # Precomputed similarity matrix

# Initialize the Flask application
app = Flask(__name__)

# Home route - displays popular books
@app.route('/')
def index():
    return render_template(
        'index.html',  # Renders HTML page with following data passed into it
        book_name=list(popular_df['Book-Title'].values),  # Book titles
        author=list(popular_df['Book-Author'].values),  # Authors
        image=list(popular_df['Image-URL-M'].values),  # Image URLs
        votes=list(popular_df['num-ratings'].values),  # Number of votes
        rating=list(popular_df['avg-ratings'].values)  # Average ratings
    )

# Route to show the recommend input UI
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')  # A page with an input form for user

# Backend route to process the book recommendation
@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')  # Get user input from form (book name)

    # Find index of the book in pivot table
    index = np.where(pt.index == user_input)[0][0]

    # Sort the similarity scores and get top 4 similar items (excluding itself)
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []  # To hold the recommended book info
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]  # Find book metadata

        # Get title, author, image (ensuring uniqueness using drop_duplicates)
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)  # For debugging, prints recommended books in console

    return render_template('recommend.html', data=data)  # Re-render the page with results

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


