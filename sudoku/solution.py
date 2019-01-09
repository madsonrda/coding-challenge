import numpy as np
class Solution(object):
    def solveSudoku(self, board):
	    # store numbers available for each column, row and cube
        rows, columns, cubes = {}, {}, {}
		# store node that needs to be filled
        nodes = []
        for i in xrange(9):
            rows[i] = set([str(s) for s in xrange(1,10)])
            for j in xrange(9):
                cube_key = i / 3 * 3 + j / 3
                columns[j] = columns.get(j,  set([str(s) for s in xrange(1,10)]))
                cubes[cube_key] = cubes.get(cube_key,  set([str(s) for s in xrange(1,10)]))
                if board[i][j] != '.':
                    rows[i].remove(board[i][j])
                    columns[j].remove(board[i][j])
                    cubes[cube_key].remove(board[i][j])
                else:
                    nodes.append([i, j])
        self.solve(board, rows, columns, cubes, nodes, 0, len(nodes))

    def solve(self, board, rows, columns, cubes, nodes, next, end):
        if next == end:
            return True
        i, j = nodes[next][0], nodes[next][1]

        for num in list(rows[i]):
            cube_key = i / 3 * 3 + j / 3
            if num not in columns[j] or num not in cubes[cube_key]:
                continue
            else:
                rows[i].remove(num)
                columns[j].remove(num)
                cubes[cube_key].remove(num)
                board[i][j] = num
                if self.solve(board, rows, columns, cubes, nodes, next+1, end):
                    return True
                else:
                    rows[i].add(num)
                    columns[j].add(num)
                    cubes[cube_key].add(num)
                    board[i][j] = '.'
        return False

s = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

sudo = Solution()
sudo.solveSudoku(s2)

print(np.array(s2))
