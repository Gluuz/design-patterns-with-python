from abc import ABC, abstractmethod

from template_method.budget import Budget


class TemplateTaxCondition(ABC):
    def calculate(self, budget: Budget):

        if self._should_use_max_tax(budget):
            return self._max_tax(budget)
        return self._min_tax(budget)

    @abstractmethod
    def _should_use_max_tax(self, budget: Budget):
        pass

    @abstractmethod
    def _max_tax(self, budget: Budget):
        pass

    @abstractmethod
    def _min_tax(self, budget: Budget):
        pass


class IncomeTax(TemplateTaxCondition):
    def _should_use_max_tax(self, budget: Budget):
        return budget.value > 2000

    def _max_tax(self, budget: Budget):
        return budget.value * 0.10

    def _min_tax(self, budget: Budget):
        return budget.value * 0.02


class XptoTax(TemplateTaxCondition):
    def _should_use_max_tax(self, budget: Budget):
        return budget.value > 5000 and budget.total_itens >= 5

    def _max_tax(self, budget: Budget):
        return budget.value * 0.20

    def _min_tax(self, budget: Budget):
        return budget.value * 0.10
