from data_access.movie_repository import get_db_connection

def add_movie_service(title,genre,release_year,rating,status, notes):
    conn = get_db_connection()
    sql = """
        INSERT INTO movies (title,genre,release_year,rating,status, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    conn.execute(sql, (title,genre,release_year,rating,status, notes))
    conn.commit()
    conn.close()

def get_all_movies_service():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close
    return movies

def get_movies_by_id_service(movie_id):
    conn = get_db_connection()
    row = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    conn.close
    movie_dict = dict(row)
    movie_dict['year'] = movie_dict['release_year']
    if not movie_dict.get('notes') or movie_dict['notes'].strip() == "":
        movie_dict['notes'] = "This movie have no notes."
    return movie_dict
    