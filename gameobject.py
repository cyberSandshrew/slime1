import pygame

#jerry french 2021 slime game

class Gameobject:
    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image,(width, height))


        self.x = x
        self.y = y
        self.width = width
        self.height = height

        
