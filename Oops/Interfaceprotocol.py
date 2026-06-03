from typing import Protocol
class PaymentProtocol(Protocol):
    def authorize_payment(self, amount: float):
        pass
class CreditCardPayment:
    def authorize_payment(self, amount: float):
        print(f"Credit Card payment authorized for {amount}")
        return True
class PayPalPayment:
    def authorize_payment(self, amount: float):
        print(f"PayPal payment authorized for {amount}")
        return True
def process_order(payment: PaymentProtocol, amount: float):
    if payment.authorize_payment(amount):
        print("Payment successful")
    else:
        print("Payment authorization failed")
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
process_order(credit_card_payment, 100.0)
process_order(paypal_payment, 200.0)