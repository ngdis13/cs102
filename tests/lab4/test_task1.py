import unittest
from src.lab4.task1.main import (
    Movie, MovieRepository,
    UserHistory, HistoryRepository,
    SimilarityCalculator, RecomendationEngine
)

class TestMovieRepository(unittest.TestCase):

    def test_get_movie_by_id(self):
        """Проверяет, что MovieRepository корректно возвращает фильм по его ID"""
        repo = MovieRepository()
        repo.movies = [
            Movie(1, "Test movie"),
            Movie(2, "Another one")
        ]

        movie = repo.get_movie_by_id(2)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, "Another one")


class TestUserHistory(unittest.TestCase):

    def test_unique_movies(self):
        """Проверяет, что UserHistory удаляет дубли и возвращает только уникальные ID фильмов"""
        history = UserHistory([1, 2, 2, 3])
        self.assertEqual(history.get_unique_movies(), {1, 2, 3})


class TestSimilarity(unittest.TestCase):

    def test_similarity(self):
        """Проверяет корректность расчёта коэффициента схожести между пользователями"""
        base = UserHistory([1, 2, 3])
        other = UserHistory([2, 3, 4])

        sim = SimilarityCalculator.calculate_similarity(base, other)
        self.assertEqual(sim, 2/3)


class TestRecommendationEngine(unittest.TestCase):

    def test_choose_best_movie(self):
        """Проверяет, что выбирается фильм с максимальной популярностью (встречаемостью)"""
        movie_repo = MovieRepository()
        movie_repo.movies = [
            Movie(1, "A"),
            Movie(2, "B"),
            Movie(3, "C")
        ]

        history_repo = HistoryRepository()
        history_repo.histories = [
            UserHistory([1, 2]),
            UserHistory([2, 3]),
            UserHistory([2])
        ]

        engine = RecomendationEngine(movie_repo, history_repo, SimilarityCalculator)

        best = engine.choose_best_movie([1, 2, 3])
        self.assertEqual(best, 2)  # фильм 2 встречается чаще всего


    def test_recommendation_simple(self):
        """Проверяет, что метод recommend_for возвращает правильный рекомендованный фильм"""
        movie_repo = MovieRepository()
        movie_repo.movies = [
            Movie(1, "Movie1"),
            Movie(2, "Movie2"),
            Movie(3, "Movie3")
        ]

        history_repo = HistoryRepository()
        history_repo.histories = [
            UserHistory([1, 2]),
            UserHistory([2, 3]),
        ]

        engine = RecomendationEngine(movie_repo, history_repo, SimilarityCalculator)

        user = UserHistory([1])  # Пользователь видел только фильм 1
        recommended = engine.recommend_for(user)

        self.assertIsNotNone(recommended)
        self.assertEqual(recommended.title, "Movie2")  # Самый популярный среди похожих пользователей


if __name__ == "__main__":
    unittest.main()