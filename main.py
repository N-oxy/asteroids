import pygame # type: ignore
from player import *
from asteroid import *
from constants import *
from logger import log_state
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group,updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    
    while True: 
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for element in drawable:
            element.draw(screen)
        for element in updatable:
            element.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
