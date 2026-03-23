#ITRATIVE METHOD
def climbStairs( n):
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
n=int(input("enter number"))
print(climbStairs(n))
# RECURSION METHOD
def climbs(n):
    if n<=2:
        return n
    return climbs(n-1)+climbs(n-2)
n=int(input("enter the number"))
print(climbs(n))
