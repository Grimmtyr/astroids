import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
         shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
         shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.cooldown > 0:
            if self.cooldown - dt < 0:
                self.cooldown = 0
            else:
                self.cooldown -= dt
            #print(self.cooldown)

        if keys[pygame.K_SPACE]:
            if self.cooldown == 0:
                self.shoot(dt)
                self.cooldown = PLAYER_SHOOT_COOLDOWN

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.width = 2
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += (self.velocity * dt)