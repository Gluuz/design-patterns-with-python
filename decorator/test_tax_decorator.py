from decorator.budget import Budget
from decorator.item import Item
from decorator.tax import IncomeTax, XptoTax
from decorator.tax_calculator import TaxCalculator


def test_should_use_income_tax_and_xpto_tax():
    tax_calculator = TaxCalculator()
    budget = Budget()
    budget.add_item(Item("ITEM 1", 500))
    budget.add_item(Item("ITEM 2", 500))
    budget.add_item(Item("ITEM 3", 5000))
    budget.add_item(Item("ITEM 4", 50))

    tax = tax_calculator.calculate_tax(budget, IncomeTax(XptoTax()))
    assert tax == 605.0


def test_should_use_xpto_tax_and_income_tax():
    tax_calculator = TaxCalculator()
    budget = Budget()
    budget.add_item(Item("ITEM 1", 500))
    budget.add_item(Item("ITEM 2", 500))
    budget.add_item(Item("ITEM 3", 5000))
    budget.add_item(Item("ITEM 4", 50))

    tax = tax_calculator.calculate_tax(budget, XptoTax(IncomeTax()))
    assert tax == 726.0
