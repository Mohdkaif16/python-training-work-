#print 1 to N
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)  
    print(n)
    return n
n =int(input("enter the number\n"))
print_numbers(n)
#print N to 1
def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)
n =int(input("enter the number\n"))
print_reverse(n)
#sum of all element of the array recursivly
def sum(l):
    if len(l) == 1:
        return l[0]
    return l[0]+sum(l[1:])
l=[]    
n =int(input("enter the number of items \n"))
for i in range(n):
    x=int(input("enter the number"))
    l.append(x)
print("list",l)    
print("sum",sum(l))
