def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print("0")
        return 0
    elif n == 1 or n == 2:
        print("1")
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
def fibo(n):
    a,b=0,1
    print(a,b,end=" ")
    for i in range(2,n):
        c= a+b
        a,b=b,c
        print(c,end=" ")
    return c
