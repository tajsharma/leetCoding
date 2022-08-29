#leetCode 242: Is anagram
#another way to solve is to simply sort and return if both are equal
#or we can use dictionaries for the counting method
def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26 #creates sempty dictionaries w 26 characters
    for item in s:
        dic1[ord(item)-ord('a')] += 1 #ord() returns number rep of unicode
    for item in t:
        dic2[ord(item)-ord('a')] += 1 
    return dic1 == dic2  #if dicts are equal then it returns true