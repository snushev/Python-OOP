from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []

    def register_user(self, username: str, age: int):
        if any(user for user in self.users_collection if user.username == username):
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if not user:
            raise Exception("This user does not exist!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attribute, value in kwargs.items():
            setattr(movie, attribute, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."


    def like_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        result = []
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        for movie in sorted_movies:
           result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        result = []
        if self.users_collection:
            users = [x.username for x in self.users_collection]
            result.append(f"All users: {', '.join(users)}")
        else:
            result.append("All users: No users.")
        if self.movies_collection:
            movies = [x.title for x in self.movies_collection]
            result.append(f"All movies: {', '.join(movies)}")
        else:
            result.append("All movies: No movies.")

        return '\n'.join(result)