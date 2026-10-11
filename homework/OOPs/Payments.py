class Paypal:
    
    def pay(self):
        print("Paying using PayPal")


class CreditCard:
    def pay(self):
        print("Paying using CreditCard")


class UPI:
    def pay(self):
        print("Paying using UPI")

# we're using polymorphism by using duck typing
def paymentprocess(payment):
    payment.pay()

paymentprocess(UPI())
paymentprocess(CreditCard())
paymentprocess(Paypal())