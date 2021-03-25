import os
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from models import (
    Movie,
    setup_db,
    Actor
)
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
from sqlalchemy import exc


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Methods',
                             'GET , POST, PATCH, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def movies(payload):
        data = Movie.query.order_by(Movie.id.desc()).all()
        formatted_movies = [i.long() for i in data]

        return jsonify(
            {
                'success': True,
                'movies': formatted_movies,
                'total': len(formatted_movies)
            }
        )

    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(payload):
        form_data = request.get_json()
        print(form_data)
        error = False
        try:
            movie = Movie(title=form_data['title'],
                          release_date=form_data['release_date'])
            casts = form_data.get('casts', None)
            if isinstance(casts, list):
                for i in casts:
                    if Actor.query.get(i):
                        movie.casts.append(Actor.query.get(i))
            movie.insert()
        except exc.DatabaseError:
            error = True
        if error:
            abort(400)
        else:
            return jsonify(
                {
                    "success": True,
                    "movie": [movie.long()]
                }), 200

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('add:movies')
    def delete_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if not movie:
            abort(404)
        try:
            movie.delete()
        except exc.DatabaseError:
            abort(400)

        return jsonify(
            {
                "success": True,
                "delete": movie_id
            }), 200

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        form_data = request.get_json()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if not movie:
            abort(404)

        try:
            title = form_data.get('title')
            release_date = form_data.get('release_date')
            if title:
                movie.title = title
            if release_date:
                movie.release_date = release_date
            movie.update()
        except exc.DatabaseError:
            abort(400)

        return jsonify(
            {
                "success": True,
                "movie": [movie.long()]
            }), 200

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def actors(payloads):
        data = Actor.query.order_by('id').all()
        formatted_data = [i.long() for i in data]

        return jsonify(
            {
                'success': True,
                'actors': formatted_data,
                'total': len(formatted_data)
            }
        )

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(payload):
        form_data = request.get_json()
        error = False
        try:
            actor = Actor(name=form_data['name'], gender=form_data['gender'],
                          age=form_data['age'])
            actor.insert()
        except exc.DatabaseError:
            error = True
        if error:
            abort(400)
        else:
            return jsonify(
                {
                    "success": True,
                    "actor": [actor.long()]
                }), 200

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('add:actors')
    def delete_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if not actor:
            abort(404)
        try:
            actor.delete()
        except exc.DatabaseError:
            abort(400)

        return jsonify(
            {
                "success": True,
                "delete": actor_id
            }), 200

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        form_data = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if not actor:
            abort(404)

        try:
            name = form_data.get('name')
            age = form_data.get('age')
            gender = form_data.get('gender')
            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()
        except exc.DatabaseError:
            abort(400)

        return jsonify(
            {
                "success": True,
                "actor": [actor.long()]
            }), 200

    @app.route('/casts/<int:movie_id>', methods=['POST'])
    @requires_auth('patch:movies')
    def add_casts(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if not movie:
            abort(404)
        try:
            form_data = request.get_json()
            casts = form_data['casts']
            if isinstance(casts, list):
                for i in casts:
                    if Actor.query.get(i):
                        movie.casts.append(Actor.query.get(i))
            movie.update()
        except exc.DatabaseError:
            abort(400)

        return jsonify(
            {
                "success": True,
                'casts': [i.short() for i in movie.casts]
            }), 200

    @app.route('/casts/<int:movie_id>', methods=['GET'])
    @requires_auth('patch:movies')
    def movie_casts(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if not movie:
            abort(404)
        return jsonify(
            {
                "success": True,
                'casts': [i.short() for i in movie.casts]
            }), 200

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify(
            {
                "success": False,
                "error": 422,
                "message": "unprocessable"
            }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
            {
                "success": False,
                "error": 404,
                "message": "resource not found"
            }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify(
            {
                "success": False,
                "error": 401,
                "message": 'unathorized'
            }), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(
            {
                "success": False,
                "error": 500,
                "message": 'Internal Server Error'
            }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(
            {
                "success": False,
                "error": 400,
                "message": 'Bad Request'
            }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify(
            {
                "success": False,
                "error": 405,
                "message": 'Method Not Allowed'
            }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify(
            {
                "success": False,
                "error": error.error['code'],
                "message": error.error['description']
            }), error.status_code

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True)

    return app


app = create_app()
