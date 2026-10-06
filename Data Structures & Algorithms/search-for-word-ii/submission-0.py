class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = Node()

            curr = curr.children[idx]

        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        tree = Trie()

        for word in words:
            tree.insert(word)

        res = []

        def dfs(r, c, node, word):
            
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == "#"
            ):
                return

            char = board[r][c]
            idx = ord(char) - ord('a')

            
            if node.children[idx] is None:
                return

            node = node.children[idx]

            word += char

            if node.end:
                res.append(word)

                node.end = False

            board[r][c] = "#"

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Restore
            board[r][c] = char

        # Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, tree.root, "")

        return res

            
        