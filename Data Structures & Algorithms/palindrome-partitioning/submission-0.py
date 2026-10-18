class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def checkpal(s):
            return s==s[::-1]

        res = []
        p = []
        def bt(idx):
            

            if idx == len(s):
                res.append(p[:])
                return 

            for i in range(idx+1,len(s)+1):
                sub = s[idx:i]

                if checkpal(sub):
                    p.append(sub)

                    bt(i)

                    p.pop()

        bt(0)

        return res


        

                