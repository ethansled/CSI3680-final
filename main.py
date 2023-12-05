# main.py
import pygame
import time
from solver import solve_puzzle
from GUI import board, run, win

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
            solution = solve_puzzle(board.model)
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
