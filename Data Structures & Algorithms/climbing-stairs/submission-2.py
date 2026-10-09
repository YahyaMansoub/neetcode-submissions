class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        
        if n==0 or n==1:
            return n

        dp[0]=1
        dp[1]=2

        for i in range(n-2):
            dp[i+2]=dp[i+1]+dp[i]
        
        return dp[-1]
