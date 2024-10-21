from unittest import TestCase
import runner

class TournamentTest(TestCase):

    def setUp(self):
        self.Useyn = runner.Runner('Усэйн', 10)
        self.Andrey = runner.Runner("Андрей", 9)
        self.Nick = runner.Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results.items():
            print(i)

    def test_1(self):
         t1 = runner.Tournament(90, self.Useyn, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')

    def test_2(self):
         t1 = runner.Tournament(90, self.Andrey, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')


    def test_3(self):
         t1 = runner.Tournament(90, self.Andrey, self.Useyn, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')


if __name__ == '__main__':
    unittest.main