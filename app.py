from flask import Flask,redirect,url_for
from data_access.movie_repository import init_db
from endpoint.movies import movies_bp

 
app = Flask(__name__)

app.secret_key = 'my_app_key_2006'

init_db()

app.register_blueprint(movies_bp)

@app.route('/')
def home():
    return redirect(url_for('movies.index'))

if __name__ == '__main__':
    app.run(debug=True)

