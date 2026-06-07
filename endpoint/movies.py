from flask import Blueprint, render_template, request, redirect, url_for
from business_logic.movie_service import add_movie_service, get_all_movies_service, get_db_connection

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        add_movie_service(title, genre, 2003 , 'watched'  , 'notes') 
        return redirect(url_for('movies.index'))
    
    movies = get_all_movies_service()
    return render_template('index.html', movies=movies)
