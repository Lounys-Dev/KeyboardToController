import pygame

pygame.joystick.init()
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        elif event.type in (pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP): print(event)