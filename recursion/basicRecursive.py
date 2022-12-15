def first():
    second()
    print("This the first print statement, i should be printed last")

def second():
    third()
    print("This the second print statement, i should be printed 3rd")

def third():
    fourth()
    print("This the third print statement; i should be printed 2nd")

def fourth():
    print("this the base case")

