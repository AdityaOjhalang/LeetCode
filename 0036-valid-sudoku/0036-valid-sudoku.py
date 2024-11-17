class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row] or val in cols[col] or val in boxes[row//3,col//3]:
                    return False
                
                rows[row].add(val)
                cols[col].add(col)
                boxes[row//3,col//3].add(val)
        return True