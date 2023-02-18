from chain_of_responsibility.budget import Budget
from chain_of_responsibility.discount import DiscountForMoreThanFiveItems


class ChainOfDiscountCalculator:
    @staticmethod
    def calculate(budget: Budget) -> int:
        discount = DiscountForMoreThanFiveItems().calculate(budget)
        return discount
