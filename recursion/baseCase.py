def baseCase1(number):
    if number>1:
        print("base case reached")
    else:
        baseCase1(number-1)
        print(number)

