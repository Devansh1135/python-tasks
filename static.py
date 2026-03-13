from abc import ABC , abstractmethod

class PaymentProcessor:
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process_payment(self , amount):
        pass

    @abstractmethod
    def refund(self , transaction_id):
        pass

    def log_transactions(self, details):
        pass

class CreditCardProcessor(PaymentProcessor):
     def validate(self, card_number):
        if len(card_number) == 16 and isinstance(card_number , int):
            return "Validation successful"
        
class PayPalProcessor(PaymentProcessor):
    def validate(self , paypal_id):
        if len(paypal_id) == 10 and paypal_id.isalnum():
            return "Validation successful"

class CryptoProcessor(PaymentProcessor):
    def validate(self, wallet_address):
        if len(wallet_address) > 26 :
            return "Validation successful"
        

