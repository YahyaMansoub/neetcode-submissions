class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = Node()

            curr = curr.children[idx]

        curr.end = True


    def search(self, word: str) -> bool:

        def dfs(i, curr):

            # We consumed the entire search word
            if i == len(word):
                return curr.end

            c = word[i]

            # Wildcard: try every possible letter
            if c == '.':
                for child in curr.children:
                    if child and dfs(i + 1, child):
                        return True

                return False

            # Normal character
            idx = ord(c) - ord('a')

            if not curr.children[idx]:
                return False

            return dfs(i + 1, curr.children[idx])

        return dfs(0, self.root)























