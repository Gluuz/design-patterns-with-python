from decorator.budget import Budget
from decorator.tax import BaseTax


class TaxCalculator:
    @staticmethod
    def calculate_tax(budget: Budget, tax: BaseTax):
        return tax.calculate(budget.value)
