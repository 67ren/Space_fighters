# ფაიგეიმის მოდულიდან ყველაფრის ინდივიდუალურად შემოტანა
import sys
from pygame import *
from pygame import mixer
# ფაიგეიმის ინიციაცია
init()
#საათის შექმნა თამაშის მთავარი ციკლის სიხშირის გასაკონტროლებლად
clock = time.Clock()
# სიხშირე
fps = 20
#ეკრანის მონაცემების მოთხოვნა
info = display.Info()

icon = image.load("Actual_display_icon.png")
display.set_icon(icon)
display.set_caption("Space_Fighters")
# თამაშის ეკრანის ზომების მორგება კომპის ეკრანის ზომებზე
width = info.current_w
height = info.current_h

screen = display.set_mode((width, height))

proportion = 2048 / 768
background = image.load("new.background.png")
background = transform.scale(background, (height * proportion, height))


differance = width - background.get_width()

# მოთამაშის კლასი
class Player(sprite.Sprite):
    #კონსტრუქტორი
    def __init__(self, name):
        super().__init__()

        self.size = 150
        self.image = image.load("new__rocket2.png")
        self.image = transform.scale(self.image, (self.size, self.size))
        self.rect = Rect(900, height - 200, self.size, self.size)
        self.speed = 10
        self.speed_x = 0
        self.speed_y = 0
        self.name = name
        self.shoot = False
        self.counter = 0
        self.bullets = []
        #მოთამაშეების საწყისი ლოკაციების განსაზღვრა
        if self.name == "rocket2":
            self.rect.center = (width / 2.9 , height * 2/2.4)
        if self.name == "rocket":
            self.rect.center = (width * 2 / 3 , height * 2/2.4)

    # დახატვის ფუნქცია
    def draw(self):
        screen.blit(self.image, self.rect)
    # მოძრაობის ფუნქცია
    def move(self):
        # მოძრაობის კოდი
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
        # ეკრანიდან გასვლის აკრძალვის კოდი
        if self.rect.centerx < self.size / 5:
            self.rect.centerx = self.size / 5

        if self.rect.centerx > width - self.size / 2:
            self.rect.centerx = width - self.size / 2

        if self.rect.centery < self.size / 2:
            self.rect.centery = self.size / 2

        if self.rect.centery >height - self.size / 2:
            self.rect.centery = height - self.size / 2


    # კლავიატურის კონტროლი (სიჩქარეების ცვლილება)
    def controls(self):
        keys = key.get_pressed()
        # სიჩქარეების განულება როცა არ ვაჭერთ კნოპს
        self.speed_x = 0
        self.speed_y = 0
        # სიჩქარეების ცვლილება კნოპზე დაჭერის მიხედვით (ორი ფლეიერისთვის სხვადასხვა)
        if self.name == "rocket":
            if keys[K_w]:
                self.speed_y = -self.speed
            if keys[K_s]:
                self.speed_y = self.speed
            if keys[K_d]:
                self.speed_x = self.speed
            if keys[K_a]:
                self.speed_x = -self.speed
            if keys[K_SPACE]:
                self.shoot = True


        if self.name == "rocket2":
            if keys[K_UP]:
                self.speed_y = -self.speed
            if keys[K_DOWN]:
                self.speed_y = self.speed
            if keys[K_RIGHT]:
                self.speed_x = self.speed
            if keys[K_LEFT]:
                self.speed_x = -self.speed
            if keys[K_z]:
                self.shoot = True

    def shooting(self):
        if self.shoot == True and self.counter == 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery)
            self.bullets.append(bullet)
            self.shoot = False
            self. counter = 180
        else:
            pass


    # ყველა საჭირო ფუნქციის ერთად გამოძახება
    def update(self):

        self.draw()
        self.controls()
        self.move()
        self.shooting()

        self.counter -= 1
        if self.counter <= 0:
            self.counter = 0


class Bullet(sprite.Sprite):
    def __init__(self, centerx, centery):
        super().__init__()
        self.size = 190
        self.images = image.load("Bullet_bomb.png")
        self.images = transform.scale(self.images, (self.size, self.size))
        self.x = centerx
        self.y = centery
        self.rect = Rect(self.x, self.y, int(width / 3000), int(width / 3000))
        self.rect.center = (self.x, self.y)
#380 550
    def draw(self):
        self.rect.centery -= 8
        screen.blit(self.images, self.rect)

        if self.rect.bottom < 0:
            self.kill()


class Enemy(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = Rect(x, y, width/20, width/20)
        self.rect.center = (x, y)
        self.vertical_speed = 0.5
        self.horizontal_speed = 1
        self.counter = 0

    def draw(self):
        draw.rect(screen, (200, 200, 100), self.rect)
        self.counter += 1
        if self.counter >= 40:
            self.horizontal_speed *= -1
            self.counter = 0
        self.rect.centery += self.vertical_speed
        self.rect.centerx += self.horizontal_speed

enemies = []
i = 1
while i <= 20:
    enemy = Enemy(i * width/20, height * 1 / 10)
    enemies.append(enemy)
    i += 2

# ობიექტების შექმნა
player1 = Player("rocket")
player2 = Player("rocket2")


# მთავარი ციკლი
run = True
while run:
    clock.tick(fps)

    screen.fill((0, 0, 0))
    for en in enemies:
        en.draw()

    for bul in player1.bullets:
        bul.draw()
    for bul in player2.bullets:
        bul.draw()
    # ობიექტების აფდეითი
    player1.update()
    player2.update()


    for ev in event.get():
        if ev.type == QUIT:
            run = False
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                quit()
                sys.exit()

    # ეკრანის განახლება
    display.update()
#ფაიგეიმიდან გამოსვლა
quit()

