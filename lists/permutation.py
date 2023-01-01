#implement an algorithm that checks if two strings are a permutation of eachother
# a permutation is same letters in a diff order
#without using dictionary
def permutation(list1, list2):
    if len(list1) != len(list2):
        return 'Not a permutation, the length is different'
    else:
        length = len(list1)
        newList = []
        for i in range(0,length):
            if list1[i] not in newList:
                newList.append(list1[i])
        for j in range(0,length):
            if list2[j] not in newList:
                return 'Not a permutation'
        return 'Is a permutation'

def sortedPerm(list1,list2):
    if len(list1) != len(list2):
        return False
    else:
        list1.sort()
        list2.sort()
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

        


word1 = ['e','v','i','l']
word2 = ['l','o','v','e']
print(permutation(word1,word2))
print(sortedPerm(word1,word2))