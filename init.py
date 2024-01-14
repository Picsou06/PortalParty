import pygame
import page
from random import *

# Définissez une taille initiale pour la fenêtre
initial_width = 1000
initial_height = 800

pygame.init()
screen = pygame.display.set_mode((initial_width, initial_height), pygame.NOFRAME)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("PortalParty")
icon = pygame.image.load("images/Ensemble/THECAKEISALIE.jpg")
pygame.display.set_icon(icon)
x = randint(1,3)
if x == 1:
    background_lobby = pygame.transform.scale(pygame.image.load("images/Lobby/Background.jpg"), (screen_width,screen_height))
elif x == 2:
    background_lobby = pygame.transform.scale(pygame.image.load("images/Lobby/Background 2.jpg"), (screen_width,screen_height))
elif x == 3:
    background_lobby = pygame.transform.scale(pygame.image.load("images/Lobby/Background 3.jpg"), (screen_width,screen_height))

running=True
while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                page.page(screen, 0)
        screen.blit(background_lobby, (0, 0))
        pygame.display.flip()
