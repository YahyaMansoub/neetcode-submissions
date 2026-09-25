class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def bt(idx, p):

            res.append(p[:])

            for i in range(idx, len(nums)):

                if i > idx and nums[i] == nums[i-1]:
                    continue 
                p.append(nums[i])
                bt(i+1, p)
                p.pop()

        bt(0, [])
        return res 