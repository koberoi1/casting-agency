#import dependencies
import os
from flask import Flask, jsonify, abort, request
from model import setup_db, Movies, Actors
from flask_cors import CORS
from auth import AuthError, requires_auth
from datetime import datetime
from werkzeug.exceptions import HTTPException

# create app
app = Flask(__name__)

# binds a flask application and a SQLAlchemy service
setup_db(app)

# Cross-Origin-Resource-Sharing
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

# endpoints
@app.route('/actors', methods=['GET'])
def get_actors():
    try:
        actors = Actors.query.all()
        actors = [actor.format() for actor in actors]

        if not actors:
            abort(404)

        return jsonify({
            'success': True,
            'actors': actors
        })
    except:
        abort(404)


@app.route('/')
def get_home():
    return('Welcome to the Casting Agency')


@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movies.query.all()
        movies = [movie.format() for movie in movies]

        if not movies:
            abort(404)

        return jsonify({
            'success': True,
            'movies': movies
        })
    except:
        abort(404)


# Authetication

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def post_actor(payload):
    if request.data:
        body = request.get_json()
        name = body['name']
        age = body['age']
        gender = body['gender']

        try:
            actor = Actors(name=name, age=age, gender=gender)
            actor.insert()
            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })
        except:
            abort(500)

# Authetication
@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def post_movie(payload):
    if request.data:
        body = request.get_json()
        print(body)
        title = body['title']
        releaseDate = body['releaseDate'].split('/')
        year = int(releaseDate[0])
        month = int(releaseDate[1])
        day = int(releaseDate[2])
        releaseDate = datetime(year, month, day)

        try:
            movie = Movies(title=title, releaseDate=releaseDate)
            movie.insert()
            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })
        except:
            abort(500)

# Authetication
@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def patch_actors(payload, id):
    try:
        actor = Actors.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)

        if request.data:
            body = request.get_json()

            if 'name' in body:
                actor.name = body['name']

            if 'age' in body:
                actor.age = body['age']

            if 'gender' in body:
                actor.gender = body['gender']

            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })
    except:
        abort(404)


# Authetication
@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movie(payload, id):
    try:
        movie = Movies.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)

        if request.data:
            body = request.get_json()

            if 'title' in body:
                movie.title = body['title']

            if 'releaseDate' in body:
                releaseDate = body['releaseDate'].split('/')
                year = int(releaseDate[0])
                month = int(releaseDate[1])
                day = int(releaseDate[2])
                releaseDate = datetime(year, month, day)
                movie.releaseDate = releaseDate

            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })

    except:
        abort(404)


# Authetication
@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('patch:movies')
def delete_actor(payload, id):
    try:
        actor = Actors.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            'success': True
        })
    except:
        abort(404)


# Authetication
@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(payload, id):
    try:
        movie = Movies.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)

        movie.delete()
        return jsonify({
            'success': True
        })

    except:
        abort(404)

# error-handlers
@app.errorhandler(AuthError)
def auth_error_handler(error):
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response


@app.errorhandler(HTTPException)
def http_exception(error):
    return jsonify(
        {"success": False,
         "error": error.code,
         "message": error.description})
