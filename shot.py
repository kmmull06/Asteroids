import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,position,direction):
        super().__init__(position,SHOT_RADIUS)
        self.velocity = direction

    def update(self, delta_time):
        self.position += self.velocity * delta_time