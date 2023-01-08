myDict = {'MVP1':'Lebron James', 'MVP2':'Stephen Curry', 'MVP3':'Kevin Durant'}

#linear search 
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return True
    return False


print(searchDict(myDict,'Lebron James'))

#deletion
print(myDict.pop('MVP3'))
print(myDict)

#add value
myDict['MVP4'] = 'Lukas Doncic'


copyofDict = myDict.copy()
print(copyofDict)
copyofDict.clear()
print(copyofDict)