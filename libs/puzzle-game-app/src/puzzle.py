import pygame
import random

class Puzzle:
    def __init__(self, size):
        # กำหนดขนาดกระดาน เช่น 4 (จะได้ 4x4)
        self.size = size
        # สร้างกระดานเริ่มต้น
        self.board = self.create_board()
        # ตำแหน่งช่องว่าง (เริ่มที่มุมขวาล่าง)
        self.empty_tile = (size - 1, size - 1)

    def create_board(self):
        """สร้างกระดานเริ่มต้น เช่น [[1,2,3,...,15,0]]"""
        return [[(i * self.size + j + 1) % (self.size * self.size)
                 for j in range(self.size)]
                for i in range(self.size)]

    def shuffle(self):
        """สับกระดานแบบสุ่ม"""
        for _ in range(200):  # ยิ่งมาก ยิ่งสุ่มเยอะ
            direction = random.choice(['up', 'down', 'left', 'right'])
            self.move(direction)

    def move(self, direction):
        """ขยับช่องว่าง (0) ไปตามทิศทางที่เลือก"""
        x, y = self.empty_tile

        if direction == 'up' and x > 0:
            # สลับตำแหน่งช่องว่างกับช่องด้านบน
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y]
            self.empty_tile = (x - 1, y)

        elif direction == 'down' and x < self.size - 1:
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y]
            self.empty_tile = (x + 1, y)

        elif direction == 'left' and y > 0:
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y]
            self.empty_tile = (x, y - 1)

        elif direction == 'right' and y < self.size - 1:
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y]
            self.empty_tile = (x, y + 1)

    def is_solved(self):
        """ตรวจสอบว่าจัดกระดานครบหรือยัง"""
        return self.board == self.create_board()

    def render(self, screen, tile_color, border_color, text_color):
        """วาดกระดานด้วยสี่เหลี่ยมและตัวเลข"""
        tile_size = 100   # ขนาดช่อง
        gap = 5           # ช่องว่างระหว่าง tile
        font = pygame.font.SysFont("Consolas", 32)

        # ขนาดหน้าจอ
        screen_width, screen_height = screen.get_size()
        # ขนาดรวมของกระดานทั้งหมด
        board_size = self.size * (tile_size + gap) + gap
        # คำนวณจุดเริ่มต้นเพื่อจัดให้อยู่กลางจอ
        start_x = (screen_width - board_size) // 2
        start_y = (screen_height - board_size) // 2

        # สีพื้นหลัง (น้ำตาลเข้ม)
        screen.fill((25, 20, 15))

        # วาดทุกช่องในกระดาน
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue  # ช่องว่างไม่ต้องวาด

                # คำนวณพิกัดช่อง
                x = start_x + j * (tile_size + gap)
                y = start_y + i * (tile_size + gap)

                rect = pygame.Rect(x, y, tile_size, tile_size)

                # วาดเงาด้านหลัง tile
                shadow_rect = pygame.Rect(x + 4, y + 4, tile_size, tile_size)
                pygame.draw.rect(screen, (0, 0, 0), shadow_rect, border_radius=8)

                # วาดสี่เหลี่ยมหลักและขอบ
                pygame.draw.rect(screen, tile_color, rect, border_radius=6)
                pygame.draw.rect(screen, border_color, rect, 3, border_radius=6)

                # วาดตัวเลขตรงกลาง tile
                text = font.render(str(tile), True, text_color)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

