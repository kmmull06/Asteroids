import pygame
from constants import SHOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):

    containers = None

    def __init__(self,position,velocity,shot_group):
        super().__init__(position.x,position.y, SHOT_RADIUS)
        self.velocity = velocity
        self.add(shot_group)
        self.add(self.containers)

    def update(self, delta_time):
        self.position += self.velocity * delta_time
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)