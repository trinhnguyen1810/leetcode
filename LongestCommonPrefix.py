#Week 1
#LONGEST COMMON PREFIX
"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.\

Input: strs = ["flower","flow","flight"]
initialize low 

 
"""
def isCommonPrefix(strs,l):
    str1= strs[0][:l]
    for i in range(1,len(strs)):
        if not strs[i].startswith(str1):
            return False
        return True
    
def longestCommonPrefix(strs):
    if not strs:
        return ""
    minLen = min(len(x) for x in strs)
    low,high = 1, minLen
    while low <= high:
        middle = (low+high)//2
        if isCommonPrefix(strs, middle):
            low = middle +1
        else:
            high = middle -1
    return strs[0][:(low+high)//2]
-
