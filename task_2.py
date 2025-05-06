class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        return self.movies.append(movie)    
    
class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'
    
class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'    
    
comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))
    