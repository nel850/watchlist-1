from app import app
from flask import render_template
from .request import get_movies
from .request import get_movies, get_movie

# @app.route('/')
# def index():
#     message = 'hello world'
#     title='home'
#     return render_template('index.html', message=message,title=title)

@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    view movie page function that returns the movie details page and its data
    '''
    title = "My post"
    movie = get_movie(id)
    title = f'{movie.title}'
        
    return render_template('movie.html',title=title, movie = movie)


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best movie review website online'
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website online'
    return render_template('index.html', title = title,popular = popular_movies, upcoming = upcoming_movies, now_playing = now_showing_movie )        