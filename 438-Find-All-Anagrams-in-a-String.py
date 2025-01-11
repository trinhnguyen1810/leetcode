class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        \\\
        cabebabacd
       
        create an array 
        get lens
        current_array = [0] * 26
        loop through each string:
            add to the current array:
            if sum current_array > len(p):
                remove the last element s[i] - len(sth)
            check if the current array = len(we check):
            if yes, we add to the res
        return res
                

        \\\
        res = []
        p_list = [0] * 26
        for char in p:
            index = ord(char) - ord(\a\)
            p_list[index] += 1
        
        current_list = [0] * 26
        for i in range (len(s)):
            index = ord(s[i]) - ord(\a\)
            current_list[index] += 1
            if sum(current_list) > len(p):
                remove_char = s[i - len(p)]
                remove_index = ord(remove_char) - ord(\a\)
                current_list[remove_index] -= 1
            if  current_list == p_list:
                res.append(i-len(p)+1)
        return res
                
            
                
                