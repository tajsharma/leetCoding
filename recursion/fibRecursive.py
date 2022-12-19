def fib(n):
    #assert n==0 and int(n) ==n , 'Cant put 0 or a decimal here brotha'
    if n ==1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

print(fib(8))