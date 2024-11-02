import pygame 

pygame.init()

window = pygame.display.set_mode((400, 400))

window.fill((214, 233, 233))

GREEN = (111, 186, 122)

pygame.draw.circle(window, GREEN, (300, 300), 50)

pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

pygame.quit()
