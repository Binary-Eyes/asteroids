import pygame
from logger import log_state
from player import Player
from constants import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    dt = 0.0
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update
        updatables.update(dt)

        #draw        
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60.0)/1000.0


if __name__ == "__main__":
    main()
