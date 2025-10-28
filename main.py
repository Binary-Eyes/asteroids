import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Asteroids v1.0.0")
    pygame.init()
    deltaTime = 0.0
    game_clock = pygame.time.Clock()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    while True:
        # UPDATE
        for entry in updatable:
            entry.update(deltaTime)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit(1)                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # DRAW
        screen.fill("black")
        for entry in drawable:
            entry.draw(screen)

        pygame.display.flip()
        deltaTime = game_clock.tick(60)/1000.0
        

if __name__ == "__main__":
    main()
