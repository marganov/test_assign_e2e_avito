import pytest
from discount_calculator import DiscountCalculator

@pytest.mark.positive
class TestDiscountCalculatorPositive:
    def test_fixed_data(self, fixed_test_data, discount_calculator):
        """Проверка расчета скидки на фиксированных тестовых данных"""
        for points, expected_discount in fixed_test_data:
            calculator = discount_calculator(points)  # Создаём объект DiscountCalculator
            actual_discount = calculator.get_discount()  # Вызываем метод 1 раз
            assert actual_discount == expected_discount, (
                f"Ошибка для {points} очков: ожидалось {expected_discount}, получено {actual_discount}"
            )
        print("Тест фиксированных граничных значений успешен.")

    def test_random_data(self, random_test_data, discount_calculator):
        """Проверка расчета скидки на сгенерированных данных"""
        for points, expected_discount in random_test_data:
            calculator = discount_calculator(points)
            actual_discount = calculator.get_discount()
            assert actual_discount == expected_discount, (
                f"Ошибка для {points} очков: ожидалось {expected_discount}, получено {actual_discount}"
            )
            
        print(f"Тест рандомных валидных значений успешен: очков {points}, скидка {expected_discount}")
            
@pytest.mark.negative
class TestDiscountCalculatorNegative:
    def test_invalid_data(self, invalid_test_data, discount_calculator):
        for points in invalid_test_data:
            with pytest.raises(ValueError,match="Invalid points value") as excinfo:
                calculator = discount_calculator(points)
                calculator.get_discount()
            print(f"Тест невалидных значений успешен, получено: {excinfo.value}")