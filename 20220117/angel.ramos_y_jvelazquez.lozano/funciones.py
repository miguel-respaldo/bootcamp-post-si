def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def fact(n):
    if n==0 or n==1:
        res =1
    elif n>1:
        res=n*fact(n-1)
    return res
