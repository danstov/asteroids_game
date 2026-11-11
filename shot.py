import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
from pygame.math import Vector2
from pygame.surface import Surface

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", Vector2(self.position.x, self.position.y), self.radius, LINE_WIDTH)
    def update(self, dt:float) -> None:
        self.position += self.velocity * dt
