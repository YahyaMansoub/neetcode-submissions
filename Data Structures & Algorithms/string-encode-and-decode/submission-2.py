from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        res += str(len(strs))

        for s in strs:
            n = len(s)
            res += "#" + str(n) + "#"
            res += s

        return res


    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []

        res = []
        i = 0

        while s[i] != "#":
            i += 1

        number_of_strings = int(s[:i])

        for _ in range(number_of_strings):
            i += 1

            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            res.append(s[i:i + length])

            i += length

        return res 