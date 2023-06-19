from pygame import *
from sprites import *
from random import randint, random
mixer.init()

width = 800
height = 600
window = display.set_mode((width, height))
clock = time.Clock()
counter = Text(words="points : 0", pos=(10,500), colour="coral", font_size=50, font_file="Pangolin-Regular.ttf")
fat_cat = PlayerSprite ("images/fat cat 2.png", (width/2, 480), (100,100))
fat_cat.rect.centerx = width/2
test_Fishy = Fishy("images/Fish.png", (width, height/2), (50, 50), (-5, 0))
bag_of_fish = sprite.Group()
bag_of_bombs = sprite.Group()
points = 0
bg = ImageSprite("background.png", (0,0), (width, height))
restart = ImageSprite("images/restart.png", (width-100, height-100), (100, 100))
GameOver = ImageSprite("game over screen.png", (0,0), (width, height))
shoot_sn = mixer.Sound("sounds/shootingsn.mp3")
explosion_sn = mixer.Sound("sounds/explosionsn.mp3")
under_sn = mixer.music.load("sounds/mainsn.mp3")
mixer.music.play()
def new_fish():
    y = randint(0,300)
    x_speed = randint(-7, -2)
    coinflip = random()
    if coinflip > 0.25:
        fish = Fishy("images/Fish.png", (width, y), (50, 50), (x_speed, 0))
        fish.tyepofish = "normal"
    else:
        fish = Fishy("images/bomb fish.png", (width, y), (50, 50), (x_speed, 0))
        fish.tyepofish = "bomb"

    bag_of_fish.add(fish)

def create_F(amount):
    for i in range(amount):
        new_fish()

create_F(20)

bullets = sprite.Group()
def shoot():
    p = Projectile("images/Fork.png", fat_cat.rect.center , (30, 50))
    bullets.add(p)

state = "play"


while not event.peek(QUIT):
    for ev in event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                shoot()
                shoot_sn.play()

    if state == "play":
        bg.draw(window)
        bullets.update()
        bullets.draw(window)
        bag_of_fish.update()
        bag_of_fish.draw(window)
        bag_of_bombs.update()
        bag_of_bombs.draw(window)
        fat_cat.update()
        fat_cat.draw(window)
        counter.draw(window)
        hits = sprite.groupcollide(bag_of_fish,bullets, True, True)
        for hit in hits:
            if hit.tyepofish == "bomb":
                bomb = Bomb("images/bomb.png", hit.rect.topleft, (30,60), -hit.speed.x)
                bag_of_bombs.add(bomb)
            points += 1
            counter.update_words(f"Points: {points}") 
            new_fish()

        if sprite.spritecollide(fat_cat, bag_of_bombs, True):
            explosion_sn.play()
            state = "game over"
    if state == "game over":
        GameOver.draw(window)
        restart.draw(window)
        counter.draw(window)
        if mouse.get_pressed()[0]:
            pos = mouse.get_pos()
            r = restart.rect
            if r.collidepoint(pos):
                state = "play"
                points = 0
                counter.update_words(f"Points: {points}")
                bag_of_bombs.empty()
                bullets.empty()
                fat_cat.rect.centerx = width/2

    display.update()
    clock.tick(60)
