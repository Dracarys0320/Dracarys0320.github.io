from Strategy import COPtoUSD, CurrencyConverter
from Adapter import Pago_Principal, PayU, MercadoPago, PayPal, PayPalAdapter

def main():
    print("Métodos de Pago Disponibles:")
    print("1. PayU")
    print("2. MercadoPago")
    print("3. PayPal")

    choice = input("Seleccione el método de pago (1/2/3): ")
    amount_cop = float(input("Ingrese el monto en pesos COP: "))

    if choice == "1":
        payment_gateway = PayU()
    elif choice == "2":
        payment_gateway = MercadoPago()
    elif choice == "3":
        paypal = PayPal()
        payment_gateway = PayPalAdapter(paypal)
    else:
        print("Método de pago no válido.")
        return

    payment_gateway.process_payment(amount_cop)
    
    strategy = COPtoUSD()
    converter = CurrencyConverter(strategy)
    amount_usd = converter.convert(amount_cop)

    print(f"Monto en pesos COP: {amount_cop}")
    print(f"Monto en dólares USD: {amount_usd:.2f}")

if __name__ == "__main__":
    main()
