from flask import Blueprint, render_template, request, redirect, url_for, flash
from business_logic.movie_service import (
    add_movie_service,
    get_all_movies_service,
    get_movies_by_id_service,
    update_movie_service
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
        rating = request.form.get('rating', '').strip()
        status = request.form.get('status', '').strip()
        notes = request.form.get('notes', '').strip()

        
        if not title:
            flash("Movie Title is required!", "danger")
            return render_template('create.html', movie=request.form)

        if not genre:
            flash("Please select a Genre!", "danger")
            return render_template('create.html', movie=request.form)

        if not release_year:
            flash("Release Year is required!", "danger")
            return render_template('create.html', movie=request.form)
        try:
            year_val = int(release_year)
            if year_val < 1888 or year_val > 2030:
                flash("Release Year must be between 1888 and 2030!", "danger")
                return render_template('create.html', movie=request.form)
        except ValueError:
            flash("Release Year must be a valid number!", "danger")
            return render_template('create.html', movie=request.form)

        if rating:
            try:
                rating_val = int(rating)
                if rating_val < 1 or rating_val > 5:
                    flash("Rating must be between 1 and 5 stars!", "danger")
                    return render_template('create.html', movie=request.form)
            except ValueError:
                flash("Rating must be a valid number!", "danger")
                return render_template('create.html', movie=request.form)

        add_movie_service(
            title=title,
            genre=genre,
            release_year=year_val,
            rating=rating,
            status=status,
            notes=notes
        )
        flash("Movie added successfully!", "success")
        return redirect(url_for('movies.index'))

    return render_template('create.html')



@movies_bp.route('/movies/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    movie = get_movies_by_id_service(movie_id)
    if not movie:
        flash("Movie not found.", "danger")
        return redirect(url_for('movies.index'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        genre = request.form.get('genre', '').strip()
        release_year = request.form.get('release_year', '').strip()
        rating = request.form.get('rating', '').strip()
        status = request.form.get('status', '').strip()
        notes = request.form.get('notes', '').strip()
        current_input = {
            'id': movie_id,
            'title': title,
            'genre': genre,
            'release_year': release_year,
            'rating': rating,
            'status': status,
            'notes': notes
        }

        if not title:
            flash("Movie Title is required!", "danger")
            return render_template('edit.html', movie=current_input)

        
        if not genre:
            flash("Please select a Genre!", "danger")
            return render_template('edit.html', movie=current_input)

        
        if not release_year:
            flash("Release Year is required!", "danger")
            return render_template('edit.html', movie=current_input)
        try:
            year_val = int(release_year)
            if year_val < 1888 or year_val > 2030:
                flash("Release Year must be between 1888 and 2030!", "danger")
                return render_template('edit.html', movie=current_input)
        except ValueError:
            flash("Release Year must be a valid number!", "danger")
            return render_template('edit.html', movie=current_input)

        
        if rating:
            try:
                rating_val = int(rating)
                if rating_val < 1 or rating_val > 5:
                    flash("Rating must be between 1 and 5 stars!", "danger")
                    return render_template('edit.html', movie=current_input)
            except ValueError:
                flash("Rating must be a valid number!", "danger")
                return render_template('edit.html', movie=current_input)

        try:
            update_movie_service(
                movie_id=movie_id,
                title=title,
                genre=genre,
                release_year=year_val,
                rating=rating_val,
                status=status,
                notes=notes
            )
            flash("Movie updated successfully!", "success")
            return redirect(url_for('movies.index'))
        except ValueError as e:
            flash(str(e), "danger")
            return render_template('edit.html', movie=movie)

    return render_template('edit.html', movie=movie)


@movies_bp.route('/delete/<int:movie_id>', methods=['POST'])
def delete(movie_id):
    delete_movie(movie_id)
    flash("Movie deleted successfully!", "success")
    return redirect(url_for('movies.index'))

@movies_bp.route('/movies/<int:movie_id>', methods=['GET'])
def view_movie(movie_id):
    movie = get_movies_by_id_service(movie_id)
    if not movie:
        flash("Movie not found.", "danger")
        return redirect(url_for('movies.index'))
    return render_template('view.html', movie=movie)

