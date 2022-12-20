def sumofDigits(n):
    if len(n) ==1: 
        return n
    else:
        return n%10 + sumofDigits(n/10)

print(sumofDigits(22))
