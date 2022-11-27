import random
class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 750
        a = random.randint(0,255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        self.bg_color = (b, a, c)