import pygame
from pygame.sprite import Sprite
import random

aliens = ['./images/broccoli-gf94ba732b_1280.bmp',
          './images/carrot-g4eb2746b4_1280.bmp', './images/eggplant-g318e4a1fd_1280.bmp']

class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.transform.scale(pygame.image.load(
            aliens[random.randrange(0, len(aliens))]), (100, 100))
        print(self.image)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
