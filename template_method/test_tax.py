from chain_of_responsibility.item import Item
from template_method.budget import Budget
from template_method.tax import IncomeTax, XptoTax


def test_income_tax_should_use_max_tax():
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=5000))

    income_tax = IncomeTax()

    tax_is_ten_percentage_of_budget = income_tax.calculate(budget)

    assert tax_is_ten_percentage_of_budget == 500.0


def test_income_tax_should_use_min_tax():
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=500))

    income_tax = IncomeTax()

    tax_is_two_percentage_of_budget = income_tax.calculate(budget)

    assert tax_is_two_percentage_of_budget == 10.0


def test_xpto_tax_should_use_max_tax():
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=5000))
    budget.add_item(Item(name="XPTO 2", value=4000))
    budget.add_item(Item(name="XPTO 3", value=20))
    budget.add_item(Item(name="XPTO 4", value=30))
    budget.add_item(Item(name="XPTO 5", value=10))

    xpto_tax = XptoTax()

    tax_is_twenty_percentage_of_budget = xpto_tax.calculate(budget)

    assert tax_is_twenty_percentage_of_budget == 1812.0


def test_xpto_tax_should_use_min_tax():
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=500))

    xpto_tax = XptoTax()

    tax_is_ten_percentage_of_budget = xpto_tax.calculate(budget)

    assert tax_is_ten_percentage_of_budget == 50.0
