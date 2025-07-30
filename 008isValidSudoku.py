class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range(9):
            for j in range(9):
                e=board[i][j]
                if e==".":
                    continue
                if (e + "row " +str(i))  in seen or  (e + "col " +str(j))  in seen or (e + "cube " +str(i//3)+str(j//3)) in seen:
                    return False
                seen.add(e + "row " +str(i))
                seen.add(e + "col " +str(j))
                seen.add(e + "cube " +str(i//3)+str(j//3))
            

        return True
