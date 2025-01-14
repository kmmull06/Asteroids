import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED,PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self,x,y,radius, shot_group):
        super().__init__(x,y,radius)
        self.rotation = 0
        self.shot_group = shot_group
        self.timer = 0

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED*dt

    def shoot(self):
        if self.timer <= 0:
            direction = pygame.Vector2(0,1).rotate(self.rotation).normalize()
            velocity = direction * PLAYER_SHOOT_SPEED
            shot = Shot(self.position, velocity)
            self.timer = PLAYER_SHOOT_COOLDOWN
    def update(self,dt):

        if self.timer >0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

    

        

        