pi = 3.1415926535897932384626433832795028841

print(f"{pi: 23f}")

sqr = lambda x, y: x * y

# num = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# print(f"{num} * {num2} is {sqr(num, num2)}")

print(f"{sqr(int(input('Enter a number : ')), int(input("Enter a number : ")))}")