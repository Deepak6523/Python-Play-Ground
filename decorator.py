def xys(function):
    def wrapper():
        function()
    
    return wrapper

@xys
def abc():
    print(10 + 5)

# abc()
xys(abc)