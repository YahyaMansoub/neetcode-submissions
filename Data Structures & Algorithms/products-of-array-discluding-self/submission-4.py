class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        

        pref = [1]*n
        suff = [1]*n


        for i in range(1, n):
            pref[i]=pref[i-1]*nums[i-1]
            suff[n-i-1]=suff[n-i]*nums[n-i]

        return [pref[i]*suff[i] for i in range(n)]

        

      