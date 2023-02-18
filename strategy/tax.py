# Functional Approach
def calculates_income_tax(value: int):
    return value * 0.10


def calculate_xpto_tax(value: int):
    return value * 0.12


# OOP Approach
class IncomeTax:
    @staticmethod
    def calculate(value: int):
        return value * 0.10


class XptoTax:
    @staticmethod
    def calculate(value: int):
        return value * 0.12
