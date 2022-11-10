import pygame
import datetime
from sys import exit
from src.game_objects import Player

class Game:
    def __init__(self):
        self.initialize_game()
        self.game_loop()

    def initialize_game(self):
        self.canvas = pygame.display.set_mode((500,500))
        self.game_started = False
        self.exit = False
        self.player = Player(self.canvas)

    def exit_game(self):
        self.exit = True;
        pygame.quit();
        exit();

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player.update_position(self.canvas, -1, 0)
        if key[pygame.K_RIGHT]:
            self.player.update_position(self.canvas, 1, 0)
        if key[pygame.K_UP]:
            self.player.update_position(self.canvas, 0, -1)
        if key[pygame.K_DOWN]:
            self.player.update_position(self.canvas, 0, 1)



    def game_loop(self):
        self.game_started = True
        pygame.display.set_caption("Testing")
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game() 
            self.handle_keys()
            self.canvas.fill((255,255,255))
            self.player.update(self.canvas)
            pygame.display.update()
            pygame.time.Clock().tick(60)

if __name__  == "__main__":
    game = Game()
