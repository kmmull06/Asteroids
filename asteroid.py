import pygame
from circleshape import CircleShape
from constants import ASTEROID_COLOR

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0,0)

    def draw(self,screen):
        pygame.draw.circle(screen,ASTEROID_COLOR,(int(self.position.x),int(self.position.y)),self.radius,2)

    def update(self,dt):
        self.position+=self.velocity * dt   
