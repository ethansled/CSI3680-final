# solver.py
import pygame
import time
from GUI import board, run, win


pygame.font.init()

class SolverGrid:
    def __init__(self, board):
        self.board = board
        self.model = [row[:] for row in board]

    def solve(self):
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True

                self.model[row][col] = 0

        return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_puzzle(board):
    solver = SolverGrid(board)
    solver.solve()
    return solver.model

# main.py
# (Your existing code goes here)

def draw_solve_button(win, solve_button_rect):
    pygame.draw.rect(win, (0, 255, 0), solve_button_rect)
    font = pygame.font.SysFont("comicsans", 30)
    text = font.render("Solve", True, (0, 0, 0))
    win.blit(text, (solve_button_rect.x + 10, solve_button_rect.y + 10))

def main():
    # (Your existing code goes here)

    solve_button_rect = pygame.Rect(440, 560, 80, 40)
    solve_button_clicked = False

    while run:
        # (Your existing code goes here)

        for event in pygame.event.get():
            # (Your existing code goes here)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if solve_button_rect.collidepoint(pos):
                    solve_button_clicked = True

        if solve_button_clicked:
            # Solve the puzzle and update the board
            solution = solve_puzzle(board.board)
            for i in range(board.rows):
                for j in range(board.cols):
                    board.cubes[i][j].set(solution[i][j])
                    board.cubes[i][j].draw_change(win, True)
                    pygame.display.update()
                    pygame.time.delay(100)

            solve_button_clicked = False  # Reset the flag

        # (Your existing code goes here)

        draw_solve_button(win, solve_button_rect)
        pygame.display.update()

# (Your existing code goes here)

if __name__ == "__main__":
    main()
    pygame.quit()