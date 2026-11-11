import pygame
import random
from pygame.math import Vector2
from pygame.surface import Surface
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", Vector2(self.position.x, self.position.y), self.radius, LINE_WIDTH)
    def update(self, dt:float) -> None:
        self.position += self.velocity * dt
    def split(self) -> None:
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_smaller_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_smaller_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2
