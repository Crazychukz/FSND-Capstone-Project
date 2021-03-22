import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, setup_db, Actor
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
from flask_migrate import Migrate


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')

        return response

    @app.route('/movies', methods=['GET'])
    # @requires_auth('get:drinks-detail')
    def movies():
        data = Movie.query.order_by('id').all()
        formatted_movies = [i.long() for i in data]

        return jsonify(
            {
                'success': True,
                'movies': formatted_movies,
                'total': len(formatted_movies)
            }
        )

    @app.route('/movies', methods=['POST'])
    def add_movie():
        form_data = request.get_json()
        error = False
        try:
            movie = Movie(title=form_data['title'], release_date=form_data['release_date'])
            casts = form_data['casts']
            if isinstance(casts, list):
                for i in casts:
                    if Actor.query.get(i):
                        movie.casts.append(Actor.query.get(i))
            movie.insert()
        except:
            error = True
        if error:
            abort(400)
        else:
            return jsonify({
                "success": True,
                "movie": [movie.long()]
            }), 200

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    # @requires_auth('delete:drinks')
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if not movie:
            abort(404)
        try:
            movie.delete()
        except:
            abort(400)

        return jsonify(
            {"success": True,
             "delete": movie_id}), 200

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    # @requires_auth('patch:drinks')
    def update_movie(movie_id):
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
        except:
            abort(400)

        return jsonify(
            {"success": True,
             "movie": [movie.long()]
             }), 200

    @app.route('/actors', methods=['GET'])
    # @requires_auth('get:drinks-detail')
    def actors():
        data = Actor.query.order_by('id').all()
        formatted_data = [i.short() for i in data]

        return jsonify(
            {
                'success': True,
                'actors': formatted_data,
                'total': len(formatted_data)
            }
        )

    @app.route('/actors', methods=['POST'])
    def add_actor():
        form_data = request.get_json()
        error = False
        try:
            actor = Actor(name=form_data['name'], gender=form_data['gender'], age=form_data['age'])
            actor.insert()
        except:
            error = True
        if error:
            abort(400)
        else:
            return jsonify({
                "success": True,
                "actors": [actor.long()]
            }), 200

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    # @requires_auth('delete:drinks')
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if not actor:
            abort(404)
        try:
            actor.delete()
        except:
            abort(400)

        return jsonify(
            {"success": True,
             "delete": actor_id}), 200

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    # @requires_auth('patch:drinks')
    def update_actor(actor_id):
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
        except:
            abort(400)

        return jsonify(
            {"success": True,
             "actor": [actor.long()]
             }), 200

    @app.route('/casts/<int:movie_id>', methods=['POST'])
    # @requires_auth('delete:drinks')
    def add_casts(movie_id):
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
        except:
            abort(400)

        return jsonify(
            {"success": True,
             'casts': [i.short() for i in movie.casts]
             }), 200

    @app.route('/casts/<int:movie_id>', methods=['GET'])
    # @requires_auth('delete:drinks')
    def movie_casts(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if not movie:
            abort(404)
        return jsonify(
            {"success": True,
             'casts': [i.short() for i in movie.casts]
             }), 200

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'unathorized'
        }), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error'
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": 'Method Not Allowed'
        }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.error,
            "message": error.status_code
        }), error.error

    if __name__ == '__main__':
        APP.run(host='0.0.0.0', port=8080, debug=True)

    return app


APP = create_app()
