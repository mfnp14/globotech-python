import time
from json import dumps, loads

class MovieModel:
    _movie_list = []
    def __init__(self, title, sinopse, review, image, cast) -> None:
        self.id = round(time.time() * 1000)
        self.title = title
        self.sinopse = sinopse
        self.review = review
        self.image = image
        self.cast = []

    @classmethod
    def add_movie(cls, movie):
        cls._movie_list.append(movie)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "sinopse": self.sinopse,
            "review": self.review,
            "image": self.image,
            "cast": loads(dumps(self.cast, default=MovieModel.to_dict))
        }
