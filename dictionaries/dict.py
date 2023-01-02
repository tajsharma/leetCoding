myDict = {'student1':'Lebron James', 'student2':'Stephen Curry', 'student3':'Kevin Durant'}

#linear search 
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return True
    return False

print(searchDict(myDict,'Lebron J2ames'))


#deletion
print(myDict.popitem())

print(myDict)