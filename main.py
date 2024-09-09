import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, PLAYER_RADIUS)

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()

        asteroids = pygame.sprite.Group()

        updatable.add(player)
        drawable.add(player)

        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        asteroid_field = AsteroidField()

        running = True
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                updatable.update(dt)

                for asteroid in asteroids:
                        if player.check_collision(asteroid):
                                print("Game over!")
                                running = False
                                break
                                

                screen.fill((0,0,0))

                for obj in drawable:
                        obj.draw(screen)

                pygame.display.flip()

                dt = clock.tick(60) / 1000
                
       
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()
