class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def robber(arr):
            m = len(arr)

            if m == 1:
                return arr[0]

            dp = [0] * m

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, m):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + arr[i]
                )

            return dp[m - 1]

        return max(
            robber(nums[:-1]),  # don't use last house
            robber(nums[1:])    # don't use first house
        )