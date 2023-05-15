from pygame import *
import math
width, height = 800, 600

class ImageSprite(sprite.Sprite):
    def __init__(self, file, pos, size):
        super().__init__()
        self.image = image.load(file).convert_alpha()
        self.image = transform.scale(self.image,size)
        self.rect = Rect(pos, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        draw.rect(surface, "yellow", self.rect, 2)

class PlayerSprite(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 10
        if keys[K_RIGHT]:
            self.rect.x += 10
        
        if self.rect.left > width:
            self.rect.right = 0

        if self.rect.right < 0:
            self.rect.left = width

class Projectile(ImageSprite):
    def update(self):
        self.rect.y = self.rect.y - 12
        if self.rect.bottom < 0:
            self.kill()

class Fishy(ImageSprite):
    def __init__(self, file, pos, size, speed):
        super() .__init__(file, pos, size)
        self.speed = Vector2(speed)
        self.angle = 0
    def update(self):
        self.rect.x = self.rect.x + self.speed.x
        self.rect.y += math.sin(self.angle) * 5
        self.angle = self.angle + 0.1
        if self.rect.right < 0:
            self.rect.left = width
