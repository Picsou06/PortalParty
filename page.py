from pygame import *
import pygame
import speedrun



def page(screen, numofsalle):
    screen_width, screen_height = screen.get_size()
    background_game = pygame.transform.scale(pygame.image.load("images/Ensemble/background.png"), (screen_width,screen_height))
    fleche_droite = pygame.transform.scale(pygame.image.load("images/Ensemble/DROITE.png"), (90,90))
    fleche_gauche = pygame.transform.scale(pygame.image.load("images/Ensemble/GAUCHE.png"), (90,90))
    portailbleu = pygame.transform.scale(pygame.image.load("images/Ensemble/bleu.png"), (40,40))
    portailjaune = pygame.transform.scale(pygame.image.load("images/Ensemble/orange.png"), (40,40))
    bouton = pygame.transform.scale(pygame.image.load("images/Ensemble/bouton.png"), (160,160))
    compagnon = pygame.transform.scale(pygame.image.load("images/Ensemble/compagnon.png"), (40,40))
    cube = pygame.transform.scale(pygame.image.load("images/Ensemble/cube.png"), (120,120))
    interupteur = pygame.transform.scale(pygame.image.load("images/Ensemble/interupteur.png"), (120,120))
    orbe = pygame.transform.scale(pygame.image.load("images/Ensemble/orbe.png"), (60,60))
    radio = pygame.transform.scale(pygame.image.load("images/Ensemble/radio.png"), (120,120))
    tourelle = pygame.transform.scale(pygame.image.load("images/Ensemble/tourelle.png"), (110,160))
    speedrunbutton = pygame.transform.scale(pygame.image.load("images/Ensemble/SPEEDRUN.png"), (200,30))
    SallePolice = pygame.font.SysFont("bold",50)
    NumberPolice = pygame.font.SysFont("bold",40)
    phaseportail=2
    hascompagnon=True
    nbbouton=0
    nbcube=0
    nbinterupteur=0
    nborbe=0
    nbradio=0
    nbtourelle=0
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
                elif screen_height/2 <= mouse[0] <= screen_height/2+200 and 90 <= mouse[1] <= 120:
                    speedrun.speedrun(screen, numofsalle)

        mouse = pygame.mouse.get_pos()
        screen.blit(background_game, (0, 0))
        if phaseportail==1:
            screen.blit(portailbleu, (screen_width-220, 70))
        elif phaseportail>1:
            screen.blit(portailbleu, (screen_width-220, 70))
            screen.blit(portailjaune, (screen_width-180, 70))
        if hascompagnon:
            screen.blit(compagnon, (screen_width-260, 70))
        screen.blit(fleche_droite, (50, screen_height-150))
        screen.blit(fleche_gauche, (screen_width-140, screen_height-150))
        texte_player = SallePolice.render("Salle "+salle[numofsalle], 1 ,(250,250,250))
        texte_nbbouton = NumberPolice.render(str(nbbouton), 1 ,(250,250,250))
        texte_nbcube = NumberPolice.render(str(nbcube), 1 ,(250,250,250))
        texte_nbinterupteur = NumberPolice.render(str(nbinterupteur), 1 ,(250,250,250))
        texte_nborbe = NumberPolice.render(str(nborbe), 1 ,(250,250,250))
        texte_nbradio = NumberPolice.render(str(nbradio), 1 ,(250,250,250))
        texte_nbtourelle = NumberPolice.render(str(nbtourelle), 1,(250,250,250))
        screen.blit(bouton, (110, 190))
        screen.blit(cube, (135, 360))
        screen.blit(interupteur, (135, 490))
        screen.blit(orbe, (screen_width-400, 210))
        screen.blit(radio, (screen_width-425, 320))
        screen.blit(tourelle, (screen_width-425, 480))
        screen.blit(texte_player, (screen_height/2+10, 10))
        screen.blit(speedrunbutton, (screen_height/2, 90))
        screen.blit(texte_nbbouton, (270, 250))
        screen.blit(texte_nbcube, (270, 400))
        screen.blit(texte_nbinterupteur, (270, 530))
        screen.blit(texte_nborbe, (screen_width-290, 250))
        screen.blit(texte_nbradio, (screen_width-290, 400))
        screen.blit(texte_nbtourelle, (screen_width-290, 530))



        pygame.display.flip()
