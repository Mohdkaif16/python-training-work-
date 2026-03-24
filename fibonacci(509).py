# using recursion function
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter the number"))
print(fib(n))

# without recursion function
def fib(n):
    if n <= 1:
        return n
    a = 0 
    b = 1   
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b
n = int(input("Enter n: "))
print(fib(n))
