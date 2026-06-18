from flask import Blueprint, render_template, request, redirect, url_for, flash
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
        title = request.form.get('title', '').strip()
        genre = request.form.get('genre', '').strip()
        release_year = request.form.get('release_year', '').strip()
        status = request.form.get('status', '').strip()
        rating = request.form.get('rating', '').strip()
        notes = request.form.get('notes', '').strip()

        
        if not title:
            flash("Movie Title is required.", "error")
            return render_template('create.html')
        
        if len(title) > 100:
            flash("Movie Title must be under 100 characters.", "error")
            return render_template('create.html')

        if not genre:
            flash("Please select a Genre.", "error")
            return render_template('create.html')

        if not release_year:
            flash("Release Year is required.", "error")
            return render_template('create.html')

        try:
            release_year_val = int(release_year)
            if release_year_val < 1888 or release_year_val > 2026:
                flash("Release Year must be between 1888 and 2026.", "error")
                return render_template('create.html')
        except ValueError:
            flash("Release Year must be a valid number.", "error")
            return render_template('create.html')

        try:
            rating_val = int(rating)
            if rating_val < 1 or rating_val > 5:
                flash("Rating must be between 1 and 5 Stars.", "error")
                return render_template('create.html')
        except ValueError:
            flash("Invalid rating value.", "error")
            return render_template('create.html')

        valid_statuses = ["To-Watch", "Watching", "Watched"]
        if status not in valid_statuses:
            flash("Invalid status selection.", "error")
            return render_template('create.html')

        if len(notes) > 500:
            flash("Notes must be under 500 characters.", "error")
            return render_template('create.html')

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
