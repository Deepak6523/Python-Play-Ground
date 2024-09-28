x = lambda a, b : a if a > b else b 
print(x(1, 3))

y = lambda a : print("Odd") if a % 2 != 0 else print("Even")
print(y(8))