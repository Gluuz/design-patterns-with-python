from typing import Callable


class TaxCalculator:
    @staticmethod
    def calculate_tax(budget: int, tax: Callable):
        return tax(budget)
