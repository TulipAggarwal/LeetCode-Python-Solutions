class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxes = [set() for x in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                if board[i][j] in boxes[(i//3)*3+(j//3)]:
                    return False
                boxes[(i//3)*3+(j//3)].add(board[i][j])
        return True
