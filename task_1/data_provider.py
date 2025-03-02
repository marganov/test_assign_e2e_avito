import random

class DataProvider:
    def __init__(self):
        self.fixed_test_data = [
            (0, 1),
            (1, 1),
            (99, 1),
            (100, 1),
            (101, 3),
            (199, 3),
            (200, 3),
            (201, 5),
            (499, 5),
            (500, 5),
            (501, 10)
        ]
    
    def get_fixed_test_data(self):
        """ Метод возвращает фиксированый набор граничных значений"""
        return self.fixed_test_data
    
    def get_random_test_data(self, num_samples=10):
        """ Метод генерирует по 10 сэмплов случайных данных"""
        random_data = []
        for _ in range(num_samples):
            points = random.randint(0, 10000)
            if 0 <= points <= 100:
                discount = 1
            elif 101 <= points <= 200:
                discount = 3
            elif 201 <= points <= 500:
                discount = 5
            else:
                discount = 10
            random_data.append((points, discount))
        return random_data
    
    def get_invalid_test_data(self, num_samples=3):
        """ Метод генерирует по 3 сэмпла невалидных значений"""
        return [random.randint(-100, -1) for _ in range(num_samples)]
