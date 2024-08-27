import pygame
import numpy as np


class TicTacToe:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 600, 600
        self.LINE_WIDTH = 5
        self.BOARD_ROWS, self.BOARD_COLS = 3, 3
        self.SQUARE_SIZE = self.WIDTH // self.BOARD_COLS
        self.CIRCLE_RADIUS = self.SQUARE_SIZE // 3
        self.CIRCLE_WIDTH = 15
        self.CROSS_WIDTH = 25
        self.SPACE = self.SQUARE_SIZE // 4

        self.BG_COLOR = (28, 170, 156)
        self.LINE_COLOR = (23, 145, 135)
        self.CIRCLE_COLOR = (239, 231, 200)
        self.CROSS_COLOR = (66, 66, 66)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.screen.fill(self.BG_COLOR)

        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))

        self.player = 1
        self.game_over = False

    def draw_grid(self):
        # Horizontal
        pygame.draw.line(
            self.screen,
            self.LINE_COLOR,
            (0, self.SQUARE_SIZE),
            (self.WIDTH, self.SQUARE_SIZE),
            self.LINE_WIDTH,
        )
        pygame.draw.line(
            self.screen,
            self.LINE_COLOR,
            (0, 2 * self.SQUARE_SIZE),
            (self.WIDTH, 2 * self.SQUARE_SIZE),
            self.LINE_WIDTH,
        )

        # Vertical
        pygame.draw.line(
            self.screen,
            self.LINE_COLOR,
            (self.SQUARE_SIZE, 0),
            (self.SQUARE_SIZE, self.HEIGHT),
            self.LINE_WIDTH,
        )
        pygame.draw.line(
            self.screen,
            self.LINE_COLOR,
            (2 * self.SQUARE_SIZE, 0),
            (2 * self.SQUARE_SIZE, self.HEIGHT),
            self.LINE_WIDTH,
        )

    def draw_figures(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(
                        self.screen,
                        self.CIRCLE_COLOR,
                        (
                            int(col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                            int(row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                        ),
                        self.CIRCLE_RADIUS,
                        self.CIRCLE_WIDTH,
                    )
                elif self.board[row][col] == 2:
                    pygame.draw.line(
                        self.screen,
                        self.CROSS_COLOR,
                        (
                            col * self.SQUARE_SIZE + self.SPACE,
                            row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                        ),
                        (
                            col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                            row * self.SQUARE_SIZE + self.SPACE,
                        ),
                        self.CROSS_WIDTH,
                    )
                    pygame.draw.line(
                        self.screen,
                        self.CROSS_COLOR,
                        (
                            col * self.SQUARE_SIZE + self.SPACE,
                            row * self.SQUARE_SIZE + self.SPACE,
                        ),
                        (
                            col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                            row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                        ),
                        self.CROSS_WIDTH,
                    )

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        return not 0 in self.board

    def check_win(self, player):
        for col in range(self.BOARD_COLS):
            if (
                self.board[0][col] == player
                and self.board[1][col] == player
                and self.board[2][col] == player
            ):
                self.draw_vertical_winning_line(col, player)
                return True

        for row in range(self.BOARD_ROWS):
            if (
                self.board[row][0] == player
                and self.board[row][1] == player
                and self.board[row][2] == player
            ):
                self.draw_horizontal_winning_line(row, player)
                return True

        if (
            self.board[2][0] == player
            and self.board[1][1] == player
            and self.board[0][2] == player
        ):
            self.draw_ascending_diagonal(player)
            return True

        if (
            self.board[0][0] == player
            and self.board[1][1] == player
            and self.board[2][2] == player
        ):
            self.draw_descending_diagonal(player)
            return True

        return False

    def draw_vertical_winning_line(self, col, player):
        posX = col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        if player == 1:
            color = self.CIRCLE_COLOR
        elif player == 2:
            color = self.CROSS_COLOR

        pygame.draw.line(
            self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), self.LINE_WIDTH
        )

    def draw_horizontal_winning_line(self, row, player):
        posY = row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        if player == 1:
            color = self.CIRCLE_COLOR
        elif player == 2:
            color = self.CROSS_COLOR

        pygame.draw.line(
            self.screen, color, (15, posY), (self.WIDTH - 15, posY), self.LINE_WIDTH
        )

    def draw_ascending_diagonal(self, player):
        if player == 1:
            color = self.CIRCLE_COLOR
        elif player == 2:
            color = self.CROSS_COLOR

        pygame.draw.line(
            self.screen,
            color,
            (15, self.HEIGHT - 15),
            (self.WIDTH - 15, 15),
            self.LINE_WIDTH,
        )

    def draw_descending_diagonal(self, player):
        if player == 1:
            color = self.CIRCLE_COLOR
        elif player == 2:
            color = self.CROSS_COLOR

        pygame.draw.line(
            self.screen,
            color,
            (15, 15),
            (self.WIDTH - 15, self.HEIGHT - 15),
            self.LINE_WIDTH,
        )

    def play(self):
        self.draw_grid()
        self.game_over = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = mouseY // self.SQUARE_SIZE
                    clicked_col = mouseX // self.SQUARE_SIZE

                    if self.available_square(clicked_row, clicked_col):
                        self.mark_square(clicked_row, clicked_col, self.player)
                        if self.check_win(self.player):
                            self.game_over = True
                        self.player = 3 - self.player

                        self.draw_figures()

            pygame.display.update()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
