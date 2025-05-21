import pygame
import random
import math
import core.loader as loader

class EatAnimation:
    def __init__(self):
        self.particles = []
        self.active = False
        self.timer = 0

    class Particle:
        def __init__(self, pos):
            self.x, self.y = pos
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            self.vx = speed * random.uniform(0.5, 1.0) * math.cos(angle)
            self.vy = speed * random.uniform(0.5, 1.0) * math.sin(angle)
            self.alpha = 255
            self.life = random.uniform(0.6, 1.0)  # seconds
            self.age = 0

        def update(self, dt):
            self.x += self.vx
            self.y += self.vy
            self.age += dt
            self.alpha = max(0, 255 * (1 - self.age / self.life))

        def draw(self, surf):
            if self.alpha > 0:
                s = pygame.Surface((10, 10), pygame.SRCALPHA)
                pygame.draw.rect(s, loader.red + (int(self.alpha),), [0, 0, 10, 10])
                surf.blit(s, (self.x - 5, self.y - 5))

    def trigger(self, pos):
        """شروع انیمیشن از موقعیت خاص"""
        for _ in range(20):
            self.particles.append(self.Particle((pos[0] + 10, pos[1] + 10)))
        self.active = True
        self.timer = 0

    def update(self, dt):
        """آپدیت ذرات - در حلقه اصلی استفاده شود"""
        if not self.active:
            return
        self.timer += dt
        for p in self.particles[:]:
            p.update(dt)
            if p.alpha <= 0:
                self.particles.remove(p)
        if not self.particles:
            self.active = False  # وقتی همه ذرات تموم شدن، غیرفعال شو

    def draw(self, screen):
        """رسم ذرات - در حلقه اصلی استفاده شود"""
        if not self.active:
            return
        for p in self.particles:
            p.draw(screen)
