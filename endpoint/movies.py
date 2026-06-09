from flask import Blueprint, render_template, request, redirect, url_for
from business_logic.movie_service import add_movie_service, get_all_movies_service, get_db_connection

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET', 'POST'])
def index():
    
    movies = get_all_movies_service()
    return render_template('index.html', movies=movies)

@movies_bp.route('/movies/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        genre = request.form.get('genre')
        release_year = request.form.get('release_year')
        status = request.form.get('status')
        notes = request.form.get('notes')
        add_movie_service(title, genre, int(release_year), 0, status , notes)
        return redirect(url_for('movies.index'))
    return render_template('create.html')