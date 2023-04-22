from homework17_framework.mongo_db_repository.movies_database import Movies


class ActionMovies(Movies):
    __action_movies_col = Movies.get_movies_database()["action_movies"]

    @staticmethod
    def get_collection():
        return ActionMovies.__action_movies_col
