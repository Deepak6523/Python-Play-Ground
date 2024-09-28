class abc:
    def __init__(self):
        self.__balance__ = 0

    def deposit(self, amount):
        self.__balance__ += amount
        return True
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance__:
            self.__balance__ -= amount
            return True
        else:
            return False
    
    def get(self):
        return self.__balance__

_amount_ = abc()
print(_amount_.get())

_amount_.deposit(100000)
print(_amount_.get())

_amount_.withdraw(10000)
print(_amount_.get())

_amount_.withdraw(100)
print(_amount_.get())

# declare_Class = abc()
# value = declare_Class.get()
# print(value)