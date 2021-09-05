class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      def dfs(board, row, col, word):
            if len(word) == 0:
              return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[0]:
              return False 
            temp = board[row][col]
            board[row][col] = '#'
            res = dfs(board, row-1, col, word[1:]) or dfs(board, row+1, col, word[1:]) or dfs(board, row, col-1, word[1:]) or dfs(board, row, col+1, word[1:])
            board[row][col] = temp
            return res
            
        if not board:
          return False
        for row in range(len(board)):
          for col in range(len(board[row])):
            if board[row][col] == word[0]:
              if dfs(board, row, col, word):
                return True
        return False 
        
            