
class Movie:
    """Описывает фильм"""
    def __init__(self, movie_id: int, title: str):
        self.movie_id = movie_id
        self.title = title
        
        
class MovieRepository:
    """Хранит коллекцию фильмов и загружает их из файла"""
    def __init__(self):
        self.movies: list[Movie] = []
        
    def load_from_file(self, path:str) -> None:
        """Загружает из файла фильмы и создает объекты фильмов и формирует список movies

        Args:
            path (str): название файла
        """
        with open(path, 'r') as files:
            try:
                for file_line in files:
                    film = file_line.strip()
                    if not film:
                        continue
                    film_list = film.split(',')
                    
                    try:
                        movie_id = int(film_list[0])
                        movie_title = film_list[1]
                        
                        movie = Movie(movie_id=movie_id, title=movie_title)
                        self.movies.append(movie)
                        
                    except ValueError: 
                        print('Не удалось преобразовать число в int')
                    
            except Exception as e:
                print(f'Ошибка при чтении файла: {e}')


    def get_all_movies(self) -> list[Movie]:
        """Возвращает все фильмы"""
        return self.movies
    
    def get_title(self, movie_id: int) -> str | None:
        """Возвращает название фильма по id"""
        for movie in self.get_all_movies():
            if movie.movie_id == movie_id:
                return movie.title
    def get_movie_by_id(self, movie_id) -> Movie | None:
        """Возвращает объект фильма по id"""
        for movie in self.get_all_movies():
            if movie.movie_id == movie_id:
                return movie
            
    

class UserHistory:
    """Хранит список фильмов, просмотренных одним пользователем"""
    def __init__(self, movie_ids: list[int]):
        self.movie_ids = movie_ids
    def get_unique_movies(self) -> set[int]:
        """Возвращает массив с уникальным набором ID фильмов пользователя"""
        return set(self.movie_ids)
             
        
class HistoryRepository:
    """Загружает и хранит историю просмотров всех пользователей"""
    def __init__(self):
        self.histories:list[UserHistory] = []
    def load_from_file(self, path:str) -> None:
        """Загружает из файла историю просмотров пользователей"""
        with open(path, 'r') as files:
            try:
                for line in files:
                    ids_list = [int(x) for x in line.strip().split(',')]
                    self.histories.append(UserHistory(ids_list))
            except Exception as e:
                print(f"Ошибка чтения файла: {e}")
                
    def get_all_histories(self) -> list[UserHistory]:
        """Возвращает всю историю просмотров пользователей"""
        return self.histories
                
        
class SimilarityCalculator:
    """Класс калькулятора для подсчета метрики схожести пользователей"""
    @staticmethod
    def calculate_similarity(base: UserHistory, other: UserHistory) -> float:
        """Считает метрику схожести - процент общих фильмов по формуле (число совпавших фильмов пользователей / число фильмов пользователя base)"""
        base_movies = base.get_unique_movies()
        other_movies = other.get_unique_movies()
        
        if len(base_movies) == 0:
            return 0
        
        intersection_films = base_movies & other_movies
        return len(intersection_films) / len(base_movies)
    
    
class RecomendationEngine:
    """Основной алгоритм рекомендаций"""
    def __init__(self, movie_repo: MovieRepository, history_repo: HistoryRepository, similarity_calculator: SimilarityCalculator):
        self.movie_repo = movie_repo
        self.history_repo = history_repo
        self.similarity_calculator = SimilarityCalculator.calculate_similarity
    
    def get_similar_users(self, base_user: UserHistory, threshold: float = 0.5) -> list[UserHistory]:
        """Выбирает пользователей с совпадением >= threshold(0.5)"""
        similar_users_list = []
        for user in self.history_repo.get_all_histories():
            if base_user == user:
                continue
            
            similarity = self.similarity_calculator(base_user, user)
            if similarity >= threshold:
                similar_users_list.append(user)
            
        return similar_users_list
        
    def get_candidate_movies(self, base_user: UserHistory, similar_users: list[UserHistory]) -> list[int]:
        """Находит фильмы из истории похожих пользователей, которых нет у base_user"""
        base_user_movies = base_user.get_unique_movies()
        candidates = set()
        for user in similar_users:
            user_movies = user.get_unique_movies()
            for movie in user_movies:
                if movie not in base_user_movies:
                    candidates.add(movie)
                    
        return list(candidates)
    
    def calculate_global_popularity(self, movie_id: int) -> int:
        """Считает, сколько раз фильм встречается в истории всех пользователей"""
        all_history_user = self.history_repo.get_all_histories()
        count = 0
        for user in all_history_user:
            count += user.movie_ids.count(movie_id)

        return count
        
    def choose_best_movie(self, candidate_ids: list[int]) -> int | None:
        """Возвращает фильм с максимальной популярностью"""
        if len(candidate_ids) == 0:
            return None
        
        best_movie = None
        best_popular = -1
        
        for movie_id in candidate_ids:
            popularity = self.calculate_global_popularity(movie_id)
            if popularity > best_popular:
                best_popular = popularity
                best_movie = movie_id
        return best_movie
        
        
    def recommend_for(self, user_history: UserHistory) -> Movie | None:
        """Объединяет шаги 1–4"""
        similar_users = self.get_similar_users(user_history)
        candidates = self.get_candidate_movies(user_history, similar_users)
        movie_id = self.choose_best_movie(candidates)
        
        if movie_id == None:
            return None
        
        return self.movie_repo.get_movie_by_id(movie_id)
            
        


        
class Application:
    """Точка входа - взаимодействие с пользователем"""
    
    MOVIES_FILE = 'films.txt'
    HISTORY_FILE = 'users_history.txt'
    
    def __init__(self):
        #создаем репозитории
        self.movie_repo = MovieRepository()
        self.history_repo = HistoryRepository()
        
        #загружаем данные из файлов
        self.movie_repo.load_from_file(self.MOVIES_FILE)
        self.history_repo.load_from_file(self.HISTORY_FILE)
        
        #создаем рекомендации
        self.engine = RecomendationEngine(
            movie_repo=self.movie_repo,
            history_repo=self.history_repo,
            similarity_calculator=SimilarityCalculator
        )
        
    def run(self):
        """Главный запуск приложения"""
        print("Введите список просмотренных фильмов через запятую (например, 2,4):")
        
        user_input = input().strip()
        
        if not user_input:
            print("Пустой ввод - рекомендации невозможны")
            return True
        try:
            movie_ids = [int(x) for x in user_input.split(',')]
        except ValueError:
            print("Ошибка: введите числа через запятую")
            return True
        
        user_history = UserHistory(movie_ids)
        movie = self.engine.recommend_for(user_history)
        
        if movie is None:
            print("Нет рекомендаций")
        else:
            print(movie.title)
        
        return True
            
        
if __name__ ==  '__main__':
    app = Application()
    app.run()
    
    