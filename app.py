from flask import Flask
from flask_restful import Api
from resources.movies import Movie
#from resources.comments import Comment

app = Flask(__name__)
api = Api(app)

api.add_resource(Movie, "/movie/<int:id>" , "/movie")
#api.add_resource(Comment, "/post/<int:post_id>/comment/<int:comment_id>", "/post/<int:post_id>/comment")

if __name__ == '__main__':
    app.run(debug=True)
