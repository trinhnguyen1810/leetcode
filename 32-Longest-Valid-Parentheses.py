class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  
        max_s = 0

        for i in range(len(s)):
            if s[i] == "(":  
                stack.append(i)
            else:
                stack.pop()  
                if stack:
                    max_s = max(max_s, i - stack[-1])
                else:
                    stack.append(i)

        return max_s
