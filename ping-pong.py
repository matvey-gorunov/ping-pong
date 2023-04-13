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
timer = pygame.time.Clock()
class Object():
    def __init__(self,x,y,image,xs,ys):
        self.rect = image.get_rect(center = (x,y))
        self.xs = xs
        self.ys = ys
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
            print(self.rect.x,self.xs)
        if self.rect.x == 0:
            self.xs = -self.xs
            self.rect.centerx = 350
            self.rect.centery = 250
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
    window.blit(background_image,(0,0))
    window.blit(racket_image,player01.rect)
    window.blit(racket_image2,player02.rect)
    window.blit(ball_image,ball01.rect)
    player01.control_1()
    player02.control_2()
    ball01.move()
    ball01.collision()
    timer.tick(10)
    pygame.display.update()