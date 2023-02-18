from strategy.functional_approach.tax import calculates_income_tax, calculate_xpto_tax, IncomeTax, XptoTax
from strategy.functional_approach.tax_calculator import TaxCalculator


# Functional approach
def test_should_calculate_income_tax_with_correctly_percentage():
    tax_calculator = TaxCalculator()
    income_tax = tax_calculator.calculate_tax(budget=500, tax=calculates_income_tax)
    assert income_tax == 50.0


def test_should_calculate_xpto_tax_with_correctly_percentage():
    tax_calculator = TaxCalculator()
    income_tax = tax_calculator.calculate_tax(budget=500, tax=calculate_xpto_tax)
    assert income_tax == 60.0


# OOP approach


def test_should_calculate_income_tax_with_correctly_percentage():
    tax_calculator = TaxCalculator()
    income_tax = tax_calculator.calculate_tax(budget=500, tax=IncomeTax().calculate)
    assert income_tax == 50.0


def test_should_calculate_xpto_tax_with_correctly_percentage():
    tax_calculator = TaxCalculator()
    income_tax = tax_calculator.calculate_tax(budget=500, tax=XptoTax().calculate)
    assert income_tax == 60.0
