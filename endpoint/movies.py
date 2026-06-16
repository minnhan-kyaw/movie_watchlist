from flask import Blueprint, render_template, request, redirect, url_for
from business_logic.movie_service import (
    add_movie_service, 
    get_all_movies_service, 
    get_movies_by_id_service
)
from data_access.movie_repository import delete_movie

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET', 'POST'])
def index():
    movies = get_all_movies_service()
    return render_template('index.html', movies=movies)

@movies_bp.route('/movies/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        genre = request.form.get('genre')
        release_year = request.form.get('release_year')
        status = request.form.get('status')
        rating = request.form.get('rating')
        notes = request.form.get('notes')
        
        try:
            release_year_val = int(release_year) if release_year else None
        except ValueError:
            release_year_val = None
            
        try:
            rating_val = int(rating) if rating else None
        except ValueError:
            rating_val = None

        add_movie_service(
            title=title,
            genre=genre,
            release_year=release_year_val,
            rating=rating_val,
            status=status,
            notes=notes
        )
        return redirect(url_for('movies.index'))
        
    return render_template('create.html')

@movies_bp.route('/delete/<int:movie_id>', methods=['POST'])
def delete(movie_id):
    delete_movie(movie_id)
    return redirect(url_for('movies.index'))

@movies_bp.route('/movies/<int:movie_id>', methods=['GET'])
def view_movie(movie_id):
    movie = get_movies_by_id_service(movie_id)
    return render_template('view.html', movie=movie)
