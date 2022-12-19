def factorial(n):
    assert n>0 and int(n), 'The number you entered is not a valid number'
    if n <= 1:
        return 1 
    else:
        return n * factorial(n-1)


        
print(factorial(6))