import pytest

# Позитивные тесты
@pytest.mark.positive
class TestPositiveCases:
    def test_discount_calculation_fixed(self, positive_tests, discount_calculator):
        for points, expected_discount in positive_tests:
            calculator = discount_calculator(points)
            assert calculator.get_discount() == expected_discount

    def test_discount_calculation_random(self, positive_tests, discount_calculator):
        for points, expected_discount in positive_tests:
            calculator = discount_calculator(points)
            assert calculator.get_discount() == expected_discount

# Негативные тесты
@pytest.mark.negative
class TestNegativeCases:
    def test_discount_calculation_invalid(self, negative_tests, discount_calculator):
        for points, expected_discount in negative_tests:
            calculator = discount_calculator(points)
            if points < 0:
                with pytest.raises(ValueError):
                    calculator.get_discount()
            else:
                assert calculator.get_discount() == expected_discount