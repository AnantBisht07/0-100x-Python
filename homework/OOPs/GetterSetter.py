class GetterSetter:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):             #Getter runs when you read the Account
        return self._balance
    
    @balance.setter
    def balance(self, )