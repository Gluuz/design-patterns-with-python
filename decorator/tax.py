from abc import ABC, abstractmethod


class BaseTax(ABC):
    def __init__(self, another_tax=None):
        self._another_tax = another_tax or None

    @abstractmethod
    def calculate(self, budget: int):
        pass

    def calculate_another_tax(self, budget: int):
        if self._another_tax is None:
            return 0
        return self._another_tax.calculate(budget)


class IncomeTax(BaseTax):
    def calculate(self, budget: int):
        return budget * 0.10 + self._another_tax.calculate_another_tax(budget)


class XptoTax(BaseTax):
    def calculate(self, budget: int):
        return budget * 0.12 + self._another_tax.calculate_another_tax(budget)
