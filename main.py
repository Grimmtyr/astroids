import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroidField = AsteroidField()

    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(delta_time)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.is_colliding(player):
                print("Game Over!")
                return 
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
#        print(delta_time)
        delta_time = game_clock.tick(60) / 1000
   

if __name__=="__main__":
    main()
