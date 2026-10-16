class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []



        def bt(i, curr, S):

            if S == target:
                res.append(curr[:])
                return 
            elif S > target:
                return 
            

            for idx in range(i, len(nums)):
                curr.append(nums[idx])
                S+=nums[idx]

                bt(idx, curr, S)

                curr.pop()
                S-=nums[idx]

        bt(0, [], 0)
        return res 
        
                
        


        