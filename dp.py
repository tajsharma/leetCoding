def climbStairs(num):
    if num > 45: return False

    one,two = 1,1

    for i in range(num-1):
        temp = one
        one = one +two
        two = temp

    return one


print(climbStairs(5))