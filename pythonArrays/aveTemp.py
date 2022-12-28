import numpy as np 

numberOfDays = int(input("How many days do you want to submit the temperature? "))

for i in range(0,numberOfDays):
    temp = int(input(f"What is the temperature for day #{i+1}: "))