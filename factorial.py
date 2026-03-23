def fact(n):
    if n==1 or n==0:
        n=1
        return n 
    s=fact(n-1)
    return s*n
n=int(input("enter the number"))
print(fact(n))
