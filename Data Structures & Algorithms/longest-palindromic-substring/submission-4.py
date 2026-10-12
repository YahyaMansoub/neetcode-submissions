class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        res = 0
        res_i , res_j = -1, -1

        for i in range(n):
            r= l = i

            while l <= r and r < n and l >=0:
                if s[r]!=s[l]:
                    break 
                else:
                    if res < r-l+1:
                        res_i, res_j = l, r
                        res = r-l+1
                    l-=1
                    r+=1
            l=i
            r=i+1

            while l <= r and r < n and l >=0:
                if s[r]!=s[l]:
                    break 
                else:
                    if res < r-l+1:
                        res_i, res_j = l, r
                        res = r-l+1
                    l-=1
                    r+=1

        if res_i <0 and res_j <0:
            return ""
        return s[res_i:res_j+1]


            

                    



          
                

