def fib(n):
    assert n>=0 and int(n)==n , '# gotta be greater than 0 and not a decimal brotha'
    if n ==1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

print(fib(8))