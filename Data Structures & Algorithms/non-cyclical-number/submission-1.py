class Solution:
    def next(self, n):
        res = 0

        while n > 0:
            res += (n % 10) ** 2
            n //= 10

        return res

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.next(slow)
            fast = self.next(self.next(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False

