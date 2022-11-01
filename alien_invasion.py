import sys
import pygame
class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.screen = pygame.display.set_mode((1366,768))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (115, 195, 215)
    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Отображение последнего прорисованного экрана
                self.screen.fill(self.bg_color)
                pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()