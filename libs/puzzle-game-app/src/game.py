
import pygame
import time   
from puzzle import Puzzle

BG_COLOR = (180, 220, 255)
TILE_COLOR = (80, 180, 220)
TILE_BORDER = (40, 80, 120)
TEXT_COLOR = (0, 0, 0)
WIN_TEXT_COLOR = (255, 50, 50)

class PuzzleGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Puzzle Game")
        self.clock = pygame.time.Clock()
        self.puzzle = Puzzle(4)
        self.puzzle.shuffle()
        if self.puzzle.is_solved():
            self.puzzle.shuffle()
        self.running = True
        self.won = False
        self.start_time = None
        self.end_time = None
        

    def render(self):
        self.screen.fill(BG_COLOR)
        self.puzzle.render(self.screen, TILE_COLOR, TILE_BORDER, TEXT_COLOR)

        font = pygame.font.SysFont("Consolas", 28)
        if self.start_time is not None:
            elapsed = (self.end_time if self.end_time else time.time()) - self.start_time
            time_text = font.render(f"Time: {elapsed:.1f} sec", True, (50, 50, 50))
            self.screen.blit(time_text, (20, 20))

        if self.won:
           
            win_font = pygame.font.Font(None, 80)
            shadow_color = (40, 0, 0)
            text_color = (255, 100, 100)
            glow_color = (255, 200, 200)
            message = "YOU WIN!"

            text = win_font.render(message, True, text_color)
            shadow = win_font.render(message, True, shadow_color)
            glow = win_font.render(message, True, glow_color)

            text_rect = text.get_rect(center=(400, 280))

            # วาดเงา + glow + ข้อความหลัก
            self.screen.blit(shadow, (text_rect.x + 4, text_rect.y + 4))
            self.screen.blit(glow, (text_rect.x - 2, text_rect.y - 2))
            self.screen.blit(text, text_rect)

            # ข้อความแนะนำให้รีสตาร์ต
            small_font = pygame.font.SysFont("Consolas", 26)
            sub = small_font.render("Press [ESC] to Restart", True, (250, 250, 250))
            sub_rect = sub.get_rect(center=(400, 350))
            self.screen.blit(sub, sub_rect)

        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
    def update(self):
            if self.puzzle.is_solved() and not self.won:
                self.won = True
                self.end_time = time.time()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # รีสตาร์ตเกม
                    self.puzzle = Puzzle(4)
                    self.puzzle.shuffle()
                    self.won = False
                    self.start_time = None
                    self.end_time = None
                    continue

            elif event.type == pygame.MOUSEBUTTONDOWN and not self.won:
                mouse_x, mouse_y = event.pos
                tile_size = 100
                screen_width, screen_height = self.screen.get_size()
                board_size = self.puzzle.size * tile_size
                start_x = (screen_width - board_size) // 2
                start_y = (screen_height - board_size) // 2
                col = (mouse_x - start_x) // tile_size
                row = (mouse_y - start_y) // tile_size

                if 0 <= row < self.puzzle.size and 0 <= col < self.puzzle.size:
                    ex, ey = self.puzzle.empty_tile
                    if self.start_time is None:
                        self.start_time = time.time()
                    if row == ex - 1 and col == ey:
                        self.puzzle.move('up')
                    elif row == ex + 1 and col == ey:
                        self.puzzle.move('down')
                    elif col == ey - 1 and row == ex:
                        self.puzzle.move('left')
                    elif col == ey + 1 and row == ex:
                        self.puzzle.move('right')

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()
    pygame.quit()