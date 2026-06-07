from data_access.movie_repository import get_db_connection

def add_movie_service(title,genre,release_year,rating,status, notes):
    conn = get_db_connection()
    sql = f"""
        INSERT INTO movies (title,genre,release_year,rating,status, notes)
        VALUES ('{title}','{genre}','{release_year}','{rating}','{status}','{notes}')
    """
    conn.execute(sql)
    conn.commit()
    conn.close()

def get_all_movies_service():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close
    return movies