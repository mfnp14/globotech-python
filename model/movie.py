import time
from json import dumps, loads
from services.database import MyDatabase

class MovieModel:
    database_service: MyDatabase = None
    def __init__(self, title, sinopse, review, image, cast, id=None) -> None:
        if id:
            self.id = id
        else:
            highest_id = int(max(self.seek_existing_ids())) if self.seek_existing_ids() else 0
            self.id = highest_id + 1
        self.title = title
        self.sinopse = sinopse
        self.review = review
        self.image = image
        self.cast = cast
    
    @classmethod
    def add_movie(cls, movie):
        cls.database_service.create_movie(movie)        

    @classmethod
    def find_movie(cls, movie_id):
        found_movie = None
        result = cls.database_service.find_movie(movie_id)
        print(result)
        if result:
            found_movie = MovieModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_movie
        
    @classmethod
    def find_movie_by_params(cls, movie_title):
        found_movie = None
        result = cls.database_service.find_filter(movie_title)
        if result:
            found_movie = MovieModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_movie

    @classmethod
    def remove_movie(cls, movie):
        cls.database_service.delete_movie(movie)
 
    @classmethod
    def list_to_dict(cls):
        result = cls.database_service.list_movies()
        movie_list = []
        for movie in result:
            movie_list.append(MovieModel(movie[1], movie[2], movie[3], movie[4], movie[5], movie[0]))
        return loads(dumps(movie_list, default=MovieModel.to_dict))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "sinopse": self.sinopse,
            "review": self.review,
            "image": self.image,
            "cast": loads(dumps(self.cast, default=MovieModel.to_dict))
        }

    @classmethod
    def seek_existing_ids(cls):
        result = cls.database_service.list_movies()
        id_list = []
        for movie in result:
            id_list.append(movie[0])
        return sorted(id_list)