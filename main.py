import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    is_running = True
    deltaTime = 0.0
    game_clock = pygame.time.Clock()
    pygame.init()        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while is_running:
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = game_clock.tick(60)/1000.0

if __name__ == "__main__":
    main()
