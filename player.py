from gameobject import Gameobject

#jerry french 2021 slime game

class Player(Gameobject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.speed = speed

        
    def move(self, direction_y, direction_x, max_height, max_width):
        self.moveVertically(direction_y, max_height)
        self.moveHorizontally(direction_x, max_width)
        
        
    def moveVertically(self, direction_y, max_height):
        if (self.y >= max_height - self.height and direction_y > 0) or (self.y == 0 and direction_y < 0):
            return 
        self.y += (direction_y * self.speed)
        
    
    def moveHorizontally(self, direction_x, max_width):
        if (self.x <= 0 and direction_x < 0) or (self.x >= max_width - self.width and direction_x > 0):
            return 
        self.x += (direction_x * self.speed)