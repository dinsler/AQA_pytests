from .db_init import Movies


ACTION_MOVIES_COL = 'action_movies'


class ActionMovies(Movies):
    __action_movies_col = Movies.get_movies_db()[ACTION_MOVIES_COL]

    @staticmethod
    def get_collection():
        return ActionMovies.__action_movies_col
