class Solution:
    def isValid(self, s: str) -> bool:
        flags = {'(': ')', '{': '}', '[' :  ']'}
        stack = []

        for c in s:
            if c in flags:
                stack.append(c)
            else:
                if not stack or flags[stack.pop()] != c :
                    return False
                    

        return len(stack)==0
