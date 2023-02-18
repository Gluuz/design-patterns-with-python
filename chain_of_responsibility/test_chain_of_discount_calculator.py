from unittest.mock import patch

from chain_of_responsibility.budget import Budget
from chain_of_responsibility.discount import (
    DiscountForMoreThanFiveHundredSpent,
    NoDiscount,
)
from chain_of_responsibility.chain_of_discount_calculator import (
    ChainOfDiscountCalculator,
)
from chain_of_responsibility.item import Item


@patch.object(DiscountForMoreThanFiveHundredSpent, "calculate")
@patch.object(NoDiscount, "calculate")
def test_should_use_discount_for_more_than_five_items(
    mock_no_discount, mock_discount_for_more_than_five_hundred
):
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=50))
    budget.add_item(Item(name="XPTO 2", value=50))
    budget.add_item(Item(name="XPTO 3", value=50))
    budget.add_item(Item(name="XPTO 4", value=50))
    budget.add_item(Item(name="XPTO 5", value=50))
    budget.add_item(Item(name="XPTO 6", value=50))

    calculator = ChainOfDiscountCalculator()

    discount = calculator.calculate(budget)

    assert discount == 5.0
    mock_no_discount.assert_not_called()
    mock_discount_for_more_than_five_hundred.assert_not_called()


@patch.object(NoDiscount, "calculate")
def test_should_use_discount_for_more_than_five_hundred(mock_no_discount):
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=501))

    calculator = ChainOfDiscountCalculator()

    discount = calculator.calculate(budget)

    assert discount == 35.07
    mock_no_discount.assert_not_called()


def test_should_use_no_discount_():
    budget = Budget()
    budget.add_item(Item(name="XPTO 1", value=50))

    calculator = ChainOfDiscountCalculator()

    discount = calculator.calculate(budget)

    assert discount == 0
