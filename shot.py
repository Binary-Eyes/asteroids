import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, deltaTime):
        self.position += self.velocity*deltaTime

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)