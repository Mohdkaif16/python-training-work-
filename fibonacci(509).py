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
# using dynamic programming 
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]   # moved up (only placement fix)

        def fib(n, dp):                  # wrapped your same function
            if n == 0 or n == 1:
                return n

            if dp[n] != -1:
                return dp[n]

            if dp[n - 1] == -1:
                ans1 = fib(n - 1, dp)
                dp[n - 1] = ans1
            else:
                ans1 = dp[n - 1]

            if dp[n - 2] == -1:
                ans2 = fib(n - 2, dp)
                dp[n - 2] = ans2
            else:
                ans2 = dp[n - 2]

            dp[n] = ans1 + ans2
            return dp[n]

        ans = fib(n, dp)
        return ans
