from data_access.movie_repository import get_db_connection
from models.movie import Movie  

def add_movie_service(title, genre, release_year, rating, status, notes):
    conn = get_db_connection()
    sql = """
        INSERT INTO movies (title, genre, release_year, rating, status, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    conn.execute(sql, (title, genre, release_year, rating, status, notes))
    conn.commit()
    conn.close()

def get_all_movies_service():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return [Movie.from_row(row) for row in rows]
    

def get_movies_by_id_service(movie_id):
    conn = get_db_connection()
    row = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    conn.close()
    return Movie.from_row(row) if row else None
    
