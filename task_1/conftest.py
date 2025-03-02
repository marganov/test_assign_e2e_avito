import pytest

from discount_calculator import DiscountCcalculator
from data_provider import DataProvider

# Фикстура для представления DiscountCcalculator
@pytest.fixture
def discount_calculator():
    return DiscountCcalculator

# Фикстура для представления DataProvider
@pytest.fixture
def data_provider():
    return DataProvider

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

# Фикстура для позитивных тестов
@pytest.fixture(scope="class", params=[
    ("fixed", "fixed_test_data"),
    ("random", "random_test_data")
], ids=["fixed_positive", "random_positive"])
def positive_tests(request, data_provider):
    test_type, data_fixture = request.param
    return getattr(data_provider,data_fixture.replace("_test_data", ""))()

# Фикстура для негативных тестов
@pytest.fixture(scope="class", params=[
    ("invalid", "invalid_test_data")
], ids=["invalid_negative"])
def negative_tests(request, data_provider):
    test_type, data_fixture = request.param
    return getattr(data_provider, data_fixture.replace("_test_data", ""))()