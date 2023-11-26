class Pago_Principal:
    def process_payment(self, amount):
        pass

class PayU(Pago_Principal):
    def process_payment(self, amount):
        print(f"Procesando pago en PayU por {amount} COP")

class MercadoPago(Pago_Principal):
    def process_payment(self, amount):
        print(f"Procesando pago en MercadoPago por {amount} COP")

class PayPal:
    def make_payment(self, amount):
        print(f"Procesando pago en PayPal por {amount} USD")

class PayPalAdapter(Pago_Principal):
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self, amount):
        amount_usd = amount / 3000
        self.paypal.make_payment(amount_usd)

