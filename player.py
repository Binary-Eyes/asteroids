import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0

    def get_forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt, -1)

        if keys[pygame.K_d]:
            self.rotate(dt, +1)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = self.get_forward()*PLAYER_SHOOT_SPEED

    def move(self, dt):
        self.position += self.get_forward()*dt*PLAYER_SPEED

    def rotate(self, dt, direction):
        self.rotation += PLAYER_TURN_SPEED*dt*direction
        if self.rotation < 0.0:
            self.rotation += 360.0
        elif self.rotation > 360.0:
            self.rotation -= 360.0
