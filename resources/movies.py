from flask_restful import Resource, reqparse
from model.movie import MovieModel

class Movie(Resource):
    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("sinopse")
        body_arguments.add_argument("review")
        body_arguments.add_argument("image")
        body_arguments.add_argument("cast")

        params = body_arguments.parse_args()
        new_movie = MovieModel(params["title"], params["sinopse"], params["review"], params["image"], params["cast"])
        MovieModel.add_movie(new_movie)
        return new_movie.to_dict()
