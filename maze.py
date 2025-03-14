#create a Maze game!

from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (85, 85))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'izquierda'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'derecha'
        if self.rect.x >= win_width - 85:
            self.direction = 'izquierda'

        
        if self.direction == 'izquierda':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super(). __init__()
        self.color1 = color_1
        self.color2 = color_2
        self.color3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
    
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Laberinto')
background = transform.scale(image.load('Black Pearl Cookie aesthetic.jpg'), (win_width, win_height))

player = Player ('Black_Pearl.png', 5, win_height - 80, 4)
monster = Enemy('Enemy.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
w1 = Wall(51, 102, 102, 100, 20, 600, 5)
w2 = Wall(51, 102, 102, 100, 480, 350, 5)
w3 = Wall(51, 102, 102, 100, 20, 5, 350)

w4 = Wall(51, 102, 102, 200, 130, 5, 350)
w5 = Wall(51, 102, 102, 450, 130, 5, 360)
w6 = Wall(51, 102, 102, 300, 20, 5, 200)
w7 = Wall(51, 102, 102, 390, 120, 130, 5)



#color, color, color, x, y, 


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('Ganaste!!', True, (58, 118, 68))
lose = font.render('Perdiste, nub', True, (141, 34, 38))

mixer.init()
mixer.music.load('jungles.ogg')




mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            #kick_play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            #money.play()


    display.update()
    clock.tick(FPS)


