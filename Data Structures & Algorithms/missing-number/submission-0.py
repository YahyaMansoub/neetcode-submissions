class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        x1, x2 = 0, 0
        for n in nums:
            x1^=n

        for i in range(len(nums)+1):
            x2^=i

        return x1^x2