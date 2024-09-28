sum = 10
def ab(a, b):
    global sum
    sum = a + b
    return sum

c = ab(3, 5)
print(c)
print(sum)