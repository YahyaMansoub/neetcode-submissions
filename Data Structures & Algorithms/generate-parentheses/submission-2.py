class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def bt(p , o, c):

            if len(p) == 2*n:
                res.append(p)
                return 

            if o < n:
                bt(p+"(", o+1, c)

            if c < o:
                bt(p+")", o, c+1)

        bt("", 0, 0)


        return res