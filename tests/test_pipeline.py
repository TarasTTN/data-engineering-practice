from decimal import Decimal

def test_environment_smoke():
    """Базовый дымовой тест окружения."""
    assert True

def test_data_types_integrity():
    """Проверка точности финансовых расчетов Decimal."""
    amount_1 = Decimal("1500.50")
    amount_2 = Decimal("499.50")
    total = amount_1 + amount_2
    assert total == Decimal("2000.00")
