import pygame

class Ship():
    '''Класс для управления кораблем.'''
    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальную позицию.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/spaceship_1.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        '''Флаг перемещения'''
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right == True:
            self.rect.x += 1
        if self.moving_left == True:
            self.rect.x -= 1
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)
