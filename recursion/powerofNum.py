def powerofNums(n,power):
    if power == 1:
        return n 
    else:
        return n * powerofNums(n,power-1)
print(powerofNums(5,6))