import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version}!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    game_constants = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(game_constants)
    flag = True
    while flag:
        log_state()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return
    
    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
    main()