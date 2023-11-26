class ConvertirDivisas:
    def convert_currency(self, amount):
        pass

# Simular la tasa de conversión COP a USD (3000 COP = 1 USD)
class COPtoUSD(ConvertirDivisas):
    def convert_currency(self, amount):
        return amount / 3000

class CurrencyConverter:
    def __init__(self, strategy):
        self.strategy = strategy

    def convert(self, amount):
        return self.strategy.convert_currency(amount)