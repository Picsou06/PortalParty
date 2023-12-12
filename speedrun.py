from pygame import *
import pygame
import page

def speedrun(screen, numofsalle):
    screen_width, screen_height = screen.get_size()
    lobby=False
    background_game = pygame.transform.scale(pygame.image.load("images/Ensemble/background.png"), (screen_width,screen_height))
    retour = pygame.transform.scale(pygame.image.load("images/Ensemble/retour.png"), (50,50))
    SallePolice = pygame.font.SysFont("bold",50)
    NumberPolice = pygame.font.SysFont("bold",40)
    mouse = pygame.mouse.get_pos()
    salle=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= mouse[0] <= 140 and screen_height-140 <= mouse[1] <= screen_height-50:
                    if numofsalle>0:
                        numofsalle=numofsalle-1
                elif screen_width-140 <= mouse[0] <= screen_width-50 and screen_height-140 <= mouse[1] <= screen_height-50:
                    if numofsalle<17:
                        numofsalle=numofsalle+1
                elif 50 <= mouse[0] <= 100 and 50 <= mouse[1] <= 100:
                    page.page(screen, numofsalle)

        mouse = pygame.mouse.get_pos()
        screen.blit(background_game, (0, 0))
        texte_player = SallePolice.render("Salle "+salle[numofsalle], 1 ,(250,250,250))
        screen.blit(retour, (50, 50))
        screen.blit(texte_player, (screen_height/2+10, 10))

        pygame.display.flip()