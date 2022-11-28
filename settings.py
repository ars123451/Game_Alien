import random
class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 750
        a = random.randint(100,255)
        b = random.randint(100, 255)
        c = random.randint(100, 255)
        self.bg_color = (b, a, c)
        '''Настройки корабля'''
        self.ship_speed = 1
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


