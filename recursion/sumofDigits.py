def sumofDigits(n):
    assert n>=0 and int(n)==n, 'Number cant be negative or a decimal'
    if n ==0: 
        return n
    else:
        return n%10 + sumofDigits(n//10)

print(sumofDigits(-4291))
