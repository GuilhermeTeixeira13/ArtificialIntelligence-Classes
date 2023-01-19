class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()

        def dfs(i, j, char_pos):
            if char_pos == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[char_pos] != board[i][j] or (
            i, j) in visited:
                return False

            visited.add((i, j))
            res = dfs(i - 1, j, char_pos + 1) or \
                  dfs(i, j - 1, char_pos + 1) or \
                  dfs(i, j + 1, char_pos + 1) or \
                  dfs(i + 1, j, char_pos + 1)
            visited.remove((i, j))
            return res

        for line in range(len(board)):
            for col in range(len(board[0])):
                if dfs(line, col, 0):
                    return True
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
