def powerofNums(n,power):
    assert int(n)== n and power>0, 'error with entries'
    if power == 1:
        return n 
    else:
        return n * powerofNums(n,power-1)
print(powerofNums(2,6))