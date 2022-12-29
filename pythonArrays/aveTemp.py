import numpy as np 

numberOfDays = int(input("How many days do you want to submit the temperature? "))
tempArray = [None]*numberOfDays
count = 0

for i in range(0,numberOfDays):
    temp = int(input(f"What is the temperature for day #{i+1}: "))
    tempArray[i] = temp

print(f"The average temp over {len(tempArray)} day(s) was: {sum(tempArray)/len(tempArray)} degrees")

for temps in tempArray:
    if temps > sum(tempArray)/len(tempArray):
        count +=1

print(f"There were {count} day(s) where the temp was higher than average")
