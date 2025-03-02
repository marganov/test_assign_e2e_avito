import pytest
from data_provider import DataProvider
from discount_calculator import DiscountCalculator


# Фикстура для создания экземпляра DiscountCalculator
@pytest.fixture
def discount_calculator():
    def _create(points):
        return DiscountCalculator(points)
    return _create

# Фикстура для представления DataProvider
@pytest.fixture
def data_provider():
    return DataProvider()

# Фикстура для получения фиксированных тестовых данных
@pytest.fixture
def fixed_test_data(data_provider):
    return data_provider.get_fixed_test_data()

# Фикстура для получения случайных тестовых данных
@pytest.fixture
def random_test_data(data_provider):
    return data_provider.get_random_test_data()

# Фикстура для получения невалидных тестовых данных
@pytest.fixture
def invalid_test_data(data_provider):
    return data_provider.get_invalid_test_data()

@pytest.fixture
def invalid_test_data(data_provider):
    return data_provider.get_invalid_test_data()
