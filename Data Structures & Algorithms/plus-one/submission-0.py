class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nber = 0

        for i in range(len(digits)):
            nber+=digits[len(digits)-i-1]*(10**i)
        nber+=1
        res = []
        while nber > 0:
            digit = nber%10
            nber //= 10

            res.append(digit)

        return res[::-1]

