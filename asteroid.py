import pygame
import random
from pygame.math import Vector2
from circleshape import CircleShape
from constants import ASTEROID_COLOR, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,velocity = None):
        super().__init__(x,y,radius)
        self.velocity = velocity if velocity else pygame.Vector2(0,0)


    def split(self, asteroids):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)

        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_velocity_1 *= 1.2
        new_velocity_2 *= 1.2

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_1)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_2)

        self.containers[0].add(asteroid_1,asteroid_2)
        

    def draw(self,screen):
        pygame.draw.circle(screen,ASTEROID_COLOR,(int(self.position.x),int(self.position.y)),self.radius,2)

    def update(self,dt):
        self.position+=self.velocity * dt   
