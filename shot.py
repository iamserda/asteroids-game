import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __ini__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = 0
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            width=LINE_WIDTH,
            radius=self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt