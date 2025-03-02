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
            (200, 5),
            (201, 5),
            (499, 5),
            (500, 10),
            (501, 10)
        ]
    
    def get_fixed_test_data(self):
        """ Метод возвращает фиксированый набор граничных значений"""
        return self.fixed_test_data
    
    def get_random_test_data(self, num_samples=10):
        """ Метод генерирует по 10 сэмплов случайных данных"""
        random_data = []
        for _ in range(num_samples):
            points = random.randint(0, 1000)
            if points < 100:
                discount = 1
            elif points < 200:
                discount = 3
            elif points < 500:
                discount = 5
            else:
                discount = 10
            random_data.append((points, discount))
        return random_data
    
    def get_invalid_test_data(self, num_samples=3):
        """ Метод генерирует по 3 семпла невалидных значений"""
        invalid_data=[]
        for _ in range(num_samples):
            points = random.randint(-100, -1)
            invalid_data.append((points, "Invalid data, check points!"))
        return invalid_data