def dec2binary(n):
    if n==0:
        return 0
    else:
        return (n%2) + 10* dec2binary(n//2)

print(dec2binary(23))