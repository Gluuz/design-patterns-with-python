from chain_of_responsibility.budget import Budget


class DiscountForMoreThanFiveItems:
    @staticmethod
    def calculate(budget: Budget):
        if budget.total_itens > 5:
            return budget.value * 0.10
        return DiscountForMoreThanFiveHundredSpent.calculate(budget)


class DiscountForMoreThanFiveHundredSpent:
    @staticmethod
    def calculate(budget: Budget):
        if budget.value > 500:
            return budget.value * 0.07
        return NoDiscount.calculate()


class NoDiscount:
    @staticmethod
    def calculate():
        return 0
