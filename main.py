import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.update(delta_time)
        player.draw(screen)
        pygame.display.flip()
#        print(delta_time)
        delta_time = game_clock.tick(60) / 1000
   

if __name__=="__main__":
    main()
