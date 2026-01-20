import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="yellow",
            center=self.position,
            width=LINE_WIDTH,
            radius=self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_asteroid1_velocity = self.velocity.rotate(angle)
        new_asteroid2_velocity = self.velocity.rotate(-angle)
        new_asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid1_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid2_radius)
        asteroid1.velocity = new_asteroid1_velocity * 1.2
        asteroid2.velocity = new_asteroid2_velocity * 1.2
