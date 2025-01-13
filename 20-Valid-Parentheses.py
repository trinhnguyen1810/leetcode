class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {\)\: \(\, \}\: \{\, \]\: \[\}
        for i in s:
            if i in mapping:
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
 
                
    
\\\ 
Pseudocode:
1. initialize a stack = []{}[]
({})
2. iterate through
3. check: 
4. - if its an open bracket: just add it in the stack
   - if its a closing bracket:
        - check if the stack still have some valiables and the stack[-1] is equal to the closing -> if so pop it
        - if not then return false
    - if there are still elements return False else return Trye

\\\