import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.randint(20, 50)
            first_vel = self.velocity.rotate(rand_angle)
            second_vel = self.velocity.rotate(-rand_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
            asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)
            asteroid1.velocity = first_vel * 1.2
            asteroid2.velocity = second_vel * 1.2
    