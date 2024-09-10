import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,position,velocity):
        super().__init__(position.x,position.y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)