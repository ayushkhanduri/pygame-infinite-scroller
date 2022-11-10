import pygame
from src.shared import Gravity

class Player(Gravity):

    def __init__(self,surface):
        self.player_sprite = None
        self.create_player(surface)

    def create_player(self, surface):
        self.color = (255,0,0)
        self.player_sprite = pygame.rect.Rect(30,30,60,60)

    def update_position(self,canvas, x_offset = 0, y_offset = 0):
        # self.player_object = pygame.Rect.move_ip(self.player_object, 200.0, 300.0)
        new_position_x = self.player_sprite.x + self.player_sprite.width * x_offset
        new_position_y = self.player_sprite.y + self.player_sprite.height * y_offset
        # print("new pos: x : ", new_position_x)
        # print("new pos y:" , new_position_y)
        # self.player_sprite.move_ip(new_position_x,new_position_y)
        self.player_sprite.move_ip(x_offset, y_offset)

    def update(self, surface):
        pygame.draw.rect(surface,self.color, self.player_sprite)

    def life_forces(self):
        pass

