def fibonacci(n):
    if n <= 1:
       return n
    else:
       return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(40))

def fibo_lijst(n):
    lijst = list()
    for i in range(n):
      lijst.append(fibonacci(i))
    return lijst

print(fibo_lijst(50))