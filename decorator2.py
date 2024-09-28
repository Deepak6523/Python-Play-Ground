import time
# print(time.time())

def tmeas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print( end - start)
        return result
    return wrapper

@tmeas
def fibo(n):
    if n <= 0:
        print ("Majak mat kr bro.....")
    elif(n == 1 ):
        return 0 
    elif (n == 2):
        return 1
    else:
        return fibo(n-1) + fibo ( n-2 )




# def sum(n):
#     if n <= 1:
#         return 1
    
#     return n + sum(n - 1)
# def pause():
#     time.sleep(2)
#     print("pause function ended")

@tmeas
def quick():
    print("quick function ended")

for i in range (1, 15 , 1):
    print(fibo(i),end=" ")
# print(sum(10))
# pause()
quick()
    