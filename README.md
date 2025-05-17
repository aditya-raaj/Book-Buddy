# Book Recommendation System

A web-based book recommendation application that suggests books to users based on popularity metrics and collaborative filtering techniques.

## Overview

This project implements a book recommendation system using two primary approaches:
- **Popularity-Based Recommendation**: Suggests books that are generally popular among all users
- **Collaborative Filtering**: Provides personalized recommendations based on similar user preferences

The system is deployed as a web application where users can discover new books tailored to their interests.

## Features

- View popular book recommendations
- Get personalized book recommendations based on collaborative filtering
- User-friendly web interface
- Search functionality for books

## Technology Stack

- **Backend**: Python with Flask
- **Data Processing**: Pandas, NumPy, scikit-learn
- **Model Serialization**: Pickle
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Ready for deployment on platforms like Heroku (Procfile included)

## Project Structure
```├── data/                      # Dataset files
├── notebook/                  # Jupyter notebooks for data exploration and model development
├── templates/                 # HTML templates for the web interface
├── app.py                     # Flask application
├── books.pkl                  # Serialized book data
├── popular.pkl                # Serialized popular books model
├── pt.pkl                     # Pivot table data
├── similarity_scores.pkl      # Collaborative filtering similarity matrix
├── requirements.txt           # Python dependencies
└── Procfile                   # Heroku deployment configuration
```
## Installation

1. Clone this repository:
```
git clone https://github.com/aditya-raaj/book-recommendation-system.git
cd book-recommendation-system
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the application:
```
python app.py
```
5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Home Page**: Displays popular book recommendations
2. **Recommendation Page**: Enter a book you like to get similar recommendations
3. **Search**: Search for specific books by title or author

## How It Works

### Popularity-Based Recommendation
Books are ranked based on factors like ratings count and average rating score. The top-rated books with significant number of ratings are recommended to new users.

### Collaborative Filtering
This approach analyzes user-book interactions to find patterns and similarities between users. When a user selects a book they like, the system finds similar books based on how other users with similar preferences have rated them.

## Future Improvements

- Content-based filtering using book descriptions and metadata
- Hybrid recommendation approach combining different techniques
- User account system to track preferences over time
- Integration with external book APIs for richer data

## Contributors

- [Aditya Raj](https://github.com/aditya-raaj)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
