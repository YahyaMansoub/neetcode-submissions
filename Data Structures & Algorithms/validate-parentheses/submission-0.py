class Solution:
    def isValid(self, s: str) -> bool:
        flags = {'(': ')', '{': '}', '[' :  ']'}
        stack = []

        for char in s: 
            if char in flags: 
                stack.append(char)
            elif not stack or flags[stack.pop()]!=char:
                return False
        return not stack 
