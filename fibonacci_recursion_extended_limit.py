fibo = {}
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    elif n in fibo:
        return fibo[n]
    else:
        result = Fibonacci(n-1)+Fibonacci(n-2)
        fibo[n] = result
        return result

print(Fibonacci(10))
print(Fibonacci(100))
print(Fibonacci(150))
print(Fibonacci(200))
print(Fibonacci(250))
print(Fibonacci(300))
print(Fibonacci(400))
print(Fibonacci(500))
print(Fibonacci(600))
print(Fibonacci(1000))
print(Fibonacci(1500))
print(Fibonacci(2000))
print(Fibonacci(2500))
print(Fibonacci(3000))
print(Fibonacci(3500))
print(Fibonacci(4000))
print(Fibonacci(4500))
print(len(str(Fibonacci(4782))))
