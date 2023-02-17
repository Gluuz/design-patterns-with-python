from strategy.functional_approach.tax import calculates_income_tax
from strategy.functional_approach.tax_calculator import TaxCalculator
def test_should_calculate_income_tax_with_correctly_percentage():
    tax_calculator = TaxCalculator()
    income_tax = tax_calculator.calculate_tax(budget=500, tax=calculates_income_tax)
    assert income_tax == 50.0

