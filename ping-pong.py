import pygame
window = pygame.display.set_mode((700,500))
racket_image = pygame.image.load('ping-pong_racket.png')
racket_image = pygame.transform.scale(racket_image,(135,81))
racket_image = pygame.transform.rotate(racket_image,240)
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
player01 = Player(65,40,racket_image,0,10)

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(background_image,(0,0))
    window.blit(racket_image,player01.rect)
    player01.control_1()
    timer.tick(10)
    pygame.display.update()