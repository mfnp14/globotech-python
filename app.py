from flask import Flask
from flask_restful import Api
from model.movie import MovieModel
from resources.movies import Movie, MovieTitle
from services.database import MyDatabase
#from resources.comments import Comment

app = Flask(__name__)
api = Api(app)
database = MyDatabase()
MovieModel.database_service = database

api.add_resource(Movie, "/movie/<int:id>" , "/movie")
api.add_resource(MovieTitle, "/movie/title/<string:title>" , "/movie/title")
#api.add_resource(Comment, "/post/<int:post_id>/comment/<int:comment_id>", "/post/<int:post_id>/comment")

if __name__ == '__main__':
    app.run(debug=True)
