import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
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
        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()
