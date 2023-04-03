import pygame
window = pygame.display.set_mode((700,500))
timer = pygame.time.Clock()

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    timer.tick(10)