def factorial(n):
    if n <= 1:
        return 1 
    elif n%1 != 0:
        return "Ur number was a decimal"
    else:
        return n * factorial(n-1)


        
print(factorial(3))