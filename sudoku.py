def find_empty(board):
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid(board, num, pos):
    
    if num in board[pos[0]]:
        return False

    
        return False

    
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    if num in [board[box_y * 3 + i][box_x * 3 + j] for i in range(3) for j in range(3)]:
        return False

    return True

def solve_sudoku(board):
    
    row, col = find_empty(board)

    
    if row is None and col is None:
        return True

    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            
            if solve_sudoku(board):
                return True

            
            board[row][col] = 0

    
    return False

# Example usage
unsolved_board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

print("Unsolved Sudoku:")
for row in unsolved_board:
    print(row)

solve_sudoku(unsolved_board)

print("\nSolved Sudoku:")
for row in unsolved_board:
    print(row)