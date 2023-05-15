from pygame import *
from sprites import *
from random import randint

width = 800
height = 600
window = display.set_mode((width, height))
clock = time.Clock()
fat_cat = PlayerSprite ("images/fat cat 2.png", (width/2, 480), (100,100))
fat_cat.rect.centerx = width/2
test_Fishy = Fishy("images/Fish.png", (width, height/2), (50, 50), (-5, 0))
bag_of_fish = sprite.Group()
def new_fish():
    y = randint(0,300)
    x_speed = randint(-7, -2)
    fish = Fishy("images/Fish.png", (width, y), (50, 50), (x_speed, 0))
    bag_of_fish.add(fish)

def create_F(amount):
    for i in range(amount):
        new_fish()

create_F(20)

bullets = sprite.Group()
def shoot():
    p = Projectile("images/Fork.png", fat_cat.rect.center , (30, 50))
    bullets.add(p)

while not event.peek(QUIT):
    for ev in event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                shoot()
    window.fill((102, 51, 153))
    bullets.update()
    bullets.draw(window)
    bag_of_fish.update()
    bag_of_fish.draw(window)
    fat_cat.update()
    fat_cat.draw(window)
    display.update()
    clock.tick(60)





