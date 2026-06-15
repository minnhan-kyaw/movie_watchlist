import sqlite3
import os

DATABASE = 'movie.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER,
            rating INTEGER,
            status TEXT NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()


def delete_movie(movie_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE id= ?', (movie_id,))
    conn.commit()
    conn.close()
    
def get_movie_by_id(movie_id):
    conn = get_db_connection()
    row = conn.execute('SELECT id, title, genre, release_year, rating, status, notes FROM movies WHERE id = ?').fetchone()
    conn.close()

    if row:
        movie_data = dict(row)
        movie_data['year'] = movie_data['release_year']
        return movie_data
    return None


