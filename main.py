import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    is_running = True
    dt = 0.0
    game_clock = pygame.time.Clock()
    pygame.init()        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while is_running:
        # UPDATE
        player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # DRAW
        screen.fill("black")
        player.draw(screen)        

        pygame.display.flip()
        dt = game_clock.tick(60)/1000.0        
        

if __name__ == "__main__":
    main()
