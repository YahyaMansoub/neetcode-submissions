class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
        used = [False]*len(nums)


        def bt( p):
            if len(p) == len(nums):
                res.append(p[:])
                return 
            for i in range(len(nums)):
                if used[i]: continue 

                used[i]= True 
                p.append(nums[i])
                bt(p)
                p.pop()
                used[i] = False

        bt([])
        return res 
        