import pygame
window = pygame.display.set_mode((700,500))
racket_image = pygame.image.load('ping-pong_racket.png')
racket_image = pygame.transform.scale(racket_image,(135,81))
racket_image2 = pygame.transform.rotate(racket_image,0)
racket_image = pygame.transform.rotate(racket_image,240)
ball_image = pygame.image.load('ping-pong-ball.png')
ball_image = pygame.transform.scale(ball_image,(81,81))
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image,(700,500))
pygame.init()
text = pygame.font.SysFont('Arial',50,1)
timer = pygame.time.Clock()
class Object():
    def __init__(self,x,y,image,xs,ys):
        self.rect = image.get_rect(center = (x,y))
        self.xs = xs
        self.ys = ys
        self.score = 0
class Player(Object):
    def control_1(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w] == 1:
            self.rect.y -= self.ys
        if key_list[pygame.K_s] == 1:
            self.rect.y += self.ys
    def control_2(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_UP] == 1:
            self.rect.y -= self.ys
        if key_list[pygame.K_DOWN] == 1:
            self.rect.y += self.ys
class Ball(Object):
    def move(self):
        self.rect.x += self.xs
        self.rect.y += self.ys
        if self.rect.y == 450:
            self.ys = -self.ys
        if self.rect.y == 0:
            self.ys = -self.ys
        if self.rect.x == 650:
            self.xs = -self.xs
            self.rect.centerx = 350
            self.rect.centery = 250
            player01.score += 1
            print(self.rect.x,self.xs)
        if self.rect.x == 0:
            self.xs = -self.xs
            self.rect.centerx = 350
            self.rect.centery = 250
            player02.score += 1
    def collision(self):
        if self.rect.colliderect(player01.rect):
            self.xs = 10
        if self.rect.colliderect(player02.rect):
            self.xs = -10

            

        
ball01 = Ball(350,250,ball_image,10,10)

player01 = Player(65,40,racket_image,0,10)
player02 = Player(635,80,racket_image2,0,10)
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    text_image01 = text.render(str(player01.score),0,(100,0,255))
    text_image02 = text.render(str(player02.score),0,(100,0,255))
    if player01.score == 3:
        win01 = text.render('1-ый игрок выиграл',0,(100,0,0))
    if player02.score == 3:
        win02 = text.render('2-ый игрок выиграл',0,(100,0,0))

    window.blit(background_image,(0,0))
    window.blit(racket_image,player01.rect)
    window.blit(racket_image2,player02.rect)
    window.blit(ball_image,ball01.rect)
    window.blit(text_image01,(200,0))
    window.blit(text_image02,(450,0))
    if player01.score == 3:
        win01 = text.render('1-ый игрок выиграл',0,(100,0,0))
        window.blit(win01,(150,300))
        ball01.xs = 0
        ball01.ys = 0
    if player02.score == 3:
        win02 = text.render('2-ый игрок выиграл',0,(100,0,0))
        window.blit(win02,(150,300))
        ball01.xs = 0
        ball01.ys = 0
    player01.control_1()
    player02.control_2()
    ball01.move()
    ball01.collision()
    timer.tick(10)
    pygame.display.update()