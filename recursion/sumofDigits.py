def sumofDigits(n):
    if n ==0: 
        return n
    else:
        return n%10 + sumofDigits(n//10)

print(sumofDigits(-4291))
