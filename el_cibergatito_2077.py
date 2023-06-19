import pygame
from game_state import GameState
from constant_stuff import CLOCK

pygame.init()
pygame.display.set_caption('EL CIBERGATITO 2077')
game_state = GameState()

while True:
    game_state.state_manager()
    pygame.display.update()
    CLOCK.tick(60)
