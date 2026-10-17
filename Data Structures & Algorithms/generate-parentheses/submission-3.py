class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        


        res = []

        def bt(curr, l, r):

            if l==r and len(curr)==2*n:
                res.append(curr)
                return
            if l < n:
                bt(curr+"(", l+1, r)
            if r < l:
                bt(curr+")", l, r+1)

        bt("", 0, 0)

        return res 


        