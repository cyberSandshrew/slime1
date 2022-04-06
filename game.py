import pygame
from gameobject import Gameobject
from player import Player
from enemy import Enemy

#jerry french 2021 slime game
class Game:

    def __init__(self):

        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)



        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()


        self.background = Gameobject(0, 0, self.width, self.height, 'assets/background.png')
        
        self.treasure = Gameobject(375, 50, 50, 50, 'assets/treasure.png')
        
        

        self.level = 1.0

        self.reset_map()

    def reset_map(self):
        self.player = Player(375, 700, 50, 50, 'assets/enemy.png', 5)

        speed = (self.level * 4)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/player.png', speed),
                Enemy(750, 400, 50, 50, 'assets/player.png', speed),
                Enemy(0, 200, 50, 50, 'assets/player.png', speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/player.png', speed),
                Enemy(750, 400, 50, 50, 'assets/player.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 200, 50, 50, 'assets/player.png', speed),
            ]



        
       
        #draw

    def draw_objects(self):
    
        self.game_window.fill(self.white_color)

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x ,self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x ,self.player.y))
        
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        
        
        
        pygame.display.update()

#movement
    
    def move_objects(self, player_direction_y, player_direction_x):
        self.player.move(player_direction_y, player_direction_x, self.height, self.width)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
                self.level += 0.5
                return True
        return False

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        
        return True
        


   
    def run_game_loop(self):

        player_direction_y = 0
        player_direction_x = 0
        

        while True:
            #handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player_direction_y = -1
                    # move player up
                    elif event.key == pygame.K_s:
                        player_direction_y = +1
                    if event.key == pygame.K_a:
                        player_direction_x = -1
                    # move player right
                    elif event.key == pygame.K_d:
                        player_direction_x = +1
                    # move player down
                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            player_direction_y = 0
                if event.type == pygame.QUIT:
                    return

                   
                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_d or event.key == pygame.K_a:
                            player_direction_x = 0   
        
                
                        

            
            
            self.move_objects(player_direction_y, player_direction_x)
            
            
            
            self.draw_objects()


            if self.check_if_collided():
                self.reset_map()

        

            self.clock.tick(60)

