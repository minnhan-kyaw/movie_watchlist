from flask import Flask
from data_access.movie_repository import init_db
from endpoint.movies import movies_bp
 
app = Flask(__name__)

init_db()

app.register_blueprint(movies_bp)

@app.route('/')
def index():
    return "Movie Watchlist app is running!"

if __name__ == '__main__':
    app.run(debug=True)

