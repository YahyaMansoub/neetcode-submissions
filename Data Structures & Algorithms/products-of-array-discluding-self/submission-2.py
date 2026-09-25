class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [
            nums[0]
        ]
        suffix = [
            nums[-1]
        ]

        n = len(nums)

        for i in range(1, n): 
            prefix.append(prefix[i-1]*nums[i])
            suffix.append(suffix[i-1]*nums[-i-1])
        
        suffix.reverse()
        return [suffix[1]] + [
            prefix[i-1] * suffix[i+1]
            for i in range(1, n-1)
        ] + [prefix[n-2]] 

        

        

      