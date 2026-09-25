class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        def bt(idx, path, r):

            if r == 0:
                res.append(path[:])
                return 

            for i in range(idx , len(nums)):

                if nums[i] > r:
                    break

                path.append(nums[i])
                bt(i, path, r - nums[i])
                path.pop()

        bt(0, [], target)

        return res 


        