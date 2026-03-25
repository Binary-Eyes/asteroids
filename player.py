import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_cooldown = 0.0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self, dt):
        axis_y = pygame.Vector2(0, 1)
        forward = axis_y.rotate(self.rotation)
        velocity = forward * PLAYER_SPEED * dt
        self.position += velocity

    def shoot(self):
        if self.shot_cooldown > 0.0:
            return        
        axis_y = pygame.Vector2(0, 1)
        forward = axis_y.rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * PLAYER_SHOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def update(self, dt):        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shot_cooldown > 0.0:
            self.shot_cooldown -= dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
